# poisson-cubic の主原稿と分割入力

2026-11-25 / v101。主論文は [papers/poisson-cubic.tex](../../poisson-cubic.tex) 一本。ここにある `common.tex`、`sections/` と `references_poisson_cubic.tex` を再帰的に読み込む。表紙日時・ファイル名の `papers/build-metadata.tex` は任意入力であり、Git管理しない。存在しなくても組版でき、日付入りPDFはルートの `python3 build_pdf.py --new-version` で生成する。

ルートで `latexmk papers/poisson-cubic.tex` または `python3 scripts/build.py --only poisson-cubic` を実行する。LuaLaTeX・LuaTeX-jaとSyncTeXを使い、生成PDF・中間物はGitで追跡せず `build/` に置く。

ソースの参照・引用・数式番号を `scripts/verify_bundle.py` と `scripts/verify_article_a_numbering.py` で検査する。量子化の全証明と検算資産は `cubic-quantization/papers/cubic-quantization.tex` を入口とし、可換復元・非可換モジュライは `nc-cubic/papers/nc-cubic.tex` を正本とする。独立の相対復元の研究は `nc-cubic2` を正本とする。
