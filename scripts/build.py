#!/usr/bin/env python3
"""Build the three main papers using the root .latexmkrc (LuaLaTeX, ignored PDFs)."""
from pathlib import Path
import argparse
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ("poisson_cubic_quantization", "generic17_ambient_recovery", "rotation_cubic_reconstruction")
parser = argparse.ArgumentParser()
parser.add_argument("--only", action="append", choices=PAPERS)
args = parser.parse_args()
if not shutil.which("latexmk") or not shutil.which("lualatex"):
    raise SystemExit("latexmk and LuaLaTeX with LuaTeX-ja are required")
for name in args.only or PAPERS:
    source = Path("papers") / (name + ".tex")
    subprocess.run(["latexmk", str(source)], cwd=ROOT, check=True)
    output = ROOT / "build" / (name + ".pdf")
    if not output.is_file():
        raise SystemExit("Missing compiled PDF: " + str(output))
    print(f"BUILT {output.relative_to(ROOT)} ({output.stat().st_size} bytes)")
