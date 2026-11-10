#!/usr/bin/env python3
"""Exact character-space check for the mixed cubic equivariant normal form.

Finite polynomial calculations only.  This script does NOT certify equivariant
Kontsevich formality, the all-order coordinate changes, or generic MF equivalence.
Run from repository root: python3 computations/verify_mixed_characters.py
"""
from itertools import combinations_with_replacement
import sympy as sp

x, y, z, u, v, lam = sp.symbols("x y z u v lambda")
variables = (x, y, z, u, v)
weights = {
    x: (1, 0, 0, 0),
    y: (0, 1, 0, 0),
    z: (0, 0, 1, 0),
    u: (2, 2, 0, 0),
    v: (0, 0, 0, 1),
}
characters = {"1": (0, 0, 0, 0), "chi": (1, 1, 1, 0),
              "chi^2": (2, 2, 2, 0)}
expected = {
    "1": {x**3, y**3, z**3, u**3, v**3, u*x*y},
    "chi": {x*y*z, u**2*z},
    "chi^2": {u*z**2},
}
expected_ranks = {"1": 5, "chi": 1, "chi^2": 1}
F = (x**3+y**3+z**3)/3 + u**3+v**3 + lam*u*x*y
gradients = [sp.diff(F, a) for a in variables]
monomials = [sp.prod(w) for w in combinations_with_replacement(variables, 3)]
assert len(monomials) == 35

def char_of_monomial(m):
    powers = sp.Poly(m, *variables).monoms()[0]
    return tuple(
        sum(weights[t][j] * powers[i] for i, t in enumerate(variables)) % 3
        for j in range(4)
    )

for name, character in characters.items():
    basis = [m for m in monomials if char_of_monomial(m) == character]
    assert set(basis) == expected[name], (name, basis)
    columns = []
    for deriv in gradients:
        for linear in variables:
            p = sp.Poly(sp.expand(linear * deriv), *variables)
            vector = sp.Matrix([p.coeff_monomial(m) for m in basis])
            if any(vector):
                assert all(
                    p.coeff_monomial(m) == 0
                    for m in monomials if m not in basis
                )
                columns.append(vector)
    mat = sp.Matrix.hstack(*columns)
    rank = mat.rank()
    assert rank == expected_ranks[name], (name, rank)
    assert len(basis) - rank == (0 if name == "chi^2" else 1)
    print(f"PASS {name}: monomials={len(basis)}, Jacobian rank={rank}, quotient={len(basis)-rank}")

# Check the three explicit spanning relations, valid for every lambda.
assert sp.expand(x*gradients[0] - x**3 - lam*u*x*y) == 0
assert sp.expand(y*gradients[1] - y**3 - lam*u*x*y) == 0
assert sp.expand(u*gradients[3] - 3*u**3 - lam*u*x*y) == 0
assert sp.expand(z*gradients[3] - 3*u**2*z - lam*x*y*z) == 0
assert sp.expand(u*gradients[2] - u*z**2) == 0

G2 = x*y*z/sp.Integer(3) - lam**2*u**2*z/sp.Integer(12)
c0 = sp.Rational(1, 3) + lam**3/sp.Integer(36)
assert sp.expand(G2-c0*x*y*z+lam**2*z*gradients[3]/36) == 0
print("PASS: mixed second jet normalizes to c0=1/3+lambda^3/36")
# Additional involution tau: x <-> y, h -> -h (u,z,v,lambda fixed).
# These are identities in the FREE noncommutative algebra.
X, Y, Z = sp.symbols("X Y Z", commutative=False)
hh, aa = sp.symbols("h a")
r1 = X*Y - Y*X - hh*Z**2
r2 = X*Z - Z*X + hh*(Y**2 + aa*X)
r3 = Y*Z - Z*Y - hh*(X**2 + aa*Y)
from itertools import permutations
T = sum(sp.Mul(*p) for p in permutations((X, Y, Z)))
omega = ((X**3+Y**3+Z**3)/3 - hh**2*T/9
         + aa*(X*Y+Y*X)/2 + hh**2*aa**2*Z/6
         + hh**4*aa*Z**2/18)
def tau(p):
    return sp.expand(p.xreplace({X:Y, Y:X, hh:-hh}))
assert sp.expand(tau(r1)+r1) == 0
assert sp.expand(tau(r2)-r3) == 0
assert sp.expand(tau(r3)-r2) == 0
assert sp.expand(tau(omega)-omega) == 0
assert sp.expand(x*gradients[0]-y*gradients[1]-(x**3-y**3)) == 0
for m in (u*x*y,x*y*z,u**2*z,u*z**2):
    assert sp.expand(m.xreplace({x:y,y:x})-m) == 0
print("PASS: free-algebra tau involution, center and antisymmetric Jacobian relation")
print("Scope: finite character/free-algebra identities only; all-order formality remains a mathematical input")
