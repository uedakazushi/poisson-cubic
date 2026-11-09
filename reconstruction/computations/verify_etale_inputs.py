#!/usr/bin/env python3
"""Exact tangent slices for two smooth cubic fivefolds; not a categorical proof."""
from __future__ import annotations
import argparse
from itertools import combinations_with_replacement
import json
from pathlib import Path
import sympy as sp


def bareiss_det(matrix: sp.Matrix) -> int:
    """Independent exact integer determinant, with checked divisions."""
    a = [[int(v) for v in row] for row in matrix.tolist()]
    n = len(a)
    sign, previous = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            pivot = next((j for j in range(k+1, n) if a[j][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot_value = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = pivot_value*a[i][j] - a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot_value
    return sign*a[-1][-1]


def tangent_slice(kind: str) -> dict:
    variables = sp.symbols('x y z a b c u')
    x, y, z, a, b, c, u = variables
    pure = x*z**2 + y**3 if kind == 'cuspidal' else x*y*z + y**3 + z**3
    F = pure + u*x**2 + a**3 + b**3 + c**3 + u*(a**2+b**2+c**2) + u**3
    exponents = []
    for word in combinations_with_replacement(range(7), 3):
        exponents.append(tuple(word.count(j) for j in range(7)))
    monomials = [sp.prod(v**e for v, e in zip(variables, powers)) for powers in exponents]
    # Column order: z_j * partial_i F, first i, then j.
    columns = [sp.Poly(v*sp.diff(F, w), *variables)
               for w in variables for v in variables]
    M = sp.Matrix([[p.coeff_monomial(m) for p in columns] for m in monomials])
    pivots = list(M.T.rref()[1])
    assert len(pivots) == 49
    free = [i for i in range(84) if i not in pivots]
    D = M.extract(pivots, list(range(49)))
    determinant = D.det(method='domain-ge')
    assert determinant == bareiss_det(D)
    expected = 2**15*3**26 if kind == 'cuspidal' else -2**6*3**25
    assert determinant == expected
    assert determinant != 0 and len(free) == 35
    Q = sp.zeros(35, 84)
    correction = M.extract(free, list(range(49))) * D.inv()
    for i, j in enumerate(free):
        Q[i, j] = 1
    for i in range(35):
        for j, k in enumerate(pivots):
            Q[i, k] = -correction[i, j]
    assert Q*M == sp.zeros(35, 49)
    assert Q.extract(list(range(35)), free) == sp.eye(35)
    return {
        'polynomial': str(F), 'variables': [str(v) for v in variables],
        'column_order': 'z_j * partial_i F; i first, then j',
        'monomial_order': 'combinations_with_replacement(range(7),3)',
        'matrix_shape': [84, 49], 'rank_over_Q': 49,
        'minor_rows_zero_based': pivots, 'minor_determinant': str(determinant),
        'independent_bareiss_determinant_check': True,
        'jacobian_degree_three_dimension': 35,
        'slice_monomial_exponents': [list(exponents[j]) for j in free],
        'slice_monomials': [str(monomials[j]) for j in free],
        'projection_annihilates_coordinate_changes': True,
        'projection_on_slice_is_identity': True,
    }


def compute() -> dict:
    N = sp.symbols('N', integer=True, positive=True)
    assert sp.expand(N*(N+1)*(N+2)/6 - N*N - N*(N-1)*(N-2)/6) == 0
    r = sp.Matrix([[0, -1], [1, -1]])
    assert r**3 == sp.eye(2)
    assert sp.eye(2)+r+r**2 == sp.zeros(2)
    assert (sp.eye(2)-r).det() == 3
    sectors = []
    for n in range(3, 16):
        m = n+2
        q = m//3 if m % 3 == 0 else None
        hh2 = int(sp.binomial(m, 3)) + (2 if q == 2 else 0)
        sectors.append({'n': n, 'nonidentity_sector_degree': q,
                        'HH2_dimension': hh2,
                        'rotation_invariant_HH2_dimension': int(sp.binomial(m, 3))})
    return {
        'arithmetic': 'exact integers and rational matrices; no finite-field sampling',
        'dimension_identity': 'binomial(N+2,3)-N^2=binomial(N,3)',
        'fourfold_extra_action': [[0, -1], [1, -1]],
        'fourfold_extra_invariant_dimension': 0,
        'low_degree_formula_checks': sectors,
        'fivefold_slices': {kind: tangent_slice(kind) for kind in ('cuspidal', 'nodal')},
        'not_verified_by_code': ['dg module obstruction theory', 'etale realization',
                                 'relative residual smoothness', 'category equivalence'],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = compute()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('Exact tangent-slice and rotation checks passed:', args.output)


if __name__ == '__main__':
    main()
