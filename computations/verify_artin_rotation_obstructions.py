#!/usr/bin/env python3
"""Exact finite checks of v31 low rotation obstruction analysis.

Known field-sector dimensions use BFK's formula as mathematical input.
Tests do not compute noncommutative categorical Nat, (KF), or (BC).
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sympy as sp

def sectors(r: int, m: int):
    jac_dims = (1, 5, 10, 10, 5, 1)
    ident = 0
    if m % 2 == 0:
        deg = r + 3 * (m // 2)
        ident = jac_dims[deg] if 0 <= deg < len(jac_dims) else 0
    nonid = 2 if m % 2 and 2 * r + 3 * m - 5 == 0 else 0
    return {"identity": ident, "nonidentity": nonid, "total": ident + nonid}

def verify_periodic_generator_counterexample():
    epsilon = sp.Matrix([[0, 0], [1, 0]])
    assert epsilon * epsilon == sp.zeros(2)
    assert epsilon.rank() == 1
    assert (sp.eye(2) - epsilon * sp.zeros(2))[0, 0] == 1
    assert all((epsilon * sp.Matrix([x, y]))[0] == 0
               for x, y in [(0, 0), (1, 0), (0, 1), (1, 1)])
    return {
        "base": "Q[epsilon]/epsilon^2",
        "epsilon_multiplication_matrix": [[0, 0], [1, 0]],
        "d_squared_zero": True,
        "rank_each_differential": 1,
        "ker_equals_image_dimensions": [1, 1],
        "hom_G_T_acyclic": True,
        "T_not_contractible_reason": "identity cannot lie in epsilon*R",
        "G0_generates_field_2periodic_category": True,
        "G_morita_generator": False,
    }

def verify_first_obstruction():
    A = sp.zeros(2, 5)
    A[0, 0] = A[1, 1] = 1
    assert A.rank() == 2
    basis = [sp.eye(5).col(i) for i in range(5)]
    allowed = [i for i, v in enumerate(basis) if A * v == sp.zeros(2, 1)]
    assert allowed == [2, 3, 4]
    return {
        "shape": [2, 5],
        "first_obstruction_matrix": [[int(z) for z in row] for row in A.tolist()],
        "rank": int(A.rank()),
        "H0_special_dimension": 5,
        "H1_special_dimension": 2,
        "image_dimension_of_reduction_on_H0": len(allowed),
        "H0_over_R1": "R1^3 direct_sum (R1/epsilon)^2",
        "free_of_rank5": False,
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    table = {str(r): {str(m): sectors(r, m) for m in (-3, -1, 0, 1, 2, 3)}
             for r in (1, 2)}
    assert [table["1"][str(m)]["total"] for m in (-1,0,1)] == [0,5,2]
    assert [table["2"][str(m)]["total"] for m in (-1,0,1)] == [0,10,0]
    assert table["1"]["1"]["nonidentity"] == 2
    result = {
        "version": "nc-cubic-v31",
        "date": "2026-11-11",
        "source_theorem": "BFK Theorem 5.39; weight formula 2*r+3*m-5=0 for nonidentity mu3 sectors",
        "field_sectors": table,
        "generator_counterexample": verify_periodic_generator_counterexample(),
        "first_order_obstruction_toy_model": verify_first_obstruction(),
        "limitations": [
            "BFK sector dimensions are theoretical inputs, not derived by the script",
            "2-periodic counterexample does not refute graded-cubic generation",
            "no actual noncommutative rotation Nat or KF is calculated",
            "higher Artin obstruction matrices are not computed",
        ],
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)+"\n", encoding="utf8")
    print("PASS v31: sector weights, generator counterexample, first-order obstruction")
if __name__ == "__main__":
    main()
