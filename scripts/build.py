#!/usr/bin/env python3
"""Build the three current Japanese LuaLaTeX papers, keeping TeX/PDF separate.

Requires LuaLaTeX, LuaTeX-ja, standard mathematical TeX packages.
No Actions, network access or generated TeX cache in the repository.
"""
from pathlib import Path
import argparse
import re
import shutil
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parents[1]
PAPERS=("poisson_cubic_quantization","generic17_ambient_recovery","rotation_cubic_reconstruction")
parser=argparse.ArgumentParser()
parser.add_argument("--only",action="append",choices=PAPERS)
args=parser.parse_args()
if not shutil.which("lualatex"):
    raise SystemExit("LuaLaTeX is required")
for name in args.only or PAPERS:
    source=ROOT/"tex"/f"{name}.tex"
    if not source.exists():
        raise SystemExit(f"Missing source: {source}")
    with tempfile.TemporaryDirectory(prefix="nc-cubic-lualatex-") as d:
        work=Path(d)
        previous=None
        for attempt in range(1,6):
            r=subprocess.run(["lualatex","-interaction=nonstopmode","-halt-on-error",
                "-file-line-error",f"-output-directory={work}",str(source)],
                cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            if r.returncode:
                print(r.stdout[-16000:])
                raise SystemExit(f"LuaLaTeX failed: {name}, pass {attempt}")
            log=(work/f"{name}.log").read_text(errors="replace")
            aux=(work/f"{name}.aux").read_bytes()
            if attempt>1 and aux==previous and not re.search(
                 r"Rerun to get|Label\(s\) may have changed|Rerun LaTeX",log):
                break
            previous=aux
        defects=[l for l in log.splitlines()
           if re.search(r"Undefined control sequence|There were undefined references|"
               r"Citation .* undefined|Reference .* undefined|Missing character|"
               r"Overfull \\hbox|Overfull \\vbox",l)]
        if defects:
            print("\n".join(defects[:40]))
            raise SystemExit(f"Unresolved typesetting issues in {name}")
        target=ROOT/"pdf"/f"{name}.pdf"
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(work/f"{name}.pdf",target)
        print(f"BUILT {target.relative_to(ROOT)} ({attempt} passes, {target.stat().st_size} bytes)")
