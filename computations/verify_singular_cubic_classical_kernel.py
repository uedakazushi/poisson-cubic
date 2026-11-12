#!/usr/bin/env python3
"""Exact rank check at a smooth cubic with *zero* ternary restriction.

F = u*x^2 + v*y^2 + w*z^2 + u^3+v^3+w^3 in six variables.
The projective cubic is smooth: grad F=0 implies, for each pair
(x,u), (y,v), (z,w), u*x=0 and x^2+3*u^2=0, hence x=u=0 etc.
Yet F(x,y,z,0,0,0)=0 identically.

The classical Jacobian Casimir operator on homogeneous degree-3
polynomials S_3 -> (S_4)^3 must have kernel span{F} + C[u,v,w]_3.
Its rank is 56 - (1+10)=45, which is independently checked over Q.

Dependency: sympy. Command:
python3 computations/verify_singular_cubic_classical_kernel.py
This tests a highly singular ternary restriction; the all-F theorem is
proved algebraically in paper A, not by the finite example here.
"""
import itertools
import sympy as sp

x, y, z, u, v, w = sp.symbols("x y z u v w")
V = (x, y, z, u, v, w)
f = u*x**2 + v*y**2 + w*z**2 + u**3 + v**3 + w**3
assert sp.expand(f.subs({u:0,v:0,w:0})) == 0


def monomials(degree):
    return [sp.prod(t**a for t, a in zip(V, exps))
            for exps in itertools.product(range(degree+1), repeat=len(V))
            if sum(exps)==degree]


basis3, basis4 = monomials(3), monomials(4)
assert (len(basis3),len(basis4)) == (56,126)
pos4 = {sp.Poly(m,*V).monoms()[0]: j for j,m in enumerate(basis4)}


def jacobian(a,b):
    ax=[sp.diff(a,t) for t in (x,y,z)]
    bx=[sp.diff(b,t) for t in (x,y,z)]
    fx=[sp.diff(f,t) for t in (x,y,z)]
    return sp.expand(sum(fx[i]*(ax[(i+1)%3]*bx[(i+2)%3] -
                                ax[(i+2)%3]*bx[(i+1)%3])
                         for i in range(3)))


D=sp.zeros(3*len(basis4),len(basis3))
for j,p in enumerate(basis3):
    for k,t in enumerate((x,y,z)):
        for exponent,value in sp.Poly(jacobian(p,t),*V).terms():
            if value:
                D[k*len(basis4)+pos4[exponent],j] = value

assert D.rank()==45
central = [m for m in basis3 if not (m.has(x) or m.has(y) or m.has(z))]
assert len(central)==10
for item in [f,*central]:
    v3=sp.Matrix([sp.Poly(item,*V).coeff_monomial(m) for m in basis3])
    assert D*v3==sp.zeros(D.rows,1)

print("PASS: projectively smooth F with zero ternary restriction")
print("PASS: degree-three classical Casimir matrix 378x56 has rank 45")
print("PASS: kernel is exactly C*F + C[u,v,w]_3 (dimension 11)")
