#!/usr/bin/env python3
"""Audit references, exact certificates, and current source/PDF snapshots.

--source-only omits PDF receipts in a parent checkout without exports.
--write-hashes and --check-hashes concern the entire scoped bundle inventory.
This is not a proof assistant for categorical results.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from build_components import ROOT, closure

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inventory() -> str:
    paths = sorted(p for p in ROOT.rglob("*") if p.is_file() and p.name != "SHA256SUMS"
                   and not any(part in (".git", "__pycache__") for part in p.relative_to(ROOT).parts))
    return "".join(f"{sha(p)}  {p.relative_to(ROOT).as_posix()}\n" for p in paths)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-hashes", action="store_true")
    parser.add_argument("--check-hashes", action="store_true")
    parser.add_argument("--source-only", action="store_true")
    args = parser.parse_args()
    paths = closure(ROOT / "papers/exports/componentwise_reconstruction.tex")
    body = "\n".join(p.read_text(encoding="utf-8") for p in sorted(paths))
    labels = re.findall(r"\\label\{([^}]+)\}", body)
    refs = re.findall(r"\\(?:eqref|ref|pageref)\{([^}]+)\}", body)
    keys = re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", body)
    cites = {k.strip() for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", body) for k in group.split(",")}
    assert len(labels) == len(set(labels)), "Duplicate labels"
    assert len(keys) == len(set(keys)), "Duplicate bibliography keys"
    assert not set(refs) - set(labels), ("Unresolved references", set(refs) - set(labels))
    assert not cites - set(keys), ("Unresolved citations", cites - set(keys))
    print(f"PASS source closure: {len(paths)} files, {len(labels)} labels")
    run = subprocess.run([sys.executable, str(ROOT / "computations/verify_componentwise_reconstruction.py")],
                         cwd=ROOT, text=True, capture_output=True, check=True)
    actual = json.loads(run.stdout)
    expected = json.loads((ROOT / "computations/componentwise_checks.json").read_text())
    assert actual == expected, "Computation certificate mismatch"
    print("PASS exact computations and universal free-algebra certificate")
    if not args.source_only:
        receipt = json.loads((ROOT / "build_receipt_components.json").read_text())
        assert set(receipt) == {"componentwise_reconstruction", "research_plan", "research_notes"}
        for name, item in receipt.items():
            assert sha(ROOT / item["pdf"]) == item["pdf_sha256"], (name, "PDF changed")
            for path, value in item["input_sha256"].items():
                assert sha(ROOT / path) == value, (name, "source changed", path)
            print(f"PASS source/PDF snapshot: {name} ({item['pages']} pages)")
    if args.write_hashes:
        (ROOT / "SHA256SUMS").write_text(inventory(), encoding="utf-8")
    if args.check_hashes:
        assert (ROOT / "SHA256SUMS").read_text() == inventory(), "Inventory/hash mismatch"
        print("PASS all inventory hashes")
    print("LIMIT: Relative saturation and categorical reconstruction are not formally verified.")

if __name__ == "__main__":
    main()
