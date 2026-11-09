#!/usr/bin/env python3
"""Build the current Japanese LuaLaTeX manuscript without retaining caches."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'tex/rotation_saturation_reduction.tex'
PDF = ROOT / 'pdf/rotation_saturation_reduction.pdf'

def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main() -> None:
    exe = shutil.which('lualatex')
    if exe is None:
        raise SystemExit('LuaLaTeX is required (with ltjsarticle and LuaTeX-ja).')
    if not SOURCE.is_file():
        raise SystemExit(f'Missing source: {SOURCE}')
    with tempfile.TemporaryDirectory(prefix='nc-cubic-v14-') as tmp:
        work = Path(tmp)
        for i in range(3):
            proc = subprocess.run(
                [exe, '-interaction=nonstopmode', '-halt-on-error',
                 f'-output-directory={work}', str(SOURCE)],
                cwd=ROOT, text=True, capture_output=True, timeout=150,
            )
            if proc.returncode:
                print(proc.stdout[-10000:])
                print(proc.stderr[-3000:])
                raise SystemExit(f'LuaLaTeX pass {i+1} failed.')
        log = (work / (SOURCE.stem+'.log')).read_text(errors='replace')
        checks = {
            'undefined_references': 'There were undefined references' in log,
            'undefined_citations': 'Citation ' in log and 'undefined' in log,
            'missing_glyphs': 'Missing character:' in log,
            'overfull_boxes': 'Overfull \\hbox' in log or 'Overfull \\vbox' in log,
        }
        if any(checks.values()):
            warnings = [ln for ln in log.splitlines()
                        if any(t in ln for t in ['Warning', 'Overfull', 'Missing character'])]
            print('\n'.join(warnings))
            raise SystemExit('Typesetting checks failed: '+str(checks))
        PDF.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(work / (SOURCE.stem+'.pdf'), PDF)
    receipt = {
        'version': 'v14', 'date_jst': '2026-11-10',
        'source': str(SOURCE.relative_to(ROOT)), 'source_sha256': digest(SOURCE),
        'pdf': str(PDF.relative_to(ROOT)), 'pdf_sha256': digest(PDF),
        'engine': subprocess.run([exe, '--version'], text=True,
                                 capture_output=True, check=True).stdout.splitlines()[0],
        'passes': 3, 'typesetting_failures': checks,
        'scope': 'Current standalone paper-C section only; not a rebuild of full parent papers A/B/C.',
    }
    (ROOT/'build_receipt.json').write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(receipt, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
