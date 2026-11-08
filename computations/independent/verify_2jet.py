#!/usr/bin/env python3
"""Sample second-order Kontsevich associativity checks; not a universal proof."""
import sympy as s
x,y,z,u,v=s.symbols('x y z u v')
vs=[x,y,z]
F=x**3+y**3+z**3+u*x**2+v*y**2+u*v*z+u**3+v**3
P=s.Matrix([[0,s.diff(F,z),-s.diff(F,y)],[-s.diff(F,z),0,s.diff(F,x)],[s.diff(F,y),-s.diff(F,x),0]])
def c1(f,g):
    return s.expand(sum(P[i,j]*s.diff(f,vs[i])*s.diff(g,vs[j]) for i in range(3) for j in range(3))/2)
def c2(f,g):
    t1=sum(P[i,j]*P[k,l]*s.diff(f,vs[i],vs[k])*s.diff(g,vs[j],vs[l])
           for i in range(3) for j in range(3) for k in range(3) for l in range(3))/8
    t2=sum(P[i,j]*s.diff(P[k,l],vs[j])*(s.diff(f,vs[i],vs[k])*s.diff(g,vs[l])-s.diff(f,vs[k])*s.diff(g,vs[i],vs[l]))
           for i in range(3) for j in range(3) for k in range(3) for l in range(3))/12
    return s.expand(t1+t2)
triples=[(x,y,z),(x**2,y,z),(x*y,y*z,z*x)]
for a,b,c in triples:
    ass=s.expand(c2(a*b,c)+c1(c1(a,b),c)+c2(a,b)*c-c2(a,b*c)-c1(a,c1(b,c))-a*c2(b,c))
    assert ass==0,('associativity',a,b,c,ass)
    assert s.expand(c1(F,a)-c1(a,F))==0
    assert s.expand(c2(F,a)-c2(a,F))==0
    print('PASS: assoc2 and F central for',a,b,c)
