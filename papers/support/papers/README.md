# 公表用論文

最初にルート 00_research_plan.md を読む。現在の最優先課題は**論文Aの完成**。
原稿 papers/poisson_cubic_quantization.tex は独立のAbstract/Introduction/文献
(papers/references_poisson_cubic.tex) を持つ。
証明監査・先行研究・未完了課題は notes/poisson_article_submission_audit.md。
A全体の組版・主定理の完全監査は未完了。主論文三本は維持する。

| 論文 | 組版入口 |
|---|---|
| A：Poisson構造・代数的量子化 | `papers/poisson_cubic_quantization.tex` |
| B：一般17次元族・ambient復元 | `papers/generic17_ambient_recovery.tex` |
| C：rotation付き可換復元 | `papers/rotation_cubic_reconstruction.tex` |

論文AのFermat固定fiberと相対Poisson schemeの既約成分比較は `papers/sections/fermat_relative_poisson_components.tex` を組み込む（一般rankと分割の計数証明。scheme非被約構造とは区別）。

`papers/sections/` は論文共通節と証明、`papers/reconstruction/` はCの共有節と独立組版、`papers/exports/` は部分節の読解用組版、独立境界原稿の証明全文は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) へ移管した。独立組版は第四の主論文ではない。

リポジトリルートから `latexmk papers/poisson_cubic_quantization.tex` などを実行する。設定は `.latexmkrc`。PDFと補助ファイルはすべて `build/` に生成し、Gitで追跡しない。

原PDF8件は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) に移転済み（論文6件、ノート2件）。本リポジトリはPDFを追跡しない。TeXへの完全復元は未了。
