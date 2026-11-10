#!/usr/bin/env python3
"""Reconstruct and verify genuine relative/absolute mixed diagonal products.
Exact arithmetic over Q(h). Full symbolic absolute calculation can be lengthy.
This does NOT certify the remaining comparison with categorical Nat.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from itertools import combinations_with_replacement
from math import comb
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from curved_diagonal import Mixed, F, h, toexpr, FIELD
from absolute_diagonal import AbsoluteMixed

def zero(M): return all(sp.cancel(x)==0 for x in M)
def zero_product(A, B):
    left=DomainMatrix.from_Matrix(A).convert_to(FIELD)
    right=DomainMatrix.from_Matrix(B).convert_to(FIELD)
    return (left*right).is_zero_matrix

def rank(M): return len(DomainMatrix.from_Matrix(M).to_field().rref()[1])
def text(x): return str(sp.factor(x))
def matrix_witness(M):
    return {'shape':[len(M),len(M[0])], 'entries':[
        [i,j,[[k,text(toexpr(c))] for k,c in sorted(a.items())]]
        for i,row in enumerate(M) for j,a in enumerate(row) if a]}
def scalar_matrix(M):
    return {'shape':list(M.shape), 'entries':[[i,j,text(M[i,j])] for i in range(M.rows) for j in range(M.cols) if M[i,j]!=0]}
def c_checks(a,d,s1,s2):
    blocks=a.blocks(d,s1,s2);out={}
    for r in (1,2):
        dm=a.cdiff(-1,r,blocks);d0=a.cdiff(0,r,blocks);d1=a.cdiff(1,r,blocks)
        assert zero_product(d0,dm) and zero_product(d1,d0)
        rm,r0=rank(dm),rank(d0)
        out[str(r)]={'dimensions':[dm.cols,d0.cols,d0.rows], 'ranks':[rm,r0], 'H0_dimension':d0.cols-rm-r0}
    return out

def run():
    u,x,y,z=sp.symbols('u x y z');xs=[u,x,y,z]
    relative=Mixed(h,1)
    d,s1,s2=relative.homotopies()
    cycles,lifts,mons,relations,mu=relative.relative_products(d,s1,s2)
    Grel=(x**3+y**3+z**3)/3+h**2*x*y*z/3+(1+h**6/54)*u*x*y-h**4*u*z**2/18-h**2*u**2*z/12
    gradients=sp.Matrix([[sp.Poly(sp.diff(Grel,v),xs).coeff_monomial(xs[i]*xs[j]) for v in [x,y,z]] for i,j in mons])
    assert zero(mu*gradients) and rank(gradients)==3 and rank(mu)==7
    relchecks=c_checks(relative,d,s1,s2)
    assert [relchecks[str(r)]['H0_dimension'] for r in (1,2)]==[4,7]
    result={'version':'v26','date':'2026-11-10','coefficient_field':'Q(h)',
      'scope':'Stabilized diagonal endomorphism products from noncommutative relations; NOT yet categorical Nat.',
      'relative':{'lambda':1,'base':'Q(h)[u]','c_checks':relchecks,'G':text(Grel),
        'd':[matrix_witness(M) for M in d[1:]], 's1':[matrix_witness(M) for M in s1],
        's2':matrix_witness(s2),'degree_one_cycles':scalar_matrix(cycles),
        'closed_endomorphism_lifts':scalar_matrix(lifts),'product_matrix':scalar_matrix(mu),
        'kernel_basis':scalar_matrix(sp.Matrix.hstack(*relations))}}
    print('PASS: relative Q(h) products and integrated cubic',flush=True)
    absolute=AbsoluteMixed(h,1)
    d,s1,s2=absolute.homotopies()
    print('PASS: absolute curvature homotopies',flush=True)
    cycles,lifts,mons,relations,mu=absolute.products(d,s1,s2)
    print('PASS: absolute closed lifts and products',flush=True)
    B=1+sp.Rational(29,648)*h**6+h**12/4374
    G=Grel+B*u**3
    gradients=sp.Matrix([[sp.Poly(sp.diff(G,v),xs).coeff_monomial(xs[i]*xs[j]) for v in xs] for i,j in mons])
    assert zero(mu*gradients) and rank(gradients)==4 and rank(mu)==6
    checks=c_checks(absolute,d,s1,s2)
    print('PASS: absolute small complexes',flush=True)
    assert [checks[str(r)]['H0_dimension'] for r in (1,2)]==[4,6]
    selected=[k for k,(i,j) in enumerate(mons) if i==j]
    det=sp.factor(gradients[selected,:].det());assert det!=0
    Ghalf=sp.factor(G.subs(h,sp.Rational(1,2)))
    ideal=sp.groebner([sp.diff(Ghalf,v) for v in xs],*xs,order='grevlex')
    assert ideal.is_zero_dimensional
    result['absolute']={'lambda':1,'base':'Q(h)','c_checks':checks,'G':text(G),
      'u_cubic_coefficient':text(B),'square_monomial_gradient_minor':text(det),
      'smooth_at_h_half':True,'smooth_generic_reason':'G(h=0) is the smooth cubic F_lambda with lambda=1.',
      'koszul_spaces':[scalar_matrix(M) for M in absolute.koszul],
      'd':[matrix_witness(M) for M in d[1:]],'s1':[matrix_witness(M) for M in s1],
      's2':[matrix_witness(M) for M in s2],'degree_one_cycles':scalar_matrix(cycles),
      'closed_endomorphism_lifts':[{f'{j}:{p}':matrix_witness(M) for (j,p),M in sorted(f.items())} for f in lifts],
      'product_matrix':scalar_matrix(mu),'kernel_basis':scalar_matrix(sp.Matrix.hstack(*relations))}
    result['five_variable_extension']={'operation':'Tensor the absolute four-variable diagonal with the ordinary factor for v^3.',
       'kernel':'The four displayed gradients together with v^2.', 'H0_dimensions':[5,10],
       'status':'Deduction using the one-variable Koszul complex; no independent five-variable elimination.'}
    result['not_proved']=['Comparison with actual residual-category derived natural transformations and their products.',
        'Generic rotation-preserving equivalence with the displayed commutative cubic.',
        'A formula for arbitrary lambda in the absolute model; only lambda=1 is symbolically certified here.',
        'Full independent reaudit of the existing all-Artin PBW and formal categorical reconstruction proofs.']
    print('PASS: absolute Q(h) products, polynomial cubic, and h=1/2 smoothness',flush=True)
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('build/curved_diagonal_certificate.json'))
    args=parser.parse_args();data=run();args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(args.output,flush=True)
