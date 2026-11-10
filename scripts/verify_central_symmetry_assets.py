#!/usr/bin/env python3
"""Check v32 standalone TeX closure and its exact finite character certificate."""
import json,re,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ENTRY=ROOT/'papers/central_symmetry_lifting.tex'
seen=set()
def visit(p):
    p=p.resolve()
    if p in seen:return ''
    assert p.is_file(),p
    seen.add(p)
    s=p.read_text(encoding='utf8')
    for inc in re.findall(r'\\(?:input|include)\{([^}]+)\}',s):
        q=ROOT/inc
        if not q.suffix:q=q.with_suffix('.tex')
        s+='\n'+visit(q)
    return s
body=visit(ENTRY)
refs=set(re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}',body))
labels=re.findall(r'\\label\{([^}]+)\}',body)
assert len(labels)==len(set(labels))
assert not refs-set(labels),refs-set(labels)
bibs=set(re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}',body))
cites=[y.strip() for x in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',body) for y in x.split(',')]
assert not set(cites)-bibs,set(cites)-bibs
with tempfile.TemporaryDirectory() as td:
    f=Path(td)/'verify.json'
    result=subprocess.run([sys.executable,str(ROOT/'computations/verify_central_symmetry.py'),'--output',str(f)],capture_output=True,text=True,timeout=40)
    assert result.returncode==0,result.stderr
    expect=json.loads((ROOT/'computations/central_symmetry_certificate.json').read_text())
    assert json.loads(f.read_text())==expect
print(f'PASS v32 TeX closure {len(seen)} files, {len(labels)} labels; character certificate exact. No categorical (KF) check.')
