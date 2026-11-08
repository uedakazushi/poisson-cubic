#!/usr/bin/env python3
"""Build this self-contained reconstruction bundle with LuaLaTeX.

Intermediate files are kept in a temporary directory. Run from any directory.
No network, git writes, or GitHub Actions are performed.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
NAMES = ('elliptic_cubic_reconstruction', 'reconstruction_notes', 'elliptic_reconstruction_plan')

def build(name: str, work: Path) -> dict:
    source = ROOT / 'tex' / f'{name}.tex'
    if name == 'elliptic_reconstruction_plan':
        body = subprocess.run(['pandoc', str(ROOT / 'elliptic_reconstruction_plan.md'),
            '--from=markdown+tex_math_dollars', '--to=latex', '--wrap=none'],
            check=True, text=True, stdout=subprocess.PIPE).stdout
        body = re.sub(r'(?=\\hypertarget\{)',
                      lambda _: '\\Needspace{6\\baselineskip}\n', body)
        body = re.sub(r'\\texttt\{([^{}]+)\}',
            lambda m: ('\\path{' + m.group(1).replace('\\_', '_') + '}')
            if '/' in m.group(1) and '\\ ' not in m.group(1) else m.group(0), body)
        source = work / 'elliptic_reconstruction_plan.tex'
        source.write_text('\\input{tex/reconstruction_preamble}\n'
          '\\providecommand{\\tightlist}{\\setlength{\\itemsep}{0pt}\\setlength{\\parskip}{0pt}}\n'
          '\\begin{document}\n'+body+'\n\\end{document}\n', encoding='utf-8')
    last = None
    for number in range(1, 6):
        run = subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',
          '-file-line-error',f'-output-directory={work}',str(source)],cwd=ROOT,
          stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if run.returncode:
            raise RuntimeError(run.stdout[-16000:])
        log=(work/f'{name}.log').read_text(errors='replace')
        aux=(work/f'{name}.aux').read_bytes()
        rerun=bool(re.search(r'Rerun to get|Rerun LaTeX|Label\(s\) may have changed', log))
        if number>=2 and aux==last and not rerun:
            break
        last=aux
    problems=[line for line in log.splitlines()
              if re.search(r'Overfull|undefined|Missing character|Rerun to get',line)]
    if problems:
        diagnostics=ROOT.parent/'work'/'reconstruction-typesetting'
        diagnostics.mkdir(parents=True,exist_ok=True)
        for ext in ('log','pdf'):
            shutil.copy2(work/f'{name}.{ext}',diagnostics/f'{name}.{ext}')
        raise RuntimeError('\n'.join(problems)+f'\nDiagnostics: {diagnostics}')
    target=ROOT/'pdf'/f'{name}.pdf'
    target.parent.mkdir(exist_ok=True)
    shutil.copy2(work/f'{name}.pdf',target)
    seen=set()
    def collect(path):
        if path in seen:
            return
        seen.add(path)
        if path.suffix == '.tex':
            for child in re.findall(r'\\(?:input|include)\{([^}]+)\}',path.read_text(encoding='utf-8')):
                nxt=ROOT/child
                if not nxt.suffix:
                    nxt=nxt.with_suffix('.tex')
                collect(nxt)
    if name == 'elliptic_reconstruction_plan':
        collect(ROOT/'elliptic_reconstruction_plan.md')
        collect(ROOT/'tex/reconstruction_preamble.tex')
    else:
        collect(ROOT/'tex'/f'{name}.tex')
    collect(Path(__file__).resolve())
    match=re.search(r'Output written on[\s\S]*?\((\d+) pages?',log)
    item={'name':name,'passes':number,'undefined_references':0,
          'missing_glyphs':0,'overfull_boxes':0,'pages':int(match.group(1)) if match else None,
          'pdf_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
          'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(seen)}}
    receipt=ROOT/'reconstruction_build_receipt.json'
    state=json.loads(receipt.read_text(encoding='utf-8')) if receipt.exists() else {}
    state[name]=item
    receipt.write_text(json.dumps(state,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    return {k:v for k,v in item.items() if k not in ('pdf_sha256','source_sha256')}

def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--only',action='append',choices=NAMES)
    args=parser.parse_args()
    if not shutil.which('lualatex'):
        raise SystemExit('LuaLaTeX with LuaTeX-ja and ltjsarticle is required.')
    names=args.only or NAMES
    if 'elliptic_reconstruction_plan' in names and not shutil.which('pandoc'):
        raise SystemExit('Pandoc is required for the research plan.')
    with tempfile.TemporaryDirectory(prefix='nc-cubic-reconstruction-') as tmp:
        for name in names:
            print(json.dumps(build(name,Path(tmp)),ensure_ascii=False),flush=True)
if __name__=='__main__':
    main()