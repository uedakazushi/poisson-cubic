#!/usr/bin/env python3
"""Regenerate exact finite diagonal examples; inspect v30 source linkage.

Not a categorical theorem prover and not a full GitHub repo build.
"""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
NEEDED=[
 'papers/support/papers/reconstruction/diagonal_kernel_identity.tex',
 'papers/support/papers/reconstruction/diagonal_kernel_references.tex',
 'papers/support/papers/diagonal_kernel_identity.tex',
 'computations/verify_diagonal_identity.py',
 'computations/diagonal_identity_certificate.json',
 'notes/diagonal_kernel_identity.md',
]
assert all((ROOT/p).is_file() for p in NEEDED)
parent=ROOT/'papers/paper_b.tex'
refs=ROOT/'papers/support/papers/references.tex'
if parent.exists():
    assert r'\input{papers/reconstruction/diagonal_kernel_identity}' in parent.read_text()
if refs.exists():
    assert r'\input{papers/reconstruction/diagonal_kernel_references}' in refs.read_text()
with tempfile.TemporaryDirectory(prefix='nc-cubic-diagonal-') as d:
    path=Path(d)/'cert.json'
    run=subprocess.run([sys.executable,str(ROOT/'computations/verify_diagonal_identity.py'),
                        '--output',str(path)],capture_output=True,text=True,cwd=ROOT,timeout=180)
    assert run.returncode==0,run.stdout+'\n'+run.stderr
    assert json.loads(path.read_text())==json.loads((ROOT/'computations/diagonal_identity_certificate.json').read_text())
print('PASS: v30 finite examples and source linkage. KF full faithfulness NOT verified.')
