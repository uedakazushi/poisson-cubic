"""Exact sanity checks for article A (not a proof of the general theorems).
Run: python3 computations/verify_poisson_article_A.py
Requires: sympy
"""
from itertools import combinations
import sympy as sp

x, y, z, a, b, c, u, v = sp.symbols("x y z a b c u v")
vars_ = (x, y, z, a, b, c, u, v)
F = ((x**3 + y**3 + z**3 + a**3 + b**3 + c**3 + u**3 + v**3)/3
     + u*x*y + v*a*b)
# Every homogeneous summand has an isolated critical point;
# hence the projective cubic V(F) is smooth.
for Q, w in ((F.subs({a: 0, b: 0, c: 0, v: 0}), (x, y, z, u)),
             (F.subs({x: 0, y: 0, z: 0, u: 0}), (a, b, c, v))):
    assert sp.groebner([sp.diff(Q, t) for t in w], *w).is_zero_dimensional

bivec = {}
for i, j, k in ((0, 1, 2), (3, 4, 5)):
    bivec[i,j] = sp.diff(F, vars_[k])
    bivec[j,k] = sp.diff(F, vars_[i])
    bivec[i,k] = -sp.diff(F, vars_[j])

def pi(i, j):
    if i == j:
        return sp.Integer(0)
    return bivec.get((i,j), sp.Integer(0)) if i < j else -bivec.get((j,i), sp.Integer(0))

for i, j, k in combinations(range(8), 3):
    jacobi = sum(pi(i,l)*sp.diff(pi(j,k),vars_[l])
                 + pi(j,l)*sp.diff(pi(k,i),vars_[l])
                 + pi(k,l)*sp.diff(pi(i,j),vars_[l])
                 for l in range(8))
    assert sp.expand(jacobi) == 0, ("Jacobi", (i,j,k))

g1 = (x**3 + y**3 + z**3)/3
g2 = (a**3 + b**3 + c**3)/3
ideal = sp.groebner([g1, g2, u, v], *vars_, order="lex")
# The join of the two plane cubics is in X, and E wedge pi^2 vanishes on it.
assert ideal.reduce(sp.expand(F))[1] == 0
for I in combinations(range(8), 5):
    coefficient = sp.Integer(0)
    for q in range(5):
        J = I[:q] + I[q+1:]
        fourform = sp.Integer(0)
        for r, s in combinations(range(4), 2):
            ij = (J[r], J[s])
            kl = tuple(J[t] for t in range(4) if t not in (r,s))
            word = [*ij, *kl]
            sign = (-1)**sum(word[t]>word[t2] for t in range(4) for t2 in range(t+1,4))
            fourform += sign*pi(*ij)*pi(*kl)
        coefficient += (-1)**q*vars_[I[q]]*fourform
    assert ideal.reduce(sp.expand(coefficient))[1] == 0, ("Join rank", I)
print("PASS: smooth test cubic, 56 Jacobi and 56 Euler-wedge identities")
