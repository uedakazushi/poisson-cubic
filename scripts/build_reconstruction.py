#!/usr/bin/env python3
"""Build current research-note LaTeX files without tracking their PDF outputs."""
from pathlib import Path
import argparse
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("research_notes", "reconstruction_notes")
parser = argparse.ArgumentParser()
parser.add_argument("--only", action="append", choices=NAMES)
args = parser.parse_args()
if not shutil.which("latexmk"):
    raise SystemExit("latexmk is required")
for name in args.only or NAMES:
    source = Path("notes") / (name + ".tex")
    subprocess.run(["latexmk", str(source)], cwd=ROOT, check=True)
    print("BUILT build/" + name + ".pdf")
