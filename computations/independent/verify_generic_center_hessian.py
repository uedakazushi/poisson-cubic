"""Exact Q-rank sanity check for the Jacobi--Hessian centre lemma."""
import sympy as sp
x,y,z=sp.symbols('x y z')
f3=3*(x**3+y**3+z**3)+5*x*y*z
H=sp.hessian(f3,(x,y,z))
C=sp.Matrix([[sp.diff(H[i,j],v) for j in range(3)] for i in range(3) for v in (x,y,z)])
assert C.rank()==3
print('Hessian contraction Q-rank:',C.rank())
