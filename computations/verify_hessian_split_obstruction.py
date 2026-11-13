#!/usr/bin/env python3
"""Exact QQ-linear checks for one cubic with a reducible Hessian determinant.

Set F = x0**3 + x1**3 + h(z1,z2,z3,z4), where
h = sum(zi**3) - (sum(zi))**3.  This script computes the constant matrices
T satisfying Hess(F)*T = T.T*Hess(F) as polynomial identities, and checks
that their space is exactly {diag(a,b,c,c,c,c)}.  Its idempotents have
ranks 0, 1, 2, 4, 5, 6, so there is no rank-three projection in this space.

The manuscript explains why a (3,3) Thom--Sebastiani decomposition would
give such a projection, including invariance under linear coordinates.
Smoothness is proved there by the sign argument for grad(h), not by this
calculation.  This is an exact check of this single example over QQ, not
a universal coefficient verification or a proof of the Poisson classification.

Run: python3 computations/verify_hessian_split_obstruction.py
The only third-party dependency is sympy; the script writes no files.
"""
from itertools import combinations, product

import sympy as sp


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    variables = sp.symbols("x0 x1 z1 z2 z3 z4")
    x0, x1, *z = variables
    total = sum(z)
    h = sum(t**3 for t in z) - total**3
    F = x0**3 + x1**3 + h
    hessian = sp.hessian(F, variables)
    expected_hessian = sp.diag(
        6*x0, 6*x1, 6*(sp.diag(*z) - total*sp.ones(4))
    )
    require(hessian == expected_hessian, "Unexpected Hessian matrix")

    e3 = sum(sp.prod(triple) for triple in combinations(z, 3))
    e4 = sp.prod(z)
    determinant = sp.Poly(hessian.det(), *variables, domain=sp.QQ)
    expected_determinant = sp.Poly(
        6**6*x0*x1*(e4 - total*e3), *variables, domain=sp.QQ
    )
    require(determinant == expected_determinant,
            "Hessian determinant does not match the block formula")
    require(not determinant.is_zero, "Hessian determinant is identically zero")
    quotient = determinant.exquo(sp.Poly(x0*x1, *variables, domain=sp.QQ))
    require(quotient.total_degree() == 4,
            "The remaining Hessian factor should have degree four")

    # All six coefficient matrices are rational.  The upper-triangular
    # entries suffice because H*T - T.T*H is skew-symmetric.
    unknowns = sp.symbols("t0:36")
    T = sp.Matrix(6, 6, unknowns)
    residual = hessian*T - T.T*hessian
    equations = [
        sp.expand(residual[i, j]).coeff(v)
        for i, j in combinations(range(6), 2)
        for v in variables
    ]
    coefficients, rhs = sp.linear_eq_to_matrix(equations, unknowns)
    require(coefficients.shape == (90, 36), "Unexpected linear-system size")
    require(rhs == sp.zeros(90, 1), "The system should be homogeneous")
    require(all(entry.is_Rational for entry in coefficients),
            "The coefficient system must be over QQ")
    kernel = coefficients.nullspace()
    require(len(kernel) == 3, "The symmetrizer should have dimension three")
    require(all(entry.is_Rational for vector in kernel for entry in vector),
            "The computed kernel basis must be over QQ")

    expected_basis = (
        sp.diag(1, 0, 0, 0, 0, 0),
        sp.diag(0, 1, 0, 0, 0, 0),
        sp.diag(0, 0, 1, 1, 1, 1),
    )
    expected_span = sp.Matrix.hstack(
        *(matrix.reshape(36, 1) for matrix in expected_basis)
    )
    require(expected_span.rank() == 3, "Expected generators are dependent")
    require(coefficients*expected_span == sp.zeros(90, 3),
            "An expected generator does not symmetrize the Hessian")
    require(sp.Matrix.hstack(expected_span, *kernel).rank() == 3,
            "The computed kernel differs from the expected span")

    # This identity exhausts idempotents even after extending QQ to C:
    # each of a, b, c must independently satisfy u**2 - u = 0.
    a, b, c = sp.symbols("a b c")
    general = a*expected_basis[0] + b*expected_basis[1] + c*expected_basis[2]
    require(general**2 - general == sp.diag(
        a**2 - a, b**2 - b, c**2 - c, c**2 - c, c**2 - c, c**2 - c
    ), "Unexpected idempotent equations")
    idempotent_ranks = set()
    for values in product((0, 1), repeat=3):
        projection = general.subs(dict(zip((a, b, c), values)))
        require(projection**2 == projection, "Candidate is not idempotent")
        idempotent_ranks.add(projection.rank())
    require(sorted(idempotent_ranks) == [0, 1, 2, 4, 5, 6],
            "Unexpected ranks of symmetrizer idempotents")

    print("Scope: exact identities and QQ-linear algebra for this single cubic.")
    print("This does NOT prove a general Hessian criterion or the Poisson classification.")
    print("F = x0^3 + x1^3 + sum(z_i^3) - (sum(z_i))^3, i=1,...,4.")
    print("PASS Hess(F) = 6*diag(x0,x1,diag(z)-s*J), where s=sum(z_i).")
    print("PASS det Hess(F) = 6^6*x0*x1*(e4-s*e3), with e_j elementary symmetric in z.")
    print(f"Factorization over QQ: {sp.factor(determinant.as_expr())}")
    print(f"PASS symmetrizer: {coefficients.rows} coefficient equations, "
          f"{coefficients.cols} unknowns, rank {coefficients.cols-len(kernel)}, "
          f"kernel dimension {len(kernel)}.")
    print("PASS kernel span: diag(1,0,0,0,0,0), diag(0,1,0,0,0,0), diag(0,0,1,1,1,1).")
    print("PASS idempotent equations: a^2=a, b^2=b, c^2=c.")
    print(f"PASS possible idempotent ranks over C: {sorted(idempotent_ranks)}.")
    print("PASS no rank-three idempotent: the manuscript's (3,3) projection condition fails.")
    print("Smoothness and the geometric projection implication are proved in the manuscript.")


if __name__ == "__main__":
    main()
