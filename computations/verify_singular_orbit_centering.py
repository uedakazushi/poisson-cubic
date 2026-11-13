#!/usr/bin/env python3
"""Exact auxiliary checks for centering on two singular cubic orbits.

For each fixed active cubic g in QQ[x,y,z], use ten independent central
coefficients in f=g+q+l+c, where q and l are general homogeneous forms of
active degrees two and one.  The checked left inverses of
delta_g(v)=sum(v_i*partial_i(g)) are

  node: g=x^3+y^3+xyz,  sigma(q)=(q_xx/3,q_yy/3,q_xy);
  cusp: g=y^2*z-x^3,    sigma(q)=(-q_xx/3,q_yz/2,q_yy).

The action is f'(X)=lambda^(-1)*f(M^(-1)*(X-D)), with three independent
central shifts D.  For B=sigma(q) and f^0(x)=f(x-B), check sigma*delta=I,
stabilizer equivariance, B'=M*B-D, and
(f')^0(X)=lambda^(-1)*f^0(M^(-1)*X).  The node checks the scalar torus,
diag(zeta,zeta^(-1),1), and the x/y swap.  All zeta identities are reduced
modulo zeta^2+zeta+1 over QQ, without numerical roots of unity.  The cusp
uses M=diag(a,d,a^3*d^(-2)), lambda=a^(-3), with a,d independent units.
No lower coefficient or translation variable is numerically specialized.

For g=x^2*z-x*y^2 (a conic and its tangent line), also compute the torus
weights and the infinitesimal action -x*d/dy-2*y*d/dz.  Exact finite
linear systems show that no torus/unipotent-equivariant left inverse can
exist.  Finally, exact Groebner reductions certify that the gradients of
the two cubics g+u*z^2+u^3 have common zero only at the affine origin.

These are auxiliary symbolic checks, not a formal verification of the
manuscript.  The classification of full stabilizers, orbit transport to
general GL3 coordinates, regularity on an orbit, quantum central lifts,
and moduli descent remain mathematical arguments outside this script.
For any number of central variables, substitute central linear forms for
the six q coefficients and D, quadratic forms for the three l
coefficients, and a cubic for c.  This is base change of the checked
identities, not sampling at a fixed number of central variables.  A
general GL_m action is not separately checked.

Run: python3 computations/verify_singular_orbit_centering.py
     python3 computations/verify_singular_orbit_centering.py --json
Optional: --output build/verify_singular_orbit_centering.json
Dependency: sympy.  No files are written unless --output is supplied.
The generated JSON is reproducible build output, not a source certificate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


ACTIVE = sp.symbols("x y z")
NEW_ACTIVE = sp.symbols("X Y Z")
COEFFICIENTS = sp.symbols("qxx qxy qxz qyy qyz qzz lx ly lz c")
SHIFTS = sp.symbols("d1 d2 d3")
DIRECTIONS = sp.symbols("v1 v2 v3")
R, A, D, ZETA = sp.symbols("r a d zeta")
CYCLOTOMIC = sp.Poly(ZETA**2+ZETA+1, ZETA, domain=sp.EX)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def normal(expression: sp.Expr) -> sp.Expr:
    """Expand exactly, and reduce zeta using its irreducible QQ polynomial."""
    expression = sp.sympify(expression)
    require(not expression.has(sp.Float), "Floating-point input")
    expression = sp.expand(expression)
    if expression.has(ZETA):
        expression = sp.Poly(expression, ZETA, domain=sp.EX).rem(CYCLOTOMIC).as_expr()
    return sp.expand(expression)


def require_zero(expression: sp.Expr, label: str) -> None:
    residual = normal(expression)
    if residual != 0:
        raise AssertionError(f"{label}: nonzero residual {residual}")


def require_matrix_equal(actual: sp.Matrix, expected: sp.Matrix, label: str) -> None:
    require(actual.shape == expected.shape, f"{label}: matrix shapes differ")
    for i in range(actual.rows):
        for j in range(actual.cols):
            require_zero(actual[i, j]-expected[i, j], f"{label}[{i},{j}]")


def matrix_strings(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(normal(matrix[i, j])) for j in range(matrix.cols)]
            for i in range(matrix.rows)]


def substitute(expression, coordinates, images):
    # xreplace performs simultaneous replacement and does not substitute
    # inside replacement expressions, including x -> x-B.
    return expression.xreplace(dict(zip(coordinates, images)))


def quadratic_basis(coordinates):
    x, y, z = coordinates
    return (x**2, x*y, x*z, y**2, y*z, z**2)


def homogeneous_part(expression, coordinates, degree):
    return sum(coefficient*sp.prod(xi**power for xi, power in zip(coordinates, powers))
               for powers, coefficient in sp.Poly(expression, *coordinates).terms()
               if sum(powers) == degree)


def sigma(quadratic, coordinates, kind):
    x, y, z = coordinates
    polynomial = sp.Poly(quadratic, *coordinates)
    coefficient = polynomial.coeff_monomial
    if kind == "node":
        return sp.Matrix([coefficient(x**2)/3, coefficient(y**2)/3, coefficient(x*y)])
    if kind == "cusp":
        return sp.Matrix([-coefficient(x**2)/3, coefficient(y*z)/2, coefficient(y**2)])
    raise ValueError(f"Unknown cubic kind: {kind}")


def require_coefficient_ring(expression, label):
    """No parameter denominators except powers of the torus coordinates."""
    numerator, denominator = sp.fraction(sp.together(expression))
    symbols = ACTIVE+NEW_ACTIVE+COEFFICIENTS+SHIFTS+DIRECTIONS+(R, A, D, ZETA)
    sp.Poly(numerator, *symbols, domain=sp.QQ)
    denominator_poly = sp.Poly(denominator, R, A, D, domain=sp.QQ)
    require(len(denominator_poly.terms()) == 1,
            f"{label}: denominator is not a Laurent monomial in r,a,d")


def verify_centering(kind, cubic, cases):
    q = sum(coefficient*monomial for coefficient, monomial
            in zip(COEFFICIENTS[:6], quadratic_basis(ACTIVE)))
    linear = sum(coefficient*xi for coefficient, xi in zip(COEFFICIENTS[6:9], ACTIVE))
    f = cubic+q+linear+COEFFICIENTS[9]
    sp.Poly(f, *(ACTIVE+COEFFICIENTS), domain=sp.QQ)
    require(set(COEFFICIENTS).issubset(f.free_symbols), "A lower coefficient is missing")
    direction = sp.Matrix(DIRECTIONS)
    delta = sum(vi*sp.diff(cubic, xi) for vi, xi in zip(direction, ACTIVE))
    require_matrix_equal(sigma(delta, ACTIVE, kind), direction, f"{kind}: sigma*delta=I")

    B = sigma(q, ACTIVE, kind)
    f_zero = sp.expand(substitute(f, ACTIVE, sp.Matrix(ACTIVE)-B))
    require_matrix_equal(sigma(homogeneous_part(f_zero, ACTIVE, 2), ACTIVE, kind),
                         sp.zeros(3, 1), f"{kind}: centered quadratic")
    results = []
    for name, matrix, inverse, scale in cases:
        require_matrix_equal(matrix*inverse, sp.eye(3), f"{kind}/{name}: inverse")
        require_zero(substitute(cubic, ACTIVE, inverse*sp.Matrix(NEW_ACTIVE))/scale
                     - substitute(cubic, ACTIVE, NEW_ACTIVE), f"{kind}/{name}: stabilizer")
        transformed_q = normal(substitute(q, ACTIVE, inverse*sp.Matrix(NEW_ACTIVE))/scale)
        require_matrix_equal(sigma(transformed_q, NEW_ACTIVE, kind), matrix*B,
                             f"{kind}/{name}: sigma equivariance")

        old_coordinates = inverse*(sp.Matrix(NEW_ACTIVE)-sp.Matrix(SHIFTS))
        f_prime_expression = substitute(f, ACTIVE, old_coordinates)/scale
        f_prime = normal(f_prime_expression)
        require_coefficient_ring(f_prime, f"{kind}/{name}: transformed coefficients")
        q_prime = homogeneous_part(f_prime, NEW_ACTIVE, 2)
        B_prime = sigma(q_prime, NEW_ACTIVE, kind).applyfunc(normal)
        require_matrix_equal(B_prime, matrix*B-sp.Matrix(SHIFTS),
                             f"{kind}/{name}: B'=MB-D")

        # Substitute the extracted B_prime into the actual transformed f.
        # Retaining its unexpanded expression avoids a needless expansion
        # before the cancellation of independent translation variables.
        f_prime_zero = normal(substitute(f_prime_expression, NEW_ACTIVE,
                                        sp.Matrix(NEW_ACTIVE)-B_prime))
        expected_zero = normal(substitute(f_zero, ACTIVE,
                                          inverse*sp.Matrix(NEW_ACTIVE))/scale)
        require_zero(f_prime_zero-expected_zero, f"{kind}/{name}: centered covariance")
        require_matrix_equal(sigma(homogeneous_part(f_prime_zero, NEW_ACTIVE, 2),
                                   NEW_ACTIVE, kind), sp.zeros(3, 1),
                             f"{kind}/{name}: transformed centered quadratic")
        require_coefficient_ring(f_prime_zero, f"{kind}/{name}: centered coefficients")
        results.append({
            "name": name,
            "M": matrix_strings(matrix),
            "M_inverse": matrix_strings(inverse),
            "lambda": str(scale),
            "stabilizes_g": True,
            "sigma_stabilizer_covariance": True,
            "B_prime": [str(value) for value in B_prime],
            "B_prime_minus_MB_plus_D": ["0", "0", "0"],
            "centered_potential_covariance_residual": "0",
            "centered_quadratic_sigma": ["0", "0", "0"],
            "coefficient_denominators": "Only numerical constants and Laurent monomials in torus coordinates.",
        })
    return {
        "g": str(cubic),
        "f": str(f),
        "delta_g_of_v": str(delta),
        "sigma_delta_is_identity": True,
        "B": [str(value) for value in B],
        "centered_quadratic_sigma": ["0", "0", "0"],
        "stabilizer_cases": results,
    }


def polynomial_columns(polynomials, basis):
    return sp.Matrix.hstack(*(sp.Matrix([sp.Poly(poly, *ACTIVE).coeff_monomial(monomial)
                                         for monomial in basis]) for poly in polynomials))


def linear_system(expressions, unknowns):
    equations = [sp.expand(value) for value in expressions if sp.expand(value) != 0]
    matrix, right = sp.linear_eq_to_matrix(equations, unknowns)
    return equations, matrix, right


def verify_tangent_obstruction():
    x, y, z = ACTIVE
    s, tau = sp.symbols("s tau")
    g = x**2*z-x*y**2
    basis = quadratic_basis(ACTIVE)
    torus = sp.diag(s, 1, 1/s)
    torus_inverse = sp.diag(1/s, 1, s)
    # lambda^(-1)=s for this stabilizer torus.
    require_zero(s*substitute(g, ACTIVE, torus_inverse*sp.Matrix(ACTIVE))-g,
                 "tangent: torus stabilizer")
    weights = []
    for monomial in basis:
        transformed = s*substitute(monomial, ACTIVE, torus_inverse*sp.Matrix(ACTIVE))
        factor = sp.cancel(transformed/monomial)
        weight = factor.as_powers_dict().get(s, sp.S.Zero)
        require_zero(factor-s**weight, "tangent: quadratic torus character")
        weights.append(int(weight))
    require(weights == [-1, 0, 1, 1, 2, 3], "Unexpected quadratic torus weights")
    direction_weights = [1, 0, -1]
    require_matrix_equal(torus, sp.diag(*(s**weight for weight in direction_weights)),
                         "tangent: direction torus weights")

    unipotent = sp.Matrix([[1, 0, 0], [tau, 1, 0], [tau**2, 2*tau, 1]])
    unipotent_inverse = unipotent.xreplace({tau: -tau})
    require_matrix_equal(unipotent*unipotent_inverse, sp.eye(3), "tangent: unipotent inverse")
    require_zero(substitute(g, ACTIVE, unipotent*sp.Matrix(ACTIVE))-g,
                 "tangent: unipotent stabilizer")
    direction_operator = unipotent.diff(tau).subs(tau, 0)

    def differential(poly):
        return sp.expand(-x*sp.diff(poly, y)-2*y*sp.diff(poly, z))

    images = [differential(monomial) for monomial in basis]
    for monomial, derivative in zip(basis, images):
        differentiated_action = sp.diff(substitute(monomial, ACTIVE,
                                                   unipotent_inverse*sp.Matrix(ACTIVE)), tau).subs(tau, 0)
        require_zero(differentiated_action-derivative, "tangent: infinitesimal sign")
    quadratic_operator = polynomial_columns(images, basis)
    delta = polynomial_columns([sp.diff(g, xi) for xi in ACTIVE], basis)
    require_matrix_equal(quadratic_operator*delta, delta*direction_operator,
                         "tangent: delta intertwines the infinitesimal actions")

    full_unknowns = sp.symbols("s0:18")
    full_sigma = sp.Matrix(3, 6, full_unknowns)
    torus_equations = full_sigma*sp.diag(*weights)-sp.diag(*direction_weights)*full_sigma
    _, torus_matrix, _ = linear_system(list(torus_equations), full_unknowns)
    require(torus_matrix.rank() == 14, "Torus-equivariant maps should have dimension four")
    full_equations, full_matrix, full_right = linear_system(
        list(torus_equations)+list(full_sigma*delta-sp.eye(3))
        + list(full_sigma*quadratic_operator-direction_operator*full_sigma), full_unknowns)
    full_rank = full_matrix.rank()
    full_augmented_rank = full_matrix.row_join(full_right).rank()
    require((full_rank, full_augmented_rank) == (18, 19),
            "The full equivariant-left-inverse system must be inconsistent")

    # Independently construct all maps allowed by the torus weights, then
    # impose the left-inverse and unipotent equations on these four entries.
    allowed = [(i, j) for i in range(3) for j in range(6)
               if direction_weights[i] == weights[j]]
    require(allowed == [(0, 2), (0, 3), (1, 1), (2, 0)], "Unexpected torus weight matches")
    restricted_unknowns = sp.symbols("alpha beta gamma epsilon")
    restricted_sigma = sp.zeros(3, 6)
    for entry, unknown in zip(allowed, restricted_unknowns):
        restricted_sigma[entry] = unknown
    equations, matrix, right = linear_system(
        list(restricted_sigma*delta-sp.eye(3))
        + list(restricted_sigma*quadratic_operator-direction_operator*restricted_sigma),
        restricted_unknowns)
    rank = matrix.rank()
    augmented_rank = matrix.row_join(right).rank()
    require((rank, augmented_rank) == (4, 5), "The four-variable system must be inconsistent")
    rref, _ = matrix.row_join(right).rref()
    require(any(all(rref[i, j] == 0 for j in range(4)) and rref[i, 4] == 1
                for i in range(rref.rows)), "Missing exact inconsistent RREF row")

    require_zero(differential(y*z)+x*z+2*y**2, "tangent: first short obstruction identity")
    require_zero(differential(x*z+2*y**2)+6*x*y, "tangent: second short obstruction identity")
    return {
        "g": str(g),
        "quadratic_basis": [str(value) for value in basis],
        "torus_M": matrix_strings(torus),
        "torus_lambda": "s**(-1)",
        "quadratic_weight_exponents": weights,
        "direction_weight_exponents": direction_weights,
        "unipotent_M": matrix_strings(unipotent),
        "polynomial_infinitesimal_operator": "-x*d/dy-2*y*d/dz",
        "quadratic_operator_matrix": matrix_strings(quadratic_operator),
        "direction_operator_matrix": matrix_strings(direction_operator),
        "delta_matrix": matrix_strings(delta),
        "full_system": {
            "unknown_count": len(full_unknowns),
            "equation_count": len(full_equations),
            "coefficient_rank": full_rank,
            "augmented_rank": full_augmented_rank,
        },
        "torus_restricted_system": {
            "unknowns": [str(value) for value in restricted_unknowns],
            "sigma_matrix": matrix_strings(restricted_sigma),
            "equations_equal_to_zero": [str(value) for value in equations],
            "coefficient_matrix": matrix_strings(matrix),
            "right_hand_side": [str(value) for value in right],
            "coefficient_rank": rank,
            "augmented_rank": augmented_rank,
            "inconsistent_augmented_RREF_row": [0, 0, 0, 0, 1],
        },
        "equivariant_left_inverse_exists": False,
        "scope": "This torus and unipotent subgroup already obstruct a left inverse; no full stabilizer classification is needed or checked.",
    }


def verify_smooth_examples(cubics):
    x, y, z = ACTIVE
    u = sp.Symbol("u")
    variables = ACTIVE+(u,)
    results = []
    for name, g in cubics:
        f = g+u*z**2+u**3
        gradients = [sp.diff(f, variable) for variable in variables]
        require(all(poly.subs(dict.fromkeys(variables, 0)) == 0 for poly in gradients),
                f"{name}: the affine origin should be a common gradient zero")
        groebner = sp.groebner(gradients, *variables, order="lex", domain=sp.QQ)
        powers = {}
        for variable in variables:
            for exponent in range(1, 9):
                quotients, remainder = groebner.reduce(variable**exponent)
                if remainder == 0:
                    require_zero(variable**exponent-sum(coefficient*polynomial.as_expr()
                                 for coefficient, polynomial in zip(quotients, groebner.polys)),
                                 f"{name}: exact pure-power reduction reconstruction")
                    powers[str(variable)] = {"exponent": exponent, "remainder": "0"}
                    break
            else:
                raise AssertionError(f"{name}: no certified pure power for {variable}")
        results.append({
            "name": name,
            "f": str(f),
            "coefficient_field": "QQ",
            "gradient_generators": [str(value) for value in gradients],
            "groebner_order": "lex: x,y,z,u",
            "groebner_basis": [str(poly.as_expr()) for poly in groebner.polys],
            "pure_powers_in_gradient_ideal": powers,
            "gradient_common_zero_set": "Only the affine origin, over every extension of QQ.",
            "interpretation": "Pure-power ideal membership forces every coordinate to vanish; the homogeneous Jacobian criterion gives a smooth projective cubic surface.",
        })
    return results


def verify() -> dict:
    x, y, z = ACTIVE
    node = x**3+y**3+x*y*z
    cusp = y**2*z-x**3
    swap = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    node_cases = [
        ("scalar torus", R*sp.eye(3), sp.eye(3)/R, R**-3),
        ("order-three diagonal", sp.diag(ZETA, ZETA**2, 1),
         sp.diag(ZETA**2, ZETA, 1), sp.S.One),
        ("x/y swap", swap, swap, sp.S.One),
    ]
    cusp_cases = [
        ("two-dimensional diagonal torus", sp.diag(A, D, A**3/D**2),
         sp.diag(1/A, 1/D, D**2/A**3), A**-3),
    ]
    node_result = verify_centering("node", node, node_cases)
    cusp_result = verify_centering("cusp", cusp, cusp_cases)
    obstruction = verify_tangent_obstruction()
    smooth_examples = verify_smooth_examples([("node extension", node), ("cusp extension", cusp)])
    return {
        "format_version": 1,
        "status": "PASS",
        "arithmetic": "Exact identities over QQ with Laurent torus coordinates; zeta reduced modulo zeta**2+zeta+1.",
        "lower_coefficient_ring": "QQ[qxx,qxy,qxz,qyy,qyz,qzz,lx,ly,lz,c]",
        "independent_translation_variables": [str(value) for value in SHIFTS],
        "cyclotomic_relation": "zeta**2+zeta+1=0 (hence zeta**3=1 and zeta != 1 in characteristic zero)",
        "coordinate_convention": "X=M*x+D; f'(X)=lambda**(-1)*f(M**(-1)*(X-D))",
        "centering_convention": "B=sigma(q); f^0(x)=f(x-B)",
        "node": node_result,
        "cusp": cusp_result,
        "tangent_conic_line_obstruction": obstruction,
        "smooth_projective_examples": smooth_examples,
        "scope": [
            "For each fixed node/cusp normal form, all ten lower coefficients and all three shifts are independent.",
            "The node scalar torus and the two displayed finite generators are checked; the cusp torus uses arbitrary independent nonzero a,d.",
            "The tangent conic-line obstruction is an exact finite rational linear system, with all torus-allowed maps included.",
            "The two smooth examples have exact pure-power membership certificates in their gradient ideals.",
            "For any number of central variables, homogeneous central coefficient substitution gives the corresponding centering identities by base change.",
        ],
        "limits": [
            "Full stabilizer classification, orbit transport under general GL3, and regularity of the transported map are not established by this computation.",
            "General GL_m covariance is not separately tested; coefficient base change must not be called a matrix-by-matrix GL_m test.",
            "No quantum central element, PBW claim, general smoothness theorem or moduli descent theorem is checked.",
            "This is auxiliary exact symbolic verification, not a formal proof checked by a proof assistant.",
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
        print(f"SymPy {sp.__version__}; exact QQ/cyclotomic/Laurent identities.")
        print("PASS node and cusp: sigma*delta=I and displayed stabilizer equivariance.")
        print("PASS all ten lower coefficients and independent D: B'=MB-D and centered covariance.")
        print("PASS tangent conic-line obstruction: coefficient rank 4, augmented rank 5.")
        print("PASS both smooth examples: positive powers of all four variables lie in the gradient ideal.")
        print("LIMITS: no full stabilizer classification, general orbit transport, quantum central lift or moduli descent check.")
        print(f"SHA256: {result['script_sha256']}")
        if args.output is not None:
            print(f"JSON: {args.output}")


if __name__ == "__main__":
    main()
