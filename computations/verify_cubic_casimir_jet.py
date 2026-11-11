#!/usr/bin/env python3
"""Exact universal cubic-Casimir second-jet certificate.

Claim (all coefficients independent, char 0):
  [sym(f - h^2 det(Hess_x f)/12), x_i] == 0 modulo h^4,
for the three Jacobian commutator relations [y,z]=h sym(f_x),
[z,x]=h sym(f_y), [x,y]=h sym(f_z).

Here f is the universal polynomial of active degree <=3, with TWENTY
independent coefficients. They may subsequently be specialized to any
commutative central coefficient ring, including C[u_1,...,u_m].

The algorithm does NOT sample coefficient values. It rewrites free words
by equality modulo the defining relations, to bounded h-degree 3, and
tests each resulting Q[a_0,...,a_19] coefficient exactly.

Usage: python3 computations/verify_cubic_casimir_jet.py
Dependency: sympy
"""
from collections import defaultdict
from functools import lru_cache
from itertools import permutations

import sympy as sp

x, y, z = sp.symbols("x y z")
xs = (x, y, z)
h_order = 3

monomials = [
    x**i * y**j * z**k
    for i in range(4)
    for j in range(4 - i)
    for k in range(4 - i - j)
]
assert len(monomials) == 20
a = sp.symbols("a0:20")
f = sp.Add(*(ci * mi for ci, mi in zip(a, monomials)))
hessian_det = sp.expand(sp.hessian(f, xs).det())


def sym_words(polynomial):
    """Weyl symmetrization: word tuple -> rational-coefficient polynomial."""
    result = defaultdict(lambda: 0)
    for powers, coefficient in sp.Poly(polynomial, *xs).terms():
        word = (0,) * powers[0] + (1,) * powers[1] + (2,) * powers[2]
        words = set(permutations(word))
        for w in words:
            result[w] += coefficient / sp.Integer(len(words))
    return dict(result)


# An inverted adjacent pair equals the correctly ordered pair plus
# h times the displayed polynomial (with its indicated sign).
# x < y < z, with x,y,z encoded as 0,1,2.
relations = {
    (1, 0): (-1, sym_words(sp.diff(f, z))),  # yx = xy - h sym(f_z)
    (2, 0): (+1, sym_words(sp.diff(f, y))),  # zx = xz + h sym(f_y)
    (2, 1): (-1, sym_words(sp.diff(f, x))),  # zy = yz - h sym(f_x)
}


@lru_cache(maxsize=None)
def normal(word, degree_left):
    """Reduce a free word modulo the relations, discarding h^>=4 terms.

    Output keys are (nondecreasing word, h-exponent). On each recursion
    either the number of inversions falls or h-exponent rises, hence
    the calculation terminates with a finite rational identity.
    """
    if degree_left < 0:
        return {}
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            result = defaultdict(lambda: 0)
            swapped = word[:i] + (word[i + 1], word[i]) + word[i + 2:]
            for key, value in normal(swapped, degree_left).items():
                result[key] += value
            sign, replacements = relations[(word[i], word[i + 1])]
            for replacement, coefficient in replacements.items():
                changed = word[:i] + replacement + word[i + 2:]
                for (ordered, exponent), value in normal(
                    changed, degree_left - 1
                ).items():
                    result[(ordered, exponent + 1)] += sign * coefficient * value
            return dict(result)
    return {(word, 0): sp.Integer(1)}


def commutator_coefficients(generator):
    result = defaultdict(lambda: 0)
    for polynomial, scalar, shift in (
        (f, sp.Integer(1), 0),
        (hessian_det, -sp.Rational(1, 12), 2),
    ):
        for word, coefficient in sym_words(polynomial).items():
            for sign, product in ((1, word + (generator,)), (-1, (generator,) + word)):
                for (ordered, exponent), value in normal(
                    product, h_order - shift
                ).items():
                    result[(ordered, exponent + shift)] += (
                        sign * scalar * coefficient * value
                    )
    return result


def main():
    assert len(a) == 20
    for i, variable in enumerate(xs):
        result = commutator_coefficients(i)
        bad = [(key, sp.expand(v)) for key, v in result.items() if sp.expand(v) != 0]
        assert not bad, f"Universal identity failed for {variable}: {bad[:5]}"
        print(f"PASS [{variable}]: {len(result)} word/order coefficients vanish")
    print("PASS: exact universal identity with 20 free coefficients; no specialization")


if __name__ == "__main__":
    main()
