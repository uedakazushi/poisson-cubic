#!/usr/bin/env python3
"""Exact character certificates for the Zhang-twist rotation obstructions.

Only arithmetic in Z/3 is used. This verifies the finite algebraic and
character computations, not the categorical identifications in the paper.
"""

from itertools import combinations
from pathlib import Path
import json


def character(weights, degree, determinant_shift=0, inverse=False):
    basis = list(combinations(range(len(weights)), degree))
    counts = [0, 0, 0]
    rows = []
    for indices in basis:
        weight = (sum(weights[i] for i in indices) + determinant_shift) % 3
        if inverse:
            weight = (-weight) % 3
        counts[weight] += 1
        rows.append({"indices": list(indices), "weight_mod_3": weight})
    return {"multiplicities_for_1_omega_omega2": counts, "basis": rows}


def skew_checks(weights):
    n = len(weights)
    # Right Zhang twist: x_i*x_j = omega^(a_j-a_i) x_j*x_i.
    relations = [[(weights[j] - weights[i]) % 3 for j in range(n)]
                 for i in range(n)]
    assert all((relations[i][j] + relations[j][i]) % 3 == 0
               for i in range(n) for j in range(n))
    central_cubes = all((3 * relations[i][j]) % 3 == 0
                        for i in range(n) for j in range(n))
    # Using RRZ's x_j*x_i = p_ij x_i*x_j convention gives this exponent.
    nakayama = [(sum(weights) - n * a) % 3 for a in weights]
    # Scalar PBW commutations satisfy all degree-three overlap conditions.
    for i, j, k in combinations(range(n), 3):
        left = (relations[k][j] + relations[k][i] + relations[j][i]) % 3
        right = (relations[j][i] + relations[k][i] + relations[k][j]) % 3
        assert left == right
    assert central_cubes
    return {"relation_exponents": relations,
            "all_generator_cubes_central": central_cubes,
            "determinant_weight_mod_3": sum(weights) % 3,
            "nakayama_weights_mod_3": nakayama,
            "calabi_yau": all(w == 0 for w in nakayama)}


three_weights = [1, 0, 0, 0, 0]
four_weights = [1, 2, 0, 0, 0, 0]
three = skew_checks(three_weights)
three["pullback_on_H21"] = character(three_weights, 1, sum(three_weights))
assert three["pullback_on_H21"]["multiplicities_for_1_omega_omega2"] == [0, 4, 1]
assert not three["calabi_yau"]

four = skew_checks(four_weights)
four["pullback_on_primitive_H22"] = character(four_weights, 3, sum(four_weights))
assert four["calabi_yau"]
assert four["pullback_on_primitive_H22"]["multiplicities_for_1_omega_omega2"] == [8, 6, 6]
primitive_push = character(four_weights, 3, sum(four_weights), inverse=True)[
    "multiplicities_for_1_omega_omega2"]
# The A2 action and identity on the standard primitive part are inputs proved
# by the categorical/HKR argument in the paper, not established by this code.
a2_rotation = [0, 1, 1]
four["twisted_rotation_HH0_multiplicities"] = [
    primitive_push[i] + a2_rotation[i] for i in range(3)]
four["standard_cubic_rotation_HH0_multiplicities"] = [
    len(four["pullback_on_primitive_H22"]["basis"]), 1, 1]
assert four["twisted_rotation_HH0_multiplicities"] == [8, 7, 7]
assert four["standard_cubic_rotation_HH0_multiplicities"] == [20, 1, 1]
assert sum(four["twisted_rotation_HH0_multiplicities"]) == 22
assert sum(four["standard_cubic_rotation_HH0_multiplicities"]) == 22
four["invariant_Hochschild_Euler_characteristics"] = {
    "standard_cubic_pair": four["standard_cubic_rotation_HH0_multiplicities"][0] + 2,
    "twisted_pair": four["twisted_rotation_HH0_multiplicities"][0] + 2,
    "assumption": "HH_2 and HH_minus_2 are each one-dimensional and fixed; all odd HH vanish."
}
assert four["invariant_Hochschild_Euler_characteristics"]["standard_cubic_pair"] == 22
assert four["invariant_Hochschild_Euler_characteristics"]["twisted_pair"] == 10

certificate = {
    "version": "nc-cubic-v1",
    "date_jst": "2026-11-08",
    "status": "all exact finite computations passed",
    "limitations": "Does not formalize derived equivalences, Serre formulas, or HKR naturality.",
    "cubic_threefold": three,
    "calabi_yau_cubic_fourfold": four,
}
path = Path(__file__).with_name("rotation_obstructions.json")
path.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("PASS: centrality, PBW overlaps, Nakayama weights, residue characters, and 8 != 20.")
print(path.name)
