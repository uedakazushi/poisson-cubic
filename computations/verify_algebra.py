#!/usr/bin/env python3
"""Exact checks for the cubic-rotation manuscript (Python standard library only).

Elements are finite polynomials in a central h and noncommuting x,y,z.
The key (h_exponent, word) has a rational coefficient.  Identities modulo
the quadratic ideal are checked by explicit polynomial certificates, not
by a numerical rank calculation or by division by a parameter.
"""

from fractions import Fraction
from itertools import permutations
from math import comb
from pathlib import Path
import json


def clean(p):
    return {k: v for k, v in p.items() if v}


def term(word="", h_power=0, coefficient=1):
    return clean({(h_power, word): Fraction(coefficient)})


def add(*polynomials):
    result = {}
    for p in polynomials:
        for key, value in p.items():
            result[key] = result.get(key, Fraction(0)) + value
    return clean(result)


def scale(p, coefficient):
    return clean({k: v * Fraction(coefficient) for k, v in p.items()})


def mul(*polynomials):
    result = term()
    for p in polynomials:
        next_result = {}
        for (i, u), a in result.items():
            for (j, v), b in p.items():
                key = (i + j, u + v)
                next_result[key] = next_result.get(key, Fraction(0)) + a * b
        result = clean(next_result)
    return result


def sub(p, q):
    return add(p, scale(q, -1))


def power(p, exponent):
    return mul(*([p] * exponent))


def abelianize(p):
    result = {}
    for (i, word), value in p.items():
        key = (i, "".join(sorted(word)))
        result[key] = result.get(key, Fraction(0)) + value
    return clean(result)


def assert_equal(p, q, label):
    difference = sub(p, q)
    if difference:
        raise AssertionError(f"{label}: {difference}")


x, y, z, h = term("x"), term("y"), term("z"), term(h_power=1)
one = term()
r_xy = add(mul(x, y), scale(mul(y, x), -1), scale(mul(h, z, z), -1))
r_yz = add(mul(y, z), scale(mul(z, y), -1), scale(mul(h, x, x), -1))
r_zx = add(mul(z, x), scale(mul(x, z), -1), scale(mul(h, y, y), -1))
D = add(power(x, 3), power(y, 3), power(z, 3))
T = scale(add(*(term("".join(p)) for p in permutations("xyz"))), Fraction(1, 6))
G = sub(D, scale(mul(h, h, T), 2))


def ell(p):
    result = {}
    for (i, word), value in p.items():
        if word in ("xxx", "yyy", "zzz"):
            contribution = term(h_power=i, coefficient=value)
        elif word in ("xyz", "yzx", "zxy"):
            contribution = term(h_power=i + 1, coefficient=value / 2)
        elif word in ("xzy", "zyx", "yxz"):
            contribution = term(h_power=i + 1, coefficient=-value / 2)
        elif len(word) == 3:
            contribution = {}
        else:
            raise ValueError("ell is defined only on word degree three")
        result = add(result, contribution)
    return result


relation_count = 0
for relation in (r_xy, r_yz, r_zx):
    for letter in (x, y, z):
        for consequence in (mul(letter, relation), mul(relation, letter)):
            assert_equal(ell(consequence), {}, "ell annihilates a relation")
            relation_count += 1
assert_equal(ell(G), term(coefficient=3), "ell(G)=3 for all h")

# Explicit certificate for T - its normal expression in the quadratic ideal.
normal_T = add(mul(x, y, z), scale(mul(h, add(scale(power(x, 3), -1),
                       power(y, 3), scale(power(z, 3), -1))), Fraction(1, 2)))
certificate_T = scale(add(scale(mul(x, r_yz), -3),
                          scale(mul(r_xy, z), -2), mul(y, r_zx),
                          scale(mul(r_zx, y), 2), scale(mul(z, r_xy), -1)),
                      Fraction(1, 6))
assert_equal(sub(T, normal_T), certificate_T, "normal T certificate")

