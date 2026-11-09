#!/usr/bin/env python3
"""Check artifact integrity and exact input computations, not categorical proofs."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def require(test: bool, message: str) -> None:
    if not test:
        raise SystemExit(message)

def main() -> None:
    required = [
        'research_notes.md', 'README.md',
        'tex/rotation_saturation_reduction.tex',
        'pdf/rotation_saturation_reduction.pdf',
        'computations/verify_nonelliptic_inputs.py', 'computations/input_checks.json',
        'build_receipt.json',
    ]
    for rel in required:
        require((ROOT/rel).is_file(), 'Missing file: '+rel)
    text = (ROOT/'tex/rotation_saturation_reduction.tex').read_text(encoding='utf-8')
    labels = re.findall(r'\\label\{([^}]+)\}', text)
    refs = re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}', text)
    require(len(labels) == len(set(labels)), 'Duplicate LaTeX labels.')
    require(set(refs) <= set(labels), 'Broken labels: '+str(set(refs)-set(labels)))
    bibs = set(re.findall(r'\\bibitem\{([^}]+)\}', text))
    cites = {item.strip() for s in re.findall(r'\\cite(?:\[[^]]*\])*\{([^}]+)\}', text)
             for item in s.split(',')}
    require(cites <= bibs, 'Broken citations: '+str(cites-bibs))
    receipt = json.loads((ROOT/'build_receipt.json').read_text())
    for field in ('source', 'pdf'):
        require(digest(ROOT/receipt[field]) == receipt[field+'_sha256'],
                'Build receipt mismatch: '+field)
    with tempfile.TemporaryDirectory(prefix='nc-cubic-check-') as tmp:
        dest = Path(tmp)/'checks.json'
        run = subprocess.run(
            [sys.executable, str(ROOT/'computations/verify_nonelliptic_inputs.py'),
             '--output', str(dest)], text=True, capture_output=True, timeout=120)
        require(run.returncode == 0, run.stdout+'\n'+run.stderr)
        expected = json.loads((ROOT/'computations/input_checks.json').read_text())
        require(json.loads(dest.read_text()) == expected, 'Input certificate does not reproduce.')
    sums = ROOT/'SHA256SUMS'
    if sums.exists():
        for line in sums.read_text().splitlines():
            h, rel = line.split('  ', 1)
            require((ROOT/rel).is_file() and digest(ROOT/rel) == h,
                    'SHA256SUMS mismatch: '+rel)
    for p in ROOT.rglob('*'):
        require(p.suffix not in {'.aux','.log','.toc','.out','.pyc','.zip'},
                'Unwanted intermediate/archive in bundle: '+str(p))
    print(json.dumps({'required_files': 'passed', 'labels': len(labels),
                      'bibliography_keys': len(bibs), 'reference_integrity': 'passed',
                      'source_pdf_hash_parity': 'passed',
                      'exact_input_recomputation': 'passed',
                      'categorical_proofs': 'not machine-verified'},
                     ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
