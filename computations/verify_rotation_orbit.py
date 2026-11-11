#!/usr/bin/env python3
"""Verify the special-fiber Koszul/Euler ingredients of the generic orbit argument.

Exact polynomial MF identities in the five-variable mixed cubic are checked.
This does NOT construct the formal functor, prove thick classification, or
compute a generic equivalence kernel/finite extension. Those are theorem inputs
and mathematical arguments in the manuscript.
"""
from __future__ import annotations
import argparse
import json
from math import comb
from pathlib import Path
import sympy as s


def exterior_operators(n: int) -> tuple[list[s.SparseMatrix], list[s.SparseMatrix]]:
    size = 1 << n
    wedges, contractions = [], []
    for i in range(n):
        w, c = {}, {}
        for mask in range(size):
            sign = (-1) ** ((mask & ((1 << i) - 1)).bit_count())
            if mask & (1 << i):
                c[(mask ^ (1 << i), mask)] = sign
            else:
                w[(mask | (1 << i), mask)] = sign
        wedges.append(s.SparseMatrix(size, size, w))
        contractions.append(s.SparseMatrix(size, size, c))
    return wedges, contractions


def assert_zero(matrix: s.MatrixBase) -> None:
    for value in matrix.todok().values():
        if s.expand(value) != 0:
            raise AssertionError(f"Nonzero polynomial identity: {s.expand(value)}")


def euler(n: int, r: int) -> int:
    return sum((-1) ** k * comb(n, k) for k in range(n + 1) if (k + r) % 3 == 0)


def check_special_mf() -> dict:
    x, y, z, u, v, t = s.symbols('x y z u v t')
    variables = (x, y, z, u, v)
    f = (x**3 + y**3 + z**3) / 3 + u**3 + v**3 + u*x*y
    fi = [s.diff(f, q)/3 for q in variables]
    a = s.Matrix(5, 5, lambda i, j: s.diff(fi[i], variables[j])/2)
    assert s.expand(sum(variables[i]*fi[i] for i in range(5)) - f) == 0
    for i in range(5):
        assert s.expand(sum(variables[j]*a[i, j] for j in range(5)) - fi[i]) == 0
    w, c = exterior_operators(5)
    zero, identity = s.zeros(32), s.eye(32)
    q = sum((variables[i]*c[i] + t*fi[i]*w[i] for i in range(5)), zero)
    xi = [c[i] - t*sum((a[i, j]*w[j] for j in range(5)), zero) for i in range(5)]
    count = 0
    assert_zero(q*q - t*f*identity)
    count += 1
    for i in range(5):
        assert_zero(q*w[i] + w[i]*q - variables[i]*identity)
        assert_zero(q*xi[i] + xi[i]*q)
        count += 2
        for j in range(5):
            assert_zero(xi[i]*xi[j] + xi[j]*xi[i] + t*(a[i,j]+a[j,i])*identity)
            count += 1
    # Residue of the cocycle generators is exterior, not an asserted all-order model.
    for i in range(5):
        assert_zero(xi[i].subs({x:0,y:0,z:0,u:0,v:0}) - c[i])
        count += 1
    classes = {}
    for r in range(3):
        terms = []
        for k in range(6):
            if (k+r) % 3 == 0:
                tj = -(k+r)//3
                degree = k + 2*tj
                assert -k - 3*tj == r
                terms.append({'exterior_degree': k, 't_power': tj,
                              'cohomological_degree': degree, 'multiplicity': comb(5,k)})
        assert sum((-1)**term['cohomological_degree']*term['multiplicity'] for term in terms) == euler(5,r)
        classes[str(r)] = terms
    return {'polynomial':str(f), 'underlying_exterior_rank':32,
            'matrix_identities_checked':count, 'Euler_vector':[-9,9,0],
            'graded_cohomology_terms':classes, 'periodic_variable_retained':True}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('build/rotation_orbit_certificate.json'))
    args = parser.parse_args()
    samples = []
    for n in range(1,65):
        vector = [euler(n,r) for r in range(3)]
        assert sum(vector)==0
        assert sum(a*a for a in vector)==2*3**(n-1)
        assert vector != [0,0,0]
        if 5 <= n <= 10:
            samples.append({'N':n, 'Euler_vector':vector})
    assert euler(9,0)==0
    result = {'version':'nc-cubic-v35', 'date':'2026-11-11',
              'scope':'Exact special cubic MF and Euler identities; no generic kernel computation.',
              'Euler_N_checked':[1,64], 'Euler_samples':samples,
              'five_variable_special_MF':check_special_mf(),
              'not_verified':['Stevenson thick-subcategory theorem or regrading/compact-generation proof.',
                              'Existing local/window input L and completed formal functor CF.',
                              'All prior noncommutative diagonal matrices and input D.',
                              'Explicit generic inverse kernel, cell bound, or extension degree.']}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS 64 Euler vectors and 41 exact 32-by-32 polynomial matrix identities.')


if __name__=='__main__':
    main()