# Walton's displayed g at (a,b,c)=(1,-1,-h).
h3 = power(h, 3)
g = add(scale(mul(h, add(one, h3), power(x, 3)), -1),
        mul(sub(h3, one), x, y, z),
        mul(add(one, h3), y, x, z),
        mul(sub(power(h, 4), h), power(y, 3)))
certificate_g = add(scale(mul(add(one, h3), r_xy, z), -1),
                    scale(mul(h3, certificate_T), -2))
assert_equal(add(g, mul(h, G)), certificate_g, "g=-hG certificate")

# Determinant is evaluated after abelianization, since point coordinates commute.
M = [[scale(y, -1), x, scale(mul(h, z), -1)],
     [scale(mul(h, x), -1), scale(z, -1), y],
     [z, scale(mul(h, y), -1), scale(x, -1)]]
det = {}
for p in permutations(range(3)):
    inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    det = add(det, scale(mul(*(M[i][p[i]] for i in range(3))), (-1) ** inversions))
hesse = add(D, mul(h, h, x, y, z))
assert_equal(abelianize(det), abelianize(scale(mul(h, hesse), -1)),
             "point-curve determinant")

# A telescoping gradient-ideal certificate for (27+h^6)(xyz)^2.
A, B, C = scale(power(x, 2), 3), scale(power(y, 2), 3), scale(power(z, 2), 3)
a, b, c = (scale(mul(h, h, y, z), -1), scale(mul(h, h, x, z), -1),
           scale(mul(h, h, x, y), -1))
gradient_certificate = add(mul(sub(A, a), B, C), mul(a, sub(B, b), C),
                           mul(a, b, sub(C, c)))
discriminant_multiple = mul(add(term(coefficient=27), power(h, 6)),
                            power(mul(x, y, z), 2))
assert_equal(abelianize(gradient_certificate), abelianize(discriminant_multiple),
             "Hesse necessary singular condition")


def reduce_cube_unity(p):
    result = {}
    for (i, word), value in p.items():
        assert not word
        result = add(result, term(h_power=i % 3, coefficient=value))
    return result


# For t=-3*mu, mu^3=1, [1:1:mu^2] is singular on D+t xyz.
# Reuse the central formal letter h to represent mu only in this check.
mu = h
t = scale(mu, -3)
special_z = power(mu, 2)
for value in (
    add(term(coefficient=2), power(special_z, 3), mul(t, special_z)),
    add(term(coefficient=3), mul(t, special_z)),
    add(scale(power(special_z, 2), 3), t),
):
    assert_equal(reduce_cube_unity(value), {}, "Hesse singular point sufficiency")

dimensions = [{"n": n, "N": n + 2, "dim_J3": comb(n + 2, 3)} for n in range(3, 8)]

# Exact group-law certificates on the Hesse point curve, with origin [1:-1:0].
# Negation interchanges the first two coordinates.  The tangent construction
# identifies double_p as 2p whenever h^6 != -27; no division by h is used.
def hesse_value(point):
    a, b, c = point
    return add(power(a, 3), power(b, 3), power(c, 3), mul(h, h, a, b, c))


def tangent_value(point, other):
    a, b, c = point
    u, v, w = other
    return add(mul(add(scale(power(a, 2), 3), mul(h, h, b, c)), u),
               mul(add(scale(power(b, 2), 3), mul(h, h, a, c)), v),
               mul(add(scale(power(c, 2), 3), mul(h, h, a, b)), w))


marked_p = (one, scale(one, -1), scale(h, -1))
double_p = (add(h3, one), sub(h3, one), scale(h, -2))
minus_double_p = (double_p[1], double_p[0], double_p[2])
origin = (one, scale(one, -1), {})


def point_matrix(point):
    a, b, c = point
    return ((scale(b, -1), a, scale(mul(h, c), -1)),
            (scale(mul(h, a), -1), scale(c, -1), b),
            (c, scale(mul(h, b), -1), scale(a, -1)))


