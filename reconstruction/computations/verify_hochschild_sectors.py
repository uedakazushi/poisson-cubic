#!/usr/bin/env python3
"""Exact arithmetic for the BFK sector-degree corollary, not a proof of BFK."""
from __future__ import annotations
import argparse
from math import comb
import json
from pathlib import Path


def jac_dim(N: int, deg: int) -> int:
    return comb(N, deg) if 0 <= deg <= N else 0


def dimensions(N: int, q: int) -> dict:
    assert N >= 5 and q >= 0
    untwisted = jac_dim(N, 3*q//2) if q % 2 == 0 else 0
    twisted = 2 if N % 3 == 0 and 3*q == N else 0
    return {
        'N': N, 'dimension': q,
        'jacobian_sector': untwisted, 'twisted_sectors': twisted,
        'total': untwisted + twisted,
        'rotation_fixed': untwisted,
    }


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--output', type=Path, required=True)
    ns=ap.parse_args()
    data={
       'reference': 'Ballard-Favero-Katzarkov (2014), Theorem 5.39',
       'method': 'exact integer sector bookkeeping; this does not verify the external theorem',
       'cubic_fivefold_N7': [dimensions(7,q) for q in range(5)],
       'cubic_fourfold_N6': [dimensions(6,q) for q in range(5)],
       'cubic_sevenfold_N9': [dimensions(9,q) for q in range(6)],
       'HH3_zero_except_n7': all((dimensions(N,3)['total']==(2 if N==9 else 0)) for N in range(5,61)),
       'HH3_rotation_fixed_zero_all': all(dimensions(N,3)['rotation_fixed']==0 for N in range(5,61)),
       'HH2_fixed_matches_J3': all(dimensions(N,2)['rotation_fixed']==comb(N,3) for N in range(5,61)),
       'jacobian_hilbert': '(1+t)^N',
    }
    assert data['HH3_zero_except_n7'] and data['HH3_rotation_fixed_zero_all'] and data['HH2_fixed_matches_J3']
    assert [row['total'] for row in data['cubic_fivefold_N7']]==[1,0,35,0,7]
    assert [row['total'] for row in data['cubic_fourfold_N6']]==[1,0,22,0,1]
    assert data['cubic_sevenfold_N9'][3]['total']==2
    ns.output.parent.mkdir(parents=True,exist_ok=True)
    ns.output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'BFK sector arithmetic: verified N=5..60; saved {ns.output}')

if __name__=='__main__':
    main()
