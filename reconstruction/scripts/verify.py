#!/usr/bin/env python3
"""Check full input closure and exact algebra; not a categorical proof assistant."""
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


def expanded_source(path: Path, seen: set[Path]) -> str:
    path = path.resolve()
    require(path.is_relative_to(ROOT), 'TeX input outside reconstruction: '+str(path))
    require(path.is_file(), 'Missing TeX input: '+str(path))
    require(path not in seen, 'Repeated or cyclic TeX input: '+str(path))
    seen.add(path)
    text = path.read_text(encoding='utf-8')
    def substitute(match: re.Match) -> str:
        rel = match.group(1)
        return expanded_source(ROOT/(rel if rel.endswith('.tex') else rel+'.tex'), seen)
    return re.sub(r'\\input\{([^}]+)\}', substitute, text)


def main() -> None:
    required = ['research_notes.md', 'README.md', 'validation.json', 'requirements.txt',
                'pdf/rotation_saturation_reduction.pdf', 'build_receipt.json']
    for rel in required:
        require((ROOT/rel).is_file(), 'Missing file: '+rel)
    seen: set[Path] = set()
    text = expanded_source(ROOT/'tex/rotation_saturation_reduction.tex', seen)
    labels = re.findall(r'\\label\{([^}]+)\}', text)
    refs = re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}', text)
    require(len(labels) == len(set(labels)), 'Duplicate LaTeX labels.')
    require(set(refs) <= set(labels), 'Broken labels: '+str(set(refs)-set(labels)))
    bibs = re.findall(r'\\bibitem\{([^}]+)\}', text)
    require(len(bibs) == len(set(bibs)), 'Duplicate bibliography keys.')
    cites = {item.strip() for s in re.findall(r'\\cite(?:\[[^]]*\])*\{([^}]+)\}', text)
             for item in s.split(',')}
    require(cites <= set(bibs), 'Broken citations: '+str(cites-set(bibs)))
    receipt = json.loads((ROOT/'build_receipt.json').read_text())
    require(set(receipt['tex_inputs']) == {str(p.relative_to(ROOT)) for p in seen},
            'Receipt does not cover precisely all TeX inputs.')
    for rel, expected in receipt['tex_inputs'].items():
        require(digest(ROOT/rel) == expected, 'TeX input hash mismatch: '+rel)
    for field in ('source', 'pdf'):
        require(digest(ROOT/receipt[field]) == receipt[field+'_sha256'],
                'Build receipt mismatch: '+field)
    pairs = [('verify_nonelliptic_inputs.py', 'input_checks.json'),
             ('verify_etale_inputs.py', 'etale_input_checks.json'),
             ('verify_hochschild_sectors.py', 'hochschild_sector_checks.json')]
    with tempfile.TemporaryDirectory(prefix='nc-cubic-check-') as tmp:
        for script, certificate in pairs:
            dest = Path(tmp)/certificate
            run = subprocess.run(
                [sys.executable, str(ROOT/'computations'/script), '--output', str(dest)],
                text=True, capture_output=True, timeout=120)
            require(run.returncode == 0, run.stdout+'\n'+run.stderr)
            expected = json.loads((ROOT/'computations'/certificate).read_text())
            require(json.loads(dest.read_text()) == expected,
                    'Certificate does not reproduce: '+certificate)
    for p in ROOT.rglob('*'):
        require(p.suffix not in {'.aux', '.log', '.toc', '.out', '.pyc', '.zip'},
                'Unwanted intermediate/archive: '+str(p))
    print(json.dumps({'version': 'v17', 'tex_inputs': len(seen), 'labels': len(labels),
                      'bibliography_keys': len(bibs), 'reference_integrity': 'passed',
                      'source_pdf_hash_parity': 'passed',
                      'exact_input_recomputation': 'passed (three certificates)',
                      'categorical_proofs': 'not machine-verified'},
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
