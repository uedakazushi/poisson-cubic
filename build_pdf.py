#!/usr/bin/env python3
"""Build the complete manuscript from the source bundle.

Use --new-version after editing to create fresh JST cover metadata and a new
dated filename. Without it, the delivered version's cover metadata is preserved.
"""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import re
import shutil
import subprocess
from zoneinfo import ZoneInfo


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--new-version", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    metadata = root / "papers/build-metadata.tex"
    if args.new_version:
        now = datetime.now(ZoneInfo("Asia/Tokyo"))
        filename = "poisson_cubic_revised_" + now.strftime("%Y%m%d_%H%M%S") + ".pdf"
        metadata.write_text(
            "\\newcommand{\\RevisionDate}{" + now.strftime("%Y-%m-%d") + "}\n"
            "\\newcommand{\\CreationTime}{" + now.strftime("%Y-%m-%d %H:%M:%S")
            + " JST（Asia/Tokyo）}\n"
            "\\newcommand{\\PDFFileName}{" + filename.replace("_", "\\_") + "}\n",
            encoding="utf-8",
        )
    content = metadata.read_text(encoding="utf-8")
    match = re.search(r"\\newcommand\{\\PDFFileName\}\{([^}]+)\}", content)
    if not match:
        raise SystemExit("PDFFileName is missing from papers/build-metadata.tex")
    filename = match.group(1).replace("\\_", "_")
    if Path(filename).name != filename or not filename.endswith(".pdf"):
        raise SystemExit("PDFFileName must be a PDF basename")
    destination = root / "dist" / filename
    if destination.exists():
        raise SystemExit(f"Already exists: {destination}\nUse --new-version for a revised PDF.")
    subprocess.run(["latexmk", "papers/poisson-cubic.tex"], cwd=root, check=True)
    destination.parent.mkdir(exist_ok=True)
    shutil.copy2(root / "build/poisson-cubic.pdf", destination)
    print(destination)


if __name__ == "__main__":
    main()
