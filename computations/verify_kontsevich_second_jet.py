#!/usr/bin/env python3
"""Exact checks for the Kontsevich second jet of the mixed cubic family.

All computations use SymPy's exact rational arithmetic and are taken modulo h^3.
The script checks polynomial identities, the three defining commutators, Weyl
symmetrization, and a presentation of the degree-two Jacobian quotient.  Graph
weights and categorical comparison theorems are inputs from the manuscript;
neither is a computational consequence of these checks.

Run:
    python computations/verify_kontsevich_second_jet.py
    python computations/verify_kontsevich_second_jet.py --output /tmp/certificate.json
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from functools import lru_cache
from itertools import combinations_with_replacement, permutations, product
import json
from pathlib import Path

import sympy as sp


x, y, z, u, v, lam, h = sp.symbols("x y z u v lambda h")
VARIABLES = (x, y, z, u, v)
ACTIVE = VARIABLES[:3]
F = (x**3 + y**3 + z**3) / 3 + u**3 + v**3 + lam * u * x * y


def truncate(expression):
    """Return the representative of h-degree at most two."""
    polynomial = sp.Poly(sp.expand(expression), h)
    return sp.expand(sum(polynomial.nth(i) * h**i for i in range(3)))


def assert_zero(expression):
    assert sp.expand(expression) == 0, sp.expand(expression)


def assert_zero_mod_h3(expression):
    assert_zero(truncate(expression))


def matrix_strings(matrix):
    return [
        [str(sp.expand(matrix[i, j])) for j in range(matrix.cols)]
        for i in range(matrix.rows)
    ]


def universal_hessian_identity():
    """Check Q=-2 adj(H) for a general symmetric three-by-three matrix."""
    H00, H01, H02, H11, H12, H22 = sp.symbols(
        "H00 H01 H02 H11 H12 H22"
    )
    H = sp.Matrix(
        [[H00, H01, H02], [H01, H11, H12], [H02, H12, H22]]
    )

    def dpi(i, j, ell):
        return sum(sp.LeviCivita(i, j, r) * H[r, ell] for r in range(3))

    Q = sp.Matrix(
        3, 3,
        lambda i, k: sp.expand(
            sum(
                dpi(i, j, ell) * dpi(k, ell, j)
                for j, ell in product(range(3), repeat=2)
            )
        ),
    )
    for entry in Q + 2 * H.adjugate():
        assert_zero(entry)
    contraction = sp.expand(
        sum(Q[i, k] * H[i, k] for i, k in product(range(3), repeat=2))
    )
    assert_zero(contraction + 6 * H.det())
    return {
        "symmetric_matrix": matrix_strings(H),
        "Q": matrix_strings(Q),
        "Q_equals_minus_two_adjugate": True,
        "contraction_Q_H_equals_minus_six_determinant": True,
    }


class StarProductJet:
    """The standard-angle Kontsevich product through order h^2.

    The normalization is B1(f,g)=pi^{ij} f_i g_j/2.  In this normalization
    the eye-graph term in B2 is -Q_{ik} f_i g_k/24.  It must not be confused
    with the inward two-wheel in the twisted tangent map, whose weight is zero.
    """

    def __init__(self, potential):
        self.potential = potential
        pi = sp.zeros(5)
        pi[0, 1] = sp.diff(potential, z)
        pi[1, 2] = sp.diff(potential, x)
        pi[2, 0] = sp.diff(potential, y)
        self.pi = pi - pi.T
        self.Q = sp.Matrix(
            5, 5,
            lambda i, k: sp.expand(
                sum(
                    sp.diff(self.pi[i, j], VARIABLES[ell])
                    * sp.diff(self.pi[k, ell], VARIABLES[j])
                    for j, ell in product(range(5), repeat=2)
                )
            ),
        )
        first = defaultdict(lambda: sp.S.Zero)
        second = defaultdict(lambda: sp.S.Zero)

        for i, j in product(range(5), repeat=2):
            first[((i,), (j,))] += self.pi[i, j] / 2

        for i, j, k, ell in product(range(3), repeat=4):
            coefficient = self.pi[i, j] * self.pi[k, ell] / 8
            second[(tuple(sorted((i, k))), tuple(sorted((j, ell))))] += (
                coefficient
            )
            coefficient = (
                self.pi[i, j]
                * sp.diff(self.pi[k, ell], VARIABLES[j])
                / 12
            )
            second[(tuple(sorted((i, k))), (ell,))] += coefficient
            second[((k,), tuple(sorted((i, ell))))] -= coefficient

        for i, k in product(range(5), repeat=2):
            second[((i,), (k,))] -= self.Q[i, k] / 24

        self.first = {
            indices: sp.expand(coefficient)
            for indices, coefficient in first.items()
            if sp.expand(coefficient) != 0
        }
        self.second = {
            indices: sp.expand(coefficient)
            for indices, coefficient in second.items()
            if sp.expand(coefficient) != 0
        }

    @staticmethod
    @lru_cache(maxsize=None)
    def derivative(polynomial, indices):
        if not indices:
            return polynomial
        return sp.diff(polynomial, *(VARIABLES[i] for i in indices))

    @lru_cache(maxsize=None)
    def B1(self, first, second):
        return sp.expand(
            sum(
                coefficient
                * self.derivative(first, left)
                * self.derivative(second, right)
                for (left, right), coefficient in self.first.items()
            )
        )

    @lru_cache(maxsize=None)
    def B2(self, first, second):
        return sp.expand(
            sum(
                coefficient
                * self.derivative(first, left)
                * self.derivative(second, right)
                for (left, right), coefficient in self.second.items()
            )
        )

    @lru_cache(maxsize=None)
    def star(self, first, second):
        first_poly = sp.Poly(sp.expand(first), h)
        second_poly = sp.Poly(sp.expand(second), h)
        answer = sp.S.Zero
        for i, j in product(range(3), repeat=2):
            if i + j > 2:
                continue
            f = first_poly.nth(i)
            g = second_poly.nth(j)
            if f == 0 or g == 0:
                continue
            answer += h ** (i + j) * f * g
            if i + j < 2:
                answer += h ** (i + j + 1) * self.B1(f, g)
            if i + j == 0:
                answer += h**2 * self.B2(f, g)
        return sp.expand(answer)

    def symmetrized_word(self, word):
        # Repeated permutations are intentional: their multiplicities give
        # the usual average over all permutations of the ordered word.
        orders = tuple(permutations(word))
        answer = sp.S.Zero
        for order in orders:
            term = sp.S.One
            for variable in order:
                term = self.star(term, variable)
            answer += term
        return sp.expand(answer / len(orders))

    def T2(self, polynomial):
        return sp.expand(
            -sum(
                self.Q[i, k] * sp.diff(polynomial, VARIABLES[i], VARIABLES[k])
                for i, k in product(range(5), repeat=2)
            )
            / 48
        )


def check_mixed_star():
    star = StarProductJet(F)
    H = sp.hessian(F, ACTIVE)
    determinant = sp.expand(H.det())
    assert_zero(determinant - (8 * x * y * z - 2 * lam**2 * u**2 * z))
    for entry in star.Q[:3, :3] + 2 * H.adjugate():
        assert_zero(entry)
    for i, k in product(range(5), repeat=2):
        if i >= 3 or k >= 3:
            assert_zero(star.Q[i, k])
    assert_zero(star.T2(F) - determinant / 8)

    for i, j, k in product(range(5), repeat=3):
        jacobi = sum(
            star.pi[i, ell] * sp.diff(star.pi[j, k], VARIABLES[ell])
            + star.pi[j, ell] * sp.diff(star.pi[k, i], VARIABLES[ell])
            + star.pi[k, ell] * sp.diff(star.pi[i, j], VARIABLES[ell])
            for ell in range(5)
        )
        assert_zero(jacobi)
    for i in range(5):
        assert_zero(
            sum(star.pi[i, j] * sp.diff(F, VARIABLES[j]) for j in range(5))
        )

    commutators = (
        star.star(y, z) - star.star(z, y)
        - h * (star.star(x, x) + lam * star.star(u, y)),
        star.star(z, x) - star.star(x, z)
        - h * (star.star(y, y) + lam * star.star(u, x)),
        star.star(x, y) - star.star(y, x) - h * star.star(z, z),
    )
    for relation in commutators:
        assert_zero_mod_h3(relation)
    for passive in (u, v):
        for variable in VARIABLES:
            assert_zero_mod_h3(star.star(passive, variable) - passive * variable)
            assert_zero_mod_h3(star.star(variable, passive) - variable * passive)

    symmetrizations = {}
    for indices in combinations_with_replacement(range(5), 3):
        word = tuple(VARIABLES[i] for i in indices)
        monomial = sp.prod(word)
        image = star.symmetrized_word(word)
        assert_zero_mod_h3(image - monomial - h**2 * star.T2(monomial))
        symmetrizations[str(monomial)] = str(sp.expand(star.T2(monomial)))
    assert len(symmetrizations) == 35

    # These finite checks support, but do not replace, the formality theorem.
    associators_checked = 0
    for first, second, third in product(VARIABLES, repeat=3):
        assert_zero_mod_h3(
            star.star(star.star(first, second), third)
            - star.star(first, star.star(second, third))
        )
        associators_checked += 1

    a = lam * u
    sym_xyz_sum = sum(
        star.star(star.star(order[0], order[1]), order[2])
        for order in permutations(ACTIVE)
    )
    omega_image = truncate(
        sum(star.star(star.star(w, w), w) for w in ACTIVE) / 3
        - h**2 * sym_xyz_sum / 9
        + a * (star.star(x, y) + star.star(y, x)) / 2
        + h**2 * a**2 * z / 6
        + u**3 + v**3
    )
    G2 = sp.expand(determinant / 24)
    G = sp.expand(F + h**2 * G2)
    assert_zero_mod_h3(omega_image - G)

    return star, G, {
        "potential": str(F),
        "poisson_matrix": matrix_strings(star.pi),
        "active_hessian": matrix_strings(H),
        "active_hessian_determinant": str(determinant),
        "Q": matrix_strings(star.Q),
        "jacobi_and_casimir_identities": True,
        "three_commutator_relations_mod_h3": True,
        "passive_generators_multiply_undeformed": True,
        "cubic_weyl_symmetrization_count": len(symmetrizations),
        "cubic_weyl_h2_coefficients": symmetrizations,
        "generator_associators_checked": associators_checked,
        "T2_F": str(star.T2(F)),
        "omega_image": str(omega_image),
        "G2": str(G2),
        "omega_image_equals_F_plus_h2_Hessian_over_24": True,
    }


def check_jacobian_product(G):
    pairs = tuple(combinations_with_replacement(range(5), 2))
    monomials = tuple(VARIABLES[i] * VARIABLES[j] for i, j in pairs)
    square_columns = tuple(k for k, (i, j) in enumerate(pairs) if i == j)
    free_columns = tuple(k for k, (i, j) in enumerate(pairs) if i != j)
    free_monomials = tuple(monomials[k] for k in free_columns)
    gradient = tuple(sp.expand(sp.diff(G, variable)) for variable in VARIABLES)
    R = sp.Matrix(
        [
            [sp.Poly(q, *VARIABLES).coeff_monomial(m) for m in monomials]
            for q in gradient
        ]
    )
    D = R[:, list(square_columns)]
    assert_zero(D.det() - 9)
    normalized_kernel = (D.inv() * R).applyfunc(truncate)
    quotient = sp.zeros(10, 15)
    for row, column in enumerate(free_columns):
        quotient[row, column] = 1
    for square_row, column in enumerate(square_columns):
        for row, free_column in enumerate(free_columns):
            quotient[row, column] = -normalized_kernel[square_row, free_column]
    quotient = quotient.applyfunc(truncate)

    for entry in quotient * R.T:
        assert_zero_mod_h3(entry)
    for entry in quotient[:, list(free_columns)] - sp.eye(10):
        assert_zero(entry)
    for entry in normalized_kernel[:, list(square_columns)] - sp.eye(5):
        assert_zero(entry)
    for entry in D * normalized_kernel - R:
        assert_zero_mod_h3(entry)

    expected_squares = (
        -lam * u * y - h**2 * y * z / 3,
        -lam * u * x - h**2 * x * z / 3,
        -h**2 * (sp.Rational(1, 3) + lam**3 / 36) * x * y,
        -lam * x * y / 3 + h**2 * lam**2 * u * z / 18,
        sp.S.Zero,
    )
    square_products = {}
    for column, expected in zip(square_columns, expected_squares):
        recovered = sp.expand(
            sum(quotient[row, column] * free_monomials[row] for row in range(10))
        )
        assert_zero_mod_h3(recovered - expected)
        square_products[str(monomials[column])] = str(recovered)

    assert_zero(sum(variable * q for variable, q in zip(VARIABLES, gradient)) / 3 - G)
    for i, j in product(range(5), repeat=2):
        assert_zero(
            sp.diff(gradient[i], VARIABLES[j])
            - sp.diff(gradient[j], VARIABLES[i])
        )

    G2 = sp.expand((G - F) / h**2)
    c = sp.Rational(1, 3) + lam**3 / 36
    jacobian_certificate = -lam**2 * z * sp.diff(F, u) / 36
    assert_zero(G2 - c * x * y * z - jacobian_certificate)
    assert_zero(sp.Poly(c, lam).nth(3) - sp.Rational(1, 36))

    return {
        "scope": (
            "Jacobian quotient of G; the manuscript MF theorem identifies its "
            "low Nat product; the projective residual bridge remains separate"
        ),
        "G": str(G),
        "gradient": [str(q) for q in gradient],
        "symmetric_square_basis": [str(m) for m in monomials],
        "quotient_basis": [str(m) for m in free_monomials],
        "gradient_coefficient_matrix_5_by_15": matrix_strings(R),
        "square_minor_determinant": str(D.det()),
        "normalized_kernel_matrix_5_by_15": matrix_strings(normalized_kernel),
        "product_matrix_10_by_15": matrix_strings(quotient),
        "product_annihilates_gradient_mod_h3": True,
        "kernel_has_identity_square_minor": True,
        "product_has_identity_cross_term_minor": True,
        "square_products": square_products,
        "euler_recovery_and_integrability": True,
        "c_lambda": str(c),
        "lambda_cubed_coefficient": str(sp.Rational(1, 36)),
        "jacobian_class_identity": {
            "left_hand_side": str(sp.expand(G2 - c * x * y * z)),
            "right_hand_side": str(sp.expand(jacobian_certificate)),
            "formula": "G2-c(lambda)*x*y*z = -lambda^2*z*F_u/36",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("kontsevich_second_jet_certificate.json"),
    )
    args = parser.parse_args()
    tensor_identity = universal_hessian_identity()
    _, G, mixed = check_mixed_star()
    jacobian_product = check_jacobian_product(G)
    certificate = {
        "version": 1,
        "date": "2026-11-10",
        "status": "All listed exact polynomial and matrix checks passed.",
        "coefficient_ring": "Q[lambda,x,y,z,u,v,h]/(h^3)",
        "limitations": [
            (
                "Graph weights are taken from Dito Eq. (3) and Shoikhet "
                "Section 1.3; this script does not recompute graph integrals."
            ),
            (
                "Kontsevich formality and the curved Maurer--Cartan comparison "
                "are mathematical inputs, not outputs of this computation."
            ),
            (
                "No categorical equivalence or direct computation of a "
                "noncommutative derived Nat complex is certified by this script."
            ),
            (
                "The MF interpretation of the product table is proved in the "
                "manuscript, not by this script; the qgr residual comparison is additional."
            ),
        ],
        "universal_tensor_identity": tensor_identity,
        "mixed_star_product": mixed,
        "jacobian_product": jacobian_product,
        "references": [
            {
                "author": "Giuseppe Dito",
                "title": "Kontsevich star-product on the dual of a Lie algebra",
                "identifier": "arXiv:math/9905080",
                "url": "https://arxiv.org/pdf/math/9905080",
                "location": "Equation (3), printed page 5",
                "normalization": "The bivector in Dito's first-order term is pi/2 here.",
            },
            {
                "author": "Boris Shoikhet",
                "title": "Vanishing of the Kontsevich integrals of the wheels",
                "identifier": "arXiv:math/0007080",
                "url": "https://arxiv.org/pdf/math/0007080",
                "location": "Section 1.3",
                "use": "Vanishing of the inward wheel in the twisted tangent map.",
            },
            {
                "author": "Maxim Kontsevich",
                "title": "Deformation quantization of Poisson manifolds, I",
                "identifier": "arXiv:q-alg/9709040",
                "url": "https://arxiv.org/pdf/q-alg/9709040",
                "location": "Sections 4.3--4.6, 6, and 8.3.3.1",
            },
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print("PASS: general symmetric 3x3 Hessian tensor identities")
    print("PASS: 3 commutators, 35 cubic symmetrizations, 125 generator associators")
    print("PASS: Omega maps to F+h^2*det(H_active)/24 modulo h^3")
    print("PASS: 10x15 product and 5x15 kernel matrices; square minor determinant 9")
    print(
        "PASS: Jacobian coefficient c(lambda)=1/3+lambda^3/36 "
        "(MF interpretation uses the manuscript proof)"
    )
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
