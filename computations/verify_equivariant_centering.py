#!/usr/bin/env python3
"""Exact checks of centring under two coordinate changes (2026-11-14).

The coefficient ring is QQ[a0,...,a11,b0,...,b8,c0,...,c3].  With two
central variables (u,v), the 25 mixed coefficients of

    f(x,u) = (x**3+y**3+z**3)/3 + sum(q_i(x)*u_i)
             + sum(x_j*l_j(u)) + c(u)

are algebraically independent.  For the fixed Fermat active cubic g,
sigma_g(q) extracts the coefficients of x**2, y**2, z**2; it is a left
inverse of delta_g(w) = sum(w_i*partial_i(g)).

For X=M*x+C*u, U=N*u, define
    f' = lambda**(-1)*f(M**(-1)*(X-C*N**(-1)*U), N**(-1)*U),
    g' = lambda**(-1)*g(M**(-1)*X),
    sigma_g'(q') = M*sigma_g(lambda*q'(M*x)).
The last formula transports the chosen left inverse for this coordinate
change.  We check B_f'=(M*B_f-C)*N**(-1), the covariance of
f^circ(x,u)=f(x-B_f*u,u), and the Jacobian bracket transformation with
t'=lambda*det(M)*t.  The bracket convention is {x,y}=t*partial_z(f),
{y,z}=t*partial_x(f), {z,x}=t*partial_y(f), and u,v are central.

Scope: finite coordinate changes with universal mixed coefficients.  This
is not a computational proof of existence of a Reynolds operator, a
globally equivariant choice of sigma, or the theorem for the whole group G.

Run: python3 computations/verify_equivariant_centering.py
The only third-party dependency is sympy; the script writes no files.
"""
from itertools import combinations

import sympy as s


def assert_zero(expression, label):
    if expression.has(s.Float):
        raise AssertionError(f"{label}: floating-point input")
    residual = s.expand(expression)
    if residual != 0:
        raise AssertionError(f"{label}: nonzero polynomial residual {residual}")


def assert_matrix_equal(actual, expected, label):
    if actual.shape != expected.shape:
        raise AssertionError(f"{label}: matrix shapes differ")
    for i in range(actual.rows):
        for j in range(actual.cols):
            assert_zero(actual[i, j] - expected[i, j], f"{label}[{i},{j}]")


def sigma(quadratic, active):
    polynomial = s.Poly(quadratic, *active)
    return s.Matrix([polynomial.coeff_monomial(xi**2) for xi in active])


def mixed_quadratics(cubic, central):
    zero_central = dict.fromkeys(central, s.Integer(0))
    return [s.diff(cubic, ui).xreplace(zero_central) for ui in central]


def jacobian_matrix(cubic, active):
    fx, fy, fz = [s.diff(cubic, xi) for xi in active]
    return s.Matrix([[0, fz, -fy], [-fz, 0, fx], [fy, -fx, 0]])


