#!/usr/bin/env python3
"""Finite checks for the geometric-projector route, NOT a categorical proof.

Checks field-sector arithmetic and exact bounded free-complex examples of
closed-basis lifting. Geometric Morita, proper base change, and the existing
formal MF equivalence are mathematical inputs, not verified by this script.
"""
from __future__ import annotations
import argparse
import json
from math import comb
from pathlib import Path
import sympy as s

h = s.Symbol('h')


def dim_sector(n: int, r: int, degree: int) -> int:
    """BFK cubic weight formula is an input; this only checks its arithmetic."""
    result = 0
    if degree % 2 == 0:
        j = r + 3 * (degree // 2)
        if 0 <= j <= n:
            result += comb(n, j)
    if (degree - n) % 2 == 0 and 2 * r + 3 * degree - n == 0:
        result += 2
    return result


def change_basis(n: int, seed: int) -> tuple[s.Matrix, s.Matrix]:
    u = s.eye(n)
    for j in range(n - 1):
        u[j, j + 1] = ((j + seed) % 3 - 1) * h + (j % 2) * h**2
    inv = s.zeros(n)
    v = u - s.eye(n)
    power = s.eye(n)
    for _ in range(n):
        inv += power
        power = -power * v
    assert (u * inv - s.eye(n)).applyfunc(s.expand) == s.zeros(n)
    return u, inv


def truncate_matrix(a: s.Matrix, m: int) -> s.Matrix:
    """Matrix of multiplication on Q[h]/h^(m+1), coefficient order 1,h,... ."""
    width = m + 1
    out = s.zeros(a.rows * width, a.cols * width)
    for i in range(a.rows):
        for j in range(a.cols):
            p = s.Poly(s.expand(a[i, j]), h)
            for (e,), c in p.terms():
                if e <= m:
                    for v in range(width - e):
                        out[i * width + v + e, j * width + v] += c
    return out


def example(d: int, h1: int) -> dict:
    """Two contractible directions, d H0 classes and h1 H1 classes."""
    incoming, outgoing = 2, 3
    n0, n1 = incoming + d + outgoing, outgoing + h1
    b = s.zeros(n0, incoming)
    for i in range(incoming):
        b[i, i] = 1
    a = s.zeros(n1, n0)
    for i in range(outgoing):
        a[i, incoming + d + i] = 1
    z = s.eye(n0)[:, incoming:incoming + d]
    u, ui = change_basis(n0, 1)
    w, wi = change_basis(n1, 2)
    bn, an, zn = u * b, (w * a * ui).applyfunc(s.expand), u * z
    assert (an * bn).applyfunc(s.expand) == s.zeros(n1, incoming)
    assert (an * zn).applyfunc(s.expand) == s.zeros(n1, d)
    assert (ui * zn - z).applyfunc(s.expand) == s.zeros(n0, d)
    assert (wi * an * u - a).applyfunc(s.expand) == s.zeros(n1, n0)
    cases = []
    for m in range(5):
        am, bm, zm = (truncate_matrix(x, m) for x in (an, bn, zn))
        rb, ra = bm.rank(), am.rank()
        assert rb == incoming * (m + 1)
        assert ra == outgoing * (m + 1)
        assert am * zm == s.zeros(am.rows, zm.cols)
        assert bm.row_join(zm).rank() == rb + d * (m + 1)
        h0_dimension = n0 * (m + 1) - ra - rb
        h1_dimension = n1 * (m + 1) - ra
        assert h0_dimension == d * (m + 1)
        assert h1_dimension == h1 * (m + 1)
        cases.append({'m': m, 'H0_Q_dimension': h0_dimension,
                      'H1_Q_dimension': h1_dimension,
                      'closed_basis_mod_boundaries': True})
    return {'H0_rank': d, 'H1_rank': h1, 'polynomial_chain_conjugacy': True,
            'coordinate_lifts_are_cycles': True, 'artin_checks': cases}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('build/geometric_rotation_certificate.json'))
    args = parser.parse_args()
    sample = []
    count = 0
    for n in range(5, 33):
        for r in (1, 2):
            dims = [dim_sector(n, r, j) for j in (-1, 0, 1)]
            assert dims[0] == 0
            assert dims[1] == (n if r == 1 else comb(n, 2))
            if n <= 8:
                sample.append({'N': n, 'r': r, 'neighbor_dimensions': dims})
            count += 1
    assert dim_sector(5, 1, 1) == 2
    assert dim_sector(7, 2, 1) == 2
    # Failure when the special H0 basis does not lift: [R --h--> R].
    hm = truncate_matrix(s.Matrix([[h]]), 1)
    cycles = hm.nullspace()
    assert len(cycles) == 1 and cycles[0][0] == 0
    certificate = {
        'version': 'nc-cubic-v33', 'date': '2026-11-11',
        'scope': 'Finite arithmetic and bounded-free-complex checks only.',
        'sector_formula_input': 'identity: even j, Jac degree r+3j/2; nonidentity: j=N mod2 and 2r+3j-N=0',
        'sector_cases_checked': count, 'sector_samples': sample,
        'nonzero_H1_lifting_examples': [example(5, 2), example(21, 2)],
        'zero_H1_lifting_example': example(10, 0),
        'missing_lift_counterexample': {'ring': 'Q[h]/h^2', 'complex': '[R --h--> R] in degrees0,1',
                                       'special_H0_dimension': 1, 'image_of_cycles_under_reduction': 0},
        'not_verified': ['Geometric derived Morita theorem or relative kernel construction.',
                         'Existing formal MF/Artin residual equivalences and characteristic map.',
                         'The noncommutative finite-diagonal matrix computation.',
                         'Generic algebraic categorical equivalence.']}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'PASS: {count} sector cases; 15 Artin bounded-complex checks; missing-lift counterexample.')


if __name__ == '__main__':
    main()
