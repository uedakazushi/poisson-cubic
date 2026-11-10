#!/usr/bin/env python3
"""Audit v29 standalone source closure and exact certificate; not a categorical proof checker."""
from pathlib import Path
import json,re,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1]
ENTRY=ROOT/"papers/relative_artin_sector.tex"
seen=set()
def closure(path):
    if path in seen:return ""
    assert path.is_file(),f"Missing TeX input: {path}"
    seen.add(path)
    body=path.read_text(encoding="utf-8")
    for x in re.findall(r"\\(?:input|include)\{([^}]+)\}",body):
        p=ROOT/x
        if not p.suffix:p=p.with_suffix(".tex")
        body+="\n"+closure(p)
    return body
s=closure(ENTRY)
labels=re.findall(r"\\label\{([^}]+)\}",s)
refs=re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}",s)
keys=re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}",s)
cites=[v.strip() for xs in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}",s) for v in xs.split(",")]
assert len(labels)==len(set(labels))
assert len(keys)==len(set(keys))
assert set(refs)<=set(labels),set(refs)-set(labels)
assert set(cites)<=set(keys),set(cites)-set(keys)
assert r"\input{papers/reconstruction/relative_artin_sector}" in (ROOT/"papers/rotation_cubic_reconstruction.tex").read_text(encoding="utf-8")
assert r"\input{papers/reconstruction/relative_artin_sector_references}" in (ROOT/"papers/references.tex").read_text(encoding="utf-8")
with tempfile.TemporaryDirectory(prefix="nc-cubic-artin-") as td:
    dest=Path(td)/"certificate.json"
    run=subprocess.run([sys.executable,str(ROOT/"computations/verify_artin_sectors.py"),"--output",str(dest)],cwd=ROOT,capture_output=True,text=True,timeout=120)
    assert run.returncode==0,run.stdout+run.stderr
    actual=json.loads(dest.read_text(encoding="utf-8"))
    expected=json.loads((ROOT/"computations/artin_sector_certificate.json").read_text(encoding="utf-8"))
    assert actual==expected,"Certificate mismatch"
print("PASS v29 refs, C integration and exact certificate; categorical (KF) not verified")
