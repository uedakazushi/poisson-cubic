#!/usr/bin/env python3
"""Audit current sources, labels, bibliography and computation entrypoints.

A missing PDF is reported as pending by default, and fails with --require-pdfs.
This is not a mathematical proof checker and never claims to have executed one.
"""
from pathlib import Path
import argparse
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
PAPERS=("poisson_cubic_quantization","generic17_ambient_recovery","rotation_cubic_reconstruction")
parser=argparse.ArgumentParser()
parser.add_argument("--require-pdfs",action="store_true")
parser.add_argument("--run-computations",action="store_true")
args=parser.parse_args()

def source_closure(path,seen=None):
    seen=set() if seen is None else seen
    if path in seen:
        return ""
    if not path.is_file():
        raise AssertionError(f"Missing included source {path}")
    seen.add(path)
    s=path.read_text(encoding="utf-8")
    for name in re.findall(r"\\(?:input|include)\{([^}]+)\}",s):
        sub=ROOT/name
        if not sub.suffix: sub=sub.with_suffix(".tex")
        s+="\n"+source_closure(sub,seen)
    return s

for name in PAPERS:
    body=source_closure(ROOT/"tex"/f"{name}.tex")
    labels=re.findall(r"\\label\{([^}]+)\}",body)
    refs=re.findall(r"\\(?:eqref|ref|pageref)\{([^}]+)\}",body)
    bibkeys=re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}",body)
    citeitems=[]
    for x in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}",body):
        citeitems.extend(y.strip() for y in x.split(","))
    assert len(labels)==len(set(labels)),f"Duplicate labels: {name}"
    assert len(bibkeys)==len(set(bibkeys)),f"Duplicate bibliography keys: {name}"
    assert not set(refs)-set(labels),(name,"undefined refs",set(refs)-set(labels))
    assert not set(citeitems)-set(bibkeys),(name,"undefined cites",set(citeitems)-set(bibkeys))
    pdf=ROOT/"pdf"/f"{name}.pdf"
    if not pdf.exists():
        print(f"PENDING PDF: {pdf.relative_to(ROOT)}")
        if args.require_pdfs: raise AssertionError(f"Missing current PDF: {name}")
    else:
        print(f"PDF EXISTS (source parity not established by this test): {pdf.relative_to(ROOT)}")
    print(f"PASS source closure: {name}; labels={len(labels)}, citations={len(citeitems)}")

for needed in ("00_research_plan.md","research_notes.md","README.md","validation.json"):
    assert (ROOT/needed).exists(),f"Missing {needed}"

if args.run_computations:
    for script in ("verify_algebra.py","verify_geometry.py",
                   "verify_rotation_obstructions.py","verify_hesse_center.py",
                   "verify_reconstruction.py"):
        r=subprocess.run([sys.executable,str(ROOT/"computations"/script)],
                         cwd=ROOT,capture_output=True,text=True)
        if r.returncode: raise AssertionError(f"{script}: {r.stdout}\n{r.stderr}")
        print(f"PASS exact computation {script}")
    for name in ("verify_generic17_slice.py","verify_split_codimension.py"):
        # The second test is stored directly under computations/.
        path=(ROOT/"computations"/"independent"/name) if name=="verify_generic17_slice.py" else (ROOT/"computations"/name)
        r=subprocess.run([sys.executable,str(path)],
                         cwd=ROOT,capture_output=True,text=True)
        if r.returncode: raise AssertionError(f"{name}: {r.stdout}\n{r.stderr}")
        print(f"PASS exact computation {name}")
print("Static audit complete. Mathematical categorical proofs are not formalized.")
