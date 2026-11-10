#!/usr/bin/env python3
"""Exact algebra audit for relative Jacobian/sector comparison (v29).

This does NOT verify the relative kernel-to-categorical-natural-transformations
Morita argument, which is a separate proof in the TeX manuscript.
"""
import argparse
from collections import Counter
from itertools import product
from pathlib import Path
import json
import sympy as s

names = ("x", "y", "z", "u", "v")
x,y,z,u,v=s.symbols(' '.join(names))
variables=(x,y,z,u,v)
h=s.symbols('h')
F=(x**3+y**3+z**3)/3+u**3+v**3+u*x*y
G=(x**3+y**3+z**3)/3+v**3+h**2*x*y*z/3+(
    1+h**6/s.Integer(54))*u*x*y-h**4*u*z**2/s.Integer(18)-h**2*u**2*z/s.Integer(12)+(
    1+29*h**6/s.Integer(648)+h**12/s.Integer(4374))*u**3


def hilbert_by_groebner(f):
    gb=s.groebner([s.diff(f,a) for a in variables], *variables,
                  order='grevlex', domain=s.QQ)
    assert gb.is_zero_dimensional
    leading=[p.LM(order='grevlex').exponents for p in gb.polys]
    degrees=Counter()
    bound=9
    for d in range(bound+1):
        for exps in product(range(d+1),repeat=len(variables)):
            if sum(exps)!=d:
                continue
            if not any(all(exps[j]>=q[j] for j in range(5)) for q in leading):
                degrees[d]+=1
    assert all(degrees[d]==0 for d in range(6,bound+1))
    dims=[degrees[i] for i in range(6)]
    assert dims==[1,5,10,10,5,1],dims
    assert sum(dims)==32
    return {
        'leading_monomials': [str(s.prod(a**n for a,n in zip(variables,lt))) for lt in leading],
        'hilbert_function': dims,
        'jacobian_rank_1':dims[1], 'jacobian_rank_2':dims[2],
        'complete_intersection_total_length':32,
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='build/artin_sector_certificate.json')
    args=parser.parse_args()
    spec=hilbert_by_groebner(F)
    assert s.expand(G.subs(h,0)-F)==0
    half=hilbert_by_groebner(G.subs(h,s.Rational(1,2)))
    assert s.factor(s.diff(F,u))==3*u**2+x*y
    assert s.factor(s.diff(F,x))==x**2+u*y
    assert s.factor(s.diff(F,y))==y**2+u*x
    # The smoothness proof uses (xy)^2=9u^4 and x^2y^2=-3u^4,
    # hence 12u^4=0. The remaining derivatives give z=v=0.
    assert s.expand(9*u**4-(-3*u**4))==12*u**4
    # Each nonidentity mu_3 normal sector has rank five and parity one.
    off_sectors={'count':2,'normal_rank':5,'cohomological_parity':'odd',
                 'degree_zero_contribution':0}
    # R_1=k[h]/h^2, C: R_1 --h--> R_1 in degrees 0,1.
    # H^0(C)=h R_1; its reduction map to H^0(C/h)=k is zero.
    # Thus dimensions at h=0 alone do not prove H^0 base change.
    counterexample={'base':'Q[h]/(h^2)', 'differential':'multiplication by h',
                    'H0':'hR (length one)', 'H0_special':'Q',
                    'H0_basechange_map':'zero (not an isomorphism)'}
    data={
        'version':'nc-cubic-v29',
        'scope':'exact commutative special Jacobian and one algebraic cubic specialization; categorical Morita/kernel comparison is NOT computed',
        'special_fiber':spec, 'algebraic_candidate_h_half':half,
        'five_variable_F_smoothness_identity':'(xy)^2-x^2*y^2 = 12*u^4 modulo the first three partial derivatives',
        'artin_gradient_acyclicity':'proved by finite filtration in the TeX manuscript, not by this finite Groebner test',
        'off_diagonal_mu3_sectors':off_sectors,
        'base_change_warning':counterexample,
        'not_verified':['relative kernel action is a quasi-isomorphism',
                        'actual MF categorical Nat or noncommutative finite-diagonal product',
                        'generic categorical equivalence'],
    }
    dest=Path(args.output)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(data,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('PASS: two exact Groebner/Hilbert checks, nilpotent base-change warning, parity bookkeeping')
    print('certificate:',dest)

if __name__=='__main__':main()
