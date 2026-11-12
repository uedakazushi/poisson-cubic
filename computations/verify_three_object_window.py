#!/usr/bin/env python3
"""Exact checks for B-v42's contraction and triangular window formulas.

The matrices are finite two-term complexes over Q(h,u), not nc MF Hom models.
The check verifies signs/convergence-compatible denominators of the perturbation
formula and the elementary degree filtration used in the mathematical proof.
It does NOT prove (CF_3), dg stabilization, or categorical equivalence.
"""
from __future__ import annotations
import argparse
import json
from math import comb
from pathlib import Path
import sympy as sp

h, u = sp.symbols('h u')


def clean(m: sp.MatrixBase) -> sp.Matrix:
    return m.applyfunc(sp.cancel)


def zero(m: sp.MatrixBase, name: str) -> None:
    for value in m:
        if sp.cancel(value) != 0:
            raise AssertionError(f'{name}: nonzero entry {value}')


def contraction(D: sp.Matrix) -> dict:
    r = D.rows
    assert D.cols == r and r >= 2
    base = sp.diag(0, *([1] * (r-1)))
    zero(D.subs({h: 0, u: 0}) - base, 'residue')
    Z = sp.zeros(r)
    d0 = sp.BlockMatrix([[Z, Z], [base, Z]]).as_explicit()
    d = sp.BlockMatrix([[Z, Z], [D, Z]]).as_explicit()
    s = sp.BlockMatrix([[Z, base], [Z, Z]]).as_explicit()
    inc = sp.zeros(2*r, 2)
    inc[0, 0] = inc[r, 1] = 1
    proj = inc.T
    zero(d0*s + s*d0 - sp.eye(2*r) + inc*proj, 'initial retract')
    delta = d-d0
    J = clean((sp.eye(2*r)+s*delta).inv())
    L = clean((sp.eye(2*r)+delta*s).inv())
    ip = clean(J*inc)
    pp = clean(proj*L)
    sh = clean(s*L)
    dh = clean(proj*delta*J*inc)
    identities = {
        'small_differential': dh*dh,
        'inclusion_chain_map': d*ip-ip*dh,
        'projection_chain_map': pp*d-dh*pp,
        'retraction': pp*ip-sp.eye(2),
        'homotopy': d*sh+sh*d-sp.eye(2*r)+ip*pp,
        'homotopy_square': sh*sh,
        'projection_side_condition': pp*sh,
        'inclusion_side_condition': sh*ip,
    }
    for name, matrix in identities.items():
        zero(matrix, name)
    schur = sp.cancel(D[0,0] - (D[0:1,1:]*D[1:,1:].inv()*D[1:,0:1])[0])
    assert sp.cancel(dh[1,0]-schur) == 0
    for matrix in (ip, pp, sh, dh):
        for value in matrix:
            denominator = sp.denom(sp.cancel(value))
            assert denominator.subs({h:0, u:0}) != 0
    # The formal inverse is not justified by nilpotence of the parameters.
    assert (s*delta).subs(u,0)**6 != sp.zeros(2*r)
    return {'rank_per_term': r, 'retract_identities': len(identities),
            'small_differential': str(schur),
            'denominators_units_at_origin': True,
            'perturbation_not_nilpotent': True}


def window(N: int) -> dict:
    a = N-3
    i = 1-a
    rows = []
    for j in range(N):
        actual = [(j+q, -q) for q in range(-j, i)]
        expected = [] if j < a else [(r, j-r) for r in range(j-a+1)]
        assert actual == expected
        if j >= a:
            assert actual[0] == (0,j)
            assert all(a <= shift < j for _, shift in actual[1:])
            rows.append([(r, shift, comb(N+r-1,r)) for r,shift in actual])
    assert sorted((a+j)%3 for j in range(3)) == [0,1,2]
    # Express the three positive twists as shifts of K,K(1),K(2).
    periodic = [(a+j, (a+j)%3, 2*((a+j)//3)) for j in range(3)]
    return {'N': N, 'window_cutoff': i, 'filtration': rows,
            'periodic_twists': periodic}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    matrices = [
        sp.Matrix([[h,u+h*h,h*u],[u,1+h,u],[h,h*u,1-u]]),
        sp.Matrix([[u,h,u*h,u*u],[h,1+h,u,0],[u,u,1-h,h],[h*u,0,u,1+u]])
    ]
    data = {'scope': 'finite algebraic sign/filtration checks only; not categorical proofs',
            'contractions': [contraction(D) for D in matrices],
            'windows': [window(N) for N in range(5,17)]}
    text = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print('PASS: 16 exact Q(h,u) retract identities; 2 Schur complements; '
          'unit denominators; 12 triangular window/periodicity checks.')
    print('LIMIT: (CF_3), enhanced window equivalences and infinite convergence '
          'are mathematical arguments, not verified by these finite matrices.')


if __name__ == '__main__':
    main()
