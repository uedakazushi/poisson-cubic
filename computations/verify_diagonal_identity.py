#!/usr/bin/env python3
"""Exact finite examples of the curved divided-difference diagonal.

Tests the actual contraction equations on polynomial test vectors for
n=1 and a mixed cubic in n=2.  This is NOT a proof of kernel full
faithfulness, (KF), categorical Nat, or generic equivalence.

Run: python3 computations/verify_diagonal_identity.py \
    --output build/diagonal_identity_certificate.json
"""
from __future__ import annotations
import argparse
from itertools import combinations
import json
from pathlib import Path
import sympy as sp


def vclean(v):
    z={}
    for key,value in v.items():
        value=sp.cancel(value)
        if value!=0: z[key]=value
    return z


def vadd(*vectors):
    out={}
    for v in vectors:
        for key,value in v.items(): out[key]=out.get(key,0)+value
    return vclean(out)


def vneg(v): return {key:-val for key,val in v.items()}


def setup(n:int):
    xs=sp.symbols(f'x0:{n}')
    ys=sp.symbols(f'y0:{n}')
    if n==1:
        W=ys[0]**3
        differential=sp.Matrix([[0,ys[0]],[ys[0]**2,0]])
    else:
        # A truly mixed cubic and its rank-four tensor-product MF.
        W=ys[0]**3+ys[1]**3+2*ys[0]**2*ys[1]
        a=sp.Matrix([[0,ys[0]],[ys[0]**2,0]])
        b=sp.Matrix([[0,ys[1]],[ys[1]**2+2*ys[0]**2,0]])
        differential=sp.kronecker_product(a,sp.eye(2))+sp.kronecker_product(sp.diag(1,-1),b)
    assert differential**2==W*sp.eye(differential.rows)
    # W(x)-W(y) = sum_i (y_i-x_i) delta_i.
    intermediate=W
    divided=[]
    for j in range(n):
        nxt=intermediate.subs(ys[j],xs[j])
        divided.append(sp.cancel((nxt-intermediate)/(ys[j]-xs[j])))
        intermediate=nxt
    assert sp.expand(sum((ys[j]-xs[j])*divided[j] for j in range(n))-(W.subs(dict(zip(ys,xs)))-W))==0
    subsets=[tuple(c) for p in range(n+1) for c in combinations(range(n),p)]
    return xs,ys,W,differential,divided,subsets


def verify(n:int):
    x,y,W,dm,divided,subsets=setup(n)
    mrank=dm.rows
    substitute=dict(zip(y,x))
    target=dm.subs(substitute,simultaneous=True)
    wx=W.subs(substitute,simultaneous=True)

    def d0(vector):
        out={}
        for (I,j),f in vector.items():
            for pos,a in enumerate(I):
                J=I[:pos]+I[pos+1:]
                k=(J,j)
                out[k]=out.get(k,0)+(-1)**pos*(y[a]-x[a])*f
        return vclean(out)

    def perturb(vector):
        out={}
        for (I,j),f in vector.items():
            for a in range(n):
                if a not in I:
                    J=tuple(sorted((*I,a)))
                    k=(J,j)
                    out[k]=out.get(k,0)+(-1)**sum(b<a for b in I)*divided[a]*f
            for k in range(mrank):
                if dm[k,j]!=0:
                    key=(I,k)
                    out[key]=out.get(key,0)+(-1)**len(I)*dm[k,j]*f
        return vclean(out)

    def d(vector):return vadd(d0(vector),perturb(vector))

    def base_h(vector):
        # Tensor product of one-variable Koszul contractions. This
        # raises exterior degree and therefore is nilpotent after n steps.
        out={}
        for (I,j),f in vector.items():
            bound=min(I) if I else n
            for a in range(bound):
                prev={y[k]:x[k] for k in range(a)}
                g=f.subs(prev,simultaneous=True)
                value=sp.cancel((g-g.subs(y[a],x[a]))/(y[a]-x[a]))
                if value:
                    J=tuple(sorted((a,*I)))
                    key=(J,j)
                    out[key]=out.get(key,0)+value
        return vclean(out)

    def pi(vector):
        out={}
        for (I,j),f in vector.items():
            if not I:out[j]=out.get(j,0)+f.subs(substitute,simultaneous=True)
        return {j:sp.cancel(z) for j,z in out.items() if sp.cancel(z)!=0}

    def inclusion_0(vector):return {((),j):f for j,f in vector.items()}

    def target_d(vector):
        out={}
        for k in range(mrank):
            z=sp.cancel(sum(target[k,j]*f for j,f in vector.items()))
            if z!=0:out[k]=z
        return out

    def incl(vector):
        out={};term=inclusion_0(vector)
        for _ in range(n+1):
            out=vadd(out,term)
            term=vneg(base_h(perturb(term)))
        return out

    def homotopy(vector):
        out={};term=base_h(vector)
        for _ in range(n+1):
            out=vadd(out,term)
            term=vneg(base_h(perturb(term)))
        return out

    vectors=[{(I,j):f} for I in subsets for j in range(mrank)
             for f in [sp.Integer(1),y[0],y[-1],y[0]**2+y[-1]**2,sp.prod(y)]]
    ntests=0
    for vec in vectors:
        assert not vadd(d0(base_h(vec)),base_h(d0(vec)),vneg(vec),inclusion_0(pi(vec)))
        assert not vadd(d(homotopy(vec)),homotopy(d(vec)),vneg(vec),incl(pi(vec)))
        assert pi(d(vec))==target_d(pi(vec))
        assert pi(incl(pi(vec)))==pi(vec)
        assert not vadd(d(d(vec)),vneg({key:wx*f for key,f in vec.items()}))
        linear=y[0]+2*y[-1]
        assert pi({key:linear*f for key,f in vec.items()}) == {j:sp.cancel((x[0]+2*x[-1])*g) for j,g in pi(vec).items()}
        ntests+=6
    for j in range(mrank):
        vec={j:sp.Integer(1)}
        assert not vadd(d(incl(vec)),vneg(incl(target_d(vec))))
        ntests+=1
    return {
        'variables':n,
        'potential':str(W),
        'mf_rank':mrank,
        'diagonal_rank':2**n,
        'test_vectors':len(vectors),
        'checked_identities':ntests,
        'tests':['Koszul contraction','curved HPL contraction',
                 'strict projection naturality','projection-inclusion',
                 'curvature square','curved inclusion on generators'],
        'not_tested':['general n proof','all objects of MF','kernel full faithfulness',
                      'the KF condition','noncommutative rotation algebra']
    }


def dual_number_kflat_test():
    # Multiplication by epsilon on k[epsilon]/epsilon^2 in basis 1,epsilon.
    d=sp.Matrix([[0,0],[1,0]])
    assert d*d==sp.zeros(2)
    assert d.rank()==1  # ker(d)=im(d): acyclic bi-infinite complex
    # Mod epsilon the differential vanishes, leaving nonzero cohomology.
    return {'ring':'Q[epsilon]/(epsilon^2)',
            'bi_infinite_free_complex_acyclic':True,
            'reduction_has_nonzero_cohomology':True,
            'implication':'termwise free does not imply K-flat'}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=None)
    args=parser.parse_args()
    report={'scope':'Examples only; exact polynomial identities at t=1.',
            'cases':[verify(1),verify(2)],
            'kflat_warning':dual_number_kflat_test(),
            'theorem_dependence':'General finite exterior filtration argument in diagonal_kernel_identity.tex',
            'kf_proved':False}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,sort_keys=True,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'pass':True,'tests':[c['checked_identities'] for c in report['cases']]},ensure_ascii=False))

if __name__=='__main__':main()
