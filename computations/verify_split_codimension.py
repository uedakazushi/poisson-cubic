#!/usr/bin/env python3
"""Exact Q-linear witness for the 20-dim split locus and 18-dim parabolic orbit.
No generic categorical reconstruction is proved by this computation.
"""
import sympy as sp
x,y,z,u,v=sp.symbols('x y z u v')
X=(x,y,z,u,v)
F=x**3+y**3+z**3+3*x*y*z+u**3+2*u**2*v+3*u*v**2+5*v**3
MON=(x**a*y**b*z**c*u**d*v**(3-a-b-c-d)
    for a in range(4) for b in range(4-a)
    for c in range(4-a-b) for d in range(4-a-b-c))
mon=list(MON)
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
print('PASS (exact Q): coefficients=35, split tangent=20, parabolic orbit=18, total split span=20')
print('PASS: codim in 35-dim coefficient space=15; rational quotient dimensions split=2 vs total=17')

# Jacobian-ring tangent of smooth cubic F=f(x)+g(u).
# f has Jacobian Hilbert function (1,3,3,1); g has (1,2,1).
J=[q*sp.diff(F,w) for w in X for q in X]
Jmat=sp.Matrix.hstack(*(vec(q) for q in J))
assert Jmat.rank()==25
mixed_linear=[q*x**a*y**b*z**(2-a-b) for q in (u,v)
              for a in range(3) for b in range(3-a)]
mixed_quadratic=[q*t for q in (x,y,z) for t in (u**2,u*v,v**2)]
center=[u**a*v**(3-a) for a in range(4)]

def jacobian_image_dimension(vectors):
    return sp.Matrix.hstack(Jmat,*(vec(q) for q in vectors)).rank()-25

assert (jacobian_image_dimension(split[:10]),
        jacobian_image_dimension(mixed_linear),
        jacobian_image_dimension(mixed_quadratic),
        jacobian_image_dimension(center))==(1,6,3,0)
print('PASS (exact Q): cubic Jacobian tangent = 1 + 6 + 3 = 10; forgetful kernel = 7')
print('PASS: split quotient maps to 1-dim image; its 15-dim normal maps to 9-dim image with 6-dim kernel')

# Explicit geometric generators of the 7-dimensional vertical kernel.
f=x**3+y**3+z**3+3*x*y*z
g=u**3+2*u**2*v+3*u*v**2+5*v**3
vertical=[f]+[w*sp.diff(g,q) for q in (u,v) for w in (x,y,z)]
assert len(vertical)==7
Jmat2=sp.Matrix.hstack(*(vec(q) for q in J))
Omat=sp.Matrix.hstack(*(vec(q) for q in orbit))
Vmat=sp.Matrix.hstack(*(vec(q) for q in vertical))
assert Omat.rank()==18
assert sp.Matrix.hstack(Omat,Vmat).rank()==25
assert sp.Matrix.hstack(Omat,Vmat,Jmat2).rank()==25
print('PASS (exact Q): vertical directions = 1 Poisson scale + 6 moving-plane directions')
print('PASS: parabolic tangent (18) + vertical tangent (7) = Jacobian ideal tangent (25)')
