#!/usr/bin/env python3
"""Exact Fermat-point maximal minors for a generic cubic Casimir determinantal formula.

Computes the classical Jacobian Poisson map on homogeneous cubics for
0 and 2 central variables. This proves a nonzero minor at the Fermat point;
it does NOT alone establish generic quantum centrality. Requires sympy.
"""
import sympy as sp


def monomials(variables, degree):
    if len(variables) == 1:
        return [variables[0]**degree]
    return [variables[0]**k * rest for k in range(degree, -1, -1)
            for rest in monomials(variables[1:], degree-k)]


def calculate(n_centers, expected_determinant):
    active = sp.symbols("x y z")
    centers = sp.symbols(f"u0:{n_centers}") if n_centers else ()
    variables = active + centers
    mon3 = monomials(variables, 3)
    mon4 = monomials(variables, 4)
    w = [p for p in mon3 if p != active[0]**3 and p.has(*active)]
    # x**3 is normalized to coefficient 1; pure center cubics are omitted.
    f = sum(v**3 for v in active) / 3
    target_exp = [sp.Poly(q, variables).monoms()[0] for q in mon4]
    matrix = sp.zeros(3*len(mon4), len(w))
    for j, p in enumerate(w):
        for i in range(3):
            bracket = sp.expand(sum(
                sp.LeviCivita(i, a, b)
                * sp.diff(f, active[a]) * sp.diff(p, active[b])
                for a in range(3) for b in range(3)))
            values = sp.Poly(bracket, variables).as_dict()
            for k, exp in enumerate(target_exp):
                matrix[i*len(mon4)+k, j] = values.get(exp, 0)
    independent_rows = list(matrix.T.rref()[1])
    minor = matrix[independent_rows, :]
    determinant = minor.det()
    assert len(independent_rows) == len(w)
    assert determinant == expected_determinant
    print(f"PASS: m={n_centers}, N3={len(mon3)}, center monomials="
          f"{len(mon3)-len(w)-1}, rank={len(w)}, det={determinant}")
    print("  selected rows (0-based):", independent_rows)


if __name__ == "__main__":
    calculate(0, -72)
    calculate(2, 4608)
