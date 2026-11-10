#!/usr/bin/env python3
"""Reproducible exact tests; no nc-derived-natural-transformation calculation."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s
from finite_recovery import (quadratic_monomials, integrability_matrix,
                             local_kernel, solve_unique_columns, recover, encode)


def mixed_product(L, C):
    x,y,z,u,v = xs = s.symbols('x y z u v')
    monomials = quadratic_monomials(xs)
    cross = [xs[i]*xs[j] for i in range(5) for j in range(i+1,5)]
    mu = s.zeros(10, 15)
    for j, monomial in enumerate(monomials):
        if monomial in cross:
            mu[cross.index(monomial),j] = 1
    for square, relation in {
        x*x:-C*y*z-L*y*u, y*y:-C*x*z-L*x*u,
        z*z:-C*x*y, u*u:-L*x*y/3, v*v:s.Integer(0)
    }.items():
        p = s.Poly(relation, *xs)
        for i,m in enumerate(cross):
            mu[i,monomials.index(square)] = p.coeff_monomial(m)
    return xs, mu


def check(condition, name):
    if not condition:
        raise AssertionError(name)


def run():
    h,L,C = s.symbols('h L C')
    result = {'version':'1.0', 'date':'2026-11-10',
              'scope':'Algebraic reconstruction from supplied matrices; commutative candidate family only',
              'not_proved':['Actual nc low-rotation matrix', 'Generic nc/commutative category equivalence']}
    # A rational kernel basis need not be saturated at h=0.
    E0=s.Matrix([[h,1,1]])
    B, steps=local_kernel(E0,h)
    a0=s.Matrix([0,1,-1])
    c=solve_unique_columns(B.subs(h,0),a0)
    check((E0*B*c)==s.zeros(1,1), 'saturation identity')
    check(B.subs(h,0).rank()==2, 'saturation residue rank')
    check(steps>0, 'saturation really exercised')
    result['local_saturation']={'steps':steps,'basis':B,'lift':B*c}
    # A formally integrable-looking special matrix can have no compatible lift.
    Bbad,_=local_kernel(s.Matrix([[h,0]]),h)
    try:
        solve_unique_columns(Bbad.subs(h,0),s.Matrix([1,0]))
    except ValueError:
        result['special_solution_without_lift_rejected']=True
    else:
        raise AssertionError('nonliftable special solution accepted')
    xs,mu=mixed_product(L,C)
    x,y,z,u,v=xs
    F=(x**3+y**3+z**3)/3+u**3+v**3+L*u*x*y+C*x*y*z
    grads=[s.diff(F,t) for t in xs]
    mons=quadratic_monomials(xs)
    Q=s.Matrix([[s.Poly(q,*xs).coeff_monomial(m) for q in grads] for m in mons])
    check(mu*Q==s.zeros(10,5),'exact mixed product kernel')
    crosscols=[j for j,m in enumerate(mons) if len(m.free_symbols)==2]
    check(mu[:,crosscols]==s.eye(10),'product identity minor')
    E=integrability_matrix(grads,xs)
    columns=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23]
    rows=[0,1,2,5,6,7,8,10,11,12,13,15,16,17,19,22,23,34,37,38,42,44,49]
    minor=s.factor(E.extract(rows,columns).det(method='domain-ge'))
    check(minor==5971968*C**5*L**5,'integrability nonzero minor')
    U=s.diag(1,1,1,1,0); V=s.diag(0,0,0,0,1)
    check(E*s.Matrix(list(U))==s.zeros(50,1),'first kernel vector')
    check(E*s.Matrix(list(V))==s.zeros(50,1),'second kernel vector')
    result['mixed_template']={'domain_basis':[str(m) for m in mons],
            'codomain_basis':[str(xs[i]*xs[j]) for i in range(5) for j in range(i+1,5)],
            'matrix':mu,'integrability_minor_rows_zero_based':rows,
            'integrability_minor_columns_zero_based':columns,
            'integrability_minor':minor,'kernel_dimension_when_LC_nonzero':2,
            'rank_at_L1_C0':E.subs({L:1,C:0}).rank(),
            'rank_at_L0_C2':E.subs({L:0,C:2}).rank()}
    Delta=(L**3+3+3*C**3)**2-12*L**3*C**3
    aa=(L**3-3-3*C**3)/6
    bb=(-3-L**3+3*C**3)/6
    check(s.expand(aa+bb+1)==0,'discriminant sum')
    check(s.expand(aa**2+L**3/3-Delta/36)==0,'discriminant u')
    check(s.expand(bb**2+C**3-Delta/36)==0,'discriminant z')
    result['smoothness_discriminant']=s.expand(Delta)
    # All-order ALGEBRAIC TEST INPUT, not the unknown nc product.
    Lt=1+2*h**6
    Ct=s.Rational(13,36)*h**2+3*h**8
    _,testmu=mixed_product(Lt,Ct)
    change=s.eye(10); change[0,1]=h; change[2,7]=h**2
    testmu=change*testmu
    F0=(x**3+y**3+z**3)/3+u**3+v**3+u*x*y
    recovered=recover(testmu,xs,h,F0)
    poly=s.Poly(recovered['cubic'],*xs)
    norm=3*poly.coeff_monomial(x**3)
    recoveredL=s.cancel(poly.coeff_monomial(u*x*y)/norm)
    recoveredC=s.cancel(poly.coeff_monomial(x*y*z)/norm)
    check(s.cancel(recoveredL-Lt)==0,'recovered L')
    check(s.cancel(recoveredC-Ct)==0,'recovered C')
    result['all_order_algebraic_test']={
       'input_provenance':'synthetic commutative product, NOT nc data',
       'target_L':Lt,'target_C':Ct,'recovered_L':recoveredL,'recovered_C':recoveredC,
       'recovered_cubic':recovered['cubic'],
       'kernel_rank':recovered['saturated_kernel_rank'],
       'saturation_steps':recovered['saturation_steps'],
       'integrability_rank_generic':recovered['integrability_rank_generic'],
       'integrability_rank_special':recovered['integrability_rank_special'],
       'smooth_special':recovered['smooth_special_over_coefficient_field']}
    # The naive Hessian polynomial agrees only modulo h^3 with the known result.
    lam=s.symbols('lam')
    classical=(x**3+y**3+z**3)/3+u**3+v**3+lam*u*x*y
    G2=x*y*z/3-lam**2*u**2*z/12
    c0=s.Rational(1,3)+lam**3/36
    check(s.expand(G2-c0*x*y*z+lam**2*z*s.diff(classical,u)/36)==0,
          'known second-jet Jacobian identity')
    result['known_second_jet_identity']=True
    result['all_checks_passed']=True
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('computations/finite_recovery_certificate.json'))
    args=parser.parse_args()
    result=run()
    root=Path(__file__).resolve().parents[1]
    result['source_sha256']={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()
        for p in [root/'computations/finite_recovery.py',Path(__file__).resolve()]}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(encode(result),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS: local saturation; exact product and rank certificate; discriminant; all-order synthetic recovery; second-jet identity')
    print('Not computed: actual nc-derived-natural-transformation product.')

if __name__=='__main__':
    main()
