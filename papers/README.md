# 公表用論文

最初にルート `00_research_plan.md` を読む。主論文は三本。

| 論文 | 組版入口 |
|---|---|
| A：Poisson構造・代数的量子化 | `papers/poisson_cubic_quantization.tex` |
| B：一般17次元族・ambient復元 | `papers/generic17_ambient_recovery.tex` |
| C：rotation付き可換復元 | `papers/rotation_cubic_reconstruction.tex` |

`papers/sections/` は論文共通節と証明、`papers/reconstruction/` はCの共有節と独立組版、`papers/exports/` は部分節の読解用組版、独立境界原稿の証明全文は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) へ移管した。独立組版は第四の主論文ではない。

リポジトリルートから `latexmk papers/poisson_cubic_quantization.tex` などを実行する。設定は `.latexmkrc`。PDFと補助ファイルはすべて `build/` に生成し、Gitで追跡しない。

`papers/pdf-only/` の6本と `notes/pdf-only/` の2本は対応する完全なTeXソースが未確認の原本なので、研究成果の欠落を防ぐため例外的にGitに保持する。対応ソースが正しく再構築された後にだけ追跡解除を検討する。
