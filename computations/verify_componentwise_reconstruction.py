#!/usr/bin/env python3
"""Exact certificates for the componentwise-chart section of paper B.

No finite-field sampling and no floating-point arithmetic.  The tests are not a
proof of relative saturation or of a categorical equivalence.  The center
certificate is an actual free-algebra identity over ZZ[h].
"""
from __future__ import annotations
from itertools import combinations, permutations
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def check_chart() -> dict:
    a,b,c,d,e,f,h = sp.symbols('a b c d e f h')
    matrix = sp.Matrix([[1,0,a,b,c],[0,1,d,e,f]])
    p = {(i,j):sp.expand(h*matrix[:,[i,j]].det())
         for i,j in combinations(range(5),2)}
    for i,j,k,l in combinations(range(5),4):
        assert sp.expand(p[i,j]*p[k,l]-p[i,k]*p[j,l]+p[i,l]*p[j,k]) == 0
    inverse = [-p[1,j]/h for j in range(2,5)] + [p[0,j]/h for j in range(2,5)]
    assert all(sp.cancel(x-y)==0 for x,y in zip(inverse,[a,b,c,d,e,f]))
    assert p[0,1] == h
    assert all(x.subs(h,0)==0 for x in p.values())
    return {'chart':'cone over Gr(2,5), p01=h', 'plucker_equations':5,
            'inverse_coordinates':6,'status':'passed'}

def check_linear_algebraization() -> dict:
    s,h = sp.symbols('s h')
    M = sp.Matrix([[1-s*h,-(1+h)]])
    z = sp.Matrix([(1+h)/(1-s*h),1])
    assert all(sp.cancel(x)==0 for x in M*z)
    assert z.subs(h,0)==sp.Matrix([1,1])
    jet = z.applyfunc(lambda x: sp.series(x,h,0,5).removeO())
    residual = M*jet
    assert all(sp.Poly(x,h).nth(i)==0 for x in residual for i in range(5))
    assert (1-s*h).subs(h,0)==1
    return {'scope':'illustration of the linear lemma, not a universal cubic center',
            'denominator':'1-s*h','verified_jet_order':4,'status':'passed'}

def check_singular_block() -> dict:
    x,y,z,a,b,c,u=sp.symbols('x y z a b c u')
    vs=(x,y,z,a,b,c,u)
    F=x**3+y**3+u*z**2+a**3+b**3+c**3+u**3
    grad=[sp.diff(F,t) for t in vs]
    G=sp.groebner(grad,*vs,domain=sp.QQ)
    for t in (x,y,a,b,c): assert G.reduce(t**2)[1]==0
    for t in (z,u): assert G.reduce(t**3)[1]==0
    assert G.reduce(F)[1]==0
    P=sp.zeros(7)
    for block in ((0,1,2),(3,4,5)):
        i,j,k=block
        for ii,jj,kk in ((i,j,k),(j,k,i),(k,i,j)):
            P[ii,jj]=sp.diff(F,vs[kk]);P[jj,ii]=-P[ii,jj]
    for i,j,k in combinations(range(7),3):
        jac = sum(P[i,r]*sp.diff(P[j,k],vs[r])+
                  P[j,r]*sp.diff(P[k,i],vs[r])+
                  P[k,r]*sp.diff(P[i,j],vs[r]) for r in range(7))
        assert sp.expand(jac)==0
    assert all(sp.expand(t)==0 for t in P*sp.Matrix(grad))
    point={x:0,y:0,z:1,a:-1,b:-1,c:0,u:1}
    assert F.subs(point)==0 and P.subs(point).rank()==4
    return {'n':5,'jacobi_triples':35,'rank_witness':4,
            'gradient_radical':'all seven variables',
            'pure_first_block':'x^3+y^3, singular at [0:0:1]', 'status':'passed'}

def check_polynomial_center() -> dict:
    cert=json.loads((ROOT/'computations/fermat_center_certificate.json').read_text())
    h=sp.symbols('h')
    relations=[{'xy':1,'yx':-1,'zz':-h},
               {'yz':1,'zy':-1,'xx':-h},
               {'zx':1,'xz':-1,'yy':-h}]
    target={w:sp.Integer(3) for w in ('xxx','yyy','zzz')}
    for perm in permutations('xyz'):target[''.join(perm)]=-h*h
    cyclic=str.maketrans('xyz','yzx')
    for shift in range(3):
        def rot(w: str) -> str:
            for _ in range(shift): w=w.translate(cyclic)
            return w
        rhs: dict[str,sp.Expr]={}
        for term in cert['terms']:
            assert isinstance(term['relation'],int) and 1<=term['relation']<=3
            assert set(term['prefix']+term['suffix'])<=set('xyz')
            assert all(isinstance(c,int) for c in term['coefficient'])
            factor=sum(sp.Integer(c)*h**i for i,c in enumerate(term['coefficient']))
            for word,c in relations[term['relation']-1].items():
                w=rot(term['prefix']+word+term['suffix'])
                rhs[w]=rhs.get(w,0)+factor*c
        lhs: dict[str,sp.Expr]={}
        generator=rot('x')
        for word,c in target.items():
            w=rot(word)
            lhs[w+generator]=lhs.get(w+generator,0)+c
            lhs[generator+w]=lhs.get(generator+w,0)-c
        assert all(sp.expand(lhs.get(w,0)-rhs.get(w,0))==0 for w in set(lhs)|set(rhs))
    return {'base_ring':'ZZ[h]','relations':3,'certificate_terms':15,
            'cyclic_commutators':3, 'uses_h_inverse':False,
            'scope':'universal Fermat centrality only, not the full mixed family', 'status':'passed'}

def main() -> None:
    results={'arithmetic':'exact Q-polynomial/free-algebra identities',
             'chart':check_chart(), 'linear_example':check_linear_algebraization(),
             'singular_block':check_singular_block(), 'center':check_polynomial_center(),
             'not_verified':['general relative saturation','general PBW on a component chart',
                             'formal/etale categorical reconstruction theorem']}
    print(json.dumps(results,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
