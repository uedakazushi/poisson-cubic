#!/usr/bin/env python3
"""Audit the geometric shortcut's sources and finite tests, not categorical proofs."""
from pathlib import Path
import json
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / "papers/support/papers/geometric_rotation_basechange.tex"
seen = set()

def closure(path):
    if path in seen:
        return ""
    if not path.is_file():
        raise AssertionError(f"Missing input: {path}")
    seen.add(path)
    body = path.read_text(encoding="utf-8")
    expanded = body
    for name in re.findall(r"\\(?:input|include)\{([^}]+)\}", body):
        child = ROOT / "papers/support" / name
        if not child.suffix:
            child = child.with_suffix(".tex")
        expanded += "\n" + closure(child)
    return expanded

body = closure(ENTRY)
labels = re.findall(r"\\label\{([^}]+)\}", body)
refs = re.findall(r"\\(?:eqref|ref|pageref)\{([^}]+)\}", body)
bib = re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", body)
cites = [key.strip() for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", body)
         for key in group.split(",")]
assert len(labels) == len(set(labels)), "Duplicate theorem labels"
assert len(bib) == len(set(bib)), "Duplicate bibliography keys"
assert not set(refs) - set(labels), set(refs) - set(labels)
assert not set(cites) - set(bib), set(cites) - set(bib)
parent = (ROOT / "papers/paper_b.tex").read_text(encoding="utf-8")
assert r"\input{papers/reconstruction/geometric_rotation_basechange}" in parent
shared = (ROOT / "papers/support/papers/references.tex").read_text(encoding="utf-8")
assert r"\input{papers/reconstruction/geometric_rotation_references}" in shared
with tempfile.TemporaryDirectory(prefix="nc-cubic-geometric-") as directory:
    dest = Path(directory) / "certificate.json"
    run = subprocess.run(
        [sys.executable, str(ROOT / "computations/verify_geometric_rotation.py"),
         "--output", str(dest)], cwd=ROOT, capture_output=True, text=True, timeout=180)
    assert run.returncode == 0, run.stdout + run.stderr
    actual = json.loads(dest.read_text(encoding="utf-8"))
    expected = json.loads((ROOT / "computations/geometric_rotation_certificate.json").read_text(encoding="utf-8"))
    assert actual == expected, "Geometric certificate mismatch"
print("PASS new standalone source closure, B integration and finite certificate; not a proof checker.")
