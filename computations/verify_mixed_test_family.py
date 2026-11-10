#!/usr/bin/env python3
"""Exact mixed-family central cubic certificate and h-adic PBW jet checks.

Free-algebra identities prove centrality over QQ[h,a] for every parameter.
The independent sorted reductions are modulo h**9. They do not compute
the commutative reconstruction or assert AS-regularity at nonzero h.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations
import json
from pathlib import Path

# A monomial is (power of h, power of the central coefficient a, active word).
Polynomial = dict[tuple[int, int, str], Q]


def clean(p: Polynomial) -> Polynomial:
    return {m: c for m, c in p.items() if c}


def add(*ps: Polynomial) -> Polynomial:
    result = defaultdict(Q)
    for p in ps:
        for m, c in p.items():
            result[m] += c
    return clean(result)


def scale(p: Polynomial, c=1, h=0, a=0) -> Polynomial:
    return clean({(i+h, j+a, w): Q(c)*v for (i, j, w), v in p.items()})


def mon(word: str) -> Polynomial:
    return {(0, 0, word): Q(1)}


def mul(*ps: Polynomial) -> Polynomial:
    result = mon("")
    for p in ps:
        nxt = defaultdict(Q)
        for (i, j, w), c in result.items():
            for (k, ell, v), d in p.items():
                nxt[(i+k, j+ell, w+v)] += c*d
        result = clean(nxt)
    return result


def comm(p: Polynomial, q: Polynomial) -> Polynomial:
    return add(mul(p, q), scale(mul(q, p), -1))


def anti(p: Polynomial, q: Polynomial) -> Polynomial:
    return add(mul(p, q), mul(q, p))


def S(r: Polynomial, p: Polynomial) -> Polynomial:
    return add(mul(r, p, p), mul(p, r, p), mul(p, p, r))


def D(r: Polynomial, p: Polynomial, q: Polynomial) -> Polynomial:
    return add(mul(r, p, q), scale(mul(p, r, q), -1),
               scale(mul(q, r, p), -1), mul(q, p, r))


x, y, z = (mon(c) for c in "xyz")
relations = [
    add(comm(x, y), scale(mul(z, z), -1, h=1)),
    add(comm(x, z), scale(mul(y, y), h=1), scale(x, h=1, a=1)),
    add(comm(y, z), scale(mul(x, x), -1, h=1), scale(y, -1, h=1, a=1)),
]
r1, r2, r3 = relations
T = add(*(mon("".join(p)) for p in permutations("xyz")))
omega = add(
    scale(add(mon("xxx"), mon("yyy"), mon("zzz")), Q(1, 3)),
    scale(T, -Q(1, 9), h=2),
    scale(anti(x, y), Q(1, 2), a=1),
    scale(z, Q(1, 6), h=2, a=2),
    scale(mul(z, z), Q(1, 18), h=4, a=1),
)

# These are identities in the FREE algebra QQ[h,a]<x,y,z>.
proofs = {
    "x": add(
        scale(S(r1, y), -Q(1, 3)), scale(S(r2, z), -Q(1, 3)),
        scale(add(D(r1, z, x), D(r2, y, x)), Q(1, 18), h=2),
        scale(comm(x, r1), Q(1, 18), h=3, a=1),
        scale(anti(x, r1), -Q(1, 2), a=1),
        scale(comm(z, r2), Q(1, 6), h=1, a=1),
        scale(comm(anti(y, z), r3), Q(1, 6), h=1),
    ),
    "y": add(
        scale(S(r1, x), Q(1, 3)), scale(S(r3, z), -Q(1, 3)),
        scale(D(r1, z, y), -Q(1, 9), h=2),
        scale(comm(y, r1), Q(1, 18), h=3, a=1),
        scale(anti(y, r1), Q(1, 2), a=1),
        scale(comm(r2, x), Q(1, 18), h=2, a=1),
        scale(comm(r2, add(scale(mul(x, z), 2), mul(z, x))), Q(1, 9), h=1),
        scale(mul(comm(r2, y), y), Q(1, 9), h=2),
        scale(comm(r3, z), Q(1, 6), h=1, a=1),
    ),
    "z": add(
        scale(comm(r1, z), Q(1, 9), h=3, a=1),
        scale(comm(r1, z), Q(1, 2), a=1),
        scale(comm(add(scale(mul(x, y), 2), mul(y, x)), r1), Q(1, 9), h=1),
        scale(mul(comm(r1, z), z), Q(1, 9), h=2),
        scale(mul(y, r2), a=1), scale(S(r2, x), Q(1, 3)),
        scale(D(r2, y, z), -Q(1, 9), h=2),
        scale(mul(r3, x), a=1), scale(S(r3, y), Q(1, 3)),
    ),
}

rules = {
    "xy": add(mon("yx"), scale(mon("zz"), h=1)),
    "xz": add(mon("zx"), scale(mon("yy"), -1, h=1), scale(x, -1, h=1, a=1)),
    "yz": add(mon("zy"), scale(mon("xx"), h=1), scale(y, h=1, a=1)),
}


@lru_cache(None)
def normal(word: str, budget: int) -> Polynomial:
    for i in range(len(word)-1):
        pair = word[i:i+2]
        if pair in rules:
            parts = []
            for (h, a, w), c in rules[pair].items():
                if h <= budget:
                    parts.append(scale(normal(word[:i]+w+word[i+2:], budget-h), c, h, a))
            return add(*parts)
    return mon(word)


def reduce(p: Polynomial, order: int) -> Polynomial:
    return add(*(scale(normal(w, order-h), c, h, a)
                 for (h, a, w), c in p.items() if h <= order))


def serialize(p: Polynomial) -> list[dict]:
    return [{"h_power": h, "a_power": a, "word": w, "coefficient": str(c)}
            for (h, a, w), c in sorted(p.items())]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("mixed_test_family_certificate.json"))
    args = parser.parse_args()
    free_checks = {}
    for letter in "xyz":
        residual = add(comm(omega, mon(letter)), scale(proofs[letter], -1))
        assert not residual, (letter, serialize(residual))
        free_checks[letter] = {"free_algebra_residual": [], "exact_identity": True}

    # The only active-word overlap is xyz, at xy and yz.
    left = mul(rules["xy"], z)
    right = mul(x, rules["yz"])
    expected = add(mon("zyx"), scale(add(mon("xxx"), scale(mon("yyy"), -1), mon("zzz")), h=1))
    jet_checks = []
    for order in (2, 3, 4, 8):
        assert reduce(left, order) == expected
        assert reduce(right, order) == expected
        assert all(not reduce(comm(omega, mon(q)), order) for q in "xyz")
        jet_checks.append({"modulus": f"h^{order+1}", "overlap_and_centrality": True})

    no_quadratic_correction = add(omega, scale(z, -Q(1, 6), h=2, a=2))
    negative = {q: serialize(reduce(comm(no_quadratic_correction, mon(q)), 3)) for q in "xyz"}
    assert any(negative.values())
    cert = {
        "date": "2026-11-10", "version": 1,
        "coefficient_ring": "QQ[h,a] with a=lambda*u central",
        "ambient_relations": [serialize(r) for r in relations],
        "central_element_without_u_cubed_plus_v_cubed": serialize(omega),
        "free_algebra_identities": free_checks,
        "proof_formulas_source": "papers/reconstruction/mixed_test_family.tex",
        "sorted_overlap_normal_form": serialize(expected),
        "jet_checks": jet_checks,
        "sorted_central_element_mod_h_cubed": serialize(reduce(omega, 2)),
        "negative_control_omitting_h_squared_a_squared_z_over_6": negative,
        "scope": {
            "universal_polynomial_centrality_proved": True,
            "formal_pbw_proof_in_note": True,
            "all_nonzero_h_as_regular_proved": False,
            "commutative_reconstruction_second_coefficient_computed": False,
            "kuznetsov_equivalence_proved": False,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(cert, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"status": "passed", "universal_free_identities": 3,
                      "jet_orders": [3, 4, 5, 9], "certificate": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
