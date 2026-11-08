#!/usr/bin/env python3
"""Rebuild the current Japanese PDFs without retaining TeX intermediates.

Requirements: Python 3, LuaLaTeX with ltjsarticle, Pandoc, and the packages
listed in README.md. No network access or GitHub Actions is used.
"""

from pathlib import Path
import argparse
import json
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("cubic_poisson_rotation", "research_notes", "research_plan")
parser = argparse.ArgumentParser()
parser.add_argument("--only", choices=NAMES, action="append")
args = parser.parse_args()
selected = args.only or list(NAMES)

if not shutil.which("lualatex"):
    raise SystemExit("LuaLaTeX with Japanese TeX support is required.")
if "research_plan" in selected and not shutil.which("pandoc"):
    raise SystemExit("Pandoc is required to render the research plan.")

results = []
with tempfile.TemporaryDirectory(prefix="nc-cubic-build-") as temporary:
    work = Path(temporary)
    for name in selected:
        source = ROOT / "tex" / f"{name}.tex"
        if name == "research_plan":
            body = subprocess.run(
                ["pandoc", str(ROOT / "00_research_plan.md"),
                 "--from=markdown+tex_math_dollars", "--to=latex", "--wrap=none"],
                check=True, stdout=subprocess.PIPE, text=True).stdout
            # Keep section headings with their opening paragraph or table.
            body = re.sub(r"(?=\\hypertarget\{)", lambda _: "\\Needspace{10\\baselineskip}\n", body)
            source = work / "research_plan.tex"
            source.write_text(
                "\\input{tex/common}\n"
                "\\usepackage{needspace}\n"
                "\\providecommand{\\tightlist}{\\setlength{\\itemsep}{0pt}\\setlength{\\parskip}{0pt}}\n"
                "\\hypersetup{pdftitle={研究方針：3次超曲面のPoisson構造と非可換化}}\n"
                "\\begin{document}\n" + body + "\n\\end{document}\n", encoding="utf-8")
        last_aux = None
        for pass_number in range(1, 5):
            result = subprocess.run(
                ["lualatex", "-interaction=nonstopmode", "-halt-on-error",
                 "-file-line-error", f"-output-directory={work}", str(source)],
                cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if result.returncode:
                print(result.stdout[-18000:])
                raise SystemExit(f"LuaLaTeX failed: {name}, pass {pass_number}")
            log = (work / f"{name}.log").read_text(encoding="utf-8", errors="replace")
            aux = (work / f"{name}.aux").read_bytes()
            rerun = bool(re.search(r"Rerun to get|Rerun LaTeX|Label\(s\) may have changed", log))
            if pass_number >= 2 and aux == last_aux and not rerun:
                break
            last_aux = aux
        problems = [line for line in log.splitlines()
                    if re.search(r"Overfull|undefined|Rerun to get|Missing character", line)]
        if problems:
            print("\n".join(problems))
            # Preserve failed diagnostics outside the deliverable tree.
            diagnostic_dir = ROOT.parent / "work" / "tex-diagnostics"
            diagnostic_dir.mkdir(parents=True, exist_ok=True)
            for suffix in ("log", "pdf"):
                p = work / f"{name}.{suffix}"
                if p.exists():
                    shutil.copy2(p, diagnostic_dir / p.name)
            raise SystemExit(f"Resolve reference/layout warnings: {name}; diagnostics in {diagnostic_dir}")
        target = ROOT / "pdf" / f"{name}.pdf"
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(work / target.name, target)
        item = {"document": target.name, "passes": pass_number,
                "undefined_references": 0, "missing_glyphs": 0, "overfull_boxes": 0}
        results.append(item)
        print(json.dumps(item, ensure_ascii=False), flush=True)
print("All selected PDFs built successfully.")
