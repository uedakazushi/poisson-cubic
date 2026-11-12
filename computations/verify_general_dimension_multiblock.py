#!/usr/bin/env python3
"""Exact symbolic tests for general-dimensional compatible Jacobian blocks.

These tests support, but do not replace, the arbitrary-k tensor-product proof.
For smooth examples of n=3,4,6,7,10 including shared center variables,
checks every Jacobi coefficient, F-Casimir condition, and zero cross-block Hessian.
Run: python3 computations/verify_general_dimension_multiblock.py
Requires: sympy
"""
from itertools import combinations, permutations
import sympy as sp


def test(k, m):
    xs = tuple(sp.symbols(f"x{s} y{s} z{s}") for s in range(k))
    us = sp.symbols(f"u0:{m}") if m else ()
    lam = sp.symbols(f"lambda0:{k}")
    variables = tuple(v for block in xs for v in block) + us
    terms = []
    for s, (x, y, z) in enumerate(xs):
        u0 = us[0] if m else sp.S.Zero
        u1 = us[1] if m > 1 else sp.S.Zero
        X = x + sp.Rational(s + 1, 5)*u0 + sp.Rational(1, 7)*u1
        Y = y + sp.Rational(s + 2, 11)*u0 + sp.Rational(1, 9)*u1
        Z = z + sp.Rational(1, 13)*u0 + sp.Rational(s + 1, 17)*u1
        t = sp.Rational(s + 1, 7)
        assert t**3 != -1
        terms.append(sp.expand((X**3 + Y**3 + Z**3)/3 + t*X*Y*Z))
    F = sp.expand(sum(terms) + sum(u**3/3 for u in us))
    # The triangular change x_s -> x_s + L_s(u) takes F to a direct
    # sum of smooth ternary Hesse cubics plus Fermat central terms;
    # hence its projective zero locus is smooth.
    q = {}
    for s, (x, y, z) in enumerate(xs):
        i = 3*s
        fs = terms[s]
        q[i, i+1] = lam[s]*sp.diff(fs, z)
        q[i+1, i+2] = lam[s]*sp.diff(fs, x)
        q[i, i+2] = -lam[s]*sp.diff(fs, y)

    def biv(i, j):
        if i == j:
            return sp.S.Zero
        return q.get((i, j), sp.S.Zero) if i < j else -q.get((j, i), sp.S.Zero)

    checked = 0
    for i, j, a in combinations(range(len(variables)), 3):
        jac = sum(biv(i, r)*sp.diff(biv(j, a), v)
                  + biv(j, r)*sp.diff(biv(a, i), v)
                  + biv(a, r)*sp.diff(biv(i, j), v)
                  for r, v in enumerate(variables))
        assert sp.expand(jac) == 0, ("Jacobi", (k, m, i, j, a))
        checked += 1
    for i in range(len(variables)):
        casimir = sum(biv(i, j)*sp.diff(F, v) for j, v in enumerate(variables))
        assert sp.expand(casimir) == 0, ("Casimir", k, m, i)
    for a, b in combinations(range(k), 2):
        for xa in xs[a]:
            for xb in xs[b]:
                assert sp.diff(F, xa, xb) == 0
    # Intrinsic (P tensor P)(Hess F)^3/6 must equal the sum of block determinants.
    P = {}
    for a in range(k):
        indices = (3*a, 3*a+1, 3*a+2)
        for perm in permutations(indices):
            inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
            P[perm] = (-1)**inversions * lam[a]
    hessian = {(i, j): sp.diff(F, variables[i], variables[j])
               for i in range(3*k) for j in range(3*k)}
    contraction = sp.expand(sum(
        Pa*Pb*hessian[p[0], q[0]]*hessian[p[1], q[1]]*hessian[p[2], q[2]]/6
        for p, Pa in P.items() for q, Pb in P.items()))
    block_formula = sp.expand(sum(
        lam[a]**2 * sp.hessian(terms[a], xs[a]).det() for a in range(k)))
    assert sp.expand(contraction-block_formula) == 0, ("invariant Hessian", k, m)
    n = 3*k + m - 2
    assert len(variables) == n + 2
    print(f"PASS n={n}, k={k}, m={m}: {checked} Jacobi triples, "
          f"{len(variables)} Casimir equations, cross-block and invariant Hessians")


if __name__ == "__main__":
    for k, m in ((1, 2), (2, 0), (2, 2), (3, 0), (3, 3), (4, 0)):
        test(k, m)
