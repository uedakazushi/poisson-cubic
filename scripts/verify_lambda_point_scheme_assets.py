#!/usr/bin/env python3
"""Regenerate exact finite lambda-point-scheme certificate and audit source closure.
This script does not prove the Sklyanin point-scheme theorem.
"""
from pathlib import Path
import json, re, subprocess, sys, tempfile
root=Path(__file__).resolve().parents[1]
for p in ("papers/support/papers/reconstruction/point_scheme_lambda_family.tex",
          "papers/support/papers/point_scheme_lambda_family.tex",
          "computations/verify_lambda_point_scheme.py",
          "computations/lambda_point_scheme_certificate.json"):
    assert (root/p).is_file(),p
tex=(root/"papers/support/papers/reconstruction/point_scheme_lambda_family.tex").read_text()
entry=(root/"papers/support/papers/point_scheme_lambda_family.tex").read_text()
parent=(root/"papers/paper_b.tex").read_text()
assert r"\input{papers/reconstruction/point_scheme_lambda_family}" in entry
assert r"\input{papers/reconstruction/point_scheme_lambda_family}" in parent
for label in ("psl:lem:free","psl:thm:universal-flat","psl:cor:collision"):
    assert r"\label{"+label+"}" in tex
with tempfile.TemporaryDirectory(prefix="nc-cubic-lambda-") as tmp:
    dest=Path(tmp)/"certificate.json"
    run=subprocess.run([sys.executable,str(root/"computations/verify_lambda_point_scheme.py"),"--output",str(dest)],
                       cwd=root, capture_output=True,text=True,timeout=180)
    assert run.returncode==0,run.stdout+run.stderr
    expected=json.loads((root/"computations/lambda_point_scheme_certificate.json").read_text())
    actual=json.loads(dest.read_text())
    assert actual==expected
print("PASS relative lambda source closure and exact certificate; NOT point-functor formal verification.")
