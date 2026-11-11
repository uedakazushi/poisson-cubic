#!/usr/bin/env python3
"""Exact polynomial checks at lambda^3=-3; NOT a proof of the full Sklyanin point functor."""
import sympy as sp
import json, argparse
from pathlib import Path
from itertools import product
x,y,z,v,L=sp.symbols("x y z v L")
gb=sp.groebner([x*x+L*y,y*y+L*x],x,y,order="grlex",domain=sp.QQ.poly_ring(L))
for e in (x**3+L*x*y,y**3+L*x*y,(x*y)**2-L**2*x*y):
    assert gb.reduce(e)[1] == 0
def artin_length(equations, variables, modulus=None, width=7):
    if modulus:
        equations=[sp.expand(6*f) for f in equations]
    g=sp.groebner(equations,*variables,order="grlex",**({"modulus":modulus} if modulus else {}))
    leading=[p.LM(order="grlex").exponents for p in g.polys]
    return sum(not any(all(a>=b for a,b in zip(exps,l)) for l in leading)
               for exps in product(range(width),repeat=len(variables)))
results=[]
for hh in [0,1,2]:
    # lambda=2 is a cube root of -3 in characteristic 11.
    ll=2
    eq=[x*x+ll*y,y*y+ll*x,z*z,
        1+v**3+sp.Rational(ll,3)*x*y+
        hh**2*z*(sp.Rational(ll**2,6)-sp.Rational(2,3)*x*y)]
    length=artin_length(eq,(x,y,z,v),modulus=11,width=6)
    assert length==24,(hh,length)
    t,s=sp.symbols("t s")
    local=artin_length([s**2,t**3-sp.Rational(ll**2*hh**2,2)*s],(t,s),width=7)
    assert local==6,(hh,local)
    results.append({"lambda_mod_11":ll,"h_mod_11":hh,
                    "total_length":length,"length_each_nonzero_xy_branch":local})
assert sp.expand((x*x+L*y)*x+(y*y+L*x)*y-x**3-y**3-2*L*x*y)==0
output={
 "version":"nc-cubic-v42","date":"2026-11-11",
 "scope":"Exact quotient identities and finite characteristic-11 checks, not categorical scheme verification",
 "boundary":"lambda^3=-3,lambda nonzero",
 "relative_free_rank":24,
 "special_support":"3 length-2 points plus 3 length-6 points",
 "h_nonzero_sixfold_ring":"C[t]/(t^6)",
 "h_zero_sixfold_ring":"C[t,s]/(t^3,s^2)",
 "modular_tests":results,
 "not_verified":["Sklyanin point-functor theorem", "General Poisson zeros for singular cubic",
                 "Degenerate h^6=-27 Sklyanin curve", "All noncommutative cubic threefolds"]
}
arg=argparse.ArgumentParser();arg.add_argument("--output",type=Path,
default=Path("build/lambda_discriminant_certificate.json"))
opt=arg.parse_args()
opt.output.parent.mkdir(parents=True,exist_ok=True)
opt.output.write_text(json.dumps(output,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
print("PASS: polynomial reduction, 3 characteristic-11 rank24 tests, length6 local checks.")
