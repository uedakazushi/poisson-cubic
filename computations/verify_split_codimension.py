#!/usr/bin/env python3
"""Exact Q-linear witness for the 20-dimensional split locus and 18-dimensional parabolic orbit.
This does not prove a generic categorical reconstruction.
"""
import sympy as sp
x,y,z,u,v=sp.symbols('x y z u v')
X=(x,y,z,u,v)
F=x**3+y**3+z**3+3*x*y*z+u**3+2*u**2*v+3*u*v**2+5*v**3
mon=[x**a*y**b*z**c*u**d*v**(3-a-b-c-d)
     for a in range(4) for b in range(4-a)
     for c in range(4-a-b) for d in range(4-a-b-c)]
assert len(mon)==35
def vec(f):
    p=sp.Poly(f,*X)
    return sp.Matrix([p.coeff_monomial(m) for m in mon])
split=[x**a*y**b*z**(3-a-b) for a in range(4) for b in range(4-a)]
split += [u**a*v**(3-a) for a in range(4)]
shears=[a*sp.diff(F,b) for a in (u,v) for b in (x,y,z)]
dF=[sp.diff(F,w) for w in X]
orbit=[(F if i==j else 0)-X[j]*dF[i]
       for i in range(3) for j in range(3)]
orbit += [-X[j]*dF[i] for i in range(3,5) for j in range(3,5)]
orbit += [-X[j]*dF[i] for i in range(3) for j in range(3,5)]
assert len(split)==14 and len(shears)==6 and len(orbit)==19
r_tangent=sp.Matrix.hstack(*(vec(q) for q in split+shears)).rank()
r_orbit=sp.Matrix.hstack(*(vec(q) for q in orbit)).rank()
r_span=sp.Matrix.hstack(*(vec(q) for q in orbit+split)).rank()
assert (r_tangent,r_orbit,r_span)==(20,18,20)
print('PASS (exact Q): coefficients=35; split tangent=20; parabolic orbit=18; total span=20')
print('PASS: codim=15 in the coefficient space and quotient; quotient dimensions split=2, total=17')
