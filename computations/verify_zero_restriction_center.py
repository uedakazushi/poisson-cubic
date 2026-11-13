#!/usr/bin/env python3
"""Universal exact identities for the active-degree-at-most-two case g=0.

Work over R=QQ[a11,a22,a33,a12,a13,a23,b1,b2,b3,c,t], with every parameter
central and algebraically independent.  For the symmetric matrix A=(aij),
set f(x)=x^T*A*x/2+b^T*x+c and Omega=sym_R(f).  The monic relations are

    yx = xy - t*f_z,   zx = xz + t*f_y,   zy = yz - t*f_x.

A dictionary of free words implements reduction to x^i*y^j*z^k.  We check
decrease in degree-lex order z>y>x, the unique overlap zyx along both first
reduction paths, and all three commutators [Omega,x_i].  No coefficient
specialization, inversion of det(A), or truncation in t is used.

Over R[d1,d2,d3], we also check f'(X)=f(X-d), b'=b-A*d and
c'=c-b^T*d+d^T*A*d/2.  The central translation Phi(X)=x+d carries each
target relation to the source relation and Phi(sym(f'))=sym(f), already
in the free algebra, hence also in PBW normal form.

For a homogeneous cubic f(x,u) with g=f(x,0)=0 and any number m of central
variables u, substitute central linear forms in u for aij, central
quadratic forms for bi, central cubics for c, and central linear forms
for di.  Thus the result is a universal coefficient identity followed by
base change, not a test at a fixed m.  The PBW interpretation uses the
Diamond lemma; the script checks its terminating rules and ambiguities.
It does not cover a nonzero active cubic g, test general linear/scalar
coordinate changes, prove smoothness, or establish moduli descent.

Run: python3 computations/verify_zero_restriction_center.py
     python3 computations/verify_zero_restriction_center.py --json
Optional: --output build/verify_zero_restriction_center.json
Dependency: sympy.  No files are written unless --output is supplied.
The JSON records the coefficient ring, normal forms, scope and limits.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from functools import lru_cache
import hashlib
from itertools import permutations
import json
from pathlib import Path

import sympy as sp


Polynomial = dict[str, sp.Expr]
COEFFICIENTS = sp.symbols("a11 a22 a33 a12 a13 a23 b1 b2 b3 c t d1 d2 d3")


def clean(poly: Polynomial) -> Polynomial:
    return {word: value for word, coefficient in poly.items()
            if (value := sp.expand(coefficient)) != 0}


def add(*polynomials: Polynomial) -> Polynomial:
    result = defaultdict(lambda: sp.S.Zero)
    for polynomial in polynomials:
        for word, coefficient in polynomial.items():
            result[word] += coefficient
    return clean(result)


def scale(poly: Polynomial, scalar: sp.Expr) -> Polynomial:
    return clean({word: scalar*coefficient for word, coefficient in poly.items()})


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result = defaultdict(lambda: sp.S.Zero)
    for word, coefficient in left.items():
        for other, value in right.items():
            result[word+other] += coefficient*value
    return clean(result)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_zero(poly: Polynomial, label: str) -> None:
    residual = clean(poly)
    if residual:
        raise AssertionError(f"{label}: nonzero free/normal polynomial {residual}")


def serialize(poly: Polynomial) -> dict[str, str]:
    # Poly(..., domain=QQ) rejects floats, noncentral coefficients and
    # parameter denominators.  The empty word is displayed as 1 in JSON.
    result = {}
    for word, coefficient in sorted(clean(poly).items()):
        require(not coefficient.has(sp.Float), "Floating-point coefficient")
        exact = sp.Poly(coefficient, *COEFFICIENTS, domain=sp.QQ)
        result[word or "1"] = str(exact.as_expr())
    return result


def word_key(word: str) -> tuple[int, tuple[int, ...]]:
    return len(word), tuple("xyz".index(letter) for letter in word)


class Normalizer:
    def __init__(self, rules: dict[str, Polynomial]):
        self.rules = {word: clean(poly) for word, poly in rules.items()}
        for leading, polynomial in self.rules.items():
            require(all(word_key(word) < word_key(leading) for word in polynomial),
                    f"Rule {leading} does not decrease degree-lex order")

    def first_step(self, word: str, position: int) -> Polynomial:
        pair = word[position:position+2]
        require(pair in self.rules, "First step is not an available reduction")
        return {word[:position]+replacement+word[position+2:]: coefficient
                for replacement, coefficient in self.rules[pair].items()}

    @lru_cache(None)
    def normal_word(self, word: str) -> Polynomial:
        for position in range(len(word)-1):
            if word[position:position+2] in self.rules:
                return self.reduce(self.first_step(word, position))
        return {word: sp.S.One}

    def reduce(self, poly: Polynomial) -> Polynomial:
        result = defaultdict(lambda: sp.S.Zero)
        for word, coefficient in poly.items():
            for normal, value in self.normal_word(word).items():
                result[normal] += coefficient*value
        return clean(result)


def quadratic(active, matrix, linear, constant):
    vector = sp.Matrix(active)
    return sp.expand((vector.T*matrix*vector)[0]/2
                     + (linear.T*vector)[0] + constant)


def symmetrize(expression, active) -> Polynomial:
    result = defaultdict(lambda: sp.S.Zero)
    polynomial = sp.Poly(expression, *active)
    require(polynomial.total_degree() <= 2, "Active degree exceeds two")
    for exponents, coefficient in polynomial.terms():
        letters = "".join(letter*power for letter, power in zip("xyz", exponents))
        words = set(permutations(letters))
        for word in words:
            result["".join(word)] += coefficient/sp.Integer(len(words))
    return clean(result)


def defining_rules(expression, active, t) -> dict[str, Polynomial]:
    derivatives = [symmetrize(sp.diff(expression, coordinate), active)
                   for coordinate in active]
    return {
        "yx": add({"xy": sp.S.One}, scale(derivatives[2], -t)),
        "zx": add({"xz": sp.S.One}, scale(derivatives[1], t)),
        "zy": add({"yz": sp.S.One}, scale(derivatives[0], -t)),
    }


def substitute_words(poly: Polynomial, images: dict[str, Polynomial]) -> Polynomial:
    terms = []
    for word, coefficient in poly.items():
        term = {"": coefficient}
        for letter in word:
            term = multiply(term, images[letter])
        terms.append(term)
    return add(*terms)


def verify() -> dict:
    a11, a22, a33, a12, a13, a23, b1, b2, b3, c, t, *shifts = COEFFICIENTS
    active = sp.symbols("x y z")
    new_active = sp.symbols("X Y Z")
    A = sp.Matrix([[a11, a12, a13], [a12, a22, a23], [a13, a23, a33]])
    b, d = sp.Matrix([b1, b2, b3]), sp.Matrix(shifts)
    f = quadratic(active, A, b, c)
    rules = defining_rules(f, active, t)
    normalizer = Normalizer(rules)

    overlaps = sorted({left+right[-1] for left in rules for right in rules
                       if left[-1] == right[0]})
    require(overlaps == ["zyx"], "Unexpected overlap ambiguities")
    # The distinct leading words all have length two: no inclusion ambiguity.
    left_path = normalizer.reduce(normalizer.first_step("zyx", 0))
    right_path = normalizer.reduce(normalizer.first_step("zyx", 1))
    require_zero(add(left_path, scale(right_path, -1)), "zyx critical pair")
    require(left_path.get("xyz") == 1, "The overlap normal form lost its leading word")

    omega = symmetrize(f, active)
    omega_normal = normalizer.reduce(omega)
    commutators = {}
    for letter in "xyz":
        generator = {letter: sp.S.One}
        left = normalizer.reduce(multiply(omega, generator))
        right = normalizer.reduce(multiply(generator, omega))
        require(bool(left) and bool(right), f"Unexpected zero product for {letter}")
        residual = add(left, scale(right, -1))
        require_zero(residual, f"[Omega,{letter}]")
        # Also certify that every product coefficient belongs to QQ[parameters].
        serialize(left)
        serialize(right)
        commutators[letter] = {"residual": serialize(residual),
                               "equal_product_normal_form_word_count": len(left)}

    b_prime = b-A*d
    c_prime = sp.expand(c-(b.T*d)[0]+(d.T*A*d)[0]/2)
    f_prime = quadratic(new_active, A, b_prime, c_prime)
    substitution = dict(zip(active, (X-di for X, di in zip(new_active, shifts))))
    classical_residual = sp.Poly(
        sp.expand(f_prime-f.subs(substitution, simultaneous=True)),
        *(new_active+COEFFICIENTS), domain=sp.QQ,
    )
    require(classical_residual.is_zero, "Translated quadratic coefficient formula")

    images = {letter: {letter: sp.S.One, "": di}
              for letter, di in zip("xyz", shifts)}
    target_rules = defining_rules(f_prime, new_active, t)
    relation_residuals = {}
    for leading in rules:
        source_relation = add({leading: sp.S.One}, scale(rules[leading], -1))
        target_relation = add({leading: sp.S.One}, scale(target_rules[leading], -1))
        residual = add(substitute_words(target_relation, images),
                       scale(source_relation, -1))
        require_zero(residual, f"Translation of relation {leading}")
        relation_residuals[leading] = serialize(residual)

    image_omega_prime = substitute_words(symmetrize(f_prime, new_active), images)
    free_residual = add(image_omega_prime, scale(omega, -1))
    require_zero(free_residual, "Phi(sym(f'))=sym(f) in the free algebra")
    normal_residual = add(normalizer.reduce(image_omega_prime), scale(omega_normal, -1))
    require_zero(normal_residual, "Phi(sym(f'))=sym(f) in PBW normal form")

    return {
        "format_version": 1,
        "status": "PASS",
        "arithmetic": "Exact polynomial identities over QQ; no numerical specialization or t truncation.",
        "coefficient_ring": "QQ[a11,a22,a33,a12,a13,a23,b1,b2,b3,c,t]",
        "translation_ring": "R[d1,d2,d3], with all d_i independent and central",
        "potential": str(f),
        "normal_words": "x^i*y^j*z^k",
        "reduction_order": "degree-lex, z>y>x; every right-hand word strictly decreases",
        "rules": {word: serialize(poly) for word, poly in rules.items()},
        "ambiguities": {"overlap_words": overlaps, "inclusion_ambiguities": [],
                        "both_paths_agree": True, "zyx_common_normal_form": serialize(left_path)},
        "symmetrized_potential": serialize(omega),
        "omega_normal_form": serialize(omega_normal),
        "central_commutators": commutators,
        "translation": {
            "b_prime": [str(sp.expand(value)) for value in b_prime],
            "c_prime": str(c_prime),
            "f_prime_equals_f_of_X_minus_d": True,
            "map": "Phi(X_i)=x_i+d_i; Phi fixes R[d1,d2,d3]",
            "defining_relation_free_residuals": relation_residuals,
            "omega_free_residual": serialize(free_residual),
            "omega_PBW_residual": serialize(normal_residual),
        },
        "scope": [
            "All ten coefficients of an active-degree-at-most-two potential are independent; t is also independent.",
            "The unique overlap and all three central commutators vanish identically, without inverting any parameter.",
            "Central translation covariance holds with three independent shifts, already in the free algebra.",
            "For any m, substitute central linear forms in u for a_ij, quadratic forms for b_i, cubic forms for c, and linear forms for d_i. This is base change of universal identities, not sampling at a fixed m.",
        ],
        "limits": [
            "The Diamond lemma supplies the mathematical PBW conclusion from the checked terminating rules and overlap.",
            "Nonzero active cubics g=f(x,0) are outside this calculation.",
            "General linear/scalar coordinate covariance, smoothness and moduli descent are not checked here.",
        ],
        "sympy_version": sp.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print the complete JSON result.")
    parser.add_argument("--output", type=Path, help="Optionally write the complete JSON result.")
    args = parser.parse_args()
    result = verify()
    encoded = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)+"\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    if args.json:
        print(encoded, end="")
    else:
        print(f"SymPy {sp.__version__}; all parameters independent over QQ.")
        print("PASS degree-lex termination and both paths of the unique overlap zyx.")
        print("PASS all three commutators of Omega=sym_R(f), with no t truncation.")
        print("PASS central translation: coefficients, three relations, and Omega in free/PBW forms.")
        print("SCOPE: g=0; arbitrary m follows by central coefficient substitution.")
        print("LIMITS: no nonzero active cubic, general linear/scalar covariance, smoothness or moduli descent check.")
        print(f"SHA256: {result['script_sha256']}")
        if args.output is not None:
            print(f"JSON: {args.output}")


if __name__ == "__main__":
    main()
