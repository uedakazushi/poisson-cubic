#!/usr/bin/env python3
"""Exact symbolic checks for central cubic fiber discriminants (SymPy)."""
import sympy as s
H,U,V,W=s.symbols("H U V W")
P=49*U**3-(13*H+14)*U**2+(H+1)**2*U
m=11*U-H-1
D=27*P-m**3
F=P+m*V*W+V**3-W**3
assert s.factor(s.discriminant(P,U))==-H*(H+1)**4*(27*H+28)
assert s.factor(s.discriminant(D,U))==-78732*H*(H+1)**3
q={H:-s.Rational(28,27),U:s.Rational(1,189),V:0,W:0}
assert s.diff(F,H).subs(q)==-s.Rational(1,1323)
assert s.det(s.hessian(F,(U,V,W))).subs(q)==-s.Rational(8,1701)
G=s.groebner([x.subs(H,9) for x in (F,s.diff(F,U),s.diff(F,V),s.diff(F,W))],U,V,W)
assert G.polys[0].as_expr()==1
print("exact central-fiber discriminants, Hessian, and H=9 smoothness: PASS")
