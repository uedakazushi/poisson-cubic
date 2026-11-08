#!/usr/bin/env python3
"""Exact certificates for one-block cubic reconstruction.

Symbolic identities over Q[h,t,tau], one Jacobian minor, and finite-field
centrality tests. This does NOT formally verify categorical equivalences.
Requires SymPy. Results are deterministic, with no floating-point arithmetic.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def zero(expr: sp.Expr, label: str) -> None:
    if sp.factor(sp.together(expr)) != 0:
        raise AssertionError(f"Failed exact identity: {label}")


def symbolic_checks() -> dict:
    h, t, tau, x, y, z = sp.symbols("h t tau x y z")
    b = 1 - h**2*t**2/4
    a = t + h**2*(1+t**3/4)/3
    theta = a/b
    delta = a**3+b**3
    U = 1+h**2*t**2/2+h**4*t/6-h**4*t**4/48
    W = (4-h**2*t**2)*(12*t+h**2*(t**3-8))/48
    aa, bb, cc = 1-h*t/2, -1-h*t/2, -h
    A = aa*(bb**3-cc**3)
    B = bb*(cc**3-aa**3)
    C = cc*(aa**3-bb**3)
    # C_word-D_word=h*S+(h*t/2)*(C_word+D_word).
    zero((A-B)*h/2+C+3*h*U, "central cubic S coefficient")
    zero((A+B)/2+(A-B)*h*t/4+sp.Rational(3,2)*h*W,
         "central cubic symmetric-word coefficient")
    zero((aa**3+bb**3+cc**3)**3-(3*aa*bb*cc)**3+27*h**3*delta,
         "Sklyanin discriminant")
    zero(delta-b**3*(1+theta**3), "Hesse discriminant")
    zero(theta-t-h**2*(1+t**3)/(3*b), "second-order deformation")
    zero(aa**3+bb**3+cc**3+3*theta*aa*bb*cc, "translation point incidence")
    mat = sp.Matrix([[cc*x,bb*z,aa*y], [aa*z,cc*y,bb*x], [bb*y,aa*x,cc*z]])
    point = sp.Matrix([aa,bb,cc])
    image = mat.subs({x:1,y:-1,z:0})*point
    for v in image:
        zero(v,"multilinearized relation at the origin")
    Q = h**2*t**3+3*tau*h**2*t**2+12*t+4*h**2-12*tau
    zero(Q-12*b*(theta-tau), "constant-model algebraic curve")
    zero(sp.diff(Q,t).subs({h:0,t:tau})-12, "etale projection")
    tseries = tau-(1+tau**3)*h**2/3
    assert sp.Poly(sp.expand(Q.subs(t,tseries)),h).nth(2) == 0
    assert sp.Poly(sp.expand(Q.subs(t,tseries)),h).nth(0) == 0
    zero(sp.diff(cc/aa,h).subs(h,0)+1, "nonzero translation tangent")
    qs = [x*x+t*y*z,y*y+t*z*x,z*z+t*x*y]
    zero((1+t**3)*x*x*y - (y*qs[0]-t*z*qs[1]+t*t*x*qs[2]),
         "Jacobian degree-three reduction")
    mons = [x**3,y**3,z**3,x*x*y,y*y*z,z*z*x,x*x*z,z*z*y,y*y*x]
    jac = sp.Matrix([[sp.Poly(v*q,x,y,z).coeff_monomial(m) for m in mons]
                     for v in (x,y,z) for q in qs])
    determinant = sp.factor(jac.det())
    zero(determinant+(1+t**3)**2,"universal 9x9 Jacobian minor")
    zero(U.subs(t,0)-1,"Fermat U")
    zero(W.subs(t,0)+2*h*h/3,"Fermat W")
    zero(delta.subs(t,0)-1-h**6/27,"Fermat discriminant")
    return {
        "coefficient_field": "Q(h,t,tau)",
        "central_cubic_coefficient_identities": True,
        "Sklyanin_discriminant": "-27*h^3*Delta(h,t)",
        "point_incidence_and_translation_orientation": True,
        "theta_minus_t": "h^2*(1+t^3)/(3*(1-h^2*t^2/4))",
        "constant_model_equation": "h^2*t^3+3*tau*h^2*t^2+12*t+4*h^2-12*tau",
        "partial_t_at_origin": 12,
        "translation_tangent": -1,
        "jacobian_minor_size": 9,
        "jacobian_minor": "-(1+t^3)^2",
        "jacobian_minor_column_monomials": [str(m) for m in mons],
        "Fermat_specialization": True,
    }


def finite_field_checks() -> list[dict]:
    prime = 1009
    letters = "xyz"
    words = ["".join(w) for w in itertools.product(letters,repeat=4)]
    index = {w:i for i,w in enumerate(words)}

    def inv(v: int) -> int:
        return pow(v % prime,-1,prime)

    def echelon(rows: list[list[int]]) -> dict[int,list[int]]:
        piv = {}
        for r0 in rows:
            r = r0[:]
            for k in sorted(piv):
                f = r[k]
                if f:
                    r = [(x-f*y)%prime for x,y in zip(r,piv[k])]
            if any(r):
                j = next(i for i,v in enumerate(r) if v)
                c = inv(r[j]); piv[j] = [(c*v)%prime for v in r]
        return piv

    out = []
    for h,t in [(0,0),(0,1),(1,0),(1,1),(7,3),(11,20),(17,200),(23,857)]:
        q = h*t*inv(2)%prime
        aa,bb,cc = (1-q)%prime,(-1-q)%prime,(-h)%prime
        relations = [{"yz":aa,"zy":bb,"xx":cc},
                     {"zx":aa,"xz":bb,"yy":cc},
                     {"xy":aa,"yx":bb,"zz":cc}]
        rows = []
        for rel in relations:
            for i in range(3):
                for pre in itertools.product(letters,repeat=i):
                    for post in itertools.product(letters,repeat=2-i):
                        row = [0]*81
                        for w,c in rel.items():
                            j = index["".join(pre)+w+"".join(post)]
                            row[j]=(row[j]+c)%prime
                        rows.append(row)
        piv = echelon(rows)
        U = (1+h*h*t*t*inv(2)+h**4*t*inv(6)-h**4*t**4*inv(48))%prime
        # Test 3*Omega, i.e. cube coefficient U, each distinct word W/2.
        v = ((4-h*h*t*t)*(12*t+h*h*(t**3-8))*inv(96))%prime
        cubic = {w:U for w in ("xxx","yyy","zzz")}
        cubic.update({"".join(w):v for w in itertools.permutations(letters)})
        for letter in letters:
            row = [0]*81
            for w,c in cubic.items():
                row[index[w+letter]]=(row[index[w+letter]]+c)%prime
                row[index[letter+w]]=(row[index[letter+w]]-c)%prime
            for k in sorted(piv):
                c = row[k]
                if c:
                    row=[(x-c*y)%prime for x,y in zip(row,piv[k])]
            assert not any(row), (h,t,letter,"commutator not in ideal")
        out.append({"h":h,"t":t,"prime":prime,"degree_four_relation_rank":len(piv),
                    "three_commutators_in_degree_four_ideal":True})
    return out


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--write",action="store_true",help="replace the current certificate")
    args=parser.parse_args()
    result={"status":"passed","symbolic":symbolic_checks(),
            "finite_field":finite_field_checks(),
            "limitations":"Polynomial and finite linear-algebra checks only. Not a formal proof of dg equivalences, generation, or family descent."}
    serialized=json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n"
    path=ROOT/"computations"/"reconstruction_certificate.json"
    if args.write:
        path.write_text(serialized,encoding="utf-8")
    else:
        if not path.exists():
            raise SystemExit("Certificate missing: first run with --write.")
        if path.read_text(encoding="utf-8") != serialized:
            raise SystemExit("Certificate differs from the exact recomputation.")
    print(json.dumps({"status":"passed","symbolic_minor":"-(1+t^3)^2",
                      "finite_field_specializations":8,"certificate":str(path)},ensure_ascii=False))


if __name__=="__main__":
    main()