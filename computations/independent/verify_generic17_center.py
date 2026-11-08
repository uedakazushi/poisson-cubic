#!/usr/bin/env python3
"""Exact rational calculation of Z(S)_d for d=1,2,3 at a witness."""
from itertools import product
import sympy as sp
A=(0,1,2)
rels=[{(0,1):1,(1,0):-1,(2,2):-1},
      {(1,2):1,(2,1):-1,(0,0):-1},
      {(2,0):1,(0,2):-1,(1,1):-1}]
def quotient(n):
    words=list(product(A,repeat=n)); pos={w:i for i,w in enumerate(words)}
    rows=[]
    for start in range(n-1):
        for pre in product(A,repeat=start):
            for post in product(A,repeat=n-2-start):
                for rel in rels:
                    row=[0]*len(words)
                    for pair,coef in rel.items(): row[pos[pre+pair+post]]+=coef
                    rows.append(row)
    if rows:
        RR,piv=sp.Matrix(rows).rref()
        r=len(piv)
        RR=RR[:r,:]
    else: RR,piv=sp.zeros(0,len(words)),()
    free=[j for j in range(len(words)) if j not in piv]
    def reduce(vec):
        v=sp.Matrix([vec.get(w,0) for w in words])
        for i,p in enumerate(piv):
            if v[p]: v-=v[p]*RR.row(i).T
        return v[free,:]
    return words,free,reduce,len(piv)
Qs={i:quotient(i) for i in range(1,5)}
for n in (1,2,3):
    W,free,_,_=Qs[n]
    Wp,freep,redp,_=Qs[n+1]
    cols=[]
    for j in free:
        w=W[j]; chunks=[]
        for a in A:
            comm={w+(a,):1}
            comm[(a,)+w]=comm.get((a,)+w,0)-1
            chunks.extend(list(redp(comm)))
        cols.append(chunks)
    mat=sp.Matrix.hstack(*(sp.Matrix(c) for c in cols))
    kernel=len(free)-mat.rank()
    print(f'n={n}: dim(S_n)={len(free)}, dim(S_{{n+1}})={len(freep)}, commutator rank={mat.rank()}, dim Z(S)_n={kernel}')
    assert kernel==(1 if n==3 else 0)
print('PASS: exact low-degree center witness')
