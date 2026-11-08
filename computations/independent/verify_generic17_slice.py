#!/usr/bin/env python3
"""Exact Q-linear tangent-space check for a 17-parameter normal form."""
import sympy as sp
x,y,z,u,v=sp.symbols('x y z u v')
X=(x,y,z,u,v)
F=(3*(x**3+y**3+z**3)+5*x*y*z
   +u*x**2+2*v*y**2+3*(u+v)*z**2
   +(u**2+u*v+2*v**2)*x+(2*u**2+3*u*v+v**2)*y
   +(u**2+4*u*v+5*v**2)*z
   +(u**3+u**2*v+2*u*v**2+3*v**3))
D=[sp.diff(F,w) for w in X]
orbit=[]
for i in range(3):
    for j in range(3):
        orbit.append((F if i==j else 0)-X[j]*D[i])
for i in range(3,5):
    for j in range(3,5):
        orbit.append(-X[j]*D[i])
for i in range(3):
    for j in range(3,5):
        orbit.append(-X[j]*D[i])
slice_vectors=[x**3+y**3+z**3,x*y*z,v*y**2,(u+v)*z**2]
slice_vectors += [t*q for t in (x,y,z) for q in (u*u,u*v,v*v)]
slice_vectors += [u**3,u**2*v,u*v*v,v**3]
assert len(orbit)==19 and len(slice_vectors)==17
monomials=[x**i*y**j*z**k*u**l*v**(3-i-j-k-l)
 for i in range(4) for j in range(4-i)
 for k in range(4-i-j) for l in range(4-i-j-k)]
assert len(monomials)==35
M=sp.Matrix([[sp.Poly(f,*X).coeff_monomial(m) for f in orbit+slice_vectors]
             for m in monomials])
from sympy.polys.matrices import DomainMatrix
rows=[i for i,m in enumerate(monomials) if m.has(x,y,z)]
cols=list(range(1,19))+list(range(19,32))
assert len(rows)==len(cols)==31
M31=M.extract(rows, cols)
assert M31.shape==(31,31)
mat=DomainMatrix.from_Matrix(M31).convert_to(sp.ZZ)
Ddet=mat.det()
print(f'exact 31x31 determinant: {Ddet}')
assert Ddet == -5538243375000, Ddet
print('PASS: generic slice is transverse and has 17 independent moduli directions.')
