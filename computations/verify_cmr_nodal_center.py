#!/usr/bin/env python3
"""Auxiliary exact checks of the CMR nodal central-element formula.

Source: L. Chekhov, M. Mazzocco, V. Rubtsov, arXiv:1905.02772v2
(accepted version), equations (4.38), (4.39), Lemma 4.6, pp.21--22.
Published metadata: Advances in Mathematics 376 (2021), article 107442,
DOI 10.1016/j.aim.2020.107442.  Equation/page numbers above refer to v2.
The formula is an independently cited input; its existence is not a new
result of this calculation.

1. Over QQ[q,q^-1,alpha,beta,a1,a2,b1,b2,c1,c2], gamma=0, verify the
   unique word overlap zyx and all three central commutators of (4.39).
2. Specialize to the symmetric Jacobian relations for
   f0=x^3+y^3+xyz+A*x^2+B*y^2+C*z^2+Lx*x+Ly*y+Lz*z+K.
   Set p=1+t/2, s=1-t/2, q=p/s, alpha=beta=3t/s,
   (a1,b1,c1)=-2t*(A,B,C)/s, (a2,b2,c2)=-t*(Lx,Ly,Lz)/s.
   Check the relations coefficientwise.  Omega_CMR/(6t) is regular at
   t=0; multiplying it by s^5 clears all parameter denominators.
3. Q=s^5*Omega_CMR/(6t)+K has classical limit f0.  For the x/y swap,
   including A<->B, Lx<->Ly and t->-t, Q^swap-Q=-6*C*Lz*t^3.
   Thus Qhat=Q-3*C*Lz*t^3 has exact swap covariance.  Every monomial
   has scalar weight three and mu_3 character zero, checking the other
   generators of the displayed nodal stabilizer.
4. For a general quadratic q2, verify that
   sigma_alt(q2)=([yz]q2,[xz]q2,[xy]q2) is a left inverse of delta_g
   and translation by this vector leaves only diagonal quadratic terms.

Arithmetic is exact over QQ, with all coefficients independent.  The
quantum comparison is on the parameter open set p*s != 0.  Polynomial
coefficients of Qhat do not, by themselves, assert PBW or flatness at
t=+/-2.  Full stabilizer classification, regular orbit transport, full
block-group descent and evenness in a chosen PBW identification are not
verified here.  Coefficient substitution gives arbitrary central base
change; this is not a proof-assistant verification of the manuscript.

Run: python3 -B verify_cmr_nodal_center.py --json
Optional: --output PATH.  Dependency: sympy.
No file is written unless --output is supplied.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from functools import lru_cache
import hashlib
import json
from pathlib import Path

import sympy as sp


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def clean(poly, simplify=sp.expand):
    result = {}
    for word, coefficient in poly.items():
        require(not sp.sympify(coefficient).has(sp.Float), "Floating-point input")
        value = simplify(coefficient)
        if value != 0:
            result[word] = value
    return result


def subtract(left, right, simplify=sp.expand):
    result = defaultdict(lambda: sp.S.Zero, left)
    for word, coefficient in right.items():
        result[word] -= coefficient
    return clean(result, simplify)


def require_zero(expression, label):
    require(sp.cancel(expression) == 0, f"{label}: {expression}")


def word_key(word):
    return len(word), tuple("xyz".index(letter) for letter in word)


class Normalizer:
    def __init__(self, rules, simplify=sp.expand):
        self.simplify = simplify
        self.rules = {word: clean(poly, simplify) for word, poly in rules.items()}
        for word, poly in self.rules.items():
            require(all(word_key(other) < word_key(word) for other in poly),
                    "A rule does not decrease degree-lex z>y>x")

    def first_step(self, word, position):
        return {word[:position]+other+word[position+2:]: coefficient
                for other, coefficient in self.rules[word[position:position+2]].items()}

    @lru_cache(None)
    def normal_word(self, word):
        for position in range(len(word)-1):
            if word[position:position+2] in self.rules:
                return self.reduce(self.first_step(word, position))
        return {word: sp.S.One}

    def reduce(self, poly):
        result = defaultdict(lambda: sp.S.Zero)
        for word, coefficient in poly.items():
            for other, value in self.normal_word(word).items():
                result[other] += coefficient*value
        return clean(result, self.simplify)


def verify():
    q, alpha, beta, a1, a2, b1, b2, c1, c2 = sp.symbols(
        "q alpha beta a1 a2 b1 b2 c1 c2")
    rules = {
        "yx": {"xy": 1/q, "z": c1/q, "": c2/q},
        "zx": {"xz": q, "yy": beta, "y": -b1, "": -b2},
        "zy": {"yz": 1/q, "xx": -alpha/q, "x": a1/q, "": a2/q},
    }
    normalizer = Normalizer(rules)
    overlaps = sorted({left+right[-1] for left in rules for right in rules
                       if left[-1] == right[0]})
    require(overlaps == ["zyx"], "Unexpected critical words")
    require(not subtract(normalizer.reduce(normalizer.first_step("zyx", 0)),
                         normalizer.reduce(normalizer.first_step("zyx", 1))),
            "Nonzero zyx ambiguity")

    # This is the cited CMR expression (4.39), in its displayed word order.
    S, T = 1+q+q**2, 1+2*q+2*q**2+q**3
    omega = {
        "zyx": q*(1+q)*(q**3-1),
        "xxx": q**3*(1+q)*alpha,
        "yyy": (1+q)*beta,
        "xx": -a1*q**2*S,
        "yx": c1*q*(1+q)*alpha*beta,
        "yy": -b1*S,
        "zz": -c1*q**2*S,
        "x": -q*(a2*T+b1*c1*alpha),
        "y": -b2*T-a1*c1*q*beta,
        "z": -q*(c2*T+c1**2*alpha*beta),
    }
    for letter in "xyz":
        left = normalizer.reduce({word+letter: coefficient for word, coefficient in omega.items()})
        right = normalizer.reduce({letter+word: coefficient for word, coefficient in omega.items()})
        require(not subtract(left, right), f"Nonzero CMR commutator with {letter}")

    t, A, B, C, Lx, Ly, Lz, K = sp.symbols("t A B C Lx Ly Lz K")
    p, s = 1+t/2, 1-t/2
    parameters = {
        q: p/s, alpha: 3*t/s, beta: 3*t/s,
        a1: -2*t*A/s, b1: -2*t*B/s, c1: -2*t*C/s,
        a2: -t*Lx/s, b2: -t*Ly/s, c2: -t*Lz/s,
    }
    cmr_relations = {
        "xy": {"xy": 1, "yx": -q, "z": c1, "": c2},
        "yz": {"yz": 1, "zy": -q, "xx": -alpha, "x": a1, "": a2},
        "zx": {"zx": 1, "xz": -q, "yy": -beta, "y": b1, "": b2},
    }
    jacobian_relations = {
        "xy": {"xy": s, "yx": -p, "z": -2*t*C, "": -t*Lz},
        "yz": {"yz": s, "zy": -p, "xx": -3*t, "x": -2*t*A, "": -t*Lx},
        "zx": {"zx": s, "xz": -p, "yy": -3*t, "y": -2*t*B, "": -t*Ly},
    }
    for key, relation in cmr_relations.items():
        specialized = {word: s*sp.sympify(value).subs(parameters) for word, value in relation.items()}
        require(not subtract(specialized, jacobian_relations[key], sp.cancel),
                f"CMR/Jacobian relation mismatch: {key}")

    normalized = {word: sp.cancel(coefficient.subs(parameters)/(6*t))
                  for word, coefficient in omega.items()}
    for coefficient in normalized.values():
        require(sp.fraction(coefficient)[1].subs(t, 0) != 0, "Normalization has a pole at t=0")
    Q = {word: sp.cancel(s**5*coefficient) for word, coefficient in normalized.items()}
    Q[""] = K
    coefficients = (t, A, B, C, Lx, Ly, Lz, K)
    for coefficient in Q.values():
        sp.Poly(coefficient, *coefficients, domain=sp.QQ)
    x, y, z = active = sp.symbols("x y z")
    monomial = lambda word: sp.prod({"x": x, "y": y, "z": z}[letter] for letter in word)
    classical = sum(coefficient.subs(t, 0)*monomial(word) for word, coefficient in Q.items())
    f0 = x**3+y**3+x*y*z+A*x**2+B*y**2+C*z**2+Lx*x+Ly*y+Lz*z+K
    require_zero(classical-f0, "Classical normalization")

    specialized_rules = {
        word: {other: sp.cancel(value.subs(parameters)) for other, value in poly.items()}
        for word, poly in normalizer.rules.items()
    }
    specialized_normalizer = Normalizer(specialized_rules, sp.cancel)

    def swap(poly):
        change = {t: -t, A: B, B: A, Lx: Ly, Ly: Lx}
        return {word.translate(str.maketrans("xy", "yx")): value.xreplace(change)
                for word, value in poly.items()}

    def swap_difference(poly):
        return subtract(specialized_normalizer.reduce(swap(poly)),
                        specialized_normalizer.reduce(poly), sp.cancel)

    residual = swap_difference(Q)
    require(residual == {"": -6*C*Lz*t**3}, f"Unexpected swap residual: {residual}")
    Qhat = dict(Q)
    Qhat[""] = K-3*C*Lz*t**3
    require(not swap_difference(Qhat), "Qhat is not swap-covariant")
    scalar_weights = (0, 1, 1, 1, 2, 2, 2, 3)
    mu3_weights = (0, 1, 2, 0, 2, 1, 0, 0)
    for word, coefficient in Qhat.items():
        for exponents, value in sp.Poly(coefficient, *coefficients, domain=sp.QQ).terms():
            require(sum(e*w for e, w in zip(exponents, scalar_weights))+len(word) == 3,
                    "Incorrect scalar character")
            require((sum(e*w for e, w in zip(exponents, mu3_weights))
                     + word.count("x")+2*word.count("y")) % 3 == 0,
                    "Incorrect mu_3 character")

    qxx, qxy, qxz, qyy, qyz, qzz = sp.symbols("qxx qxy qxz qyy qyz qzz")
    q2 = qxx*x**2+qxy*x*y+qxz*x*z+qyy*y**2+qyz*y*z+qzz*z**2
    g = x**3+y**3+x*y*z
    v = sp.symbols("v1 v2 v3")

    def sigma_alt(poly):
        poly = sp.Poly(poly, *active)
        return sp.Matrix([poly.coeff_monomial(y*z), poly.coeff_monomial(x*z),
                          poly.coeff_monomial(x*y)])

    require(sigma_alt(sum(vi*sp.diff(g, xi) for vi, xi in zip(v, active))) == sp.Matrix(v),
            "sigma_alt is not a left inverse")
    center = sigma_alt(q2)
    translated = sp.expand((g+q2+Lx*x+Ly*y+Lz*z+K).xreplace(
        dict(zip(active, sp.Matrix(active)-center))))
    quadratic = sum(coefficient*sp.prod(xi**power for xi, power in zip(active, powers))
                    for powers, coefficient in sp.Poly(translated, *active).terms()
                    if sum(powers) == 2)
    require_zero(quadratic-((qxx-3*qyz)*x**2+(qyy-3*qxz)*y**2+qzz*z**2),
                 "General quadratic to diagonal quadratic")

    return {
        "status": "PASS",
        "source": "Chekhov--Mazzocco--Rubtsov, arXiv:1905.02772v2, (4.38)--(4.39), Lemma 4.6, pp.21--22; Table 5, p.41.",
        "published_doi": "10.1016/j.aim.2020.107442",
        "arithmetic": "Exact QQ arithmetic; all displayed parameters independent.",
        "generic_CMR_ring": "QQ[q,q^-1,alpha,beta,a1,a2,b1,b2,c1,c2], gamma=0",
        "monic_rules_decrease_degree_lex": "z>y>x",
        "critical_words": overlaps,
        "critical_pair_residual": {},
        "central_commutator_residuals": {letter: 0 for letter in "xyz"},
        "CMR_parameter_map": {str(key): str(value) for key, value in parameters.items()},
        "Jacobian_relation_residuals": {key: {} for key in cmr_relations},
        "normalization": "Q=(1-t/2)^5*Omega_CMR/(6t)+K",
        "regular_at_t_zero": True,
        "Q_polynomial_in_t_and_all_coefficients": True,
        "classical_residual": 0,
        "swap": "x<->y, A<->B, Lx<->Ly, t->-t",
        "Q_swap_minus_Q": {"1": str(residual[""])},
        "Qhat": "Q-3*C*Lz*t^3",
        "Qhat_swap_residual": {},
        "Qhat_scalar_weight": 3,
        "Qhat_mu3_weight": 0,
        "Qhat_coefficients_in_displayed_word_order": {
            word or "1": str(sp.factor(value)) for word, value in Qhat.items()},
        "centering": {"sigma_alt_delta": "I3", "B": [str(value) for value in center],
                      "translated_quadratic": str(quadratic)},
        "parameter_open_set": "(1-t/2)*(1+t/2) != 0",
        "limits": [
            "The CMR expression is a cited known formula, independently checked here; central-element existence is not claimed as new.",
            "Polynomial coefficients alone do not assert PBW or flatness at t=+/-2.",
            "Full stabilizer classification, regular orbit transport and full block-group/moduli descent are not verified by this calculation.",
            "Evenness in a chosen PBW identification is not tested.",
        ],
        "sympy_version": sp.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print all results as JSON.")
    parser.add_argument("--output", type=Path, help="Optionally write JSON to this file.")
    args = parser.parse_args()
    result = verify()
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)+"\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    if args.json:
        print(text, end="")
    else:
        print("PASS: generic gamma=0 CMR overlap and all central commutators.")
        print("PASS: exact Jacobian specialization, regular normalization and classical limit.")
        print("PASS: Qhat covariance under the nodal stabilizer generators.")
        print("PASS: alternative centering eliminates all three mixed quadratic monomials.")
        print("SCOPE: parameter open set 1-t^2/4 != 0; orbit transport/descent not checked.")
        print("SHA256:", result["script_sha256"])


if __name__ == "__main__":
    main()
