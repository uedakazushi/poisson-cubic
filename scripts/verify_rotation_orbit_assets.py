#!/usr/bin/env python3
"""Audit the complete orbit-proof sources and regenerate its finite certificate.
Not a proof assistant or a computation of the generic equivalence kernel.
"""
from pathlib import Path
import json
import re
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]
seen=set()
def closure(path):
    if path in seen:
        return ''
    if not path.is_file():
        raise AssertionError(f'Missing input: {path}')
    seen.add(path)
    body=path.read_text(encoding='utf-8')
    result=body
    for name in re.findall(r'\\(?:input|include)\{([^}]+)\}',body):
        child=ROOT/name
        if not child.suffix:
            child=child.with_suffix('.tex')
        result+='\n'+closure(child)
    return result
body=closure(ROOT/'papers/support/papers/rotation_orbit_generic_reconstruction.tex')
labels=re.findall(r'\\label\{([^}]+)\}',body)
refs=re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}',body)
bib=re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}',body)
cites=[x.strip() for y in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',body) for x in y.split(',')]
assert len(labels)==len(set(labels)),'duplicate labels'
assert len(bib)==len(set(bib)),'duplicate bibliography keys'
assert not set(refs)-set(labels),set(refs)-set(labels)
assert not set(cites)-set(bib),set(cites)-set(bib)
assert r'\input{papers/reconstruction/rotation_orbit_generic_reconstruction}' in (ROOT/'papers/paper_b.tex').read_text(encoding='utf-8')
assert r'\input{papers/reconstruction/rotation_orbit_references}' in (ROOT/'papers/support/papers/references.tex').read_text(encoding='utf-8')
with tempfile.TemporaryDirectory(prefix='nc-cubic-orbit-') as d:
    out=Path(d)/'certificate.json'
    p=subprocess.run([sys.executable,str(ROOT/'computations/verify_rotation_orbit.py'),'--output',str(out)],cwd=ROOT,capture_output=True,text=True,timeout=180)
    assert p.returncode==0,p.stdout+p.stderr
    assert json.loads(out.read_text())==json.loads((ROOT/'computations/rotation_orbit_certificate.json').read_text()),'certificate mismatch'
print('PASS standalone source closure, B integration, and exact Euler/Koszul certificate; generic kernel not computed.')
