#!/usr/bin/env python3
"""Exact Q/ZZ certificates for non-elliptic Poisson components.
No categorical reconstruction is asserted by these computations.
"""
from __future__ import annotations
from itertools import combinations, permutations, product
from pathlib import Path
import argparse, hashlib, json
import sympy as s
from sympy.polys.matrices import DomainMatrix
ROOT=Path(__file__).resolve().parents[1]
V=s.symbols('x y z a b c u'); x,y,z,a,b,c,u=V
T=list(combinations(range(7),3))
def alt(t):
    return {p:(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)) for p in permutations(t)}
P={**alt((0,1,2)),**alt((3,4,5))}
Q=[alt(t) for t in T]
def cubic(kind):
    f=x*y*z+y**3+z**3 if kind=='node' else x*z**2+y**3
    return f+a**3+b**3+c**3+u*(x**2+a**2+b**2+c**2)+u**3

def matrix(F):
    H={(b,r,l):int(s.diff(F,V[b],V[r],V[l])) for b,r,l in product(range(7),repeat=3)}
    H={k:v for k,v in H.items() if v}
    rows={}
    for column,q in enumerate(Q):
        for i,j,k in T:
            for alpha in range(7):
                for (b,r,l),value in H.items():
                    v=sum(q.get((ii,r,alpha),0)*P.get((jj,kk,b),0)+P.get((ii,r,alpha),0)*q.get((jj,kk,b),0)
                          for ii,jj,kk in ((i,j,k),(j,k,i),(k,i,j)))
                    if v: rows.setdefault((i,j,k,alpha,l),[0]*35)[column]+=v*value
    keys=sorted(k for k,row in rows.items() if any(row))
    return s.Matrix([rows[k] for k in keys]),keys

def direct_rank(F):
    grad=[s.diff(F,q) for q in V]
    pi={(i,j):s.expand(sum(P.get((i,j,r),0)*grad[r] for r in range(7))) for i,j in product(range(7),repeat=2)}
    rows={}
    for column,q in enumerate(Q):
        dpi={(i,j):s.expand(sum(q.get((i,j,r),0)*grad[r] for r in range(7))) for i,j in product(range(7),repeat=2)}
        for i,j,k in T:
            J=s.expand(sum(pi[ii,r]*s.diff(dpi[jj,kk],V[r])+dpi[ii,r]*s.diff(pi[jj,kk],V[r])
                           for ii,jj,kk in ((i,j,k),(j,k,i),(k,i,j)) for r in range(7)))
            for mon,coef in s.Poly(J,*V).terms():
                if coef: rows.setdefault((i,j,k,mon),[0]*35)[column]=int(coef)
    return DomainMatrix.from_Matrix(s.Matrix(list(rows.values()))).convert_to(s.QQ).rank()

def verify(kind,direct=False):
    F=cubic(kind)
    # The u=0 patch is handled by an elementary proof in the manuscript.
    G=s.groebner([s.diff(F,q).subs(u,1) for q in V],x,y,z,a,b,c,order='grevlex')
    assert list(G)==[s.Integer(1)]
    M,keys=matrix(F); dm=DomainMatrix.from_Matrix(M).convert_to(s.QQ)
    _,cp=dm.rref(); _,rp=dm.transpose().rref()
    assert len(cp)==len(rp)==33
    zero=[T.index((0,1,2)),T.index((3,4,5))]
    assert all(not any(M[:,j]) for j in zero)
    assert set(cp)==set(range(35))-set(zero)
    minor=M.extract(rp,cp)
    det=int(DomainMatrix.from_Matrix(minor).convert_to(s.ZZ).det())
    expected=2**24*3**12 if kind=='node' else -2**33*3**12
    assert det==expected,(kind,det)
    aa,bb=s.symbols('alpha beta')
    pp={k:aa*v for k,v in alt((0,1,2)).items()}; pp.update({k:bb*v for k,v in alt((3,4,5)).items()})
    grad=[s.diff(F,q) for q in V]
    pi={(i,j):sum(pp.get((i,j,r),0)*grad[r] for r in range(7)) for i,j in product(range(7),repeat=2)}
    for i,j,k in T:
        assert s.expand(sum(pi[ii,r]*s.diff(pi[jj,kk],V[r]) for ii,jj,kk in ((i,j,k),(j,k,i),(k,i,j)) for r in range(7)))==0
    point=[0,1,0,-1,0,0,0]; d=dict(zip(V,point))
    assert F.subs(d)==0
    pm=s.Matrix([[pi[i,j].subs(d).subs({aa:1,bb:1}) for j in range(7)] for i in range(7)])
    assert pm.rank()==4 and pm.row_join(s.Matrix(point)).rank()==5
    h=s.symbols('h')
    if kind=='node':
        B=s.Matrix([[0,-(1+h/2)*z,(1-h/2)*y],[(1-h/2)*z,-3*h*y,-(1+h/2)*x],[-(1+h/2)*y,(1-h/2)*x,-3*h*z]])
        e=-h*((h*h+12)*x*y*z+(12-3*h*h)*(y**3+z**3))/4
        condition='h != 0; h^2 != 4,-12'
    else:
        B=s.Matrix([[0,-z,y-h*z],[z,-3*h*y,-x],[-y-h*z,x,-h*x]])
        e=-3*h*(x*z*z+y**3-h*h*y*z*z)
        assert s.expand((x*z*z+y**3-h*h*y*z*z).subs(x,x+h*h*y))==x*z*z+y**3
        condition='h != 0'
    assert s.expand(B.det()-e)==0
    record={'kind':kind,'cubic':str(F),'nonzero_rows':M.rows,'columns':35,'rank':33,
       'kernel_triples':[[0,1,2],[3,4,5]],'minor_rows':[list(keys[i]) for i in rp],
       'minor_columns':[list(T[i]) for i in cp], 'minor_determinant':str(det),
       'minor_matrix':[[int(v) for v in row] for row in minor.tolist()],
       'u1_gradient_groebner_basis':['1'],'jacobi_plane':'zero over QQ[alpha,beta]',
       'projective_rank_witness':{'point':point,'rank':4,'rank_with_euler':5},
       'quantum_multilinear_matrix':[[str(v) for v in row] for row in B.tolist()],
       'quantum_multilinear_determinant':str(s.factor(e)), 'determinant_curve_condition':condition}
    if direct:
        rank=direct_rank(F); assert rank==33
        record['independent_direct_schouten_rank']=rank
    return record

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--write',action='store_true'); ap.add_argument('--direct',action='store_true')
    args=ap.parse_args()
    result={'version':'v11','date':'2026-11-09','field':'QQ',
      'definition':'Indices 0..6 correspond to x,y,z,a,b,c,u. Rows (i,j,k,alpha,l) and columns (i,j,k) use lexicographic order.',
      'scope':'Exact component/tangent certificates, NOT proof of categorical reconstruction.',
      'examples':[verify(k,args.direct) for k in ('node','cusp')]}
    target=ROOT/'computations/nonelliptic_components_certificate.json'
    if args.write: target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    elif target.exists():
        saved=json.loads(target.read_text()); copy=json.loads(json.dumps(result))
        for data in (saved,copy):
            for e in data['examples']:e.pop('independent_direct_schouten_rank',None)
        assert saved==copy,'Certificate mismatch'
    for e in result['examples']:
        print('PASS',e['kind'],'rank',e['rank'],'det',e['minor_determinant'],'u=1 smooth, projective rank 4')
    print('Exact Q checks passed. The manuscript gives the u=0 smoothness proof.')
if __name__=='__main__':main()