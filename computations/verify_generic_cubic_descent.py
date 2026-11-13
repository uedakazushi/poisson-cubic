#!/usr/bin/env python3
"""Exact Q(t) tests of the field-model extraction step (not an nc-category test).

The input is a known geometric gradient space in a non-gradient basis.
The computation recovers the integrability space, selects a rational invertible
matrix, and integrates it.  The first three inputs are smooth by Fermat
specialization at t=0.  A fourth calculation checks a nonsplit symmetrizer
algebra, using a cubic that is smooth at t=1.  No categorical equivalence,
(L), or (CF) is tested.
"""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import sympy as sp


def integrability_kernel(q: sp.Matrix, x: tuple) -> tuple:
    n = len(x)
    unknowns = sp.symbols(f'a0:{n*n}')
    a = sp.Matrix(n, n, unknowns)
    g = a*q
    equations = []
    for i in range(n):
        for j in range(i+1, n):
            difference = sp.expand(sp.diff(g[i], x[j])-sp.diff(g[j], x[i]))
            equations.extend(sp.Poly(difference, *x).coeffs())
    linear, rhs = sp.linear_eq_to_matrix(equations, unknowns)
    assert rhs == sp.zeros(rhs.rows, 1)
    matrices = [sp.Matrix(n, n, list(v)) for v in linear.nullspace()]
    assert matrices
    return linear, matrices


def recover(n: int, mixed: bool) -> dict:
    t = sp.Symbol('t')
    x = sp.symbols(f'x0:{n}')
    f = sum(z**3 for z in x)
    if mixed:
        f += t * sum(x[i]**2 * x[(i + 1) % n] for i in range(n))
    gradient = sp.Matrix([sp.diff(f, z) for z in x])
    m = sp.eye(n)
    for i in range(n-1):
        m[i, i+1] = t + i + 1
    assert m.det() == 1
    q = m * gradient
    linear, matrices = integrability_kernel(q, x)
    # Usually the sum works. The finite grid is a guaranteed exact fallback.
    chosen = sum(matrices, sp.zeros(n))
    determinant = sp.factor(chosen.det())
    if determinant == 0:
        for point in itertools.product(range(n+1), repeat=len(matrices)):
            chosen = sum((c*b for c, b in zip(point, matrices)), sp.zeros(n))
            determinant = sp.factor(chosen.det())
            if determinant != 0:
                break
        else:
            raise AssertionError('No invertible integrability matrix found')
    recovered_gradient = chosen*q
    model = sp.cancel(sum(x[i]*recovered_gradient[i] for i in range(n))/3)
    for i in range(n):
        assert sp.cancel(sp.diff(model, x[i])-recovered_gradient[i]) == 0
    assert sp.cancel(chosen.det()) != 0
    assert sp.expand(f.subs(t, 0)-sum(z**3 for z in x)) == 0
    return {
        'variables': n, 'mixed': mixed, 'field': 'Q(t)',
        'linear_system_shape': list(linear.shape),
        'integrability_dimension': len(matrices),
        'chosen_matrix_determinant': str(determinant),
        'gradient_identities': n, 'all_gradient_identities_zero': True,
        'smoothness_input': 'Fermat specialization at t=0; generic smoothness',
        'recovered_model': str(sp.factor(model)),
    }


def nonsplit_symmetrizer() -> dict:
    """Check E_F = Q(t)[u]/(u^2-t) x Q(t)^3, including its cubic action."""
    t = sp.Symbol('t')
    x = sp.symbols('x0:5')
    f = x[0]**3 + 3*t*x[0]*x[1]**2 + sum(z**3 for z in x[2:])
    gradient = sp.Matrix([sp.diff(f, z) for z in x])
    _, matrices = integrability_kernel(gradient, x)
    # Integrable gradient matrices are transposes of one-slot symmetrizers.
    computed = [a.T for a in matrices]
    e = sp.diag(1, 1, 0, 0, 0)
    u = sp.zeros(5)
    u[0, 1], u[1, 0] = t, 1
    expected = [e, u]
    for i in range(2, 5):
        p = sp.zeros(5)
        p[i, i] = 1
        expected.append(p)
    flatten = lambda a: sp.Matrix(list(a))
    span = sp.Matrix.hstack(*(flatten(a) for a in expected))
    assert len(computed) == span.rank() == 5
    assert sp.Matrix.hstack(span, *(flatten(a) for a in computed)).rank() == 5
    assert u*u == t*e and e*e == e and e*u == u*e == u
    for i, p in enumerate(expected[2:]):
        assert p*p == p and p*u == u*p == sp.zeros(5)
        assert p*e == e*p == sp.zeros(5)
        for q in expected[2+i+1:]:
            assert p*q == q*p == sp.zeros(5)
    assert sp.factor(4*t) != 0

    # At t=1 the binary summand is ((x0+x1)^3+(x0-x1)^3)/2.
    fermat_binary = ((x[0]+x[1])**3 + (x[0]-x[1])**3)/2
    assert sp.expand(f.subs(t, 1)-fermat_binary-sum(z**3 for z in x[2:])) == 0
    v = sp.Matrix(x)
    one_slot = lambda a: sp.expand((gradient.T*a*v)[0]/3)
    a, b = sp.eye(5)+2*u, sp.eye(5)+u
    assert sp.factor(a.det()) == 1-4*t
    assert sp.factor(b.det()) == 1-t
    fa = one_slot(a)
    assert all(sp.expand(sp.diff(fa, x[i])-(a.T*gradient)[i]) == 0 for i in range(5))
    substituted = fa.subs(dict(zip(x, list(b*v))), simultaneous=True)
    assert sp.expand(substituted-one_slot(a*b**3)) == 0
    return {
        'field': 'Q(t)', 'variables': 5, 'polynomial': str(f),
        'integrability_dimension': 5,
        'symmetrizer_algebra': 'Q(t)[u]/(u^2-t) x Q(t)^3',
        'quadratic_discriminant': '4*t',
        'nonsplit_reason': 'The t-adic valuation of t is 1, so t is not a square in Q(t).',
        'smoothness_input': 'At t=1, the binary summand is a sum of two independent cubes.',
        'geometric_ST_blocks': 5, 'matrix_span_and_multiplication_verified': True,
        'one_slot_gradient_identities': 5,
        'cubic_action_identity_Fa_bx_equals_Fab3': True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    examples = [recover(5, False), recover(5, True), recover(6, True)]
    assert examples[0]['integrability_dimension'] == 5
    assert examples[1]['integrability_dimension'] == 1
    assert examples[2]['integrability_dimension'] == 1
    result = {
        'scope': 'Exact commutative linear algebra over Q(t); no nc natural transformations computed.',
        'examples': examples,
        'nonsplit_symmetrizer': nonsplit_symmetrizer(),
        'generation_bounds': {str(n): 2*(n+2)*(n+3)-1 for n in range(3, 11)},
        'not_tested': ['BFK theorem', 'categorical (L)/(CF)', 'equivalence kernel', 'finite extension degree'],
    }
    text = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
