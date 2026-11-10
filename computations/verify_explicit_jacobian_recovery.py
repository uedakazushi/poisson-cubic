#!/usr/bin/env python3
"""Exact low-degree cubic recovery checks over QQ.

The multiplication inputs here are commutative polynomial quotients.  This
script does not compute derived natural transformations of any nc cubic,
does not verify smoothness of a dg category, and does not prove a category
equivalence.  See papers/reconstruction/explicit_jacobian_recovery.tex.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import combinations_with_replacement
from pathlib import Path

import sympy as sp


def exponent_vectors(total: int, length: int):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in exponent_vectors(total - first, length - 1):
            yield (first,) + tail


def quadratic_quotient(q, variables):
    """Return Sym^2(V) -> (S/(q))_2 in explicit monomial bases."""
    pairs = list(combinations_with_replacement(range(len(variables)), 2))
    monomials = [variables[i] * variables[j] for i, j in pairs]
    relation_matrix = sp.Matrix(
        [[sp.Poly(f, *variables).coeff_monomial(m) for m in monomials] for f in q]
    )
    rref, pivots = relation_matrix.rref()
    assert len(pivots) == len(q)
    free = [j for j in range(len(monomials)) if j not in pivots]
    quotient = sp.zeros(len(free), len(monomials))
    for row, col in enumerate(free):
        quotient[row, col] = 1
    for row, pivot in enumerate(pivots):
        for target, col in enumerate(free):
            quotient[target, pivot] = -rref[row, col]
    assert quotient * relation_matrix.T == sp.zeros(len(free), len(q))
    return pairs, monomials, quotient


def symmetric_tensor_multiplication(pairs, quotient, number_of_variables):
    """A genuine V tensor V table, before checking it descends to Sym^2 V."""
    columns = {pair: quotient[:, col] for col, pair in enumerate(pairs)}
    return sp.Matrix.hstack(
        *[
            columns[tuple(sorted((i, j)))]
            for i in range(number_of_variables)
            for j in range(number_of_variables)
        ]
    )


def descend_symmetric(tensor_table, number_of_variables):
    for i in range(number_of_variables):
        for j in range(i + 1, number_of_variables):
            if tensor_table[:, i * number_of_variables + j] != tensor_table[
                :, j * number_of_variables + i
            ]:
                raise ValueError("The degree-one product is not symmetric.")
    return sp.Matrix.hstack(
        *[
            tensor_table[:, i * number_of_variables + j]
            for i, j in combinations_with_replacement(range(number_of_variables), 2)
        ]
    )


def recovered_quadrics(quotient, monomials):
    return [
        sp.expand(sum(coefficient * monomial for coefficient, monomial in zip(v, monomials)))
        for v in quotient.nullspace()
    ]


def integrability_space(q, variables):
    number = len(variables)
    assert len(q) == number
    unknowns = sp.symbols(f"a0:{number * number}")
    matrix = sp.Matrix(number, number, unknowns)
    quadrics = matrix * sp.Matrix(q)
    equations = []
    for i in range(number):
        for j in range(i + 1, number):
            difference = sp.Poly(
                sp.diff(quadrics[i], variables[j])
                - sp.diff(quadrics[j], variables[i]),
                *variables,
            )
            equations.extend(difference.coeff_monomial(x) for x in variables)
    linear_matrix, rhs = sp.linear_eq_to_matrix(equations, unknowns)
    assert rhs == sp.zeros(len(equations), 1)
    basis = [sp.Matrix(number, number, v) for v in linear_matrix.nullspace()]
    return linear_matrix, basis


def euler_integrate(q, variables, matrix):
    gradient = matrix * sp.Matrix(q)
    polynomial = sp.expand(sum(x * g for x, g in zip(variables, gradient)) / 3)
    assert all(
        sp.expand(sp.diff(polynomial, x) - g) == 0
        for x, g in zip(variables, gradient)
    )
    return polynomial


def hilbert_function(q, variables, final_degree):
    groebner = sp.groebner(q, *variables, domain=sp.QQ)
    assert groebner.is_zero_dimensional
    leading_exponents = [p.LM(order=groebner.order).exponents for p in groebner.polys]
    counts = []
    for degree in range(final_degree + 1):
        count = 0
        for exponent in exponent_vectors(degree, len(variables)):
            if not any(
                all(a >= b for a, b in zip(exponent, leading))
                for leading in leading_exponents
            ):
                count += 1
        counts.append(count)
    return counts


def proportional(first, second, variables):
    p, q = sp.Poly(first, *variables), sp.Poly(second, *variables)
    ratio = p.LC() / q.coeff_monomial(p.monoms()[0])
    assert ratio != 0 and sp.expand(first - ratio * second) == 0
    return ratio


def polynomial_recovery(name, polynomial, variables):
    original_gradient = [sp.diff(polynomial, variable) for variable in variables]
    pairs, monomials, quotient = quadratic_quotient(original_gradient, variables)
    tensor_table = symmetric_tensor_multiplication(pairs, quotient, len(variables))
    assert descend_symmetric(tensor_table, len(variables)) == quotient
    q = recovered_quadrics(quotient, monomials)
    linear_matrix, basis = integrability_space(q, variables)
    assert basis
    chosen = sum(basis, sp.zeros(len(variables)))
    assert chosen.det() != 0
    recovered = euler_integrate(q, variables, chosen)
    ratio = proportional(recovered, polynomial, variables)
    counts = hilbert_function(q, variables, len(variables) + 1)
    expected = [int(sp.binomial(len(variables), i)) for i in range(len(variables) + 1)] + [0]
    assert counts == expected
    return {
        "example": name,
        "variables": len(variables),
        "input_polynomial": str(polynomial),
        "low_degree_dimensions": {"V": len(variables), "W": quotient.rows, "K": len(q)},
        "commutative_tensor_product_checked": True,
        "quotient_multiplication_rank": quotient.rank(),
        "integrability_matrix_shape": list(linear_matrix.shape),
        "integrability_matrix_rank": linear_matrix.rank(),
        "integrability_kernel_dimension": len(basis),
        "chosen_integrating_determinant": str(chosen.det()),
        "recovered_polynomial": str(recovered),
        "recovered_to_input_scalar": str(ratio),
        "gradient_identity_checked": True,
        "homogeneous_common_zero_only_origin": True,
        "hilbert_function": counts,
    }, tensor_table


def cycle_obstruction(variables):
    number = len(variables)
    assert number == 5
    q = [
        variables[i] ** 2 + variables[(i + 1) % number] * variables[(i + 2) % number]
        for i in range(number)
    ]
    linear_matrix, basis = integrability_space(q, variables)
    assert not basis
    pivot_rows = list(linear_matrix.T.rref()[1])
    minor = linear_matrix.extract(pivot_rows, range(number * number))
    determinant = minor.det()
    assert determinant != 0
    counts = hilbert_function(q, variables, 6)
    assert counts == [1, 5, 10, 10, 5, 1, 0]
    return {
        "example": "nonintegrable_cyclic_complete_intersection",
        "quadrics": [str(f) for f in q],
        "homogeneous_common_zero_only_origin": True,
        "hilbert_function": counts,
        "integrability_matrix_shape": list(linear_matrix.shape),
        "integrability_matrix_rank": linear_matrix.rank(),
        "integrability_kernel_dimension": 0,
        "full_rank_minor_rows_zero_based": pivot_rows,
        "full_rank_minor_determinant": str(determinant),
        "is_cubic_jacobian": False,
        "elementary_proof": "papers/reconstruction/explicit_jacobian_recovery.tex, proposition prop:ej-nonintegrable-ci",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("explicit_jacobian_certificate.json"),
    )
    args = parser.parse_args()
    variables = sp.symbols("x0:5")
    fermat = sum(x ** 3 for x in variables) / 3
    mixed = (
        fermat
        + sp.Rational(1, 2) * variables[0] * variables[1] * variables[2]
        + sp.Rational(1, 3) * variables[2] * variables[3] * variables[4]
    )
    fermat_check, tensor_table = polynomial_recovery("fermat_cubic_threefold", fermat, variables)
    mixed_check, _ = polynomial_recovery("mixed_smooth_cubic_threefold", mixed, variables)
    assert fermat_check["integrability_kernel_dimension"] == 5
    assert mixed_check["integrability_kernel_dimension"] == 1
    bad_table = tensor_table.copy()
    bad_table[0, 1] += 1  # alter mu(x0,x1) without altering mu(x1,x0)
    try:
        descend_symmetric(bad_table, len(variables))
    except ValueError:
        asymmetry_rejected = True
    else:
        raise AssertionError("A nonsymmetric product was incorrectly accepted.")
    result = {
        "date": "2026-11-10",
        "version": "v21",
        "arithmetic": "exact rational arithmetic with SymPy",
        "scope": "finite polynomial/linear-algebra recovery; no nc dg Hom computation or categorical equivalence",
        "examples": [fermat_check, mixed_check, cycle_obstruction(variables)],
        "nonsymmetric_product_rejected_before_Sym2": asymmetry_rejected,
        "all_assertions_passed": True,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"all_assertions_passed": True, "output": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
