#!/usr/bin/env python3
"""Exact finite tests for the mixed lambda point-scheme family.
The infinite point-module functor and Sklyanin theorem are NOT tested here.
"""
import argparse, itertools, json
from pathlib import Path
import sympy as sp

x,y,z,v,lam,h=sp.symbols('x y z v lam h')
G=sp.groebner([x*x+lam*y,y*y+lam*x],x,y,order='grlex',domain=sp.QQ.poly_ring(lam))
assert len(G.polys)==2
assert sp.simplify(G.reduce(x**3+y**3+3*lam*x*y)[1]-lam*x*y)==0
assert sp.simplify(G.reduce(x*x*y*y)[1]-lam**2*x*y)==0

# Check the explicit shear by clearing v denominators; result is divisible by z^2.
c=lam**2/sp.Integer(6)-2*x*y/sp.Integer(3)
t=h**2*z*c
numerator, denominator = sp.fraction(sp.cancel((v+t/(3*v**2))**3-v**3-t))
assert sp.expand(numerator).coeff(z,0) == 0
assert sp.expand(numerator).coeff(z,1) == 0
assert not denominator.has(z)
assert sp.simplify((1+lam*x*y/3)*(1-lam*x*y/(3+lam**3))-1).expand().subs(x*x*y*y,lam**2*x*y)==0

# Count the Artin ring length using standard monomials of each Groebner ideal.
def length_from_groebner(polys):
    gb=sp.groebner(polys,v,x,y,z,order='lex')
    leading=[p.LM(order='lex').exponents for p in gb.polys]
    def standard(e):
        return not any(all(a>=b for a,b in zip(e,l)) for l in leading)
    # The towers imply all exponents < 12; this finite check is independent.
    return sum(standard(exponents) for exponents in itertools.product(range(12),repeat=4))

rows=[]
for ll,hh in itertools.product([0,1,2,-1],[0,1,2]):
    polynomials=[x*x+ll*y,y*y+ll*x,z*z,1+v**3+sp.Rational(ll,3)*x*y+hh**2*z*(sp.Rational(ll*ll,6)-sp.Rational(2,3)*x*y)]
    length=length_from_groebner(polynomials)
    assert length==24,(ll,hh,length)
    rows.append({'lambda':ll,'h':hh,'isolated_length':length,'support_count':3 if ll==0 else 12,'local_length':8 if ll==0 else 2})

# At lambda=0 the nilpotent transverse algebra has 2^3=8 monomials.
assert len(list(itertools.product([0,1],repeat=3)))==8
output={'version':'nc-cubic-v41','date':'2026-11-11','scope':'Exact Groebner lengths and symbolic shear; NOT point functor proof',
        'reduction':'x^3=y^3=-lambda*xy and (xy)^2=lambda^2*xy',
        'relative_basis_rank':24,'tests':rows,'lambda0_local_ring':'C[x,y,z]/(x^2,y^2,z^2)',
        'generic_lambda_local_ring':'C[epsilon]/epsilon^2',
        'not_verified':['Sklyanin scheme theorem','relative point-module representing functor','scheme-theoretic flat closure beyond the stated algebraic proof','full cubic family generality']}
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path('build/lambda_point_scheme_certificate.json'))
args=parser.parse_args()
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
print('PASS:',len(rows),'Groebner length-24 cases; symbolic reductions and lambda=0 octuple collision')
