#!/usr/bin/env python3
"""Finite-field regression check for Fermat nc cubic centrality and Hilbert dimensions."""
from itertools import product, permutations
from collections import defaultdict
P=1009
X,Y,Z=0,1,2
def words(n): return list(product(range(3),repeat=n))
def rank_mod(columns,nrows):
    basis={}
    for vec in columns:
        v={k:(a%P) for k,a in vec.items() if a%P}
        while v:
            pivot=min(v)
            if pivot in basis:
                b=basis[pivot]; factor=v[pivot]
                for k,coeff in b.items():
                    new=(v.get(k,0)-factor*coeff)%P
                    if new: v[k]=new
                    elif k in v: del v[k]
            else:
                scale=pow(v[pivot],-1,P)
                basis[pivot]={k:(coeff*scale)%P for k,coeff in v.items()}
                break
    return len(basis),basis
def in_span(v,basis):
    v={k:(a%P) for k,a in v.items() if a%P}
    while v:
        pivot=min(v)
        if pivot not in basis: return False
        fac=v[pivot]
        for k,c in basis[pivot].items():
            new=(v.get(k,0)-fac*c)%P
            if new: v[k]=new
            elif k in v: del v[k]
    return True
def relation(h):
    return [{(X,Y):1,(Y,X):-1,(Z,Z):-h},
            {(Y,Z):1,(Z,Y):-1,(X,X):-h},
            {(Z,X):1,(X,Z):-1,(Y,Y):-h}]
def ideal_columns(n,h):
    basis={w:i for i,w in enumerate(words(n))}
    cols=[]
    for r in relation(h):
        for prelen in range(n-1):
            postlen=n-2-prelen
            for pre in words(prelen):
                for post in words(postlen):
                    cols.append({basis[pre+w+post]:c for w,c in r.items()})
    return cols,basis
def central_commutator(i,h):
    inv3=pow(3,-1,P);g=defaultdict(int)
    for j in range(3):g[(j,j,j)]+=1
    for w in permutations(range(3)):g[w]-=h*h*inv3
    result=defaultdict(int)
    for w,c in g.items():
        result[w+(i,)]+=c
        result[(i,)+w]-=c
    return result
def test(h):
    dims=[]
    for d in range(2,5):
        cols,idx=ideal_columns(d,h)
        r,b=rank_mod(cols,3**d);dims.append(3**d-r)
        if d==4:
            for i in range(3):
                v={idx[w]:c for w,c in central_commutator(i,h).items()}
                assert in_span(v,b),(h,i,'G not central')
    assert dims==[6,10,15],(h,dims)
    print(f'h={h}, char={P}: PASS, dimensions B_2..B_4={dims}')
for h in [0,1,2,5,15]:test(h)
