#!/usr/bin/env python3
"""Exact finite checks for filtered curved transport (not categorical verification).

The one-letter tensor coalgebra is a nonautonomous, noncommuting flow model.
The polyvector examples test Casimir/Jacobi/Koszul identities and a negative
control. No Kontsevich graph integrals or nc MF Hom complexes are computed.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from itertools import combinations
import sympy as sp


def wedge(I, J):
    if set(I) & set(J):
        return None, 0
    return tuple(sorted(I+J)), (-1)**sum(i>j for i in I for j in J)


def add(P, Q, scale=1):
    out = dict(P)
    for I, c in Q.items():
        out[I] = sp.expand(out.get(I, 0)+scale*c)
    return {I:c for I,c in out.items() if c != 0}


def bullet(P, Q, x):
    out = {}
    for I,c in P.items():
        for p,i in enumerate(I):
            for J,d in Q.items():
                K, sign = wedge(I[:p]+I[p+1:], J)
                if sign:
                    out[K] = out.get(K,0)+(-1)**p*sign*c*sp.diff(d,x[i])
    return {I:sp.expand(c) for I,c in out.items() if sp.expand(c)!=0}


def bracket(P, Q, x):
    if not P or not Q:
        return {}
    p=len(next(iter(P))); q=len(next(iter(Q)))
    sign=1 if ((p-1)*(q-1))%2==0 else -1
    return add(bullet(P,Q,x),bullet(Q,P,x),-sign)


def polyvectors():
    results=[]
    h,u=sp.symbols('h u')
    for N in (5,7):
        x=sp.symbols('x:'+str(N))
        if N==5:
            W=sum(t**3 for t in x)/3+x[3]*x[0]*x[1]
            Xi={(0,1,2):h}
        else:
            W=sum(t**3 for t in x)/3+x[6]*(x[0]*x[1]+x[3]*x[4])
            Xi={(0,1,2):h,(3,4,5):u}
        pi=bracket(Xi,{():W},x)
        assert not bracket(pi,{():W},x), 'Casimir failure'
        assert not bracket(pi,pi,x), 'Jacobi failure'
        assert not bracket(Xi,pi,x), 'second-action failure'
        # For Fermat, contraction on constant trivectors is injective.
        triples=list(combinations(range(N),3))
        columns=[]
        for I in triples:
            p=bracket({I:sp.Integer(1)},{():sum(t**3 for t in x)/3},x)
            col=[]
            for J in combinations(range(N),2):
                poly=sp.Poly(p.get(J,0),*x)
                col += [poly.coeff_monomial(t*t) for t in x]
            columns.append(col)
        rank=sp.Matrix.hstack(*(sp.Matrix(c) for c in columns)).rank()
        assert rank==len(triples)
        results.append({'N':N,'Casimir':True,'Jacobi':True,
                        'second_action':True,'constant_trivector_rank':rank})
    x=sp.symbols('z:5'); W=sum(t**3 for t in x)/3
    Xi={(0,1,2):sp.Integer(1),(0,3,4):sp.Integer(1)}
    pi=bracket(Xi,{():W},x)
    assert not bracket(pi,{():W},x)
    assert bracket(pi,pi,x) and bracket(Xi,pi,x)
    return {'positive_examples':results,
            'negative_control':'Casimir alone does not imply Jacobi or second-action vanishing'}


def flow(M=4,L=9):
    s,z=sp.symbols('s z')
    unary=sp.diag(*range(L+1))
    ternary=sp.zeros(L+1)
    for n in range(3,L+1):
        ternary[n-2,n]=n-2
    assert unary*ternary != ternary*unary
    gamma={1:s*unary+(1+s)*ternary,2:s*s*ternary}
    F=[sp.eye(L+1)]
    for m in range(1,M+1):
        rhs=sp.zeros(L+1)
        for a,g in gamma.items():
            if a<=m:
                rhs += g*F[m-a]
        F.append(rhs.applyfunc(lambda q:sp.integrate(sp.expand(q),(s,0,s))))
    for m in range(1,M+1):
        rhs=sp.zeros(L+1)
        for a,g in gamma.items():
            if a<=m: rhs += g*F[m-a]
        assert (F[m].diff(s)-rhs).applyfunc(sp.expand)==sp.zeros(L+1)
    F=[f.subs(s,1) for f in F]
    H=[sp.eye(L+1)]
    for m in range(1,M+1):
        H.append(-sum((F[a]*H[m-a] for a in range(1,m+1)),sp.zeros(L+1)))
    identity_checks=0
    for m in range(M+1):
        expected=sp.eye(L+1) if m==0 else sp.zeros(L+1)
        assert sum((F[a]*H[m-a] for a in range(m+1)),sp.zeros(L+1))==expected
        assert sum((H[a]*F[m-a] for a in range(m+1)),sp.zeros(L+1))==expected
        identity_checks+=2
    coproduct_checks=0
    for m in range(M+1):
        for n in range(L+1):
            for q in range(L+1):
                for r in range(L+1-q):
                    left=F[m][q+r,n]
                    right=sum(F[a][q,i]*F[m-a][r,n-i]
                              for a in range(m+1) for i in range(n+1))
                    assert left==right
                    coproduct_checks+=1
    for matrices in (F,H):
        for m,T in enumerate(matrices):
            for n in range(L+1):
                if n==0 or n%2==0 or n>2*m+1:
                    assert T[1,n]==0
    # Taylor substitutions: inverse on a possibly nonnilpotent object symbol z.
    t=sp.symbols('t')
    f=sum(t**m*sum(F[m][1,n]*z**n for n in range(1,L+1)) for m in range(M+1))
    g=sum(t**m*sum(H[m][1,n]*z**n for n in range(1,L+1)) for m in range(M+1))
    # Truncate in t after each multiplication to control expression size.
    def trunc(p):
        p=sp.Poly(sp.expand(p),t)
        return sum(p.nth(k)*t**k for k in range(M+1))
    def sub(p,a):
        out=0;power=1
        pp=sp.Poly(p,z)
        for n in range(pp.degree()+1):
            out=trunc(out+pp.nth(n)*power)
            power=trunc(power*a)
        return sp.expand(out)
    assert sub(f,g)==z and sub(g,f)==z
    return {'max_parameter_order':M,'max_tensor_length':L,
            'inverse_matrix_identities':identity_checks,
            'coproduct_coefficient_identities':coproduct_checks,
            'noncommuting_time_dependent_generator':True,
            'odd_arity_filtration':True,'object_substitution_inverse':True}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    result={'scope':'finite algebra and combinatorics only, not graph/formality/category verification',
            'polyvectors':polyvectors(),'bar_flow':flow()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2,ensure_ascii=False))
    print('PASS: exact Schouten and filtered noncommuting coalgebra-flow checks')

if __name__=='__main__':
    main()