for point, successor in ((origin, marked_p), (marked_p, double_p)):
    for row in point_matrix(point):
        assert_equal(add(*(mul(entry, coordinate) for entry, coordinate in zip(row, successor))),
                     {}, "point-curve translation orientation")
assert_equal(hesse_value(marked_p), {}, "p lies on the Hesse curve")
assert_equal(hesse_value(double_p), {}, "2p formula lies on the Hesse curve")
assert_equal(tangent_value(marked_p, minus_double_p), {}, "tangent at p contains -2p")
curve_parameter = term("t")
tangent_direction = ({}, scale(power(h, 2), 2), sub(h3, term(coefficient=3)))
tangent_line = tuple(add(a, mul(curve_parameter, b))
                     for a, b in zip(marked_p, tangent_direction))
assert_equal(hesse_value(tangent_line),
             mul(add(power(h, 6), term(coefficient=27)), power(curve_parameter, 2),
                 sub(mul(sub(h3, one), curve_parameter), h)),
             "tangent intersection multiplicity certificate")
assert_equal(tangent_value(double_p, marked_p),
             mul(h3, sub(term(coefficient=5), power(h, 6))),
             "tangent at 2p contains p exactly when h^3*(5-h^6)=0")

# The Koszul homotopy used for a central cubic with mixed monomials.
# This is a universal ternary cubic: its ten coefficients are independent
# commuting symbols.  The check is exact over Q[a_0,...,a_9,u_0,u_1,u_2].
monomials = [(i, j, 3 - i - j) for i in range(4) for j in range(4 - i)]
number_variables = 3 + len(monomials)
zero_exponents = (0,) * number_variables


def cterm(exponents, coefficient=1):
    return {tuple(exponents): Fraction(coefficient)} if coefficient else {}


def cadd(*polynomials):
    out = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            out[monomial] = out.get(monomial, 0) + coefficient
    return clean(out)


def cmul(p, q):
    out = {}
    for a, ca in p.items():
        for b, cb in q.items():
            key = tuple(x + y for x, y in zip(a, b))
            out[key] = out.get(key, 0) + ca * cb
    return clean(out)


def cmatrix_product(p, q):
    out = {}
    for (i, k), left in p.items():
        for (ell, j), right in q.items():
            if k == ell:
                out[i, j] = cadd(out.get((i, j), {}), cmul(left, right))
    return {key: value for key, value in out.items() if value}


central_P = {}
central_q = [{}, {}, {}]
central_u = []
for i in range(3):
    exponents = list(zero_exponents)
    exponents[i] = 1
    central_u.append(cterm(exponents))
for index, abc in enumerate(monomials):
    exponents = list(abc) + [int(j == index) for j in range(len(monomials))]
    central_P = cadd(central_P, cterm(exponents))
    for i in range(3):
        if abc[i]:
            derivative = exponents.copy()
            derivative[i] -= 1
            central_q[i] = cadd(central_q[i], cterm(derivative, Fraction(abc[i], 3)))

koszul_d, koszul_s = {}, {}
for mask in range(8):
    for i in range(3):
        sign = (-1) ** sum(bool(mask & (1 << j)) for j in range(i))
        if mask & (1 << i):
            koszul_d[mask ^ (1 << i), mask] = scale(central_u[i], sign)
        else:
            koszul_s[mask | (1 << i), mask] = scale(central_q[i], sign)
assert cmatrix_product(koszul_d, koszul_d) == {}, "Koszul d^2=0"
assert cmatrix_product(koszul_s, koszul_s) == {}, "Koszul s^2=0"
ds = cmatrix_product(koszul_d, koszul_s)
sd = cmatrix_product(koszul_s, koszul_d)
ds_plus_sd = {key: cadd(ds.get(key, {}), sd.get(key, {})) for key in set(ds) | set(sd)}
ds_plus_sd = {key: value for key, value in ds_plus_sd.items() if value}
assert ds_plus_sd == {(i, i): central_P for i in range(8)}, "ds+sd=P on every exterior degree"

