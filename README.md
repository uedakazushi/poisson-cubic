# nc-cubic — Poisson cubic の量子化とrotation付き可換復元

**2026-11-12 / v56。** 正本は GitHub `main`。研究再開は[現行研究方針](00_research_plan.md)から。

## 現行の二論文

| 論文 | 現行LuaLaTeX原稿 | 主題 |
|---|---|---|
| **A** | [papers/paper_a.tex](papers/paper_a.tex) | 滑らかな三次超曲面のPoisson正規形、退化スキーム、Bondal予想、代数的量子化、Poisson moduli stacks |
| **B** | [papers/paper_b.tex](papers/paper_b.tex) | 一般次元の中心三次非可換超曲面に関するrotation付き全coherent残余圏の可換復元 |

論文A（A-v51）は、各smooth cubic $n$-fold（$n\ge3$）の全Poisson構造をJacobian三変数ブロックに分解し、形式的中心元存在に依存しない普遍Cramer中心元・AS正則ambientによる代数量子化を主張する。定理の証明を記載済みだが、正規形Lie補題、普遍Hesseの全係数恒等式、PBW/AS条件、Bondal予想・stack成分数の独立監査と包括的な新規性調査は未完了。監査は[notes/poisson_article_submission_audit.md](notes/poisson_article_submission_audit.md)。

論文B（旧Cの内容をそのまま継承する B-v40）は、局所proper/window模型(L)、実際の完備graded MF同値(CF)、一般ファイバーのnoetherian Koszul AS正則性を仮定し、有限拡大後に非可換中心三次商の全coherent残余pairとsmooth cubicのKuznetsov pairのrotation付きMorita同値を得る。(L),(CF)は原稿に証明があるが、全依存の独立監査は未完了。特定の混合族には追加で(D)が必要。主定理は[general_dimension_recovery.tex](papers/support/papers/reconstruction/general_dimension_recovery.tex)、監査は[notes/general_dimension_categorical_reconstruction.md](notes/general_dimension_categorical_reconstruction.md)。

17次元非可換三次三様体モジュライ、ambientの1周期性、六・七次元Poisson退化schemeと独立境界研究は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) を正本とする。一般次元のquadratic-envelopeによるambient復元定理は論文Aに残す。

## 現行ディレクトリ

- `00_research_plan.md`：最初に読む研究方針、証明状態、研究の優先順位。
- `papers/paper_a.tex`・`papers/paper_b.tex`：二つの主論文入口。入力節と文献は `papers/support/papers/sections/`・`papers/support/papers/reconstruction/`・`papers/support/papers/references*.tex`。
- `notes/`：現在有効な計算・反例・独立監査上の課題。
- `computations/`：再生成可能な有限計算と、必要な証明書。
- `reconstruction/`：論文Bの局所・étale比較の再現スクリプト。
- `sources/candidates/`：まだ現行原稿との内容照合が必要な候補TeX。新しい主論文の入口ではなく、照合なしに削除しない。
- `notes/source_recovery/`：外部に保全されたPDF原本の[内容一覧](notes/source_recovery/pdf_mathematical_inventory.md)・[未照合箇所](notes/source_recovery/pdf_source_checklist.md)と、必要部分のTeX復元。

## 組版と静的検査

リポジトリルートから実行する。

```sh
python3 scripts/check_layout.py
python3 scripts/verify_bundle.py
python3 scripts/verify_article_a_numbering.py
latexmk papers/paper_a.tex
latexmk papers/paper_b.tex
# 領収記録付きで二論文をまとめて組版する場合
python3 scripts/build.py
```

必要なものはLuaLaTeX（LuaTeX-jaを含む）とlatexmk。VS Code の LaTeX Workshop はルートの `.latexmkrc` を使用し、PDF・aux・log・syncTeXは `build/` に作る。**ソースの静的整合性が通ったことは組版成功や数学的証明の独立検証を意味しない。** 実際の検証は [validation.json](validation.json) に記録する。

GitHub main にfast-forward pushし、GitHub Actions・force pushは使わない。PDFと中間ファイルはGitで追跡しない。LibraryはGitHub push失敗時のみ緊急退避する。
