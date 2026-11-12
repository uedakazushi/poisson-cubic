#!/usr/bin/env python3
"""Audit v36 source closure and optionally rerun the unchanged orbit certificate.

This is not a proof assistant. The saturation and coherent-category assertions
are mathematical theorems with explicit hypotheses in the manuscript.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / "papers/support/papers/coherent_residual_saturation.tex"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rerun-orbit", action="store_true")
    args = parser.parse_args()
    seen: set[Path] = set()

    def closure(path: Path) -> str:
        if path in seen:
            return ""
        if not path.is_file():
            raise AssertionError(f"Missing TeX input: {path}")
        seen.add(path)
        text = path.read_text(encoding="utf-8")
        result = text
        for name in re.findall(r"\\(?:input|include)\{([^}]+)\}", text):
            child = ROOT / "papers/support" / name
            if not child.suffix:
                child = child.with_suffix(".tex")
            result += "\n" + closure(child)
        return result

    text = closure(ENTRY)
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", text)
    bib = re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", text)
    cites = [key.strip() for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", text)
             for key in group.split(",")]
    assert len(labels) == len(set(labels)), "Duplicate labels"
    assert len(bib) == len(set(bib)), "Duplicate bibliography keys"
    assert not set(refs) - set(labels), set(refs) - set(labels)
    assert not set(cites) - set(bib), set(cites) - set(bib)
    parent = (ROOT / "papers/paper_b.tex").read_text(encoding="utf-8")
    shared = (ROOT / "papers/support/papers/references.tex").read_text(encoding="utf-8")
    assert r"\input{papers/reconstruction/coherent_residual_saturation}" in parent
    assert r"\input{papers/reconstruction/coherent_residual_references}" in shared
    if args.rerun_orbit:
        with tempfile.TemporaryDirectory(prefix="nc-cubic-v36-") as tmp:
            output = Path(tmp) / "orbit.json"
            result = subprocess.run(
                [sys.executable, str(ROOT / "computations/verify_rotation_orbit.py"),
                 "--output", str(output)], cwd=ROOT, capture_output=True, text=True, timeout=180)
            if result.returncode:
                raise RuntimeError(result.stdout + result.stderr)
            expected = json.loads((ROOT / "computations/rotation_orbit_certificate.json").read_text(encoding="utf-8"))
            actual = json.loads(output.read_text(encoding="utf-8"))
            assert actual == expected, "Existing orbit certificate mismatch"
        print("PASS new source integration and unchanged 64 Euler/41 MF checks; not a categorical proof checker.")
    else:
        print("PASS new source closure and B integration; numerical and categorical proofs not rerun.")


if __name__ == "__main__":
    main()