def main():
    x, y, z = active = s.symbols("x y z")
    u, v = central = s.symbols("u v")
    X, Y, Z = new_active = s.symbols("X Y Z")
    U, V = new_central = s.symbols("U V")
    t, t_prime = s.symbols("t t_prime")
    w = s.Matrix(s.symbols("w0:3"))
    a = s.symbols("a0:12")
    b = s.symbols("b0:9")
    c = s.symbols("c0:4")
    quadratic_basis = (x**2, x*y, x*z, y**2, y*z, z**2)
    central_quadratics = (u**2, u*v, v**2)
    central_cubics = (u**3, u**2*v, u*v**2, v**3)
    q = [sum(a[6*i+j]*monomial
             for j, monomial in enumerate(quadratic_basis)) for i in range(2)]
    linear = [sum(b[3*i+j]*monomial
                  for j, monomial in enumerate(central_quadratics)) for i in range(3)]
    g = (x**3 + y**3 + z**3) / s.Integer(3)
    f = g + sum(qi*ui for qi, ui in zip(q, central))
    f += sum(xi*li for xi, li in zip(active, linear))
    f += sum(ci*monomial for ci, monomial in zip(c, central_cubics))
    # Construct the polynomial over QQ with all coefficients as generators;
    # no mixed coefficient is specialized in any of the checks below.
    polynomial = s.Poly(f, *(active + central + a + b + c), domain=s.QQ)
    if polynomial.as_expr().free_symbols != set(active + central + a + b + c):
        raise AssertionError("not all 25 independent mixed coefficients occur")

    B = s.Matrix.hstack(*(sigma(qi, active) for qi in mixed_quadratics(f, central)))
    assert_matrix_equal(B, s.Matrix([[a[0], a[6]], [a[3], a[9]], [a[5], a[11]]]),
                        "original B from coefficient extraction")
    delta_g = sum(wi*s.diff(g, xi) for wi, xi in zip(w, active))
    assert_matrix_equal(sigma(delta_g, active), w, "original left inverse")
    centred_x = s.Matrix(active) - B*s.Matrix(central)
    f_circ = s.expand(f.xreplace(dict(zip(active, centred_x))))
    for i, qi in enumerate(mixed_quadratics(f_circ, central)):
        assert_matrix_equal(sigma(qi, active), s.zeros(3, 1), f"centred B column {i}")

    cases = [
        ("positive determinant", s.Matrix([[1, 1, 0], [0, 1, 1], [1, 0, 1]]),
         s.Matrix([[1, 1], [1, -1]]), s.Matrix([[1, 0], [0, -1], [1, 1]]),
         s.Rational(2, 3)),
        ("negative determinant", s.Matrix([[0, 1, 0], [1, 1, 1], [0, 0, 2]]),
         s.Matrix([[2, 1], [1, 1]]), s.Matrix([[-1, 2], [s.Rational(1, 2), 0], [0, 1]]),
         s.Rational(3, 2)),
    ]
    print(f"SymPy {s.__version__}; exact polynomial arithmetic over QQ.")
    print("Scope: two finite coordinate changes, with all 25 mixed coefficients symbolic.")
    print("This does NOT prove Reynolds existence or equivariance for the whole group G.")
    print(f"PASS original left inverse and centring; B_f = {B.tolist()}")

    for name, M, N, C, scale in cases:
        if M.det() == 0 or N.det() == 0 or scale == 0:
            raise AssertionError(f"{name}: coordinate change is not invertible")
        old_u = N.inv()*s.Matrix(new_central)
        old_x = M.inv()*(s.Matrix(new_active) - C*old_u)
        inverse = dict(zip(active + central, tuple(old_x) + tuple(old_u)))
        f_prime = s.expand(f.xreplace(inverse) / scale)
        g_prime = s.expand(g.xreplace(dict(zip(active, M.inv()*s.Matrix(new_active))))
                           / scale)
        assert_zero(f_prime.xreplace(dict.fromkeys(new_central, s.Integer(0))) - g_prime,
                    f"{name}: active cubic")

        def sigma_prime(quadratic):
            pulled_back = quadratic.xreplace(dict(zip(new_active, M*s.Matrix(active))))
            return (M*sigma(s.expand(scale*pulled_back), active)).applyfunc(s.expand)

        delta_prime = sum(wi*s.diff(g_prime, Xi) for wi, Xi in zip(w, new_active))
        assert_matrix_equal(sigma_prime(delta_prime), w, f"{name}: transported left inverse")
        B_prime = s.Matrix.hstack(*(sigma_prime(qi)
                                   for qi in mixed_quadratics(f_prime, new_central)))
        assert_matrix_equal(B_prime, (M*B-C)*N.inv(), f"{name}: B covariance")

        centred_X = s.Matrix(new_active) - B_prime*s.Matrix(new_central)
        f_prime_circ = f_prime.xreplace(dict(zip(new_active, centred_X)))
        linear_inverse = dict(zip(active + central,
                                  tuple(M.inv()*s.Matrix(new_active)) + tuple(old_u)))
        expected_circ = f_circ.xreplace(linear_inverse) / scale
        assert_zero(f_prime_circ - expected_circ, f"{name}: centred cubic covariance")

        # Pull back the three independent target brackets, comparing them
        # with brackets of the coordinate images computed in the source.
        images = M*s.Matrix(active) + C*s.Matrix(central)
        forward = dict(zip(new_active + new_central,
                           tuple(images) + tuple(N*s.Matrix(central))))
        forward[t_prime] = scale*M.det()*t
        source = t*jacobian_matrix(f, active)
        target = t_prime*jacobian_matrix(f_prime, new_active)
        image_derivatives = images.jacobian(active)
        bracket_images = image_derivatives*source*image_derivatives.T
        for i, j in combinations(range(3), 2):
            assert_zero(target[i, j].xreplace(forward) - bracket_images[i, j],
                        f"{name}: Jacobian bracket ({i},{j})")

        print(f"PASS {name}: det(M)={M.det()}, det(N)={N.det()}, lambda={scale}.")
        print(f"  M={M.tolist()}, N={N.tolist()}, C={C.tolist()}")
        print("  Transported left inverse, extracted B_f'=(M*B_f-C)*N^(-1),")
        print("  and (f')^circ=lambda^(-1)*f^circ(M^(-1)*X,N^(-1)*U) verified.")
        print(f"  All 3 Jacobian brackets verified with t'={scale*M.det()}*t.")

    print("All checks passed; finite coordinate changes with universal mixed coefficients.")
    print("The Reynolds and full-group arguments remain mathematical proofs in the manuscript.")


if __name__ == "__main__":
    main()
