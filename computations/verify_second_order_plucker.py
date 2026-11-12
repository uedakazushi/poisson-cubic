#!/usr/bin/env python3
"""Exact scheme-theoretic Plucker/Jacobi quadratic-span checks in five variables.
Checks Fermat and a smooth mixed cubic. Mathematical theorem for every smooth
F is proved in the TeX source, not by these two specializations.
"""
import itertools
import sympy as sp

N = 5
x = sp.symbols("x0:5")
triples = list(itertools.combinations(range(N), 3))
a = sp.symbols("a0:10")
a_by = dict(zip(triples, a))
monoms_a2 = list(itertools.combinations_with_replacement(range(10), 2))
monoms_x3 = list(itertools.combinations_with_replacement(range(N), 3))

def sign(seq):
    return (-1)**sum(seq[i] > seq[j] for i in range(len(seq))
                     for j in range(i + 1, len(seq)))

def xi(indices):
    if len(set(indices)) != 3:
        return sp.Integer(0)
    return sign(indices) * a_by[tuple(sorted(indices))]

def quad_vector(poly):
    p = sp.Poly(sp.expand(poly), *a)
    return [p.coeff_monomial(a[i] * a[j]) for i, j in monoms_a2]

omega = {}
for i, j in itertools.combinations(range(N), 2):
    rem = tuple(k for k in range(N) if k not in (i, j))
    omega[(i,j)] = sign((i, j) + rem) * a_by[rem]

def skew(i, j):
    if i == j:
        return sp.Integer(0)
    return omega[(i, j)] if i < j else -omega[(j, i)]

plucker = []
for omitted in range(N):
    i, j, k, l = [v for v in range(N) if v != omitted]
    plucker.append(sp.expand(skew(i, j) * skew(k, l)
                             - skew(i, k) * skew(j, l)
                             + skew(i, l) * skew(j, k)))
P = sp.Matrix([quad_vector(q) for q in plucker])
assert P.rank() == 5

def verify(F, label):
    grad = [sp.diff(F, z) for z in x]
    pi = {(i,j): sp.expand(sum(xi((i,j,k)) * grad[k] for k in range(N)))
          for i,j in itertools.combinations(range(N), 2)}
    def pij(i,j):
        return pi[(i,j)] if i<j else -pi[(j,i)] if i>j else sp.Integer(0)
    Jac = {}
    for i,j,k in triples:
        Jac[(i,j,k)] = sp.expand(sum(
            pij(i,l)*sp.diff(pij(j,k),x[l]) +
            pij(j,l)*sp.diff(pij(k,i),x[l]) +
            pij(k,l)*sp.diff(pij(i,j),x[l]) for l in range(N)))
    coeff = []
    for expr in Jac.values():
        f = sp.Poly(expr, *x)
        coeff.extend(f.coeff_monomial(x[i]*x[j]*x[k])
                     for i,j,k in monoms_x3)
    coeff = [q for q in coeff if q != 0]
    J = sp.Matrix([quad_vector(q) for q in coeff])
    rank = J.rank()
    joint = J.col_join(P).rank()
    assert rank == joint == 5, (rank, joint)
    sub = {v: 0 for v in a}
    sub[a_by[(0,1,2)]] = sub[a_by[(0,3,4)]] = 1
    assert any(expr.subs(sub) != 0 for expr in Jac.values())
    print(label, "coefficient quadrics:", len(coeff),
          "Jacobi span:", rank, "joined with Plucker:", joint)

verify(sum(z**3 / 3 for z in x), "Fermat")
verify(sum(z**3 / 3 for z in x) + x[0]*x[1]*x[2]/7,
       "Smooth mixed")
print("PASS: exact equality of quadratic spans in both test cubics")
