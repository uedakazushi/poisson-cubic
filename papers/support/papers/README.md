# 主論文の支持ソース

正本は `nc-cubic/00_research_plan.md` と `nc-cubic/papers/paper_a.tex`・`nc-cubic/papers/paper_b.tex`。
このディレクトリは `papers/paper_a.tex` と `papers/paper_b.tex` の `\input@path{{papers/support/}}` で参照される。以下のパスはリポジトリルートからの表示。

| 主論文 | 組版入口 | 支持節 |
|---|---|---|
| A：Poisson正規形・量子化 | `papers/paper_a.tex` | `papers/support/papers/sections/`、`papers/support/papers/references_poisson_cubic.tex` |
| B：rotation付き可換復元 | `papers/paper_b.tex` | `papers/support/papers/reconstruction/`、`papers/support/papers/sections/`、`papers/support/papers/references.tex` |

`papers/support/papers/exports/` と `papers/support/papers/*.tex` にある独立節の組版入口は、研究再現の補助であり第三の主論文ではない。原稿Bの(L),(CF),(D)の仮定と独立監査未完の状態は現行主原稿・研究方針に従う。

```sh
latexmk papers/paper_a.tex
latexmk papers/paper_b.tex
python3 scripts/check_layout.py
python3 scripts/verify_bundle.py
```

LuaLaTeX/PDFの確認は別作業とし、現行内容のビルド結果を未実行でPASSと記載しない。原PDFの未照合内容はnc-cubic2やsources/candidatesの監査対象であり、現行主定理の証明をそこへのリンクだけで代用しない。
