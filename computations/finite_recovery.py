#!/usr/bin/env python3
"""Exact recovery from a supplied algebraic low-rotation product.

This module DOES NOT compute derived natural transformations of an nc algebra.
It consumes their proposed Sym^2(V)->W matrix and checks the algebraic steps.
The local algorithm works over k[h]_(h), k a rational-function field of char 0.
"""
from __future__ import annotations
import argparse
import json
from itertools import combinations_with_replacement
from pathlib import Path
from typing import Sequence
import sympy as sp


def simp(x: sp.Expr) -> sp.Expr:
    return sp.cancel(x)


def regular_value(expr: sp.Expr, h: sp.Symbol) -> sp.Expr:
    num, den = sp.fraction(simp(expr))
    if sp.simplify(den.subs(h, 0)) == 0:
        raise ValueError(f"Pole at {h}=0: {expr}")
    return simp(num.subs(h, 0) / den.subs(h, 0))


def local_kernel(matrix: sp.Matrix, h: sp.Symbol,
                 coefficients: Sequence[sp.Symbol] = ()) -> tuple[sp.Matrix, int]:
    """Return a saturated k[h]_(h)-basis of the rational kernel.

    First clear denominators, then divide relations among residue columns by h.
    Each division lowers the valuation of the exterior product by exactly one.
    Full residue-column rank certifies saturation (a maximal minor is a unit).
    """
    field = sp.QQ.frac_field(*coefficients) if coefficients else sp.QQ
    vectors = matrix.nullspace()
    if not vectors:
        return sp.zeros(matrix.cols, 0), 0
    columns = []
    for vector in vectors:
        common = sp.Poly(1, h, domain=field)
        for entry in vector:
            common = common.lcm(sp.Poly(sp.fraction(simp(entry))[1], h, domain=field))
        col = vector.applyfunc(lambda entry: simp(common.as_expr() * entry))
        for entry in col:
            sp.Poly(entry, h, domain=field)  # certify polynomial, not Laurent
        columns.append(col)
    basis = sp.Matrix.hstack(*columns)
    steps = 0
    while True:
        residue = basis.subs(h, 0)
        dependencies = residue.nullspace()
        if not dependencies:
            break
        relation = dependencies[0]
        j = next(i for i, value in enumerate(relation) if value != 0)
        replacement = (basis * relation).applyfunc(lambda entry: simp(entry / h))
        for entry in replacement:
            sp.Poly(entry, h, domain=field)
        basis[:, j] = replacement
        steps += 1
    if (matrix * basis).applyfunc(simp) != sp.zeros(matrix.rows, basis.cols):
        raise ArithmeticError("Saturation lost the exact kernel identity")
    if basis.subs(h, 0).rank() != basis.cols:
        raise ArithmeticError("Residue columns are not independent")
    return basis, steps


def quadratic_monomials(xs: Sequence[sp.Symbol]) -> list[sp.Expr]:
    return [xs[i] * xs[j] for i, j in combinations_with_replacement(range(len(xs)), 2)]


def coefficient_vector(f: sp.Expr, xs: Sequence[sp.Symbol], monomials: Sequence[sp.Expr]) -> sp.Matrix:
    poly = sp.Poly(sp.expand(f), *xs)
    return sp.Matrix([poly.coeff_monomial(m) for m in monomials])


def integrability_matrix(quadrics: Sequence[sp.Expr], xs: Sequence[sp.Symbol]) -> sp.Matrix:
    n = len(xs)
    if len(quadrics) != n:
        raise ValueError("Need exactly N quadrics")
    unknowns = sp.symbols(f'a0:{n*n}')
    A = sp.Matrix(n, n, unknowns)
    g = A * sp.Matrix(quadrics)
    equations = []
    for i in range(n):
        for j in range(i + 1, n):
            poly = sp.Poly(sp.diff(g[i], xs[j]) - sp.diff(g[j], xs[i]), *xs)
            for variable in xs:
                eq = sp.expand(poly.coeff_monomial(variable))
                equations.append([eq.coeff(a) for a in unknowns])
    return sp.Matrix(equations)


def solve_unique_columns(M: sp.Matrix, rhs: sp.Matrix) -> sp.Matrix:
    """M has independent columns. Verify consistency instead of just sampling."""
    if M.cols == 0:
        if any(rhs):
            raise ValueError("Requested special solution has no algebraic lift")
        return sp.zeros(0, 1)
    rows = list(M.T.rref()[1])
    if len(rows) != M.cols:
        raise ValueError("Columns are not independent")
    answer = M.extract(rows, list(range(M.cols))).inv() * rhs.extract(rows, [0])
    answer = answer.applyfunc(simp)
    if (M * answer - rhs).applyfunc(simp) != sp.zeros(M.rows, 1):
        raise ValueError("Requested special solution has no algebraic lift")
    return answer


