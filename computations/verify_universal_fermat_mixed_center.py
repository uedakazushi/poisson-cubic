#!/usr/bin/env python3
"""Exact universal Fermat-mixed central cubic certificate.

Central A,B,C,D,E,H are algebraically independent, with weights 1,1,1,2,2,2.
h remains an indeterminate. All row reduction is over Q(h); there are NO
random samples or finite-field specializations. Run with Python + SymPy.
The degree-four free-word quotient gives 339 columns and 162 relation multiples;
all three commutators reduce to zero in the 144-dimensional relation span.
Near h=0 PBW flatness removes the generic rational-function localization.
"""
from collections import defaultdict
from itertools import product
import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.fields import field

h = sp.symbols("h")
K, _h = field("h", QQ)
WEIGHTS = (1, 1, 1, 2, 2, 2)
ZERO = (0,) * 6


def central_monomials(weight):
    def rec(i, remaining, powers):
        if i == 6:
            if not remaining:
                yield tuple(powers)
            return
        for k in range(remaining // WEIGHTS[i] + 1):
            yield from rec(i + 1, remaining - k * WEIGHTS[i], powers + [k])
    return list(rec(0, weight, []))


def add(*polys):
    ans = defaultdict(lambda: 0)
    for p in polys:
        for term, value in p.items():
            ans[term] += value
    return {key: v for key, v in ans.items() if v != 0}


def scale(poly, number):
    return {key: v * number for key, v in poly.items() if v * number != 0}


def mul(p, q):
    ans = defaultdict(lambda: 0)
    for (a, w), v in p.items():
        for (b, z), t in q.items():
            ans[(tuple(i + j for i, j in zip(a, b)), w + z)] += v * t
    return {key: v for key, v in ans.items() if v != 0}


def word(w="", center=ZERO):
    return {(center, tuple(w)): sp.S.One}


def central(i):
    return word("", tuple(int(i == j) for j in range(6)))


def cub(p):
    return mul(mul(p, p), p)


x, y, z = (word(a) for a in "xyz")
A, B, C, D, E, H = (central(i) for i in range(6))


def relations():
    return (
        add(mul(x, y), scale(mul(y, x), -1),
            scale(add(mul(z, z), mul(B, y), mul(C, x), H), -h)),
        add(mul(y, z), scale(mul(z, y), -1),
            scale(add(mul(x, x), mul(A, y), mul(C, z), D), -h)),
        add(mul(z, x), scale(mul(x, z), -1),
            scale(add(mul(y, y), mul(A, x), mul(B, z), E), -h)),
    )


def omega():
    perm = add(*(word(w) for w in ("xyz", "xzy", "yxz", "yzx", "zxy", "zyx")))
    def sym2(a, b):
        return scale(add(mul(a, b), mul(b, a)), sp.Rational(1, 2))
    return add(
        scale(add(cub(x), cub(y), cub(z)), sp.Rational(1, 3)),
        scale(perm, -h**2 / sp.Integer(9)),
        mul(A, sym2(x, y)), mul(B, sym2(y, z)), mul(C, sym2(z, x)),
        mul(D, x), mul(E, y), mul(H, z),
        scale(add(mul(mul(B, B), x), mul(mul(C, C), y),
                  mul(mul(A, A), z)), h**2 / sp.Integer(6)),
        scale(add(mul(A, mul(z, z)), mul(B, mul(x, x)), mul(C, mul(y, y)),
                  scale(mul(mul(A, C), x), -1),
                  scale(mul(mul(A, B), y), -1),
                  scale(mul(mul(B, C), z), -1)), h**4 / sp.Integer(18)),
    )


def basis_degree_four():
    return [(c, w) for k in range(5) for c in central_monomials(k)
            for w in product("xyz", repeat=4-k)]


def relation_multiples():
    for k in range(3):
        for c in central_monomials(k):
            for left_size in range(3-k):
                for left in product("xyz", repeat=left_size):
                    for right in product("xyz", repeat=2-k-left_size):
                        for r in relations():
                            yield mul(mul(word("".join(left), c), r),
                                      word("".join(right)))


def verify():
    B = basis_degree_four()
    positions = {key: i for i, key in enumerate(B)}
    pivots = {}
    def reduce(poly, insert=False):
        row = {positions[key]: K.from_expr(sp.sympify(value))
               for key, value in poly.items() if value != 0}
        while row:
            first = min(row)
            if first not in pivots:
                if insert:
                    lead = row[first]
                    pivots[first] = {j: val / lead for j, val in row.items()}
                    return {}
                return row
            multiple = row[first]
            for j, val in pivots[first].items():
                new = row.get(j, K.zero) - multiple * val
                if new:
                    row[j] = new
                else:
                    row.pop(j, None)
        return {}

    R = list(relation_multiples())
    for r in R:
        reduce(r, insert=True)
    assert (len(B), len(R), len(pivots)) == (339, 162, 144)
    # A separate rational-rank calculation at h=0 proves h-flatness in degree 4:
    # the rank over Q(h) and the rank at h=0 are both 144.
    special_pivots = {}
    for relation in R:
        row = {positions[key]: sp.Rational(sp.sympify(value).subs(h, 0))
               for key, value in relation.items()
               if sp.sympify(value).subs(h, 0) != 0}
        while row:
            lead = min(row)
            if lead not in special_pivots:
                coefficient = row[lead]
                special_pivots[lead] = {i: v / coefficient for i, v in row.items()}
                break
            factor = row[lead]
            for i, v in special_pivots[lead].items():
                new = row.get(i, sp.S.Zero) - factor * v
                if new:
                    row[i] = new
                else:
                    row.pop(i, None)
    assert len(special_pivots) == 144
    Om = omega()
    for generator in (x, y, z):
        comm = add(mul(Om, generator), scale(mul(generator, Om), -1))
        assert not reduce(comm), "universal centrality failed"
    print("PASS: 339 basis words; 162 relation multiples; ranks 144 at h=0 and over Q(h)")
    print("PASS: 3 exact universal commutators vanish over Q(h)[A,B,C,D,E,H]")


if __name__ == "__main__":
    verify()
