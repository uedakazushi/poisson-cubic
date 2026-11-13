#!/usr/bin/env python3
"""Exact SymPy checks for one split Fermat cubic fourfold (2026-11-13).

This is a finite-example verification over QQ, not a proof for all smooth
ternary cubics f and g, nor a proof of the classification in paper A.

Set F = (x0**3 + x1**3 + x2**3 + y0**3 + y1**3 + y2**3)/3 and
q = i_(dF)(d_x0 ^ d_x1 ^ d_x2 + d_y0 ^ d_y1 ^ d_y2).
On x0 != 0 use (a,b,c,d,e) = (x1,x2,y0,y1,y2)/x0.  On X and b != 0,
b is eliminated implicitly from H = 1+a**3+b**3+c**3+d**3+e**3 = 0.

Conventions: {r,s} = sum(P[i,j] * D_i(r) * D_j(s)); the ordered local
coordinates are (a,c,d,e), and the volume is da ^ dc ^ dd ^ de.  We use
Z^j = sum_i D_i(P[i,j]) for the modular vector field.  Equivalently,
Z(r) = div(X_r) with X_r(s) = {s,r}.  Thus Z = i_(d log pf(P))(P) off
the degeneracy divisor, and the script checks its regular extension on
this chart.  The opposite Hamiltonian convention reverses the sign of Z.

Run: python3 computations/verify_split_cubic_fourfold.py
The only third-party dependency is sympy; the script writes no files.
"""
from itertools import combinations

import sympy as s


def assert_zero(expression, label):
    residual = s.cancel(expression)
    if residual != 0:
        raise AssertionError(f"{label}: nonzero residual {residual}")


def assert_matrix_equal(actual, expected, label):
    if actual.shape != expected.shape:
        raise AssertionError(f"{label}: matrix shapes differ")
    for i in range(actual.rows):
        for j in range(actual.cols):
            assert_zero(actual[i, j] - expected[i, j], f"{label}[{i},{j}]")


def verify_jacobi(matrix, derivative, label):
    triples = list(combinations(range(matrix.rows), 3))
    for i, j, k in triples:
        jacobiator = sum(
            matrix[ii, r] * derivative(matrix[jj, kk], r)
            for ii, jj, kk in ((i, j, k), (j, k, i), (k, i, j))
            for r in range(matrix.rows)
        )
        assert_zero(jacobiator, f"{label} Jacobi({i},{j},{k})")
    return len(triples)


