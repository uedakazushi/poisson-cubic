#!/usr/bin/env python3
"""Validate the paper-C export and exact certificates; not a categorical proof assistant."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import tempfile

REPO = Path(__file__).resolve().parents[2]
SCOPE = REPO/"reconstruction"

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def require(condition, message):
    if not condition:
        raise SystemExit(message)

def expanded(path, seen):
    path = path.resolve()
    require(path.is_relative_to(REPO), "TeX outside repo: "+str(path))
    require(path.is_file(), "Missing TeX: "+str(path))
    require(path not in seen, "Repeated/cyclic TeX input: "+str(path))
    seen.add(path)
    body = path.read_text(encoding="utf-8")
    def include(m):
        rel = m.group(1)
        return expanded(REPO/(rel if rel.endswith(".tex") else rel+".tex"), seen)
    return re.sub(r"\\input\{([^}]+)\}", include, body)

def main():
    for p in (SCOPE/"README.md", SCOPE/"validation.json", SCOPE/"requirements.txt",
              SCOPE/"build_receipt.json", REPO/"notes/reconstruction.md",
              REPO/"build/rotation_saturation_reduction.pdf"):
        require(p.is_file(), "Missing: "+str(p))
    seen = set()
    body = expanded(REPO/"papers/reconstruction/rotation_saturation_reduction.tex", seen)
    labels = re.findall(r"\\label\{([^}]+)\}", body)
    refs = re.findall(r"\\(?:eqref|ref|pageref)\{([^}]+)\}", body)
    require(len(labels)==len(set(labels)), "Duplicate labels")
    require(set(refs)<=set(labels), "Unresolved references: "+str(set(refs)-set(labels)))
    bibs = re.findall(r"\\bibitem\{([^}]+)\}", body)
    require(len(bibs)==len(set(bibs)), "Duplicate bibliography entries")
    cites = {v.strip() for s in re.findall(r"\\cite(?:\[[^]]*\])*\{([^}]+)\}", body) for v in s.split(",")}
    require(cites<=set(bibs), "Unresolved citations: "+str(cites-set(bibs)))
    receipt = json.loads((SCOPE/"build_receipt.json").read_text(encoding="utf-8"))
    require(set(receipt["tex_inputs"])=={p.relative_to(REPO).as_posix() for p in seen},
            "Build receipt missing TeX inputs")
    for rel, expected in receipt["tex_inputs"].items():
        require(sha(REPO/rel)==expected, "Input changed: "+rel)
    for field in ("pdf", "source"):
        require(sha(REPO/receipt[field])==receipt[field+"_sha256"],
                "Receipt mismatch: "+field)
    pairs = (("verify_nonelliptic_inputs.py", "input_checks.json"),
             ("verify_etale_inputs.py", "etale_input_checks.json"),
             ("verify_hochschild_sectors.py", "hochschild_sector_checks.json"))
    with tempfile.TemporaryDirectory() as td:
        for script, certificate in pairs:
            p = Path(td)/certificate
            run = subprocess.run([sys.executable, str(SCOPE/"computations"/script),
                                  "--output", str(p)], capture_output=True, text=True, timeout=120)
            require(run.returncode==0, run.stdout+"\n"+run.stderr)
            expected = json.loads((SCOPE/"computations"/certificate).read_text())
            require(json.loads(p.read_text())==expected, "Certificate mismatch: "+certificate)
    print(json.dumps({"source_closure":len(seen),"labels":len(labels),
                      "bibliography_entries":len(bibs),"build_parity":"passed",
                      "exact_certificates":"passed","categorical_proof":"not formalized"},
                     ensure_ascii=False, indent=2))

if __name__=="__main__":
    main()
