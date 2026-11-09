#!/usr/bin/env python3
"""Build the current Japanese paper-C export and hash every TeX input."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'tex/rotation_saturation_reduction.tex'
PDF = ROOT / 'pdf/rotation_saturation_reduction.pdf'
INPUTS = [SOURCE, ROOT/'tex/etale_realization.tex', ROOT/'tex/hochschild_obstructions.tex', ROOT/'tex/etale_references.tex']


def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> None:
    exe = shutil.which('lualatex')
    if exe is None:
        raise SystemExit('LuaLaTeX with ltjsarticle and LuaTeX-ja is required.')
    for source in INPUTS:
        if not source.is_file():
            raise SystemExit(f'Missing TeX input: {source}')
    env = dict(os.environ, SOURCE_DATE_EPOCH='1794268800', FORCE_SOURCE_DATE='1')
    with tempfile.TemporaryDirectory(prefix='nc-cubic-build-') as tmp:
        work = Path(tmp)
        for i in range(3):
            proc = subprocess.run(
                [exe, '-interaction=nonstopmode', '-halt-on-error',
                 f'-output-directory={work}', str(SOURCE)],
                cwd=ROOT, env=env, text=True, capture_output=True, timeout=150,
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
            print('\n'.join(ln for ln in log.splitlines()
                            if any(t in ln for t in ['Warning', 'Overfull', 'Missing character'])))
            raise SystemExit('Typesetting checks failed: '+str(checks))
        PDF.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(work / (SOURCE.stem+'.pdf'), PDF)
    receipt = {
        'version': 'v17', 'date_jst': '2026-11-10',
        'source': str(SOURCE.relative_to(ROOT)), 'source_sha256': digest(SOURCE),
        'tex_inputs': {str(p.relative_to(ROOT)): digest(p) for p in INPUTS},
        'pdf': str(PDF.relative_to(ROOT)), 'pdf_sha256': digest(PDF),
        'engine': subprocess.run([exe, '--version'], text=True,
                                 capture_output=True, check=True).stdout.splitlines()[0],
        'passes': 3, 'typesetting_failures': checks,
        'source_date_epoch': env['SOURCE_DATE_EPOCH'],
        'scope': 'Current standalone paper-C export, including the full etale proof and Hochschild sectors. '
                 'Not a rebuild of all parent papers A/B/C.',
    }
    (ROOT/'build_receipt.json').write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
