#!/usr/bin/env python3
"""Exact finite sanity checks for the v28 multiplicative bar comparison.

These tests check cap signs and curvature on finite associative test algebras,
a nonzero multiplicativity homotopy, and algebraic normalization of the v27
candidate. They do NOT prove categorical comparison, formal MF equivalence,
or the infinite bar identities. Those claims depend on the manuscript proof.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from itertools import product
import json
from pathlib import Path
import random
import sympy as s


class MatrixDualNumbers:
    """M_2(Q)[z]/(z^2), basis E_ij*z^e; all base elements are even."""
    def __init__(self):
        self.basis = tuple(product(range(2), range(2), range(2)))
        self.index = {a:i for i,a in enumerate(self.basis)}
        self.one = {self.index[(i,i,0)]:1 for i in range(2)}
        self.w = {self.index[(i,i,1)]:1 for i in range(2)}
    def mul(self, a, b):
        i,j,e = self.basis[a]; k,l,f = self.basis[b]
        return {} if j != k or e+f >= 2 else {self.index[(i,l,e+f)]:1}


def clean(d):
    return {k:v for k,v in d.items() if v}


def add(*terms):
    result=defaultdict(int)
    for c,d in terms:
        for k,v in d.items(): result[k]+=c*v
    return clean(result)


def extend(f, vector):
    out=defaultdict(int)
    for word,c in vector.items():
        for v,a in f(word).items(): out[v]+=c*a
    return clean(out)


def bar_d(A, word):
    """b + delta_W at t=1 (t is even); input includes the two endpoints."""
    n=len(word)-2; out=defaultdict(int)
    if n:
        for i in range(n+1):
            for a,c in A.mul(word[i],word[i+1]).items():
                out[word[:i]+(a,)+word[i+2:]]+=(-1)**i*c
    for i in range(n+1):
        for a,c in A.w.items():
            out[word[:i+1]+(a,)+word[i+1:]]+=(-1)**i*c
    return clean(out)


def endpoints(A,left,value,right):
    out=defaultdict(int)
    for a,c in value.items():
        for b,d in A.mul(left,a).items():
            for e,f in A.mul(b,right).items(): out[e]+=c*d*f
    return clean(out)


def cochain_on_bar(A,phi,word):
    p=len(word)-2
    table=phi.get(p)
    return {} if table is None else endpoints(A,word[0],table[word[1:-1]],word[-1])


def right_cap(A,phi,word):
    """R_phi=(1 tensor phi) Delta with the tensor Koszul sign."""
    n=len(word)-2; out=defaultdict(int)
    for p,table in phi.items():
        if p>n: continue
        # The stored cochains are parity-p maps before multiplication by t powers.
        # All arities of a homogeneous totalized cochain have the same parity.
        sign=(-1)**(p*(n-p))
        args=word[n-p+1:n+1]
        for a,c in table[args].items():
            for b,d in A.mul(a,word[-1]).items():
                out[word[:n-p+1]+(b,)]+=sign*c*d
    return clean(out)


def random_cochain(A,p,rng):
    return {p:{args:{rng.randrange(8):rng.choice((-2,-1,1,2))}
               for args in product(range(8),repeat=p)}}


def differential_cochain(A,phi):
    """d phi = -(-1)^|phi| phi D, computed on all basis tuples."""
    parity=next(iter(phi))%2
    degrees=sorted({q for p in phi for q in (p-1,p+1) if q>=0})
    out={}
    for p in degrees:
        tab={}
        for args in product(range(8),repeat=p):
            value=defaultdict(int)
            for a,ca in A.one.items():
                for b,cb in A.one.items():
                    for w,cw in bar_d(A,(a,)+args+(b,)).items():
                        for v,cv in cochain_on_bar(A,phi,w).items():
                            value[v]+=(-1)**(parity+1)*ca*cb*cw*cv
            tab[args]=clean(value)
        out[p]=tab
    return out


def cup(A,phi,psi):
    out={}
    for p,tabp in phi.items():
        for q,tabq in psi.items():
            tab=out.setdefault(p+q,{args:{} for args in product(range(8),repeat=p+q)})
            for args in tab:
                val=defaultdict(int,tab[args])
                for a,c in tabp[args[:p]].items():
                    for b,d in tabq[args[p:]].items():
                        for e,f in A.mul(a,b).items(): val[e]+=(-1)**(p*q)*c*d*f
                tab[args]=clean(val)
    return out


def check_bar():
    A=MatrixDualNumbers(); rng=random.Random(280611); counts=defaultdict(int)
    for n in range(6):
        for _ in range(24):
            word=tuple(rng.randrange(8) for _ in range(n+2))
            lhs=extend(lambda w:bar_d(A,w),bar_d(A,word))
            rhs=defaultdict(int)
            for z,c in A.w.items():
                for a,d in A.mul(word[0],z).items(): rhs[(a,)+word[1:]]+=c*d
                for a,d in A.mul(z,word[-1]).items(): rhs[word[:-1]+(a,) ]-=c*d
            assert lhs==clean(rhs), ('curvature',word,lhs,rhs)
            counts['curvature_words']+=1
    cochains=[random_cochain(A,p,rng) for p in range(3)]
    for phi in cochains:
        p=next(iter(phi)); dphi=differential_cochain(A,phi)
        for n in range(6):
            for _ in range(16):
                word=tuple(rng.randrange(8) for _ in range(n+2))
                lhs=add((1,extend(lambda w:bar_d(A,w),right_cap(A,phi,word))),
                        (-(-1)**p,extend(lambda w:right_cap(A,phi,w),bar_d(A,word))))
                rhs=right_cap(A,dphi,word)
                assert lhs==rhs,('cap differential',p,word,lhs,rhs)
                counts['cap_differential_words']+=1
    for p,q in ((0,0),(0,1),(1,0),(1,1),(1,2),(2,1)):
        phi=cochains[p]; psi=cochains[q]; phipsi=cup(A,phi,psi)
        for n in range(5):
            for _ in range(12):
                word=tuple(rng.randrange(8) for _ in range(n+2))
                lhs=extend(lambda w:right_cap(A,phi,w),right_cap(A,psi,word))
                assert lhs==right_cap(A,phipsi,word),('cap product',p,q,n)
                counts['cap_product_words']+=1
    return {'algebra':'M_2(Q)[z]/(z^2)', 'curvature':'z I_2',
            't_specialization':'t=1; parity and all Koszul signs retained',
            'seed':280611, **dict(counts)}


def check_transfer():
    # P has degrees (0,0,1); Q is the acyclic pair of degrees (0,1).
    D=s.zeros(5); D[2,1]=1; D[4,3]=1
    I=s.eye(5)[:,:3]; Pi=I.T; H=s.zeros(5); H[3,4]=1
    dp=Pi*D*I
    assert D*H+H*D==s.eye(5)-I*Pi
    assert Pi*I==s.eye(3) and H*H==s.zeros(5)
    rng=random.Random(280612); count=0; nonzero=0
    for _ in range(30):
        maps=[]
        for j in range(2):
            S=s.zeros(5)
            for a in (0,1,3):
                for b in (2,4): S[a,b]=rng.randint(-3,3)
            maps.append((j+1)*s.eye(5)+D*S+S*D)
        a,b=maps
        assert D*a==a*D and D*b==b*D
        defect=(Pi*a*I)*(Pi*b*I)-Pi*a*b*I
        primitive=-Pi*a*H*b*I
        assert defect==dp*primitive+primitive*dp
        count+=1; nonzero+=int(defect!=s.zeros(3))
    assert nonzero>0
    return {'cases':count,'nonzero_multiplicativity_defects':nonzero,
            'identity':'J(a)J(b)-J(ab)=-d(Pi a H b I)',
            'scope':'un-curved finite SDR test of the sign; not a categorical proof'}


def check_normal_form():
    q,h=s.symbols('q h'); U,Z=s.symbols('U Z')
    a,b,c,d=s.symbols('a b c d')
    # u=a U+h^2 b Z, z=h^4 c U+d Z, q=h^6.
    A=1+s.Rational(29,648)*q+q*q/s.Integer(4374)
    equations=[
        A*a**3-q*a*a*c/12-q*q*a*c*c/18+q*q*c**3/3-1,
        3*A*a*a*b-(a*a*d+2*q*a*b*c)/12
           -q*(2*a*c*d+q*b*c*c)/18+q*c*c*d,
        3*A*a*b*b-(2*a*b*d+q*b*b*c)/12
           -(a*d*d+2*q*b*c*d)/18+c*d*d,
        A*q*b**3-q*b*b*d/12-q*b*d*d/18+d**3/3-s.Rational(1,3),
    ]
    # Independently derive the four equations from the actual binary cubic.
    us=a*U+h**2*b*Z; zs=h**4*c*U+d*Z
    binary=s.expand(A.subs(q,h**6)*us**3-h**2*us**2*zs/12
                    -h**4*us*zs**2/18+zs**3/3)
    poly=s.Poly(binary,U,Z)
    extracted=[poly.coeff_monomial(U**3)-1,
               poly.coeff_monomial(U**2*Z)/h**2,
               poly.coeff_monomial(U*Z**2)/h**4,
               poly.coeff_monomial(Z**3)-s.Rational(1,3)]
    assert all(s.expand(e.subs(q,h**6)-got)==0 for e,got in zip(equations,extracted))
    start={a:1,b:s.Rational(1,36),c:s.Rational(25,432),d:1}
    assert all(s.expand(e.subs(start)).subs(q,0)==0 for e in equations)
    Jac=s.Matrix(equations).jacobian([a,b,c,d]).subs(start).subs(q,0)
    jacdet=s.factor(Jac.det()); assert jacdet!=0
    rhs=s.Matrix([s.diff(e,q).subs(start).subs(q,0) for e in equations])
    first=-Jac.inv()*rhs
    sub={v:start[v]+first[i]*q for i,v in enumerate((a,b,c,d))}
    assert all(s.series(e.subs(sub),q,0,2).removeO().expand()==0 for e in equations)
    L=s.expand((1+q/54)*sub[a]+q*sub[c]/3)
    C=s.expand((1+q/54)*sub[b]+sub[d]/3)
    L1=s.expand(L).coeff(q); C1=s.expand(C).coeff(q)
    return {'scope':'normalization of the computed polynomial G only; no Nat comparison assumed',
            'substitution':'u=a(q)U+h^2 b(q)Z; z=h^4 c(q)U+d(q)Z; q=h^6',
            'polynomial_equations':[str(s.expand(e)) for e in equations],
            'direct_binary_substitution_verified':True,
            'initial_values':{str(v):str(start[v]) for v in (a,b,c,d)},
            'implicit_jacobian_determinant':str(jacdet),
            'first_derivatives':{str(v):str(first[i]) for i,v in enumerate((a,b,c,d))},
            'L':'1+('+str(L1)+')q+O(q^2)',
            'C_over_h_squared':'13/36+('+str(C1)+')q+O(q^2)',
            'linear_change_determinant_at_zero':'1'}


def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,
        default=Path('build/bar_comparison_certificate.json')); args=p.parse_args()
    cert={'version':'nc-cubic-v28','date':'2026-11-11',
          'bar_cap':check_bar(),'multiplicativity_homotopy':check_transfer(),
          'algebraic_candidate_normalization':check_normal_form(),
          'not_verified_by_this_script':[
              'infinite completed-bar and Hochschild quasi-isomorphism proofs',
              'categorical or residual rotation comparison',
              'generic algebraic categorical equivalence',
              'the entire existing v27 matrix computation']}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(cert,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
