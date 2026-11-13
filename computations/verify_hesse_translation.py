#!/usr/bin/env python3
"""Verify the Hesse-to-Etingof--Ginzburg coordinate identities exactly.

Run: python3 computations/verify_hesse_translation.py
Dependency: sympy.  No files are written.

All coefficients A,...,G and parameters h,t are independent symbols.  The
calculation takes place over QQ(A,B,C,D,E,H,G,h,t), with t and 1-h*t/2
invertible.  We check the entire translated cubic and each defining
relation as an equality of free associative polynomials.  This verifies
the coordinate comparison, not centrality or flatness of the algebras.
"""
import sympy as s


def require_zero(expression, label):
    if expression.has(s.Float):
        raise AssertionError(f"{label}: floating-point coefficient")
    residual = s.expand(expression)
    if residual.is_commutative:
        residual = s.cancel(residual)
    if residual != 0:
        raise AssertionError(f"{label}: nonzero residual {residual}")


def main():
    x, y, z, X, Y, Z = s.symbols("x y z X Y Z")
    A, B, C, D, E, H, G, h, t = s.symbols("A B C D E H G h t")
    f = (x**3 + y**3 + z**3) / 3 + t*x*y*z
    f += A*x*y + B*y*z + C*z*x + D*x + E*y + H*z + G
    translated = f.subs({x: X-B/t, y: Y-C/t, z: Z-A/t}, simultaneous=True)
    d = D + B**2/t**2 - A*C/t
    e = E + C**2/t**2 - A*B/t
    h_coefficient = H + A**2/t**2 - B*C/t
    constant = G - (B*D+C*E+A*H)/t + 2*A*B*C/t**2
    constant -= (A**3+B**3+C**3)/(3*t**3)
    expected = (X**3+Y**3+Z**3)/3 + t*X*Y*Z
    expected += -B*X**2/t-C*Y**2/t-A*Z**2/t
    expected += d*X+e*Y+h_coefficient*Z+constant
    require_zero(translated-expected, "translated cubic")

    # Noncommuting letters retain every word separately.  All parameters
    # commute with them, as required for the central coordinate shift.
    X, Y, Z = s.symbols("X Y Z", commutative=False)
    old_x, old_y, old_z = X-B/t, Y-C/t, Z-A/t
    q = (1+h*t/2)/(1-h*t/2)
    mu = h/(1-h*t/2)
    cyclic = [
        (old_x, old_y, old_z, X, Y, Z, B, C, H, A, h_coefficient),
        (old_y, old_z, old_x, Y, Z, X, C, A, D, B, d),
        (old_z, old_x, old_y, Z, X, Y, A, B, E, C, e),
    ]
    for index, (a,b,c,U,V,W,left,right,linear,shift,new_linear) in enumerate(cyclic):
        original = a*b-b*a-h*(c**2+t*(a*b+b*a)/2+left*b+right*a+linear)
        normalized = U*V-q*V*U-mu*(W**2-2*shift*W/t+new_linear)
        # Compare the rational scalar coefficient of each free word.
        residual = s.expand(original-(1-h*t/2)*normalized)
        coefficients = {}
        for term in s.Add.make_args(residual):
            scalars, letters = term.args_cnc()
            word = s.Mul(*letters)
            coefficients[word] = coefficients.get(word, s.Integer(0)) + s.Mul(*scalars)
        for word, coefficient in coefficients.items():
            require_zero(coefficient, f"cyclic relation {index}, word {word}")

    print(f"SymPy {s.__version__}; exact rational arithmetic; all coefficients independent.")
    print("PASS translated cubic including its constant term and all three free-word relations.")
    print("Scope: t and 1-h*t/2 invertible; no centrality or flatness assertion is tested.")


if __name__ == "__main__":
    main()
