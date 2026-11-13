#!/usr/bin/env python3
"""Exact finite checks for paper B's noncommutative Hesse recovery example.

All coefficients are rational; h is symbolic. Checks the two exact scalar
identities used to import the known Sklyanin center, three central
commutators modulo h**4, and the Weyl first product modulo h**2. Evaluates
Dito's full harmonic-angle second-order product, its Weyl gauge, the central
image modulo h**3, and the corresponding Jacobian classes.
Also checks the rational point-curve Hesse coefficient, its Weierstrass
transformation and invariants, the cleared-denominator cubic, its low jet,
and the smooth special fibre by exact polynomial and rational identities.

The graph weights and Shoikhet's inner-wheel vanishing are cited inputs,
not configuration integrals computed here. These finite checks do not
prove all-degree flatness, formality, THCR identifications, Orlov
equivalences, or an all-order categorical comparison. Those claims have
separate proofs and cited inputs in the paper.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product
import json
from pathlib import Path

import sympy as sp

Word = tuple[int, ...]
R = Fraction


def sym_word(word: Word) -> dict[Word, Fraction]:
    words = set(permutations(word))
    return {w: R(1, len(words)) for w in words}


@lru_cache(maxsize=None)
def normal(word: Word, budget: int) -> dict[tuple[Word, int], Fraction]:
    """An equality-preserving reduction, truncated in h (not a PBW proof)."""
    if budget < 0:
        return {}
    for i in range(len(word) - 1):
        p, q = word[i:i + 2]
        if p <= q:
            continue
        # yx = xy - h z² - h²(xy+yx)/2, and cyclic versions.
        sign, square = {(1, 0): (-1, 2), (2, 0): (1, 1),
                        (2, 1): (-1, 0)}[(p, q)]
        replacements = [((q, p), R(1), 0),
                        ((square, square), R(sign), 1),
                        ((p, q), R(sign, 2), 2),
                        ((q, p), R(sign, 2), 2)]
        result = defaultdict(Fraction)
        for pair, coefficient, exponent in replacements:
            changed = word[:i] + pair + word[i + 2:]
            for (ordered, power), value in normal(changed, budget - exponent).items():
                result[(ordered, power + exponent)] += coefficient * value
        return {key: value for key, value in result.items() if value}
    return {(word, 0): R(1)}


def add_normal(result, word, coefficient, shift, budget):
    for (ordered, power), value in normal(word, budget - shift).items():
        result[(ordered, power + shift)] += coefficient * value


def assert_zero(result, label):
    bad = {str(key): str(value) for key, value in result.items() if value}
    assert not bad, (label, bad)


def central_commutator(generator):
    # u_h = 1 mod h**4, v_h = h - 2*h**2/3 mod h**4.
    terms = [(w, R(1, 3), 0) for w in ((0, 0, 0), (1, 1, 1), (2, 2, 2))]
    for word, coefficient in sym_word((0, 1, 2)).items():
        terms.extend([(word, coefficient, 1), (word, -R(2, 3) * coefficient, 2)])
    result = defaultdict(Fraction)
    for word, coefficient, shift in terms:
        add_normal(result, word + (generator,), coefficient, shift, 3)
        add_normal(result, (generator,) + word, -coefficient, shift, 3)
    assert_zero(result, f"central commutator with {generator} mod h^4")


def poisson_words(left, right):
    result = defaultdict(Fraction)
    for i, p in enumerate(left):
        for j, q in enumerate(right):
            if p == q:
                continue
            sign, square = {
                (0, 1): (1, 2), (1, 0): (-1, 2),
                (1, 2): (1, 0), (2, 1): (-1, 0),
                (2, 0): (1, 1), (0, 2): (-1, 1)
            }[(p, q)]
            word = tuple(sorted(left[:i] + left[i + 1:]
                                + right[:j] + right[j + 1:] + (square, square)))
            result[word] += R(sign)
    return {key: value for key, value in result.items() if value}


def first_product(left, right):
    result = defaultdict(Fraction)
    for wl, cl in sym_word(left).items():
        for wr, cr in sym_word(right).items():
            add_normal(result, wl + wr, cl * cr, 0, 1)
    for word, coefficient in sym_word(left + right).items():
        add_normal(result, word, -coefficient, 0, 1)
    for word, coefficient in poisson_words(left, right).items():
        for w, c in sym_word(word).items():
            add_normal(result, w, -coefficient * c / 2, 1, 1)
    assert_zero(result, f"Weyl first product {left}, {right}")


def second_jet_checks(h, uh, vh):
    """Exact algebra for the second jet, conditional on cited graph weights.

    Inputs uh,vh are the exact scalar coefficients of the central cubic.
    Dito's full harmonic-angle B2 and Shoikhet's inner W2=0 are mathematical
    inputs. The script evaluates B2 and the resulting gauge, center image,
    and Jacobian classes; it does not evaluate any configuration integral
    or prove the existence of all-order formality or the strict isomorphism.
    """
    x, y, z, u, v = sp.symbols("x y z u v")
    active, variables = (x, y, z), (x, y, z, u, v)
    P0 = sp.Matrix([[0, z**2, -y**2],
                    [-z**2, 0, x**2], [y**2, -x**2, 0]])
    theta = sp.Matrix(3, 3, lambda i, k: sp.expand(sum(
        sp.diff(P0[i, j], active[l]) * sp.diff(P0[k, l], active[j])
        for j in range(3) for l in range(3))))
    assert theta == sp.diag(-8*y*z, -8*x*z, -8*x*y)

    def B2(f, g):
        # Dito, math/9905080v1, (3), with his pi replaced by P0/2.
        value = sum(
            P0[i, j]*P0[k, l]*sp.diff(f, active[i], active[k])
            * sp.diff(g, active[j], active[l])/8
            + P0[i, j]*sp.diff(P0[k, l], active[i])
            * (sp.diff(f, active[j], active[l])*sp.diff(g, active[k])
               + sp.diff(f, active[k])*sp.diff(g, active[j], active[l]))/12
            for i, j, k, l in product(range(3), repeat=4))
        value -= sum(theta[i, k]*sp.diff(f, active[i])*sp.diff(g, active[k])
                     for i in range(3) for k in range(3))/24
        return sp.expand(value)

    def rho2(f):
        return sp.expand(-sum(theta[i, k]*sp.diff(f, active[i], active[k])
                              for i in range(3) for k in range(3))/48)

    def truncate(f):
        expanded = sp.expand(f)
        return sp.expand(sum(expanded.coeff(h, j)*h**j for j in range(3)))

    assert B2(x, x) == y*z/3
    assert B2(x**2, x) == 2*x*y*z/3

    # A polynomial identity in five independent linear coefficients checks
    # the degree-two and degree-three Weyl gauge by polarization. Both
    # first-order brackets and the P1 term vanish on powers of one X.
    linear_coefficients = sp.symbols("ell_x ell_y ell_z ell_u ell_v")
    X = sum(a*q for a, q in zip(linear_coefficients, variables))
    assert sp.expand(B2(X, X) - rho2(X**2)) == 0
    assert sp.expand(B2(X**2, X) + X*B2(X, X) - rho2(X**3)) == 0

    F = sum(q**3 for q in variables)/3
    assert rho2(F) == x*y*z
    omega_symbol = truncate(uh*(x**3+y**3+z**3)/3 + vh*x*y*z
                            + (u**3+v**3)/3)
    assert sp.expand(omega_symbol - F - h*x*y*z
                     + sp.Rational(2, 3)*h**2*x*y*z) == 0
    phi_omega = truncate(omega_symbol + h**2*rho2(omega_symbol))
    expected = F + h*x*y*z + sp.Rational(1, 3)*h**2*x*y*z
    assert sp.expand(phi_omega - expected) == 0
    # Identifying this image with W_rec modulo h**3 additionally uses the
    # cited analytic theorem C_pi = Id + O(h**3); it is not proved here.
    ideal = sp.groebner([q**2 for q in variables], *variables, domain=sp.QQ)
    first_class = ideal.reduce(x*y*z)[1]
    second_class = ideal.reduce(x*y*z/3)[1]
    assert first_class == x*y*z and second_class == x*y*z/3

    return {
        "full_harmonic_angle_B2_source": "Dito math/9905080v1 (3), pi=P0/2",
        "theta_active_matrix": [[str(theta[i, k]) for k in range(3)]
                                 for i in range(3)],
        "B2_x_x": str(B2(x, x)),
        "B2_x2_x": str(B2(x**2, x)),
        "rho2_F": str(rho2(F)),
        "weyl_gauge_polynomial_identity_degrees": [2, 3],
        "center_image_mod_h3": str(phi_omega),
        "recovered_potential_mod_h3": str(expected),
        "jacobian_remainder_first_coefficient": str(first_class),
        "jacobian_remainder_second_coefficient": str(second_class),
        "analytic_input_not_recomputed":
            "Shoikhet math/0007080: harmonic-angle inner W2=0; "
            "with the graph classification this gives C_pi=Id mod h^3",
        "scope": "Exact finite polynomial identities only. Graph weights, "
                 "all-order formality, and the strict comparison are cited "
                 "or proved separately in the manuscript.",
    }


def rational_hesse_checks(h, a, b, c, second_jet):
    """Exact identities for the point cubic and a rational Hesse model.

    These calculations do not identify any categories or prove that the
    recovered formal Hesse series equals the point-curve coefficient at
    all orders. That identification uses the separate THCR/Orlov argument.
    """
    lam = sp.symbols("lambda")
    x, y, z, u, v, X, Y, Z, T = sp.symbols("x y z u v X Y Z T")
    variables = (x, y, z, u, v)
    active_sum = x**3 + y**3 + z**3
    F = sum(q**3 for q in variables)/3
    lambda_point = (h + h**2/3 + h**5/12)/(1 - h**4/4)
    assert sp.cancel(-(a**3 + b**3 + c**3)/(3*a*b*c)
                     - lambda_point) == 0

    # Invert X=z, Y=x-y, Z=x+y-lambda*z simultaneously.
    hesse_cubic = active_sum + 3*lam*x*y*z
    inverse_coordinates = {x: (Z + lam*X + Y)/2,
                           y: (Z + lam*X - Y)/2, z: X}
    transformed = sp.expand(4*hesse_cubic.subs(inverse_coordinates,
                                              simultaneous=True))
    expected_transform = (3*Z*Y**2 + 4*(1 + lam**3)*X**3
                          + 9*lam**2*X**2*Z + 6*lam*X*Z**2 + Z**3)
    assert sp.expand(transformed - expected_transform) == 0
    coordinate_matrix = sp.Matrix([[0, 0, 1], [1, -1, 0], [1, 1, -lam]])
    assert coordinate_matrix.det() == 2

    # First Y^2 Z = alpha X^3 + beta X^2 Z + gamma X Z^2 + delta Z^3.
    # Then (X_w,Y_w,Z_w)=(alpha X,alpha Y,Z) gives the monic model.
    alpha = -sp.Rational(4, 3)*(1 + lam**3)
    beta, gamma, delta = -3*lam**2, -2*lam, -sp.Rational(1, 3)
    a2, a4, a6 = beta, alpha*gamma, alpha**2*delta
    monic_cubic = T**3 + a2*T**2 + a4*T + a6
    b2, b4, b6 = 4*a2, 2*a4, 4*a6
    b8 = 4*a2*a6 - a4**2
    c4 = sp.expand(b2**2 - 24*b4)
    c6 = sp.expand(-b2**3 + 36*b2*b4 - 216*b6)
    discriminant = sp.expand(-b2**2*b8 - 8*b4**3 - 27*b6**2
                             + 9*b2*b4*b6)
    expected_c4 = 16*lam*(lam**3 - 8)
    expected_discriminant = -sp.Rational(4096, 27)*(1 + lam**3)**3
    expected_j = 27*lam**3*(8 - lam**3)**3/(1 + lam**3)**3
    assert sp.expand(c4 - expected_c4) == 0
    assert sp.expand(discriminant - expected_discriminant) == 0
    assert sp.expand(c4**3 - c6**2 - 1728*discriminant) == 0
    assert sp.expand(discriminant - 16*sp.discriminant(monic_cubic, T)) == 0
    assert sp.cancel(c4**3/discriminant - expected_j) == 0

    Q = ((4 - h**4)*sum(q**3 for q in variables)
         + (12*h + 4*h**2 + h**5)*x*y*z)
    assert sp.cancel(Q - 3*(4 - h**4)*(F + lambda_point*x*y*z)) == 0
    lambda_low_jet = sp.series(lambda_point, h, 0, 3).removeO()
    assert lambda_low_jet == h + h**2/3
    recovered_low_jet = F + lambda_low_jet*x*y*z
    independent_low_jet = sp.sympify(second_jet["recovered_potential_mod_h3"])
    assert sp.expand(recovered_low_jet - independent_low_jet) == 0

    # The special cubic is 4 times the Fermat cubic sum. In each projective
    # chart q=1, its partial derivatives generate the unit ideal; these are
    # exact certificates that the five standard charts have no singularity.
    special_Q = sp.expand(Q.subs(h, 0))
    assert special_Q == 4*sum(q**3 for q in variables)
    partials = [sp.diff(special_Q, q) for q in variables]
    assert partials == [12*q**2 for q in variables]
    for coordinate in variables:
        chart_ideal = sp.groebner(partials + [coordinate - 1],
                                  *variables, domain=sp.QQ)
        assert list(chart_ideal) == [1]
    assert sp.cancel((1 + lambda_point**3).subs(h, 0)) == 1

    return {
        "lambda_point": str(lambda_point),
        "sklyanin_ratio_identity": "-(a^3+b^3+c^3)/(3abc) = lambda_point",
        "weierstrass_coordinates": "X=z, Y=x-y, Z=x+y-lambda*z",
        "coordinate_determinant": str(coordinate_matrix.det()),
        "four_times_transformed_hesse_cubic": str(expected_transform),
        "monic_weierstrass_coefficients": {
            "a1": "0", "a2": str(a2), "a3": "0",
            "a4": str(sp.expand(a4)), "a6": str(sp.expand(a6)),
        },
        "c4": str(expected_c4),
        "discriminant": str(expected_discriminant),
        "j_invariant": str(expected_j),
        "discriminant_cross_checks": [
            "c4^3-c6^2 = 1728*Delta", "Delta = 16*disc(monic cubic)"],
        "cleared_denominator_Q": str(Q),
        "Q_identity": "Q = 3*(4-h^4)*(F+lambda_point*x*y*z)",
        "lambda_point_mod_h3": str(lambda_low_jet),
        "matches_independent_recovered_second_jet": True,
        "special_fibre_Q": str(special_Q),
        "smooth_special_fibre_projective_charts_verified": len(variables),
        "scope": "Exact symbolic polynomial and rational identities only. "
                 "No THCR identification, Orlov equivalence, or all-order "
                 "categorical argument identifying the recovered series "
                 "with lambda_point is verified by these computations.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    h, S, P = sp.symbols("h S P")
    a, b, c = 1 - h**2 / 2, -1 - h**2 / 2, -h
    uh = 1 + h**4 / 2 + h**5 / 6 - h**8 / 48
    vh = (4 - h**4) * (12*h + h**5 - 8*h**2) / 48
    delta = (h + h**2 / 3 * (1 + h**3 / 4))**3 + (1 - h**4 / 4)**3
    assert sp.expand((a**3 + b**3 + c**3)**3 - (3*a*b*c)**3 + 27*h**3*delta) == 0
    C = (P + h*S + h**2 * P/2) / 2
    D = (P - h*S - h**2 * P/2) / 2
    G = a*(b**3 - c**3)*C + b*(c**3 - a**3)*D + c*(a**3 - b**3)*S
    assert sp.expand(G + 9*h*(uh*S/3 + vh*P/6)) == 0
    assert sp.series(uh, h, 0, 2).removeO() == 1
    assert sp.series(vh, h, 0, 2).removeO() == h
    for generator in range(3):
        central_commutator(generator)

    monomials = [tuple(sorted(word)) for degree in range(4)
                 for word in product(range(3), repeat=degree)]
    monomials = sorted(set(monomials), key=lambda w: (len(w), w))
    assert len(monomials) == 20
    for left in monomials:
        for right in monomials:
            first_product(left, right)
    commutator = defaultdict(Fraction)
    add_normal(commutator, (1, 2), R(1), 0, 1)
    add_normal(commutator, (2, 1), R(-1), 0, 1)
    assert {k: v for k, v in commutator.items() if v} == {((0, 0), 1): R(1)}

    x, y, z, u, v = sp.symbols("x y z u v")
    variables = (x, y, z, u, v)
    ideal = sp.groebner([q**2 for q in variables], *variables)
    assert ideal.reduce(x*y*z)[1] == x*y*z
    second_jet = second_jet_checks(h, uh, vh)
    rational_hesse = rational_hesse_checks(h, a, b, c, second_jet)
    output = {
        "status": "passed",
        "coefficient_ring": "Q[h, lambda] and Q(h, lambda) (exact); finite h-jets use rational coefficients",
        "exact_polynomial_identities": ["Sklyanin discriminant", "G = -9h (u_h S/3 + v_h T)"],
        "central_commutators_mod_h4": 3,
        "weyl_first_product_mod_h2_monomial_pairs": len(monomials)**2,
        "noncommutative_first_commutator": "[y,z] = h*x^2 mod h^2",
        "recovered_potential_first_jet": "(x^3+y^3+z^3+u^3+v^3)/3 + h*x*y*z mod h^2",
        "jacobian_remainder_of_xyz": "x*y*z (nonzero)",
        "second_jet": second_jet,
        "rational_hesse": rational_hesse,
        "scope": "Finite algebraic identities only. Graph weights and inner-wheel vanishing are cited inputs. All-degree freeness, formality, THCR identifications, Orlov equivalences, the all-order categorical comparison, and generic descent are not verified by this script.",
    }
    serialized = json.dumps(output, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized, end="")


if __name__ == "__main__":
    main()
