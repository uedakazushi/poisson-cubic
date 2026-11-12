# PDF照合のための関連TeX候補

ここに置いたTeXは、現行の`papers/`・`notes/`へ未統合の候補、または内容照合のために一時的に重複保持した原稿である。**どのPDFも、このディレクトリに候補があるというだけで追跡解除しないこと。**

- `poisson_ambient_bridge_v6.tex`：Poisson pencil・17次元族・中心三次対・quadratic envelopeの比較。
- `elliptic_v5/main.tex`、`elliptic_v5/notes.tex`、`elliptic_v5/tex/*`：一楕円ブロックのrotation付き可換復元と研究ノート。もとの`\input`構造を残してあり、主論文・PDFとの完全一致は未確認。
- `longform/`：2026年10月末の大部の包括TeX。v18相当の内容は既にhttps://github.com/uedakazushi/nc-cubic2/blob/main/papers/pfaffian_brill_noether_technical.texにある。v16・v17・初期の原稿は差分照合のため一時的に確保したもの。研究の現在有効な主張に統合したら整理する。

追跡中9本のPDFとの詳細対応と今後のチェック項目は [TODO_PDF_SOURCES.md](../../TODO_PDF_SOURCES.md) を参照する。

独立大部原稿の現行TeXは [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) に移した。候補群は現行の主論文からは読み込まない。現行成果との数学的内容照合が未完成のlongform原稿は削除しない。elliptic_v5では、独立入力main.texが使用する単一のTeXコピーを保ち、Git blobが完全一致する未使用の重複2ファイルだけ除外した。目標3のSMに直接必要な未収録の補題が判明した場合に限り主論文・ノートへ統合する。
