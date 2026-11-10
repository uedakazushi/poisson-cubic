#!/usr/bin/env python3
"""Exact algebra checks for the explicit model comparison section.

These checks do not prove equivalence of dg categories or relative smoothness.
Run from any directory; the default certificate is next to this script.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).with_name("explicit_model_comparison_certificate.json"),
    )
    args = parser.parse_args()
    h, t, x, y, z, u, v = sp.symbols("h t x y z u v")
    variables = (x, y, z)
    monomials = [
        x**3, x**2*y, x**2*z, x*y**2, x*y*z,
        x*z**2, y**3, y**2*z, y*z**2, z**3,
    ]
    cubic_coefficients = sp.symbols("c0:10")
    general_f = sum(c*m for c, m in zip(cubic_coefficients, monomials))
    K = sp.Matrix([[0, -z, y], [z, 0, -x], [-y, x, 0]])
    H = sp.hessian(general_f, variables)
    general_hessian = sp.expand(H.det())
    general_matrix = K-h*H/2
    general_det = sp.expand(general_matrix.det())
    assert sp.expand(general_det+3*h*general_f+h**3*general_hessian/8) == 0
    vv = sp.Matrix(variables)
    assert K.adjugate() == vv*vv.T
    assert sp.expand((vv.T*H*vv)[0]-6*general_f) == 0
    alpha, beta, gamma = 1-h*t/2, -1-h*t/2, -h
    b = 1-h**2*t**2/4
    a = t+h**2*(1+t**3/4)/3
    theta = a/b
    U = 1+h**2*t**2/2+h**4*t/6-h**4*t**4/48
    W = (4-h**2*t**2)*(12*t+h**2*(t**3-8))/48
    S3 = x**3+y**3+z**3
    M = sp.Matrix([
        [gamma*x, beta*z, alpha*y],
        [alpha*z, gamma*y, beta*x],
        [beta*y, alpha*x, gamma*z],
    ])
    det_expression = sp.expand(-M.det())
    assert sp.expand(det_expression - 3*h*(b*S3/3+a*x*y*z)) == 0

    rec_second = sp.factor(sp.diff(theta, h, 2).subs(h, 0)/2)
    sym_second = sp.factor(sp.diff(W/U, h, 2).subs(h, 0)/2)
    assert sp.expand(rec_second-(1+t**3)/3) == 0
    assert sp.expand(sym_second+2*(1+t**3)/3) == 0
    assert sp.expand(rec_second-sym_second-(1+t**3)) == 0

    f = S3/3+t*x*y*z
    hesse_hessian = sp.expand(sp.hessian(f, variables).det())
    assert sp.expand(hesse_hessian-(2*(t**3+4)*x*y*z-2*t**2*S3)) == 0
    assert sp.expand(f+h**2*hesse_hessian/24-(b*S3/3+a*x*y*z)) == 0
    columns = [sp.expand(vv*sp.diff(f, w)) for w in variables for vv in variables]
    columns.append(x*y*z)
    coeff_matrix = sp.Matrix([
        [sp.Poly(c, *variables).coeff_monomial(m) for c in columns]
        for m in monomials
    ])
    jacobian_minor = sp.factor(coeff_matrix.det())
    assert sp.expand(jacobian_minor+(1+t**3)**2) == 0

    F0 = S3/3+u**3+v**3
    F_rec = F0+h**2*x*y*z/3
    F_sym = F0-2*h**2*x*y*z/3
    assert sp.expand(F_rec-F_sym-h**2*x*y*z) == 0
    G = sp.groebner([sp.diff(F0, w) for w in (x, y, z, u, v)], x, y, z, u, v)
    fermat_remainder = G.reduce(x*y*z)[1]
    assert fermat_remainder == x*y*z

    singular_point = {x: 1, y: 0, z: 0}
    mixing = {}
    for name, f_block in (("node", y**3+z**3+x*y*z), ("cusp", x*z**2+y**3)):
        values = [sp.diff(f_block, w).subs(singular_point) for w in variables]
        assert values == [0, 0, 0]
        assert (x**2).subs(singular_point) == 1
        mixing[name] = {"gradient_at_1_0_0": [int(q) for q in values], "x_squared": 1}

    certificate = {
        "date": "2026-11-10",
        "version": 2,
        "arithmetic": "exact rational functions over QQ",
        "sympy_version": sp.__version__,
        "claims_checked": {
            "general_ternary_cubic_coefficients": [str(c) for c in cubic_coefficients],
            "general_hessian_identity": True,
            "general_hessian_identity_statement": "det(K-h*HessMatrix(f)/2) = -3*h*(f+h**2*det(HessMatrix(f))/24)",
            "cross_product_adjugate_identity": True,
            "cubic_euler_hessian_identity": True,
            "hesse_hessian": str(hesse_hessian),
            "hessian_candidate_equals_b_times_f_theta": True,
            "multilinear_determinant_identity": True,
            "point_parameter": str(theta),
            "reconstruction_second_coefficient": str(rec_second),
            "symmetrized_center_second_coefficient_after_block_scaling": str(sym_second),
            "difference_in_jacobian_ring": "(1+t**3)*x*y*z",
            "jacobian_degree_three_matrix_shape": list(coeff_matrix.shape),
            "jacobian_augmented_determinant": str(jacobian_minor),
            "smooth_parameter_condition": "1+t**3 != 0",
            "fermat_jacobian_remainder": str(fermat_remainder),
            "essential_mixing": mixing,
        },
        "scope": {
            "hessian_formula_known_reference": "Mori-Smith, arXiv:1502.07403v2, Lemma 7.1 and Theorem 7.2, pp.23-25",
            "category_equivalence_proved_by_script": False,
            "relative_smoothness_proved_by_script": False,
            "general_mixed_reconstruction_proved_by_script": False,
            "existence_input": "papers/sections/elliptic_reconstruction.tex, er:thm:main",
            "proof_source": "papers/reconstruction/explicit_model_comparison.tex",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"status": "passed", "certificate": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
