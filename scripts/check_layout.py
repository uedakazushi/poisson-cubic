#!/usr/bin/env python3
"""Check the current A/B source layout and exclude tracked PDFs."""
from pathlib import Path
import subprocess

from build import ROOT, PAPERS, source_closure


def main():
    assert sorted(x.name for x in (ROOT / "papers").glob("paper_*.tex")) == [
        "paper_a.tex", "paper_b.tex"
    ], "Only the two current A/B papers may be top-level paper_*.tex"
    seen = set()
    for name in PAPERS:
        seen |= source_closure(ROOT / "papers" / (name + ".tex"))
    for path in ("AGENTS.md", "00_research_plan.md", "README.md",
                 "papers/support/papers/README.md", "notes/README.md", ".latexmkrc",
                 ".vscode/settings.json", "validation.json"):
        assert (ROOT / path).is_file(), "Required file missing: " + path
    for path in ("papers/paper_c.tex", "papers/paper_b_old.tex"):
        assert not (ROOT / path).exists(), "Obsolete paper entry: " + path
    tracked = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT,
                             capture_output=True, check=True).stdout.split(b"\0")
    pdf = [x.decode() for x in tracked if x.lower().endswith(b".pdf")]
    assert not pdf, "Tracked PDFs: " + ", ".join(pdf)
    print(f"PASS: papers A/B, {len(seen)} distinct TeX inputs, 0 tracked PDFs")


if __name__ == "__main__":
    main()
