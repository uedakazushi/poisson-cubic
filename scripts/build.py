#!/usr/bin/env python3
"""Compile the current LuaLaTeX paper and record source/PDF parity."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ("poisson-cubic",)
SUPPORT = ROOT / "papers" / "support"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_input(name: str) -> Path:
    candidate = Path(name if name.endswith(".tex") else name + ".tex")
    for root in (ROOT, SUPPORT):
        path = (root / candidate).resolve()
        if path.is_relative_to(ROOT) and path.is_file():
            return path
    raise FileNotFoundError(f"Missing TeX input: {name}")


def source_closure(path: Path, seen=None) -> set[Path]:
    seen = set() if seen is None else seen
    path = path.resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        raise FileNotFoundError(path)
    if path in seen:
        return seen
    seen.add(path)
    for name in re.findall(r"\\(?:input|include)\{([^}]+)\}", path.read_text(encoding="utf-8")):
        source_closure(resolve_input(name), seen)
    return seen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", choices=PAPERS, action="append")
    args = parser.parse_args()
    if not shutil.which("latexmk") or not shutil.which("lualatex"):
        raise SystemExit("latexmk and LuaLaTeX (LuaTeX-ja) are required")
    engine = subprocess.run(["lualatex", "--version"], text=True,
                            capture_output=True, check=True).stdout.splitlines()[0]
    env = dict(os.environ, SOURCE_DATE_EPOCH="1794441600", FORCE_SOURCE_DATE="1")
    for name in args.only or PAPERS:
        source = ROOT / "papers" / (name + ".tex")
        inputs = source_closure(source)
        subprocess.run(["latexmk", "-r", ".latexmkrc", source.relative_to(ROOT).as_posix()],
                       cwd=ROOT, env=env, check=True)
        pdf = ROOT / "build" / (name + ".pdf")
        log = ROOT / "build" / (name + ".log")
        if not pdf.is_file() or not log.is_file():
            raise SystemExit("Missing output PDF or log for " + name)
        messages = log.read_text(errors="replace")
        failures = {
            "undefined_references": bool(re.search(r"Reference .* undefined|There were undefined references", messages)),
            "undefined_citations": bool(re.search(r"Citation .* undefined|There were undefined citations", messages)),
            "missing_glyphs": "Missing character:" in messages,
            "overfull_boxes": bool(re.search(r"Overfull \\[hv]box", messages)),
        }
        if any(failures.values()):
            raise SystemExit("Typesetting warnings: " + json.dumps(failures))
        receipt = {
            "version": json.loads((ROOT / "validation.json").read_text())["version"],
            "source": source.relative_to(ROOT).as_posix(),
            "tex_inputs": {p.relative_to(ROOT).as_posix(): sha(p) for p in sorted(inputs)},
            "build_config_sha256": sha(ROOT / ".latexmkrc"),
            "pdf": pdf.relative_to(ROOT).as_posix(),
            "pdf_sha256": sha(pdf),
            "engine": engine,
            "source_date_epoch": env["SOURCE_DATE_EPOCH"],
            "typesetting_failures": failures,
            "scope": "Typesetting and file parity only; not independent mathematical verification.",
        }
        (ROOT / "build" / (name + ".receipt.json")).write_text(
            json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("BUILT", pdf.relative_to(ROOT), len(inputs), "TeX inputs")


if __name__ == "__main__":
    main()
