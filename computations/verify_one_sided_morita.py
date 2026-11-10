#!/usr/bin/env python3
"""Finite identity checks for the one-sided Morita criterion.

These are ordinary matrix-algebra tests and a scalar-period calculation.
They do NOT construct the compact formal kernel of the nc cubic family,
verify the general dg proofs, or prove Popescu approximation computationally.
"""
from __future__ import annotations
import argparse
from itertools import product
import json
from pathlib import Path
import sympy as s


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path('build/one_sided_morita_certificate.json'))
    args = parser.parse_args()
    h = s.Symbol('h')
    T = s.Matrix([[1, h], [h, 1 + h**2]])
    Ti = s.Matrix([[1 + h**2, -h], [-h, 1]])
    rows = [s.eye(2)[i, :] for i in range(2)]
    cols = [s.eye(2)[:, i] for i in range(2)]
    matrices = [cols[i] * rows[j] for i, j in product(range(2), repeat=2)]
    counts = {}

    def check(name, lhs, rhs):
        difference = lhs - rhs
        if isinstance(difference, s.MatrixBase):
            good = all(s.expand(x) == 0 for x in difference)
        else:
            good = s.expand(difference) == 0
        if not good:
            raise AssertionError((name, difference))
        counts[name] = counts.get(name, 0) + 1

    # A has multiplication X*Y=XTY and unit T^{-1}; B=Q[h].
    check('invertible_twist', T * Ti, s.eye(2))
    check('invertible_twist', Ti * T, s.eye(2))
    for X, Y, Z in product(matrices, repeat=3):
        check('associativity', (X*T*Y)*T*Z, X*T*(Y*T*Z))
    for X in matrices:
        check('algebra_unit', Ti*T*X, X)
        check('algebra_unit', X*T*Ti, X)
    # P is the row module, Q the column module; P acts via pTX, Q via XTq.
    for p, X, Y in product(rows, matrices, matrices):
        check('right_module', (p*T*X)*T*Y, p*T*(X*T*Y))
    for X, Y, q in product(matrices, matrices, cols):
        check('left_module', (X*T*Y)*T*q, X*T*(Y*T*q))
    for p, X, q in product(rows, matrices, cols):
        check('balanced_pairing', (p*T*X*T*q)[0], (p*T*(X*T*q))[0])
    # Q tensor_B P -> A is q tensor p |-> qp.  Verify A-A-linearity.
    for X, q, p in product(matrices, cols, rows):
        check('evaluation_linearity', (X*T*q)*p, X*T*(q*p))
        check('evaluation_linearity', q*(p*T*X), (q*p)*T*X)
    evaluation = s.Matrix.hstack(*[s.Matrix(list(q*p)) for q, p in product(cols, rows)])
    check('evaluation_isomorphism', evaluation.det(), 1)
    for p, q, z in product(rows, cols, rows):
        check('triangle_rows', p*T*(q*z), (p*T*q)[0]*z)
    for q, p, z in product(cols, rows, cols):
        check('triangle_columns', (q*p)*T*z, q*(p*T*z)[0])
    check('unit_lift', (rows[0]*T*(Ti*cols[0]))[0], 1)

    def tensor_pq(p, q):
        return s.Matrix([p[i]*q[j] for i, j in product(range(2), repeat=2)])

    # Relations in P tensor_A Q: rank three, pairing identifies quotient with B.
    relations = s.Matrix.hstack(*[
        tensor_pq(p*T*X, q)-tensor_pq(p, X*T*q)
        for p, X, q in product(rows, matrices, cols)])
    pairing = s.Matrix([[T[i,j] for i,j in product(range(2), repeat=2)]])
    check('pairing_kills_relations', pairing*relations, s.zeros(1, relations.cols))
    generic_rank, residue_rank = relations.rank(), relations.subs(h, 0).rank()
    assert generic_rank == residue_rank == 3

    # Period mismatch u=1+h is removed étale-locally by c^3(1+h)=1.
    c = s.Symbol('c')
    period_equation = c**3*(1+h)-1
    derivative_at_origin = s.diff(period_equation, c).subs({c:1, h:0})
    assert derivative_at_origin == 3
    order = 8
    root = s.series((1+h)**s.Rational(-1, 3), h, 0, order).removeO()
    remainder = s.Poly(s.expand(root**3*(1+h)-1), h)
    assert all(remainder.nth(i) == 0 for i in range(order))

    # Underlying R-perfect is not right-algebra-perfect: k over k[e]/e^2.
    e = s.Matrix([[0,0],[1,0]])
    check('dual_number_resolution', e*e, s.zeros(2))
    assert e.rank() == 1 and e.columnspace() == e.nullspace()
    certificate = {
        'version':'nc-cubic-v34', 'date':'2026-11-11',
        'scope':'Ordinary Morita matrix identities, scalar period correction, compactness warning only.',
        'twisted_matrix_model':{
            'base':'Q[h]', 'T':[[str(x) for x in T.row(i)] for i in range(2)],
            'determinant':str(T.det()), 'A_product':'X*Y=X T Y',
            'A_unit':'T^(-1)', 'P':'row module p.X=p T X',
            'Q':'column module X.q=X T q', 'pairing':'p T q',
            'evaluation':'q tensor p -> q p', 'evaluation_determinant':'1',
            'balanced_relation_rank_generic':generic_rank,
            'balanced_relation_rank_at_zero':residue_rank},
        'identity_counts':counts, 'total_identities':sum(counts.values()),
        'period_correction':{'equation':'c^3(1+h)=1', 'initial_c':'1',
                             'initial_derivative':str(derivative_at_origin),
                             'verified_mod_h_power':order, 'root_truncation':str(root)},
        'compactness_warning':{'algebra':'k[e]/e^2', 'module':'k',
                               'base_perfect':True, 'algebra_perfect':False,
                               'reason':'The exact positive-degree periodic resolution by multiplication by e becomes zero-differential after tensoring with k, so Tor_i=k for every i>=0.'},
        'not_verified':['The actual cubic formal inverse kernel and its compactness.',
                        'The abstract dg Morita and Popescu descent proofs.',
                        'Existing nc diagonal matrices or generic cubic equivalence.']}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f"PASS: {sum(counts.values())} polynomial identities; two relation ranks; period mod h^{order}; compactness warning.")


if __name__ == '__main__':
    main()