def recover(mu: sp.Matrix, xs: Sequence[sp.Symbol], h: sp.Symbol,
            special: sp.Expr, coefficients: Sequence[sp.Symbol] = ()) -> dict:
    n = len(xs)
    monomials = quadratic_monomials(xs)
    m = n * (n - 1) // 2
    if mu.shape != (m, len(monomials)):
        raise ValueError(f"Expected {(m, len(monomials))}, got {mu.shape}")
    mu = mu.applyfunc(simp)
    mu0 = mu.applyfunc(lambda e: regular_value(e, h))
    pivots = list(mu0.rref()[1])
    if len(pivots) != m:
        raise ValueError("Product is not surjective at the special fibre")
    free = [j for j in range(mu.cols) if j not in pivots]
    pivot_matrix = mu[:, pivots]
    block = (-(pivot_matrix.inv() * mu[:, free])).applyfunc(simp)
    Q = sp.zeros(mu.cols, n)
    for a, j in enumerate(free):
        Q[j, a] = 1
        for row, pivot in enumerate(pivots):
            Q[pivot, a] = block[row, a]
    if (mu * Q).applyfunc(simp) != sp.zeros(m, n):
        raise ArithmeticError("Wrong quadratic kernel")
    for entry in Q:
        regular_value(entry, h)
    quadrics = [sp.expand(sum(Q[j, a] * monomials[j] for j in range(len(monomials))))
                for a in range(n)]
    Q0 = Q.applyfunc(lambda e: regular_value(e, h))
    A0 = sp.zeros(n)
    for i, variable in enumerate(xs):
        target = coefficient_vector(sp.diff(special, variable), xs, monomials)
        A0[i, :] = solve_unique_columns(Q0, target).T
    if sp.simplify(A0.det()) == 0:
        raise ValueError("The special gradient is not a basis of the kernel")
    E = integrability_matrix(quadrics, xs)
    basis, steps = local_kernel(E, h, coefficients)
    values = solve_unique_columns(basis.subs(h, 0), sp.Matrix(list(A0)))
    A = sp.Matrix(n, n, basis * values).applyfunc(simp)
    g = A * sp.Matrix(quadrics)
    cubic = sp.expand(sum(xs[i] * g[i] for i in range(n)) / 3)
    cubic = sp.Add(*(simp(c) * sp.prod(x**e for x,e in zip(xs,powers))
                     for powers,c in sp.Poly(cubic, *xs).terms()))
    identities = [simp(sp.diff(cubic, xs[i]) - g[i]) for i in range(n)]
    if any(identities):
        raise ArithmeticError("Euler integration failed")
    if simp(cubic.subs(h, 0) - special) != 0:
        raise ArithmeticError("Special cubic was not preserved")
    if A.subs(h, 0).det() == 0:
        raise ArithmeticError("Recovered gradient change is not locally invertible")
    # This is over the coefficient FIELD. No assertion of uniformity at poles
    # of coefficient parameters is made.
    gb = sp.groebner([sp.diff(special, t) for t in xs], *xs,
                    domain=sp.QQ.frac_field(*coefficients) if coefficients else sp.QQ)
    smooth_special = gb.is_zero_dimensional
    if not smooth_special:
        raise ValueError("Special cubic is not smooth over the coefficient field")
    return dict(cubic=cubic, quadrics=quadrics, A=A, A0=A0,
                pivot_columns=pivots, kernel_matrix=Q,
                integrability_rank_generic=E.rank(),
                integrability_rank_special=E.subs(h, 0).rank(),
                saturated_kernel_rank=basis.cols, saturation_steps=steps,
                smooth_special_over_coefficient_field=smooth_special,
                checked_identities=True,
                computes_nc_natural_transformations=False,
                proves_generic_category_equivalence=False)


def encode(value):
    if isinstance(value, sp.MatrixBase):
        return [[str(e) for e in row] for row in value.tolist()]
    if isinstance(value, sp.Basic):
        return str(value)
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding='utf-8'))
    xs = tuple(sp.Symbol(n) for n in data['variables'])
    h = sp.Symbol(data['deformation_parameter'])
    parameters = tuple(sp.Symbol(n) for n in data.get('coefficient_parameters', []))
    names = {str(v): v for v in (*xs, h, *parameters)}
    # Input files are mathematical data, not untrusted executable programs.
    mu = sp.Matrix([[sp.sympify(e, locals=names) for e in row] for row in data['multiplication']])
    special = sp.sympify(data['special_cubic'], locals=names)
    result = recover(mu, xs, h, special, parameters)
    text = json.dumps(encode(result), ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    else:
        print(text, end='')

if __name__ == '__main__':
    main()
