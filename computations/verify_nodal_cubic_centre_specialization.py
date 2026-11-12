#!/usr/bin/env python3
"""Exact rational test of a nontrivial singular ternary cubic quantization.

Total cubic f=x^3+y^3+xyz+u*z^2+u^3 is smooth in P^3, but the
ternary restriction g=f(x,y,z,0) has a node at [0:0:1].
At h=2/5, check (over Q, NOT floating point) the degree-three
centre has dimension two and contains the explicit specialization
  Omega = u^3+x^3+y^3 + 228/253*sym(xyz)
          +722/759*u*z^2 -216/253*u*sym(xy).
The degree-four free-word space has 121 elements, the quadratic
relations have 102 degree-four multiples and relation rank 86.
The cubic Weyl-space has dimension20, commutator map rank18.

This is a finite exact special-parameter check and is NOT the proof
of the full all-f, all-h centre existence theorem (paper A).
Requires SymPy. Run:
python3 computations/verify_nodal_cubic_centre_specialization.py
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import permutations,product
import sympy as sp

x,y,z,u=sp.symbols("x y z u")
f=x**3+y**3+x*y*z+u*z**2+u**3
assert sp.groebner([sp.diff(f,v) for v in (x,y,z,u)],x,y,z,u,
                   order="grevlex").is_zero_dimensional
h=Q(2,5)


def word(s="",power=0): return {(power,tuple(s)):Q(1)}
def add(*parts):
    out=defaultdict(Q)
    for p in parts:
        for k,v in p.items(): out[k]+=v
    return {k:v for k,v in out.items() if v}
def mul(p,q):
    out=defaultdict(Q)
    for (a,v),c in p.items():
        for (b,w),d in q.items():out[(a+b,v+w)]+=c*d
    return {k:v for k,v in out.items() if v}
def scale(p,a):
    return {k:v*a for k,v in p.items() if v*a}
def sym2(p,q): return scale(add(mul(p,q),mul(q,p)),Q(1,2))
def cube(p): return mul(mul(p,p),p)

X,Y,Z,U=(word(v) for v in "xyz")+ (word("",1),)
relations=[
  add(mul(X,Y),scale(mul(Y,X),-1),
      scale(add(sym2(X,Y),scale(mul(U,Z),2)),-h)),
  add(mul(Y,Z),scale(mul(Z,Y),-1),
      scale(add(scale(mul(X,X),3),sym2(Y,Z)),-h)),
  add(mul(Z,X),scale(mul(X,Z),-1),
      scale(add(scale(mul(Y,Y),3),sym2(X,Z)),-h)),
]


def degree4_basis():
    return [(i,tuple(v)) for i in range(5)
            for v in product("xyz", repeat=4-i)]


def rel_multiples():
    for rel in relations:
        for cent in range(3):
            for left_n in range(3-cent):
                for left in product("xyz",repeat=left_n):
                    for right in product("xyz",repeat=2-cent-left_n):
                        yield mul(mul(word("".join(left),cent),rel),
                                  word("".join(right)))


B=degree4_basis();pos={w:i for i,w in enumerate(B)}
assert len(B)==121
pivots={}


def reduce_coeff(poly, insert=False):
    row={pos[key]:sp.Rational(v.numerator,v.denominator)
         for key,v in poly.items() if v}
    for k in sorted(pivots):
        if k not in row: continue
        coefficient=row[k]
        for j,a in pivots[k].items():
            val=row.get(j,0)-coefficient*a
            if val:row[j]=val
            else:row.pop(j,None)
    if insert:
        if row:
            k=min(row);c=row[k]
            pivots[k]={j:v/c for j,v in row.items()}
        return {}
    return row


R=list(rel_multiples())
assert len(R)==102
for v in R:reduce_coeff(v,insert=True)
assert len(pivots)==86


def sym_monomial(m):
    exp=sp.Poly(m,x,y,z,u).monoms()[0]
    active=("x",)*exp[0]+("y",)*exp[1]+("z",)*exp[2]
    permutations_set=set(permutations(active))
    return {(exp[3],v):Q(1,len(permutations_set)) for v in permutations_set}


def degree3_monomials():
    return [x**i*y**j*z**k*u**l
            for i,j,k,l in product(range(4),repeat=4)
            if i+j+k+l==3]

basis3=degree3_monomials()
assert len(basis3)==20
basis_rem=[]
for mono in basis3:
    col=[]
    for i,g in enumerate((X,Y,Z)):
        comm=add(mul(sym_monomial(mono),g),
                 scale(mul(g,sym_monomial(mono)),-1))
        col.append(reduce_coeff(comm))
    basis_rem.append({i+len(B)*a:c
                     for a,part in enumerate(col)
                     for i,c in part.items()})
row_indices=sorted({i for col in basis_rem for i in col})
D=sp.Matrix([[col.get(i,0) for col in basis_rem] for i in row_indices])
assert D.rank()==18
assert len(D.nullspace())==2

omega=(u**3+x**3+y**3+sp.Rational(228,253)*x*y*z
       +sp.Rational(722,759)*u*z*z
       -sp.Rational(216,253)*u*x*y)
coords=sp.Matrix([sp.Poly(omega,x,y,z,u).coeff_monomial(m)
                  for m in basis3])
assert D*coords==sp.zeros(D.rows,1)
print("PASS smooth total cubic with nodal ternary restriction")
print("PASS degree-four free basis 121, quadratic relation multiples 102, rank86")
print("PASS degree-three Weyl commutator matrix rank18, kernel dimension2")
print("PASS explicit specialized Cramer-type central cubic at h=2/5")
