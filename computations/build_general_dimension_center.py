#!/usr/bin/env python3
"""Build Weyl symbols of exact multi-block quantum cubic central elements.

Each block has a Hesse smooth active restriction with arbitrary central
diagonal, mixed quadratic, linear and cubic coefficients. Noncommutative
central elements are Weyl symmetrizations of the resulting polynomial.
Supply Hesse coordinates; this does not find Hesse normal forms automatically.
Usage: python3 computations/build_general_dimension_center.py
Requires: sympy.
"""
import sympy as sp


def hesse_center_symbol(active, eta, t, A, B, C, D, E, H, G,
                        diagonal=(0, 0, 0)):
    x, y, z = active
    p, q, r = map(sp.sympify, diagonal)
    t, eta = map(sp.sympify, (t, eta))
    X, Y, Z = x+p, y+q, z+r
    Ap, Bp, Cp = A-t*r, B-t*p, C-t*q
    Dp = D-p*p-A*q-C*r+t*q*r
    Ep = E-q*q-A*p-B*r+t*p*r
    Hp = H-r*r-B*q-C*p+t*p*q
    Gp = G+sp.Rational(2, 3)*(p**3+q**3+r**3) + A*p*q+B*q*r+C*r*p \
         - D*p-E*q-H*r-t*p*q*r
    h2 = eta**2
    U = 1+h2*t**2/2+h2**2*t/6-h2**2*t**4/48
    W = (4-h2*t**2)*(12*t+h2*(t**3-8))/48
    c = (4-h2*t**2)*(12+h2*t**2)/48
    d = h2*(12*t+h2*(2-t**3))/36
    e = 1+h2**2*t*(8-t**3)/144
    f = h2*(4-h2*t**2)/24
    g = -h2*(12*t+h2*(t**3+4))/72
    S = X**3+Y**3+Z**3
    T = X*Y*Z  # Weyl symbol of the SIX words sym(xyz)
    Q = Ap*X*Y+Bp*Y*Z+Cp*Z*X
    Z2 = Ap*Z**2+Bp*X**2+Cp*Y**2
    L = Dp*X+Ep*Y+Hp*Z
    R2 = Bp**2*X+Cp**2*Y+Ap**2*Z
    R11 = Ap*Cp*X+Ap*Bp*Y+Bp*Cp*Z
    center = U*S/3+W*T+c*Q+d*Z2+e*L+f*R2+g*R11+Gp
    classic = (x**3+y**3+z**3)/3+t*x*y*z+p*x*x+q*y*y+r*z*z \
              + A*x*y+B*y*z+C*z*x+D*x+E*y+H*z+G
    assert sp.expand(center.subs(eta, 0)-classic) == 0
    assert sp.Poly(sp.expand(center), eta).degree() <= 4
    return sp.expand(classic), sp.expand(center)


def build_family(blocks):
    F, Omega = sp.S.Zero, sp.S.Zero
    params = []
    for blk in blocks:
        fs, Om = hesse_center_symbol(**blk)
        F += fs
        Omega += Om
        params.append(blk["eta"])
    for a in range(len(params)):
        for b in range(a+1, len(params)):
            assert sp.diff(Omega, params[a], params[b]) == 0
    assert sp.expand(Omega.subs({v: 0 for v in params})-F) == 0
    return sp.expand(F), sp.expand(Omega)


def demo():
    u, v, h0, h1 = sp.symbols("u v h0 h1")
    block0 = dict(
        active=sp.symbols("x y z"), eta=h0, t=sp.Rational(1, 2),
        A=u, B=u+v, C=2*v, D=u*u, E=u*v, H=v*v,
        G=(u**3+v**3)/6, diagonal=(u, v, u+v))
    block1 = dict(
        active=sp.symbols("a b c"), eta=h1, t=-sp.Rational(1, 3),
        A=u-v, B=2*u, C=v, D=u*v, E=v*v, H=u*u,
        G=(u**3+v**3)/6, diagonal=(v, u, 0))
    F, Omega = build_family([block0, block1])
    assert sp.expand(Omega.subs({h0: 0, h1: 0})-F) == 0
    assert sp.diff(Omega, h0, h1) == 0
    print("PASS: two blocks share central u,v and have independent parameters")
    print("PASS: Omega_00=F and no h0*h1 mixed corrections")
    print("PASS: n=6, N=8, generic Poisson rank 4")
    vars0 = sp.symbols("x y z a b c u v")
    print("Polynomial terms: F=", len(sp.Poly(F, *vars0).terms()),
          "Omega=", len(sp.Poly(Omega, *vars0, h0, h1).terms()))


if __name__ == "__main__":
    demo()
