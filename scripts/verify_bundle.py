#!/usr/bin/env python3
"""Source-only checks by default; --require-pdfs enforces current receipts.

--run-computations reruns a small, explicit set of exact sanity checks.
A successful check does not verify categorical arguments or theorem hypotheses.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess
import sys

from build import ROOT, PAPERS, source_closure, sha


def contents(files: set[Path]) -> str:
    return "\n".join(p.read_text(encoding="utf-8") for p in sorted(files))


def audit(name: str, require_pdfs: bool):
    source = ROOT / "papers" / (name + ".tex")
    seen = source_closure(source)
    body = contents(seen)
    labels = re.findall(r"\\label\{([^}]+)\}", body)
    refs = re.findall(r"\\(?:eqref|ref|pageref|autoref)\{([^}]+)\}", body)
    keys = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", body)
    citations = [c.strip() for group in re.findall(
        r"\\cite(?:\[[^\]]*\])*\{([^}]+)\}", body) for c in group.split(",")]
    if len(set(labels)) != len(labels):
        raise AssertionError(f"{name}: duplicate labels")
    if len(set(keys)) != len(keys):
        raise AssertionError(f"{name}: duplicate bibliography keys")
    if set(refs) - set(labels):
        raise AssertionError(f"{name}: unresolved references {set(refs)-set(labels)}")
    if set(citations) - set(keys):
        raise AssertionError(f"{name}: unresolved citations {set(citations)-set(keys)}")
    if name == "nc-cubic":
        assert r"\numberwithin{equation}{section}" in body
        assert not re.search(
            r"\\\[|\\\]|\\(?:begin|end)\{(?:equation|align|gather|multline|flalign|alignat)\*\}|\\tag\*?\{", body)
    print(f"PASS {name} source closure: {len(seen)} files; labels={len(labels)}, refs={len(refs)}, citations={len(citations)}")
    pdf = ROOT / "build" / (name + ".pdf")
    receipt = ROOT / "build" / (name + ".receipt.json")
    if not pdf.is_file() or not receipt.is_file():
        if require_pdfs:
            raise AssertionError(f"Missing current typesetting receipt/PDF for {name}")
        print(f"PENDING {name} PDF and receipt (not a source error)")
        return
    record = json.loads(receipt.read_text(encoding="utf-8"))
    expected_paths = {p.relative_to(ROOT).as_posix() for p in seen}
    assert record["source"] == source.relative_to(ROOT).as_posix()
    assert set(record["tex_inputs"]) == expected_paths, f"{name}: mismatched TeX input list"
    for rel, value in record["tex_inputs"].items():
        assert sha(ROOT / rel) == value, f"{name}: stale TeX input {rel}"
    assert sha(pdf) == record["pdf_sha256"], f"{name}: changed PDF"
    assert sha(ROOT / ".latexmkrc") == record["build_config_sha256"]
    assert not any(record["typesetting_failures"].values())
    print(f"PASS {name} current source/PDF receipt")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--only", choices=PAPERS, action="append")
    p.add_argument("--require-pdfs", action="store_true")
    p.add_argument("--run-computations", action="store_true")
    args = p.parse_args()
    for path in ["00_research_plan.md", "notes/research_notes.md", "AGENTS.md", "README.md", "validation.json"]:
        assert (ROOT / path).is_file(), path
    for name in args.only or PAPERS:
        audit(name, args.require_pdfs)
    if args.run_computations:
        for path in ["computations/verify_poisson_stack_component_counts.py",
                     "computations/verify_poisson_article_A.py"]:
            run = subprocess.run([sys.executable, str(ROOT / path)], cwd=ROOT,
                                 capture_output=True, text=True, timeout=180)
            if run.returncode:
                raise AssertionError(f"{path} failed: {run.stdout}\n{run.stderr}")
            print(f"PASS finite sanity test {path}")
    print("LIMIT: source checks and finite calculations are not mathematical proof audits.")


if __name__ == "__main__":
    main()
