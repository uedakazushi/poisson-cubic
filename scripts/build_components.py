#!/usr/bin/env python3
"""Build the current Japanese componentwise section, plan and research notes.

Requires LuaLaTeX/LuaTeX-ja, Pandoc, pypdf. No network or Git writes.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "componentwise_reconstruction": ("tex/exports/componentwise_reconstruction.tex", "pdf/sections/componentwise_reconstruction.pdf"),
    "research_plan": ("00_research_plan.md", "pdf/research_plan.pdf"),
    "research_notes": ("research_notes.md", "pdf/research_notes.pdf"),
}
PREAMBLE = r'''\documentclass[a4paper,11pt]{ltjsarticle}
\usepackage[margin=24mm,headheight=16pt]{geometry}
\usepackage{amsmath,amssymb,mathtools,booktabs,longtable,array,enumitem,needspace}
\usepackage{xcolor}
\usepackage[unicode,colorlinks=true,linkcolor=blue!45!black,urlcolor=blue!45!black]{hyperref}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\setlength{\emergencystretch}{3em}
\setlength{\parskip}{0.2em}
\begin{document}
'''

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def closure(path: Path, seen: set[Path] | None = None) -> set[Path]:
    seen = set() if seen is None else seen
    if path in seen:
        return seen
    if not path.is_file():
        raise FileNotFoundError(path)
    seen.add(path)
    if path.suffix == ".tex":
        for inc in re.findall(r"\\(?:input|include)\{([^}]+)\}", path.read_text(encoding="utf-8")):
            child = ROOT / inc
            closure(child if child.suffix else child.with_suffix(".tex"), seen)
    return seen

def build(name: str, work: Path) -> dict:
    source_path, output_path = TARGETS[name]
    original = ROOT / source_path
    source = original
    if original.suffix == ".md":
        proc = subprocess.run(["pandoc", str(original), "--from=markdown+tex_math_dollars", "--to=latex", "--wrap=none"],
                              check=True, text=True, stdout=subprocess.PIPE)
        body = re.sub(r"\\texttt\{([^{}]+)\}", lambda m: "\\path{" + m.group(1).replace("\\_", "_") + "}" if "/" in m.group(1) else m.group(0), proc.stdout)
        source = work / f"{name}.tex"
        source.write_text(PREAMBLE + body + "\n\\end{document}\n", encoding="utf-8")
    previous = None
    for attempt in range(1, 6):
        run = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
                              f"-output-directory={work}", str(source)], cwd=ROOT,
                             text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if run.returncode:
            raise RuntimeError(run.stdout[-16000:])
        log = (work / f"{name}.log").read_text(errors="replace")
        aux = (work / f"{name}.aux").read_bytes()
        if attempt >= 2 and previous == aux and not re.search(r"Rerun to get|Rerun LaTeX|Label\(s\) may have changed", log):
            break
        previous = aux
    problems = [line for line in log.splitlines() if re.search(r"undefined|Missing character|Overfull|Rerun to get", line)]
    if problems:
        raise RuntimeError("Typesetting defects in " + name + "\n" + "\n".join(problems))
    target = ROOT / output_path
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(work / f"{name}.pdf", target)
    from pypdf import PdfReader
    inputs = closure(original)
    inputs.add(Path(__file__).resolve())
    return {"source": source_path, "pdf": output_path, "pages": len(PdfReader(target).pages),
            "passes": attempt, "undefined_references": 0, "missing_glyphs": 0, "overfull_boxes": 0,
            "pdf_sha256": digest(target),
            "input_sha256": {p.relative_to(ROOT).as_posix(): digest(p) for p in sorted(inputs)}}

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", choices=TARGETS, action="append")
    args = parser.parse_args()
    selected = args.only or list(TARGETS)
    for program in ("lualatex", "pandoc"):
        if not shutil.which(program):
            raise SystemExit(f"Required program missing: {program}")
    receipt = ROOT / "build_receipt_components.json"
    state = json.loads(receipt.read_text()) if receipt.exists() else {}
    with tempfile.TemporaryDirectory(prefix="nc-cubic-components-") as temporary:
        for name in selected:
            state[name] = build(name, Path(temporary))
            print(json.dumps({"name": name, "pages": state[name]["pages"], "passes": state[name]["passes"]}), flush=True)
    receipt.write_text(json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
