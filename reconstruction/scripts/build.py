#!/usr/bin/env python3
"""Build the standalone paper-C reconstruction export with the root .latexmkrc."""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess

REPO = Path(__file__).resolve().parents[2]
SCOPE = REPO / "reconstruction"
SOURCE = REPO / "papers/support/papers/reconstruction/rotation_saturation_reduction.tex"
INPUTS = [SOURCE, REPO/"papers/support/papers/reconstruction/etale_realization.tex",
          REPO/"papers/support/papers/reconstruction/hochschild_obstructions.tex",
          REPO/"papers/support/papers/reconstruction/etale_references.tex"]
PDF = REPO / "build/rotation_saturation_reduction.pdf"

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    if not shutil.which("latexmk") or not shutil.which("lualatex"):
        raise SystemExit("latexmk and LuaLaTeX are required")
    for p in INPUTS:
        if not p.is_file():
            raise SystemExit("Missing TeX input: "+str(p))
    env = dict(os.environ, SOURCE_DATE_EPOCH="1794268800", FORCE_SOURCE_DATE="1")
    subprocess.run(["latexmk", str(SOURCE.relative_to(REPO))], cwd=REPO, env=env, check=True)
    if not PDF.is_file():
        raise SystemExit("Expected PDF missing: "+str(PDF))
    log = (REPO/"build"/(SOURCE.stem+".log")).read_text(errors="replace")
    checks = {
        "undefined_references": bool(re.search("There were undefined references|Reference .* undefined", log)),
        "undefined_citations": bool(re.search("Citation .* undefined", log)),
        "missing_glyphs": "Missing character:" in log,
        "overfull_boxes": "Overfull \\hbox" in log or "Overfull \\vbox" in log
    }
    if any(checks.values()):
        raise SystemExit("Typesetting warning: "+str(checks))
    receipt = {
        "version": "v21",
        "source": SOURCE.relative_to(REPO).as_posix(),
        "source_sha256": sha(SOURCE),
        "tex_inputs": {p.relative_to(REPO).as_posix(): sha(p) for p in INPUTS},
        "pdf": PDF.relative_to(REPO).as_posix(), "pdf_sha256": sha(PDF),
        "engine": subprocess.run(["lualatex", "--version"], capture_output=True, text=True,
                                 check=True).stdout.splitlines()[0],
        "typesetting_failures": checks,
        "source_date_epoch": env["SOURCE_DATE_EPOCH"],
        "scope": "Standalone current paper-C section; not a rebuild of all main papers."
    }
    (SCOPE/"build_receipt.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))

if __name__=="__main__":
    main()
