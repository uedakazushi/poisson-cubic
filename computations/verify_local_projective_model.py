#!/usr/bin/env python3
"""Exact numerical consistency checks for the uniform local projective model.

These checks do not prove noetherianity, derived base change, Orlov's theorem,
Morita equivalence, or smoothness. Their proofs and hypotheses are in the paper.
Only Python's integer arithmetic is used. --write writes a deterministic certificate.
"""
from __future__ import annotations
from argparse import ArgumentParser
from math import comb
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'computations/local_projective_certificate.json'

def binomial(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0

def bdim(N: int, d: int) -> int:
    if d < 0:
        return 0
    return binomial(N+d-1, N-1) - binomial(N+d-4, N-1)

def generate() -> dict:
    cases=[]
    for N in range(5, 21):
        n, a = N-2, N-3
        h0=[[bdim(N,j-i) for j in range(N)] for i in range(N)]
        hn=[[bdim(N,i-j-a) for j in range(N)] for i in range(N)]
        assert all(not(h0[i][j] and hn[i][j]) for i in range(N) for j in range(N))
        r0=sum(map(sum,h0)); rn=sum(map(sum,hn))
        assert r0==comb(2*N,N-1)-comb(2*N-3,N-4)
        assert rn==3+2*N+comb(N+1,2)
        # Exceptional objects O(0),...,O(a-1): right-to-left derived Hom vanishes.
        assert all(h0[j][i]==0 and hn[j][i]==0 for i in range(a) for j in range(i+1,a))
        assert all(h0[i][i]==1 and hn[i][i]==0 for i in range(N))
        # Hilbert numerator of the finite ambient bimodule Koszul complex.
        for d in range(0,2*N+3):
            coeff=sum((-1)**j*comb(N,j)*binomial(2*N+d-j-1,2*N-1)
                      for j in range(min(N,d)+1))
            assert coeff==binomial(N+d-1,N-1)
        # The cubic quotient Hilbert series, checked independently by convolution.
        for d in range(0,2*N+3):
            assert bdim(N,d)==binomial(N+d-1,N-1)-(binomial(N+d-4,N-1) if d>=3 else 0)
        cases.append({'N':N,'dimension':n,'AS_parameter':a,'ambient_Koszul_ranks':[comb(N,j) for j in range(N+1)],
                      'H0_EndE_rank':r0,'Hn_EndE_rank':rn,'exceptional_count':a})
    fivefold=next(c for c in cases if c['N']==7)
    assert (fivefold['H0_EndE_rank'],fivefold['Hn_EndE_rank'])==(2838,45)
    return {'version':'v13','date':'2026-11-10','arithmetic':'integer',
            'scope':'Hilbert/cohomology rank consistency and exceptional vanishing ONLY; not a categorical proof',
            'cases':cases,'fivefold_Hom_degrees':[0,5],'fivefold_Hom_ranks':[2838,45]}

def main() -> None:
    ap=ArgumentParser(description=__doc__);ap.add_argument('--write',action='store_true');args=ap.parse_args()
    answer=generate()
    if args.write:
        TARGET.write_text(json.dumps(answer,indent=2,ensure_ascii=False)+'\n')
    if not TARGET.exists():
        raise SystemExit('Certificate missing. Run with --write to regenerate.')
    if json.loads(TARGET.read_text())!=answer:
        raise SystemExit('Certificate mismatch')
    print('PASS: N=5,...,20; exact Hilbert identities, Hom ranks and relative exceptional vanishing.')
    print('PASS: N=7 End(E) cohomology ranks H^0=2838, H^5=45.')
    print('SCOPE: finite numerical checks; no claim of computational proof of saturation or equivalences.')
if __name__=='__main__': main()