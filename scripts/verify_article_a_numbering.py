#!/usr/bin/env python3
"""Check article A has numbered display equations, valid citations and labels.

Run from repository root: python3 scripts/verify_article_a_numbering.py
This is a STATIC source audit, not a LuaLaTeX build. It follows direct
\\input statements in the article A entrypoint. It does not number tables.
"""
from collections import Counter
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
start = root / "papers/poisson-cubic.tex"
paths = [start]
visited = set()
texts = []

def visit(path):
    if path in visited:
        return
    visited.add(path)
    source = path.read_text(encoding="utf-8")
    paths.append(path) if path != start else None
    texts.append(source)
    for ref in re.findall(r"\\input\{([^}]+)\}", source):
        relative = Path(ref if ref.endswith(".tex") else ref + ".tex")
        # Prefer explicit paths from the repository root; support older
        # auxiliary inputs that were relative to papers/support/.
        candidates = [root / relative, root / "papers/support" / relative]
        target = next((p for p in candidates if p.is_file()), None)
        if target is None:
            raise AssertionError(f"Missing input {ref}; tried: {candidates}")
        visit(target)

visit(start)
body = "\n".join(texts)
unused = []
total = 0
for p, source in zip(paths, texts):
    nbegin = len(re.findall(r"\\begin\{equation\}", source))
    nend = len(re.findall(r"\\end\{equation\}", source))
    assert nbegin == nend, f"{p}: unbalanced equation environments"
    total += nbegin
    assert "\\[" not in source and "\\]" not in source, f"{p}: unnumbered display"
    assert not re.search(r"\\(?:begin|end)\{(?:align|equation|gather|multline|flalign|alignat)\*\}", source), f"{p}: starred unnumbered math"
    assert not re.search(r"\\tag\*?\{", source), f"{p}: non-numeric custom equation tag"

labels = re.findall(r"\\label\{([^}]+)\}", body)
refs = re.findall(r"\\(?:eqref|ref|autoref|pageref)\{([^}]+)\}", body)
bibliography = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", body)
citations = [s.strip() for v in re.findall(r"\\cite(?:\[[^\]]*\])*\{([^}]+)\}", body)
             for s in v.split(",")]
for name, values in [("label", labels), ("bibitem", bibliography)]:
    duplicate = [k for k, n in Counter(values).items() if n > 1]
    assert not duplicate, (name, duplicate)
missing_refs = sorted(set(refs) - set(labels))
missing_cites = sorted(set(citations) - set(bibliography))
assert not missing_refs, ("missing refs", missing_refs)
assert not missing_cites, ("missing cites", missing_cites)
assert "\\numberwithin{equation}{section}" in start.read_text(), "missing section numbering"
print("PASS article A static audit")
print(f"Input files: {len(paths)}, equation environments: {total}, "
      f"labels: {len(labels)}, refs: {len(refs)}, "
      f"bibitems: {len(bibliography)}, citations: {len(citations)}")
print("No unnumbered display math, non-numeric tags, missing or duplicate refs")
