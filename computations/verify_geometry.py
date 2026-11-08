#!/usr/bin/env python3
"""Reproduce the complete-intersection numbers in poisson_geometry.tex.

All inputs are below, and only Python's standard library is required.
For W=(d_1,...,d_c) in P^M we use
  degree(W) = product(d_i), K_W = O_W(sum(d_i)-M-1),
  c(T_W) = (1+H)^(M+1) / product(1+d_i*H),
  Hilb_W(t) = product(1-t^d_i) / (1-t)^(M+1).
The Koszul resolution also computes chi(O_W(t)) by generalized binomials.
Adjunction and Todd-genus computations are checked independently against it.

Hodge numbers use the smoothness, Lefschetz, Koszul-vanishing and normal-
sequence arguments in the manuscript. This script checks their exact
numerical consequences; it does not prove those hypotheses or formalize
the geometric proofs. Arithmetic genera remain valid for nonreduced
complete intersections of the same types.

Run: python3 computations/verify_geometry.py
The certificate is written next to this script, independently of the cwd.
"""

from fractions import Fraction
from math import comb, factorial, prod
from pathlib import Path
import json


VERSION = "nc-cubic-v1"
DATE = "2026-11-08"

# Each tuple is (ambient projective dimension, equation degrees).
INPUTS = {
    "Y_n6": (7, (2, 2, 2, 3)),
    "Y_n7": (8, (2, 2, 2, 3)),
    "critical_curve": (4, (2, 2, 2)),
    "critical_K3": (5, (2, 2, 2)),
    "Delta_n6": (7, (2, 2, 2, 2, 2, 2)),
    "Z_n6": (7, (2, 2, 2, 2, 2, 2, 3)),
    "Delta_n7": (8, (2, 2, 2, 2, 2, 2)),
    "Z_n7": (8, (2, 2, 2, 2, 2, 2, 3)),
}


class Checks:
    """Checks remain active even when Python is invoked with -O."""

    def __init__(self):
        self.count = 0

    def equal(self, name, actual, expected):
        if actual != expected:
            raise ArithmeticError(f"{name}: computed {actual!r}, expected {expected!r}")
        self.count += 1


def integer(value):
    value = Fraction(value)
    if value.denominator != 1:
        raise ArithmeticError(f"Expected an integer, got {value}")
    return value.numerator


def generalized_binomial(n, r):
    """Polynomial binomial n choose r, including negative integer n."""
    return Fraction(prod(n - j for j in range(r)), factorial(r))


def hilbert_numerator(degrees):
    coefficients = [1]
    for degree in degrees:
        updated = coefficients + [0] * degree
        for j, coefficient in enumerate(coefficients):
            updated[j + degree] -= coefficient
        coefficients = updated
    return coefficients


def hilbert_function(ambient, degrees, twist):
    """Dimension of the twist-degree part of the homogeneous coordinate ring."""
    if twist < 0:
        return 0
    return sum(coefficient * comb(ambient + twist - j, ambient)
               for j, coefficient in enumerate(hilbert_numerator(degrees))
               if j <= twist)


def chi_line_bundle(ambient, degrees, twist=0):
    """Euler characteristic computed by the Koszul resolution, not by Chern classes."""
    return integer(sum(coefficient * generalized_binomial(ambient + twist - j, ambient)
                       for j, coefficient in enumerate(hilbert_numerator(degrees))))


def chern_coefficients(ambient, degrees):
    dimension = ambient - len(degrees)
    coefficients = [comb(ambient + 1, j) for j in range(dimension + 1)]
    # Dividing a(H) by 1+dH gives b_0=a_0 and b_j=a_j-d*b_(j-1).
    for degree in degrees:
        quotient = [coefficients[0]]
        for j in range(1, dimension + 1):
            quotient.append(coefficients[j] - degree * quotient[j - 1])
        coefficients = quotient
    return coefficients


