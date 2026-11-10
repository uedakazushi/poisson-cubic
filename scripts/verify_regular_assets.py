#!/usr/bin/env python3
"""Check regular-diagonal source closure and optional regenerated witnesses.

Default checks validate saved assets and finite displayed algebra only; they
DO NOT rerun the expensive nc diagonal. Use --recompute for that calculation.
"""
from pathlib import Path
import argparse, hashlib, json, re, subprocess, sys, tempfile
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--recompute', action='store_true')
p.add_argument('--witness', type=Path)
a=p.parse_args()
paths=['computations/regular_diagonal.py','computations/verify_regular_diagonal.py',
       'computations/absolute_diagonal.py','computations/curved_diagonal.py',
       'computations/verify_curved_diagonal.py',
       'papers/reconstruction/regular_diagonal_recovery.tex',
       'papers/reconstruction/regular_diagonal_references.tex','notes/curved_diagonal.md']
assert all((ROOT/q).is_file() for q in paths)
c=json.loads((ROOT/'computations/regular_diagonal_certificate.json').read_text())
assert c['version']=='nc-cubic-v27' and all(c['checks'].values())
assert c['boundary_and_class_unit_minor']['residue_determinant']=='-3'
assert c['number_of_local_systems']==45
h=sp.Symbol('h')
mu=sp.zeros(*c['product_matrix']['shape'])
for i,j,v in c['product_matrix']['entries']: mu[i,j]=sp.sympify(v)
assert mu.shape==(6,10) and mu[:,[1,2,3,5,6,8]]==sp.eye(6)
for v in mu:
    assert sp.fraction(sp.cancel(v))[1].subs(h,0)!=0
u,x,y,z=sp.symbols('u x y z');xs=[u,x,y,z]
mons=[xs[i]*xs[j] for i in range(4) for j in range(i,4)]
G=sp.sympify(c['integrated_cubic'])
Q=sp.Matrix.hstack(*(sp.Matrix([sp.Poly(sp.diff(G,v),xs).coeff_monomial(m) for m in mons]) for v in xs))
assert all(sp.cancel(v)==0 for v in mu*Q)
assert sp.expand(sp.sympify(c['coefficient_denominator_audit']['monic_lcm'])-(h**3-1)*(h**6+162))==0
seen=set()
def closure(path):
    if path in seen:return ''
    assert path.is_file(),path
    seen.add(path);s=path.read_text()
    for inc in re.findall(r'\\input\{([^}]+)\}',s):
        q=ROOT/inc
        if not q.suffix:q=q.with_suffix('.tex')
        s+='\n'+closure(q)
    return s
text=closure(ROOT/'papers/curved_diagonal_recovery.tex')
labels=re.findall(r'\\label\{([^}]+)\}',text)
refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}',text)
bib=re.findall(r'\\bibitem\{([^}]+)\}',text)
cites=[s.strip() for block in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',text) for s in block.split(',')]
assert len(labels)==len(set(labels)) and not set(refs)-set(labels)
assert not set(cites)-set(bib)
if a.witness:
    full=json.loads(a.witness.read_text())
    digest=hashlib.sha256(json.dumps(full,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert digest==c['full_witness_sha256']
    print('PASS full-witness canonical SHA256')
if a.recompute:
    with tempfile.TemporaryDirectory(prefix='nc-regular-') as d:
        dest=Path(d)/'regular.json'
        subprocess.run([sys.executable,str(ROOT/'computations/verify_regular_diagonal.py'),'--output',str(dest)],cwd=ROOT,check=True)
        assert json.loads(dest.read_text())==c
    print('PASS full nc calculation regenerated and matched')
print('PASS regular source closure, saved finite product, and gradient identities')
if not a.recompute: print('Full nc diagonal NOT recomputed by this invocation; categorical comparison remains open.')
