#!/usr/bin/env python3
"""Audit v31 manuscript references and regenerate the finite certificate."""
from pathlib import Path
import json, re, subprocess, sys, tempfile
ROOT=Path(__file__).resolve().parents[1]
manu=ROOT/"papers"/"artin_rotation_obstructions.tex"
seen=set()
def src(path):
    if path in seen:return ""
    assert path.is_file(),str(path)
    seen.add(path)
    t=path.read_text()
    out=t
    for q in re.findall(r"\\(?:input|include)\{([^{}]+)\}",t):
        x=ROOT/q
        if not x.suffix:x=x.with_suffix(".tex")
        out+="\n"+src(x)
    return out
content=src(manu)
labels=re.findall(r"\\label\{([^}]+)\}",content)
refs=re.findall(r"\\(?:eqref|ref|pageref)\{([^}]+)\}",content)
bib=re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}",content)
cites=[y.strip() for c in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}",content) for y in c.split(",")]
assert len(labels)==len(set(labels))
assert not set(refs)-set(labels),set(refs)-set(labels)
assert not set(cites)-set(bib),set(cites)-set(bib)
assert r"\input{papers/reconstruction/artin_rotation_obstructions}" in (ROOT/"papers/rotation_cubic_reconstruction.tex").read_text()
assert r"\input{papers/reconstruction/artin_rotation_obstructions_references}" in (ROOT/"papers/references.tex").read_text()
with tempfile.TemporaryDirectory() as d:
    tmp=Path(d)/"cert.json"
    subprocess.run([sys.executable,str(ROOT/"computations/verify_artin_rotation_obstructions.py"),"--output",str(tmp)],check=True,cwd=ROOT)
    assert json.loads(tmp.read_text())==json.loads((ROOT/"computations/artin_rotation_obstructions_certificate.json").read_text())
print("PASS v31 source, exact finite certificate; actual KF and BC not verified")