def todd_chi(dimension, chern, degree):
    """Integral of the Todd class through complex dimension four."""
    if dimension == 0:
        return degree
    c1 = chern[1]
    if dimension == 1:
        return Fraction(c1 * degree, 2)
    c2 = chern[2]
    if dimension == 2:
        return Fraction((c1 * c1 + c2) * degree, 12)
    c3 = chern[3]
    if dimension == 3:
        return Fraction(c1 * c2 * degree, 24)
    if dimension == 4:
        c4 = chern[4]
        return Fraction((-c1**4 + 4*c1*c1*c2 + 3*c2*c2 + c1*c3 - c4) * degree, 720)
    raise ValueError("Todd formula is implemented only through dimension four")


def complete_intersection(name, ambient, degrees, checks):
    dimension = ambient - len(degrees)
    degree = prod(degrees)
    canonical = sum(degrees) - ambient - 1
    chern = chern_coefficients(ambient, degrees)
    chi = chi_line_bundle(ambient, degrees)
    checks.equal(name + ": Koszul chi equals Todd genus",
                 chi, todd_chi(dimension, chern, degree))
    record = {
        "ambient_projective_dimension": ambient,
        "equation_degrees": list(degrees),
        "dimension": dimension,
        "degree": degree,
        "canonical_H_coefficient": canonical,
        "chern_coefficients_from_H0": chern,
        "chi_structure_sheaf": chi,
        "euler_if_smooth": chern[dimension] * degree,
    }
    if dimension > 0:
        # For these projectively normal complete intersections, h^0(omega)
        # is the indicated Hilbert-function value, by adjunction.
        pg = hilbert_function(ambient, degrees, canonical)
        checks.equal(name + ": chi and geometric genus", chi, 1 + (-1)**dimension * pg)
        record["geometric_genus_if_smooth"] = pg
    if dimension == 1:
        genus = 1 - chi
        checks.equal(name + ": Koszul and adjunction genus",
                     genus, 1 + Fraction(canonical * degree, 2))
        record["arithmetic_genus"] = genus
    return record


def hodge_euler(dimension, entries):
    """Expand Hodge symmetry and Poincare duality, then take the Euler sum."""
    diamond = {}
    for (p, q), value in entries.items():
        for position in ((p, q), (q, p), (dimension-p, dimension-q),
                         (dimension-q, dimension-p)):
            if position in diamond and diamond[position] != value:
                raise ArithmeticError(f"Inconsistent Hodge values at {position}")
            diamond[position] = value
    return sum((-1)**(p+q) * value for (p, q), value in diamond.items())