# Exact projective enumeration certifying an infinite-order point at h=2.
def projective_hesse_points(prime: int, h_value: int):
    if prime not in (5, 11):
        raise ValueError("This certificate uses the verified primes 5 and 11.")
    representatives = ([(a, b, 1) for a in range(prime) for b in range(prime)]
                       + [(a, 1, 0) for a in range(prime)] + [(1, 0, 0)])
    points = []
    for a, b, c in representatives:
        value = a**3 + b**3 + c**3 + h_value**2 * a*b*c
        if value % prime == 0:
            gradient = (3*a*a + h_value**2*b*c,
                        3*b*b + h_value**2*a*c,
                        3*c*c + h_value**2*a*b)
            assert any(t % prime for t in gradient), "Singular rational point"
            points.append((a, b, c))
    assert (h_value**6 + 27) % prime != 0, "Good reduction discriminant"
    return points

infinite_order_points = {str(p): projective_hesse_points(p, 2) for p in (5, 11)}
assert len(infinite_order_points["5"]) == 9
assert len(infinite_order_points["11"]) == 12
p2, q2, minus_p2 = (1, -1, -2), (9, 7, -4), (1, -1, 2)
for a, b, c in (p2, q2, minus_p2):
    assert a**3 + b**3 + c**3 + 4*a*b*c == 0
assert any(q2[i] * minus_p2[j] != q2[j] * minus_p2[i]
           for i in range(3) for j in range(i+1, 3)), "2p != -p"

result = {
    "date": "2026-11-08",
    "version": "nc-cubic-v1",
    "status": "all exact checks passed",
    "arithmetic": "rational polynomial identities and exact finite-field enumeration; no floating point",
    "degree_three_relations_annihilated": relation_count,
    "ell_G": 3,
    "normal_T_certificate": "passed",
    "standard_center_g_equals_minus_h_G_certificate": "passed",
    "point_matrix_determinant": "-h*(x^3+y^3+z^3+h^2*x*y*z)",
    "hesse_singular_parameters": "h^6 + 27 = 0",
    "hesse_gradient_certificate": "passed",
    "hesse_singular_point_sufficiency": "passed modulo mu^3-1",
    "jacobian_dimensions": dimensions,
    "finite_order_point_certificates": {
        "origin": "[1:-1:0]",
        "p": "[1:-1:-h]",
        "double_p": "[h^3+1:h^3-1:-2h]",
        "tangent_at_double_p_evaluated_on_p": "h^3*(5-h^6)",
        "translation_orientation": "M(o)*p=0 and M(p)*(2p)=0",
        "conclusion_with_chord_tangent_group_law": "h^6=5 implies exact order 5",
        "identities": "curve incidence, tangent incidence, and intersection multiplicity checked exactly",
    },
    "universal_ternary_cubic_koszul": {
        "coefficient_symbols": len(monomials),
        "exterior_rank": 8,
        "d_squared": "0",
        "s_squared": "0",
        "d_s_plus_s_d": "P times the identity",
        "coverage": "all ternary cubics, including mixed monomials; no isolated-critical-point assumption is used for this identity",
    },
    "infinite_order_parameter_h2": {
        "curve": "x^3+y^3+z^3+4xyz=0",
        "good_reduction_primes": [5, 11],
        "projective_points": infinite_order_points,
        "counts": {p: len(points) for p, points in infinite_order_points.items()},
        "p": p2, "double_p": q2, "minus_p": minus_p2,
        "proof": "Prime-to-p torsion injection forces torsion order to divide 3; p != O and 2p != -p exclude it.",
    },
    "scope": "Checks algebraic formulas only; categorical proofs are in the manuscript.",
}
destination = Path(__file__).resolve().parent / "verification.json"
destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
