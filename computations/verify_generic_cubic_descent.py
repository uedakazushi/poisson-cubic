#!/usr/bin/env python3
"""Exact Q(t) tests of the field-model extraction step (not an nc-category test).

The input is a known geometric gradient space in a non-gradient basis.
The computation recovers the integrability space, selects a rational invertible
matrix, and integrates it.  Smoothness of each input over Q(t) follows from its
Fermat specialization at t=0.  No categorical equivalence, (L), or (CF) is tested.
"""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import sympy as sp


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
    kernel = linear.nullspace()
    assert kernel
    matrices = [sp.Matrix(n, n, list(v)) for v in kernel]
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
        'integrability_dimension': len(kernel),
        'chosen_matrix_determinant': str(determinant),
        'gradient_identities': n, 'all_gradient_identities_zero': True,
        'smoothness_input': 'Fermat specialization at t=0; generic smoothness',
        'recovered_model': str(sp.factor(model)),
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
