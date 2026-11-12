#!/usr/bin/env python3
"""Audit v28 inputs and regenerate its small exact certificate; not a proof checker."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
ENTRY=ROOT/"papers/support/papers/multiplicative_bar_comparison.tex"
seen=set()
def closure(p):
    if p in seen:return ""
    if not p.is_file():raise AssertionError(f"Missing input: {p}")
    seen.add(p); text=p.read_text(encoding="utf-8")
    result=text
    for name in re.findall(r"\\(?:input|include)\{([^}]+)\}",text):
        q=ROOT/name
        if not q.suffix:q=q.with_suffix(".tex")
        result+="\n"+closure(q)
    return result
body=closure(ENTRY)
labels=re.findall(r"\\label\{([^}]+)\}",body)
refs=re.findall(r"\\(?:eqref|ref|pageref)\{([^}]+)\}",body)
bib=re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}",body)
cites=[y.strip() for x in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}",body) for y in x.split(",")]
assert len(labels)==len(set(labels)), "Duplicate labels"
assert len(bib)==len(set(bib)), "Duplicate bibliography keys"
assert not set(refs)-set(labels),set(refs)-set(labels)
assert not set(cites)-set(bib),set(cites)-set(bib)
parent=(ROOT/"papers/paper_b.tex").read_text(encoding="utf-8")
assert r"\input{papers/reconstruction/multiplicative_bar_comparison}" in parent
assert r"\input{papers/reconstruction/multiplicative_bar_references}" in (ROOT/"papers/support/papers/references.tex").read_text(encoding="utf-8")
with tempfile.TemporaryDirectory(prefix="nc-cubic-bar-") as td:
    dest=Path(td)/"certificate.json"
    run=subprocess.run([sys.executable,str(ROOT/"computations/verify_bar_comparison.py"),"--output",str(dest)],cwd=ROOT,capture_output=True,text=True,timeout=120)
    assert run.returncode==0,run.stdout+run.stderr
    actual=json.loads(dest.read_text(encoding="utf-8"))
    expected=json.loads((ROOT/"computations/bar_comparison_certificate.json").read_text(encoding="utf-8"))
    assert actual==expected,"Certificate mismatch"
print("PASS standalone source closure, B integration, and exact v28 certificate; categorical BC NOT checked.")
