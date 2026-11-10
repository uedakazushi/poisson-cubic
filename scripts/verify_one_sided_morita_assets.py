#!/usr/bin/env python3
"""Check complete source integration and regenerate the finite certificate.

This is not a proof checker and does not construct the nc cubic inverse kernel.
"""
from pathlib import Path
import json
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / 'papers/one_sided_morita_algebraization.tex'
seen = set()


def closure(path):
    if path in seen:
        return ''
    if not path.is_file():
        raise AssertionError(f'Missing source: {path}')
    seen.add(path)
    body = path.read_text(encoding='utf-8')
    result = body
    for name in re.findall(r'\\(?:input|include)\{([^}]+)\}', body):
        child = ROOT / name
        if not child.suffix:
            child = child.with_suffix('.tex')
        result += '\n' + closure(child)
    return result


body = closure(ENTRY)
labels = re.findall(r'\\label\{([^}]+)\}', body)
refs = re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}', body)
bib = re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}', body)
cites = [key.strip() for group in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}', body)
         for key in group.split(',')]
assert len(labels) == len(set(labels)), 'Duplicate labels'
assert len(bib) == len(set(bib)), 'Duplicate bibliography keys'
assert not set(refs) - set(labels), set(refs) - set(labels)
assert not set(cites) - set(bib), set(cites) - set(bib)
parent = (ROOT / 'papers/rotation_cubic_reconstruction.tex').read_text(encoding='utf-8')
assert r'\input{papers/reconstruction/one_sided_morita_algebraization}' in parent
shared = (ROOT / 'papers/references.tex').read_text(encoding='utf-8')
assert r'\input{papers/reconstruction/one_sided_morita_references}' in shared
with tempfile.TemporaryDirectory(prefix='nc-cubic-one-sided-') as directory:
    dest = Path(directory) / 'certificate.json'
    run = subprocess.run([sys.executable, str(ROOT / 'computations/verify_one_sided_morita.py'),
                          '--output', str(dest)], cwd=ROOT, capture_output=True,
                         text=True, timeout=120)
    assert run.returncode == 0, run.stdout + run.stderr
    actual = json.loads(dest.read_text(encoding='utf-8'))
    expected = json.loads((ROOT / 'computations/one_sided_morita_certificate.json').read_text(encoding='utf-8'))
    assert actual == expected, 'Certificate mismatch'
print('PASS complete new source closure, parent integration, and exact finite certificate; actual nc kernel not constructed.')
