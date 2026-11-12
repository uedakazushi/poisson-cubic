# 主論文の支持ソース

正本は `nc-cubic/00_research_plan.md` と `nc-cubic/papers/paper_a.tex`・`nc-cubic/papers/paper_b.tex`。
このディレクトリは `papers/paper_a.tex` と `papers/paper_b.tex` の `\input@path{{papers/support/}}` で参照される。論文Bは各節を五部の論理順に直接読み込む。`papers/support/papers/sections/rotation_models.tex` は互換用の読込入口であり、論文Bから重複入力しない。以下のパスはリポジトリルートからの表示。

| 主論文 | 組版入口 | 支持節 |
|---|---|---|
| A：Poisson正規形・量子化 | `papers/paper_a.tex` | `papers/support/papers/sections/`、`papers/support/papers/references_poisson_cubic.tex` |
| B：rotation付き可換復元 | `papers/paper_b.tex` | `papers/support/papers/reconstruction/`、`papers/support/papers/sections/`、`papers/support/papers/references.tex` |

`papers/support/papers/exports/` と `papers/support/papers/*.tex` にある独立節の組版入口は、研究再現の補助であり第三の主論文ではない。論文Bの局所window比較(L)と完備MF比較(CF)は本文中の構成定理であり、独立の追加仮定ではない。明示式の特定には(D)を用いる場合がある。独立監査の実施範囲は研究方針と検証記録に従う。

```sh
latexmk papers/paper_a.tex
latexmk papers/paper_b.tex
python3 scripts/check_layout.py
python3 scripts/verify_bundle.py
```

LuaLaTeX/PDFの確認は別作業とし、現行内容のビルド結果を未実行でPASSと記載しない。原PDFの未照合内容はnc-cubic2やsources/candidatesの監査対象であり、現行主定理の証明をそこへのリンクだけで代用しない。
