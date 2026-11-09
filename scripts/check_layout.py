#!/usr/bin/env python3
"""Check repository layout and TeX dependency closure without compiling mathematics."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MAIN = (
    "papers/poisson_cubic_quantization.tex",
    "papers/generic17_ambient_recovery.tex",
    "papers/rotation_cubic_reconstruction.tex",
    "papers/reconstruction/rotation_saturation_reduction.tex",
    "papers/exports/componentwise_reconstruction.tex",
    "notes/research_notes.tex",
    "notes/reconstruction_notes.tex",
)
seen = set()

def visit(rel):
    path = ROOT / rel
    if not path.is_file():
        raise SystemExit(f"Broken TeX input: {rel}")
    if rel in seen:
        return
    seen.add(rel)
    for name in re.findall(r"\\(?:input|include)\{([^}]+)\}", path.read_text(encoding="utf-8")):
        if name.startswith(("tex/", "reconstruction/tex/")):
            raise SystemExit(f"Obsolete input in {rel}: {name}")
        visit(name if name.endswith(".tex") else name+".tex")

for entry in MAIN:
    visit(entry)
if (ROOT/"tex").exists() or (ROOT/"pdf").exists():
    raise SystemExit("Legacy tex/ or pdf/ directory remains")
for item in ("AGENTS.md","00_research_plan.md","notes/research_notes.md",
             "notes/reconstruction.md",".latexmkrc","papers/README.md","notes/README.md"):
    if not (ROOT/item).is_file():
        raise SystemExit("Required source missing: "+item)
result = subprocess.run(["git","ls-files","-z"], cwd=ROOT, capture_output=True, check=True)
tracked = [p.decode() for p in result.stdout.split(b"\0") if p]
bad_pdf = [p for p in tracked if p.endswith(".pdf") and not (p.startswith("papers/pdf-only/") or p.startswith("notes/pdf-only/"))]
if bad_pdf:
    raise SystemExit("Generated PDFs are tracked: "+", ".join(bad_pdf))
print(f"PASS: {len(MAIN)} document roots, {len(seen)} TeX files in their closure, "
      f"{sum(p.endswith('.pdf') for p in tracked)} preserved PDF-only originals.")
