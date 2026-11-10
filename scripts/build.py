#!/usr/bin/env python3
"""Build main papers with LuaLaTeX and record exact source/PDF correspondence."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ("poisson_cubic_quantization", "generic17_ambient_recovery", "rotation_cubic_reconstruction")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_closure(path, seen=None):
    seen = set() if seen is None else seen
    path = path.resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        raise SystemExit("Missing or external TeX input: " + str(path))
    if path in seen:
        return seen
    seen.add(path)
    for name in re.findall(r"\\(?:input|include)\{([^}]+)\}", path.read_text()):
        sub = ROOT / name
        source_closure(sub if sub.suffix else sub.with_suffix(".tex"), seen)
    return seen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", action="append", choices=PAPERS)
    args = parser.parse_args()
    if not shutil.which("latexmk") or not shutil.which("lualatex"):
        raise SystemExit("latexmk and LuaLaTeX with LuaTeX-ja are required")
    env = dict(os.environ, SOURCE_DATE_EPOCH="1794268800", FORCE_SOURCE_DATE="1")
    engine = subprocess.run(
        ["lualatex", "--version"], capture_output=True, text=True, check=True
    ).stdout.splitlines()[0]
    for name in args.only or PAPERS:
        source = ROOT / "papers" / (name + ".tex")
        inputs = source_closure(source)
        subprocess.run(["latexmk", str(source.relative_to(ROOT))], cwd=ROOT, env=env, check=True)
        pdf = ROOT / "build" / (name + ".pdf")
        if not pdf.is_file():
            raise SystemExit("Missing compiled PDF: " + str(pdf))
        log = (ROOT / "build" / (name + ".log")).read_text(errors="replace")
        failures = {
            "undefined_references": bool(re.search(r"There were undefined references|Reference .* undefined", log)),
            "undefined_citations": bool(re.search(r"Citation .* undefined", log)),
            "missing_glyphs": "Missing character:" in log,
            "overfull_boxes": bool(re.search(r"Overfull \\[hv]box", log)),
        }
        if any(failures.values()):
            raise SystemExit("Typesetting checks failed: " + json.dumps(failures))
        receipt = {
            "version": json.loads((ROOT / "validation.json").read_text(encoding="utf-8"))["version"],
            "source": source.relative_to(ROOT).as_posix(),
            "tex_inputs": {p.relative_to(ROOT).as_posix(): sha(p) for p in sorted(inputs)},
            "build_config_sha256": sha(ROOT / ".latexmkrc"),
            "pdf": pdf.relative_to(ROOT).as_posix(),
            "pdf_sha256": sha(pdf),
            "engine": engine,
            "source_date_epoch": env["SOURCE_DATE_EPOCH"],
            "typesetting_failures": failures,
            "scope": "Typesetting and source correspondence only; not a mathematical proof audit.",
        }
        dest = ROOT / "build" / (name + ".receipt.json")
        dest.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
        print(f"BUILT {pdf.relative_to(ROOT)} ({pdf.stat().st_size} bytes; {len(inputs)} TeX inputs)")


if __name__ == "__main__":
    main()
