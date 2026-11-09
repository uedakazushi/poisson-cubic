# TeX ソース未確認の独立論文 PDF（暫定例外）

2026-11-10 時点で、完全な TeX ソースと各 PDF の内容を一対一に照合できないものだけを保持する。PDF の本文を捨てて数学的な証明が欠落することを避けるための暫定的な例外であり、再生成可能な PDF を Git に置く方針ではない。

- `papers/pdf-only/ambient/central_cubic_technical.pdf`
- `papers/pdf-only/ambient/central_pair_formal_moduli.pdf`
- `papers/pdf-only/boundary/brill_noether.pdf`
- `papers/pdf-only/boundary/central_quotient_singularities.pdf`
- `papers/pdf-only/boundary/pfaffian_contact.pdf`
- `papers/pdf-only/boundary/reye_stationary.pdf`
- `papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf`

旧 `papers/pdf-only/quantization/poisson_second_jet.pdf` は `papers/independent/poisson_second_jet.tex` に二次ジェットの独立議論をソース化し、関連する17次元族・量子化の結果は `papers/generic17_ambient_recovery.tex`、`papers/sections/poisson_geometry.tex` に分散して保持しているため追跡解除した。

大型の `papers/boundary/pfaffian_brill_noether_technical.tex` には複数の PDF と重なる議論があるが、完全一致や未収録補題の不存在を確認できていない。PDF を削除する際は、元 PDF の各定理・仮定・証明と新しい TeX を照合してから実施する。PDF を古いコミットから復旧することを再開前提にはしない。

個別PDFと対応TeX候補、追跡解除までのチェック項目は [`TODO_PDF_SOURCES.md`](../../TODO_PDF_SOURCES.md) に記載する。
