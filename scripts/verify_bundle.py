#!/usr/bin/env python3
"""Check current source closure, finite certificates, and delivery hashes."""

from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--write-hashes", action="store_true")
args = parser.parse_args()


def source_closure(path, seen=None):
    seen = set() if seen is None else seen
    if path in seen:
        return ""
    if not path.is_file():
        raise AssertionError(f"Missing source: {path.relative_to(ROOT)}")
    seen.add(path)
    text = path.read_text(encoding="utf-8")
    for child in re.findall(r"\\(?:input|include)\{([^}]+)\}", text):
        child_path = ROOT / child
        if not child_path.suffix:
            child_path = child_path.with_suffix(".tex")
        text += "\n" + source_closure(child_path, seen)
    return text


for name in ("cubic_poisson_rotation", "research_notes"):
    text = source_closure(ROOT / "tex" / f"{name}.tex")
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    assert len(labels) == len(set(labels)), f"Duplicate labels in {name}"
    refs = set(re.findall(r"\\(?:eqref|ref|pageref)\{([^}]+)\}", text))
    assert not refs.difference(labels), f"Missing labels in {name}: {refs.difference(labels)}"
    bibkeys = set(re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", text))
    citations = set()
    for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", text):
        citations.update(k.strip() for k in group.split(","))
    assert not citations.difference(bibkeys), f"Missing citations in {name}: {citations.difference(bibkeys)}"
    assert (ROOT / "pdf" / f"{name}.pdf").is_file(), f"Missing PDF: {name}"

for name in ("verify_algebra.py", "verify_rotation_obstructions.py", "verify_geometry.py", "verify_hesse_center.py"):
    result = subprocess.run([sys.executable, str(ROOT / "computations" / name)],
                            cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if result.returncode:
        raise AssertionError(result.stdout)
    print(f"PASS {name}")

required = ("00_research_plan.md", "pdf/research_plan.pdf", "README.md", "AGENTS.md", "validation.json")
for name in required:
    assert (ROOT / name).is_file(), f"Missing required file: {name}"

files = sorted(p for p in ROOT.rglob("*") if p.is_file()
               and ".git" not in p.relative_to(ROOT).parts
               and p.name != "SHA256SUMS")
for p in files:
    assert p.suffix not in {".aux", ".log", ".toc", ".out", ".pyc", ".zip", ".bak"}, p
    assert "__pycache__" not in p.parts, p
lines = [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT).as_posix()}" for p in files]
expected = "\n".join(lines) + "\n"
hash_path = ROOT / "SHA256SUMS"
if args.write_hashes:
    hash_path.write_text(expected, encoding="utf-8")
else:
    if not hash_path.is_file():
        raise SystemExit("SHA256SUMS missing: rebuild the current PDFs, then run --write-hashes.")
    assert hash_path.read_text(encoding="utf-8") == expected, "Checksum or file inventory mismatch"
print(json.dumps({"status": "passed", "files_hashed": len(files),
                  "source_closure": "complete", "reference_check": "passed"}, ensure_ascii=False))
