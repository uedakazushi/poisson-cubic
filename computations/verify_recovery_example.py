#!/usr/bin/env python3
"""Exact finite checks for paper B's noncommutative Hesse recovery example.

All coefficients are rational; h is symbolic. Checks the two exact scalar
identities used to import the known Sklyanin center, three central
commutators modulo h**4, and the Weyl first product modulo h**2.
These finite checks do not prove all-degree flatness or a categorical
equivalence. Those claims have separate proofs and cited inputs in the paper.
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
    output = {
        "status": "passed",
        "coefficient_ring": "Q[h] (exact); finite h-jets use rational coefficients",
        "exact_polynomial_identities": ["Sklyanin discriminant", "G = -9h (u_h S/3 + v_h T)"],
        "central_commutators_mod_h4": 3,
        "weyl_first_product_mod_h2_monomial_pairs": len(monomials)**2,
        "noncommutative_first_commutator": "[y,z] = h*x^2 mod h^2",
        "recovered_potential_first_jet": "(x^3+y^3+z^3+u^3+v^3)/3 + h*x*y*z mod h^2",
        "jacobian_remainder_of_xyz": "x*y*z (nonzero)",
        "scope": "Finite algebraic identities only. All-degree freeness, the formality comparison, categorical equivalence, and generic descent are proved in the text, not by this script.",
    }
    serialized = json.dumps(output, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized, end="")


if __name__ == "__main__":
    main()