def main():
    checks = Checks()
    data = {name: complete_intersection(name, ambient, degrees, checks)
            for name, (ambient, degrees) in INPUTS.items()}

    # The three displayed Chern expansions in the original manuscript.
    for name, expected in {
        "Y_n6": [1, -1, 7, -21],
        "Y_n7": [1, 0, 6, -14, 48],
        "Delta_n7": [1, -3, 12],
    }.items():
        checks.equal(name + ": displayed Chern expansion",
                     data[name]["chern_coefficients_from_H0"], expected)

    y3 = data["Y_n6"]
    h21 = integer(Fraction(4 - 2*y3["geometric_genus_if_smooth"] - y3["euler_if_smooth"], 2))
    y3["canonical_top_intersection"] = y3["canonical_H_coefficient"]**3 * y3["degree"]
    y3["hodge_if_smooth"] = {"h10": 0, "h20": 0, "h11": 1, "h21": h21}
    checks.equal("Y_n6: degree, K^3, pg, Euler, h21",
                 (y3["degree"], y3["canonical_top_intersection"],
                  y3["geometric_genus_if_smooth"], y3["euler_if_smooth"], h21),
                 (24, 24, 8, -504, 246))
    checks.equal("Y_n6: Hodge Euler sum", hodge_euler(3, {
        (0, 0): 1, (1, 1): 1, (3, 0): y3["geometric_genus_if_smooth"], (2, 1): h21,
    }), y3["euler_if_smooth"])

    y4 = data["Y_n7"]
    ambient, degrees = INPUTS["Y_n7"]
    sections = {twist: hilbert_function(ambient, degrees, twist) for twist in (1, 2, 3)}
    ambient_vector_fields = (ambient + 1)*sections[1] - 1
    normal_sections = sum(sections[degree] for degree in degrees)
    h31 = normal_sections - ambient_vector_fields
    h22 = y4["euler_if_smooth"] - 6 - 2*h31
    y4["normal_sequence_counts"] = {
        "h0_O1": sections[1], "h0_O2": sections[2], "h0_O3": sections[3],
        "ambient_vector_fields": ambient_vector_fields, "normal_sections": normal_sections,
    }
    y4["hodge_if_smooth"] = {"h11": 1, "h21": 0, "h31": h31, "h22": h22}
    checks.equal("Y_n7: normal-sequence counts",
                 (sections[1], sections[2], sections[3], ambient_vector_fields, normal_sections),
                 (9, 42, 137, 80, 263))
    checks.equal("Y_n7: degree, Euler, h31, h22",
                 (y4["degree"], y4["euler_if_smooth"], h31, h22), (24, 1152, 183, 780))
    checks.equal("Y_n7: Hodge Euler sum", hodge_euler(4, {
        (0, 0): 1, (1, 1): 1, (4, 0): 1, (3, 1): h31, (2, 2): h22,
    }), y4["euler_if_smooth"])

    delta = data["Delta_n7"]
    delta["canonical_square"] = delta["canonical_H_coefficient"]**2 * delta["degree"]
    delta["h1_structure_sheaf_if_smooth"] = 0
    checks.equal("Delta_n7: degree, K^2, c2, chi, pg",
                 (delta["degree"], delta["canonical_square"], delta["euler_if_smooth"],
                  delta["chi_structure_sheaf"], delta["geometric_genus_if_smooth"]),
                 (64, 576, 768, 112, 111))
    checks.equal("critical K3: K, degree, chi, Euler",
                 tuple(data["critical_K3"][key] for key in (
                     "canonical_H_coefficient", "degree", "chi_structure_sheaf", "euler_if_smooth")),
                 (0, 8, 2, 24))
    for name, expected_degree, expected_genus in (
        ("critical_curve", 8, 5), ("Delta_n6", 64, 129), ("Z_n7", 192, 577),
    ):
        checks.equal(name + ": degree and arithmetic genus",
                     (data[name]["degree"], data[name]["arithmetic_genus"]),
                     (expected_degree, expected_genus))
    checks.equal("Z_n6: complete-intersection length",
                 (data["Z_n6"]["degree"], data["Z_n6"]["chi_structure_sheaf"]), (192, 192))
    checks.equal("Z_n7: Hilbert polynomial is 192*t-576",
                 [chi_line_bundle(*INPUTS["Z_n7"], t) for t in (0, 1, 2)],
                 [-576, -384, -192])

    fermat = {"one_block_artin_length": 2**3, "two_block_transverse_length": (2**3)**2}
    fermat["zero_scheme_degree"] = 3 * fermat["two_block_transverse_length"]
    checks.equal("Fermat thickening: lengths and degree", tuple(fermat.values()), (8, 64, 192))

    certificate = {
        "version": VERSION,
        "date_jst": DATE,
        "status": "all exact arithmetic checks passed",
        "checks_passed": checks.count,
        "arithmetic": "Python integers and fractions.Fraction; no floating point",
        "source": "papers/poisson_geometry.tex, sec:pg-numerical and prop:pg-fermat-thickening",
        "limitations": (
            "Numerical consequences of the stated complete-intersection, smoothness, "
            "Lefschetz, Koszul and normal-sequence arguments. Does not verify smoothness "
            "or formalize the geometric proofs. Arithmetic genera also apply to "
            "nonreduced complete intersections of the same type."
        ),
        "complete_intersections": data,
        "fermat_thickening": fermat,
    }
    output = Path(__file__).resolve().with_name("geometry_verification.json")
    output.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {checks.count} exact checks; Chern, degree, genus, Euler and Hodge numbers agree.")
    print(output.name)


if __name__ == "__main__":
    main()
