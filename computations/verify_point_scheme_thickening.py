#!/usr/bin/env python3
"""Verify the isolated point-scheme chart, not the Sklyanin classification."""
import json, itertools, argparse
from pathlib import Path
import sympy as s
x,y,z,v,h=s.symbols("x y z v h")
F=(x**3+y**3+z**3)/3+1+v**3+x*y
O=F+h*h*z*(s.Rational(1,6)-s.Rational(2,3)*x*y)+h**4*z*z/18
GB=s.groebner([x*x+y,y*y+x,z*z],x,y,z,v,h,order="lex",domain=s.QQ)
rem=lambda q:s.expand(GB.reduce(s.expand(q))[1])
assert rem(x*y*(x*y-1))==0
assert rem(O-F-h*h*z*(s.Rational(1,6)-s.Rational(2,3)*x*y))==0
cases=[]
for H in [1,2,3]:
    g=s.groebner([x*x+y,y*y+x,z*z,O.subs(h,H)],x,y,v,z,order="lex",domain=s.QQ)
    leading=[p.monoms()[0] for p in g.polys]
    basis=[e for e in itertools.product(range(4),range(4),range(8),range(3))
           if not any(all(a>=b for a,b in zip(e,m)) for m in leading)]
    assert g.is_zero_dimensional and len(basis)==24
    cases.append({"h":H,"length":24,"leading_monomials":[list(t) for t in leading]})
cert={"version":"v39","exact_chart":"u=1","parameter":"h nonzero; elliptic case excludes h^6=-27",
      "poisson_ideal":["x^2+y","y^2+x","z^2","1+v^3+xy/3"],
      "point_ideal":["x^2+y","y^2+x","z^2","1+v^3+xy/3+h^2*z*(1/6-2*xy/3)"],
      "x_y_solutions":4,"isolated_support_points":12,"local_length":2,
      "shear":"v'=v+h^2*z*(1/6-2*xy/3)/(3*v^2), valid modulo z^2",
      "groebner_checks":cases,
      "not_verified":["global Sklyanin theorem","point functor representability","flat limit h=0"]}
ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path,required=True);args=ap.parse_args()
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+"\n")
print("PASS: chart symbolic reductions and three 24-dimensional Groebner quotients")
