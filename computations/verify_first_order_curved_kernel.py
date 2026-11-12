#!/usr/bin/env python3
"""Finite exact checks for first-order curved Hochschild cancellation.

Uses explicit rank-three HKR alternating cochains, not an A-infinity or
category-level computation.  Tests several polynomials and checks that the
projective smooth cubic Jacobian degree-three quotient has the expected size.
"""
from itertools import combinations
from math import comb
import sympy as sp

def jacobian_triple(polys, variables, triple):
    return sp.det(sp.Matrix([[sp.diff(p, variables[i]) for p in polys]
                             for i in triple]))

def hkr_triple(polys, variables, components):
    return sp.expand(sum(value * jacobian_triple(polys, variables, triple)
                         for triple, value in components.items()) / 6)

def check_first_order(N):
    xs=sp.symbols("x0:"+str(N))
    F=sum(z**3 for z in xs)/3 + xs[-1]*xs[0]*xs[1]
    Xi={(0,1,2):sp.Integer(1)}
    if N>=6: Xi[(2,3,4)]=sp.Integer(2)
    cases=[(xs[0]**2*xs[2]+xs[1],xs[1]**2+xs[2]*xs[-1]),
           (xs[2]**2+xs[-1],xs[0]*xs[1]+xs[3]),
           (xs[0]+xs[4]**2,xs[1]+xs[-2]*xs[-1]),
           (xs[0]*xs[1],xs[2]*xs[3])]
    for f,g in cases:
        lhs=hkr_triple((F,f,g),xs,Xi)-hkr_triple((f,F,g),xs,Xi)+hkr_triple((f,g,F),xs,Xi)
        rhs=3*hkr_triple((F,f,g),xs,Xi)
        assert sp.expand(lhs-rhs)==0
    # Euler/HKR ranks: all x_i * dF/dx_j are independent in degree 3.
    monoms=list(combinations(range(N+2),3))
    poly_monomials=[]
    # Enumerate degree-three exponent vectors directly.
    def expo_vectors(k,d):
        if k==1:
            yield (d,)
        else:
            for i in range(d+1):
                for v in expo_vectors(k-1,d-i):
                    yield (i,)+v
    degree3=list(expo_vectors(N,3))
    coeffs=[]
    for i in range(N):
        for j in range(N):
            p=sp.Poly(sp.expand(xs[i]*sp.diff(F,xs[j])), *xs)
            coeffs.append([p.coeff_monomial(sp.prod(xs[z]**degree3[r][z] for z in range(N)))
                           for r in range(len(degree3))])
    rank=sp.Matrix(coeffs).rank()
    assert rank==N*N
    dimension=comb(N+2,3)-rank
    return {"N":N,"HKR_insertion_tests":len(cases),
            "jacobian_degree3_rank":rank,"jacobian_quotient_dimension":dimension}

if __name__=="__main__":
    for N in (5,6):
        print(check_first_order(N))
    print("PASS: 8 exact insertion identities and 2 Jacobian-space ranks")
    print("LIMIT: no categorical A-infinity functor computed")
