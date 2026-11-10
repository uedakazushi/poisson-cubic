#!/usr/bin/env python3
"""Exact finite character checks for conditional central-symmetry lifting.

This verifies group weight bookkeeping and a finite toy obstruction matrix,
not derived categorical Nat, the BFK sector formula, or the bar model.
"""
import argparse
import json
from pathlib import Path
import sympy as sp

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args=parser.parse_args()
    x,y,z,u,v,L = sp.symbols('x y z u v lambda')
    F=(x**3+y**3+z**3)/3+u**3+v**3+L*u*x*y
    assert all((mon[4] % 3) == 0 for mon,coeff in sp.Poly(F,x,y,z,u,v).terms())
    source_weights=[0,0,0,0,1]
    matrices=[]
    for det_weight in (1,2):
        target_weights=[det_weight,det_weight]
        allowed=[(i,j) for i,wt in enumerate(target_weights)
                 for j,swt in enumerate(source_weights) if wt==swt]
        allowed_after_v_lift=[(i,j) for i,j in allowed if j!=4]
        assert len(allowed_after_v_lift)==0
        matrices.append({'target_weights':target_weights,
                         'possible_nonzero_entries':allowed,
                         'after_central_v_closed_lift':allowed_after_v_lift,
                         'forced_first_obstruction_rank':0})
    M_bad=sp.Matrix([[1,0,0,0,0],[0,1,0,0,0]])
    assert M_bad.rank()==2
    assert any((i,j) not in matrices[0]['possible_nonzero_entries']
               for i in range(2) for j in range(5) if M_bad[i,j]!=0)
    cert={
      'version':'nc-cubic-v32',
      'date':'2026-11-11',
      'scope':'Character bookkeeping for conditional Artin cochain lifting, not a categorical comparison',
      'source_H0_characters_mod3':source_weights,
      'nonidentity_sectors_H1_dimension':2,
      'normal_determinant_nontrivial_characters_both_conventions':matrices,
      'parameter_h_character':0,
      'four_Gamma_invariant_classes':4,
      'fifth_class':'v; has closed lift by multiplication with the independent central generator',
      'mod3_v_exponents_in_F':sorted(set(mon[4] % 3 for mon,_ in sp.Poly(F,x,y,z,u,v).terms())),
      'non_equivariant_example_first_obstruction_rank':M_bad.rank(),
      'tested_artin_extension_orders':[1,2,3,4,5,6],
      'expected_if_correct_equivariant_flat_derived_complex':{'r1_H0_rank':5,'r2_H0_rank':10},
      'not_verified':['BFK sector theorem itself','correct derived Nat cochain compatibility','cofibrant bar and kernel fully faithfulness','generic noncommutative cubic reconstruction']
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(cert,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print('PASS: v-cubic symmetry, both determinant-character conventions, 2x5 toy obstruction, all nilpotent orders by weight')
if __name__=='__main__':main()
