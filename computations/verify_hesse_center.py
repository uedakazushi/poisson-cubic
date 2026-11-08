#!/usr/bin/env python3
"""Finite-field checks of the Hesse cubic central-element formula.

Checks degree-four membership in the quadratic ideal at explicit finite-field
specializations. Not a universal algebraic proof; the latter uses the
Sklyanin central-element theorem and flatness (see manuscript).
Python standard library only.
"""
from itertools import product
import json

P=1009
LETTERS="xyz"
WORDS=["".join(w) for w in product(LETTERS,repeat=4)]
INDEX={w:i for i,w in enumerate(WORDS)}

def inv(a):
    return pow(a%P,-1,P)

def add(row,w,coef):
    row[INDEX[w]]=(row[INDEX[w]]+coef)%P

def product_words(a,b):
    d={}
    for x,c in a.items():
        for y,e in b.items():
            d[x+y]=(d.get(x+y,0)+c*e)%P
    return d

def echelon(rows):
    piv={}
    for rr in rows:
        r=rr.copy()
        for k in sorted(piv):
            f=r[k]
            if f:
                r=[(x-f*y)%P for x,y in zip(r,piv[k])]
        if not any(r):
            continue
        j=next(i for i,x in enumerate(r) if x)
        v=inv(r[j])
        piv[j]=[(v*x)%P for x in r]
    return piv

def in_span(vec,piv):
    r=vec[:]
    for k in sorted(piv):
        if r[k]:
            f=r[k]
            r=[(x-f*y)%P for x,y in zip(r,piv[k])]
    return not any(r)

def verify_one(h,t):
    h=h%P;t=t%P;q=h*t*inv(2)%P
    a=(1-q)%P;b=(-1-q)%P;c=(-h)%P
    relations=[{"yz":a,"zy":b,"xx":c},
               {"zx":a,"xz":b,"yy":c},
               {"xy":a,"yx":b,"zz":c}]
    rows=[]
    for rel in relations:
        for j in range(3):
            for prefix in product(LETTERS,repeat=j):
                for suffix in product(LETTERS,repeat=2-j):
                    r=[0]*81
                    for word,k in rel.items():
                        add(r,"".join(prefix)+word+"".join(suffix),k)
                    rows.append(r)
    basis=echelon(rows)
    u=(1+h*h*t*t*inv(2)+h**4*t*inv(6)-h**4*t**4*inv(48))%P
    v=((4-h*h*t*t)*(12*t+h*h*(t**3-8))*inv(96))%P
    f={w:u for w in ("xxx","yyy","zzz")}
    f.update({w:v for w in ("xyz","yzx","zxy","yxz","xzy","zyx")})
    for letter in LETTERS:
        A=product_words(f,{letter:1})
        B=product_words({letter:1},f)
        r=[0]*81
        for word,k in A.items():add(r,word,k)
        for word,k in B.items():add(r,word,-k)
        if not in_span(r,basis):
            raise AssertionError(f"Not central for (h,t,letter)={(h,t,letter)}")
    return len(basis)

examples=[(0,0),(0,1),(1,0),(1,1),(7,3),(11,20),(17,200),(23,857)]
results=[{"h":h,"t":t,"relation_rank":verify_one(h,t),
          "commutators_in_ideal":True} for h,t in examples]
print(json.dumps({"field":"F_1009","degree":4,
                  "verified_specializations":results,
                  "status":"passed",
                  "scope":"Finite checks only; not the universal proof."},
                 indent=2))