def main():
    z = s.symbols("x0 x1 x2 y0 y1 y2")
    x0 = z[0]
    F = sum(t**3 for t in z) / s.Integer(3)
    q = s.zeros(6)
    for offset in (0, 3):
        for i, j, k in ((offset, offset + 1, offset + 2),
                        (offset + 1, offset + 2, offset),
                        (offset + 2, offset, offset + 1)):
            q[i, j] = s.diff(F, z[k])
            q[j, i] = -q[i, j]
    ambient_count = verify_jacobi(q, lambda expr, i: s.diff(expr, z[i]),
                                  "ambient")
    assert_matrix_equal(q * s.Matrix([s.diff(F, t) for t in z]), s.zeros(6, 1),
                        "F Casimir")

    # Compute the quotient-coordinate brackets before setting x0 = 1.
    a, b, c, d, e = chart = s.symbols("a b c d e")
    ratios = s.Matrix([t / x0 for t in z[1:]])
    jacobian = ratios.jacobian(z)
    substitution = dict(zip(z, (s.Integer(1), a, b, c, d, e)))
    projective = (jacobian * q * jacobian.T).applyfunc(
        lambda expr: s.cancel(expr).subs(substitution, simultaneous=True)
    )
    h0 = 1 + a**3 + b**3
    expected_projective = s.Matrix([
        [0, h0, b**2*c, b**2*d, b**2*e],
        [-h0, 0, -a**2*c, -a**2*d, -a**2*e],
        [-b**2*c, a**2*c, 0, e**2, -d**2],
        [-b**2*d, a**2*d, -e**2, 0, c**2],
        [-b**2*e, a**2*e, d**2, -c**2, 0],
    ])
    assert_matrix_equal(projective, expected_projective, "projective bracket")
    projective_count = verify_jacobi(
        projective, lambda expr, i: s.diff(expr, chart[i]), "projective"
    )
    g3 = c**3 + d**3 + e**3
    H = h0 + g3
    assert_zero(3 * F.subs(substitution) - H, "chart equation")
    assert_matrix_equal(
        projective * s.Matrix([s.diff(H, t) for t in chart]),
        3 * H * s.Matrix([b**2, -a**2, 0, 0, 0]),
        "tangency to H=0",
    )

    # These derivations act on QQ[a,b,c,d,e,b^(-1)]/(H), without choosing
    # a cube-root branch: D_t = partial_t - (t**2/b**2) partial_b.
    local = (a, c, d, e)
    indices = (0, 2, 3, 4)
    db = tuple(s.cancel(-s.diff(H, t) / s.diff(H, b)) for t in local)

    def derivative(expr, i):
        return s.diff(expr, local[i]) + db[i] * s.diff(expr, b)

    p = projective.extract(indices, indices)
    for i, t in enumerate(local):
        assert_zero(derivative(H, i), f"D_{t}(H)")
        induced = sum(p[i, j] * db[j] for j in range(4))
        residual = s.cancel(induced - projective[indices[i], 1])
        numerator, _ = residual.as_numer_denom()
        assert_zero(s.rem(numerator, H, b), f"implicit bracket {{{t},b}} mod H")
    local_count = verify_jacobi(p, derivative, "implicit chart")

    # In this orientation, pi^2 = 2*pfaffian*d_a ^ d_c ^ d_d ^ d_e.
    pfaffian = s.factor(p[0, 1]*p[2, 3] - p[0, 2]*p[1, 3]
                        + p[0, 3]*p[1, 2])
    assert_zero(pfaffian - b**2*g3, "Pfaffian")
    assert_zero(p.det() - pfaffian**2, "determinant equals Pfaffian squared")

    modular = s.Matrix([
        s.cancel(sum(derivative(p[i, j], i) for i in range(4)))
        for j in range(4)
    ])
    from_pfaffian = s.Matrix([
        s.cancel(sum(derivative(pfaffian, i) * p[i, j] for i in range(4))
                 / pfaffian)
        for j in range(4)
    ])
    expected_modular = s.Matrix([
        -3*b**2 + 2*g3/b,
        -2*a**2*c/b,
        -2*a**2*d/b,
        -2*a**2*e/b,
    ])
    assert_matrix_equal(modular, expected_modular, "modular field")
    assert_matrix_equal(from_pfaffian, modular, "modular field from Pfaffian")
    # E_f is c=d=e=0, with 1+a^3+b^3=0; this chart has b != 0.
    on_ef = modular.subs({c: 0, d: 0, e: 0})
    assert_matrix_equal(on_ef, s.Matrix([-3*b**2, 0, 0, 0]), "modular field on E_f")

    print("Scope: exact finite-example verification over QQ for the split Fermat cubic.")
    print("This does NOT prove the statements for all smooth ternary cubics f and g.")
    print(f"PASS ambient: Jacobi on {ambient_count} coordinate triples; F is Casimir.")
    print(f"PASS projective x0=1 chart: all 10 brackets, "
          f"{projective_count} Jacobi triples, tangency to H=0.")
    print("Projective brackets in order (a,b,c,d,e):")
    for i, j in combinations(range(5), 2):
        print(f"  {{{chart[i]},{chart[j]}}} = {projective[i, j]}")
    print(f"PASS implicit chart H=0, b!=0: b-brackets and {local_count} Jacobi triples.")
    print("Local coordinate order: (a,c,d,e); volume: da ^ dc ^ dd ^ de.")
    print(f"PASS Pfaffian = {pfaffian}; coefficient of pi^2 is twice this.")
    print("Modular convention: Z^j = sum_i D_i(P[i,j]), with implicit derivatives.")
    print(f"PASS modular coefficients (a,c,d,e): {list(modular)}")
    print("PASS independent Pfaffian formula Z = i_(d log Pfaffian)(pi).")
    print("PASS on E_f: Z = -3*b**2*d/da, nonzero because b!=0.")
    print("All checks passed; the general smooth-f,g arguments belong to the manuscript.")


if __name__ == "__main__":
    main()
