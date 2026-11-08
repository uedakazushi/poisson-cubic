# nc-cubic

**3次超曲面のPoisson構造と非可換量子化：正規形・退化スキーム・rotation付き残余圏**

2026年11月8日（日本標準時）・統合第2版 / `nc-cubic-v2`

## 読む順序

1. [00_research_plan.md](00_research_plan.md) — 現在の目標、結果の状態、未解決の核心、具体的な次の課題、一般研究原則と保存許可。印刷用は [research_plan.pdf](research_plan.pdf)。
2. [cubic_poisson_rotation.pdf](cubic_poisson_rotation.pdf) — 日本語LuaLaTeXの公表用草稿。第I部はPoisson分類・退化・量子化、第II部は可換復元・反例・形式変形・明示的ブロック模型。
3. [research_notes.pdf](research_notes.pdf) — 相対saturationの条件付き構成、補助証明、障害、文献比較、研究再開のための知識。

現行版だけから研究を継続できる一式である。旧bundle、旧入力PDF、会話履歴を必要としない。公刊・査読済みではなく、研究全体の新規性は確認継続中。

## 主な結論

滑らかなcubicのPoisson構造を、互いに可換な三変数Jacobianブロックの和へ分類する。中心変数との混合項を許す。全退化スキームのイデアル、sixfold・sevenfoldの完全交叉や非被約構造、および三次の中心元を持つ代数的量子化の証明を保持する。

rotation付き可換復元には次の範囲で肯定的結果がある。

- 滑らかなcubicからの次数付きArtin変形のmarkedな形式復元。
- 既にsmooth properな代数的pair族が与えられた場合のétale局所実現。
- 一つの楕円Sklyaninブロックと、原点だけに臨界点を持つ任意の中心三次式。
- 複数の独立ブロックで、高々一つを除く平行移動が有限位数の場合。残る一つは無限位数でもよい。

**任意のAS-regular中心三次商に対する普遍的な存在命題は成立しない。smooth proper性と周囲のCalabi–Yau性を加えても反例がある。**

Fermat cubic fourfoldを `diag(ω, ω², 1, 1, 1, 1)`（`ω³=1≠ω`）でZhang twistすると、射影圏は元の可換cubicと同値でも、標準次数シフトに由来するrotationが変わる。rotation不変 `HH_0` の次元は8で、任意の可換cubic fourfoldの20と異なる。全Hochschild homologyの不変Euler標数は10と22で異なり、相対三次周期性を保つsmooth properな連結族でも結べない。

この反例を、本稿の特定のPoisson量子化族のファイバーと同定したわけではない。その族の相対saturation、二つ以上の無限位数ブロックの全生成、非可換変数との混合項、局所モデルの大域降下は未解決として区別する。

## ファイル構成

| ファイル | 役割 |
| --- | --- |
| `00_research_plan.md` | 再開の入口となる研究方針の正本 |
| `cubic_poisson_rotation.tex` | 論文の序論と全体構成 |
| `papers/poisson_geometry.tex` | 一般Poisson分類、退化、量子化、特殊例、数値不変量の全証明 |
| `papers/rotation_obstruction.tex` | Zhang twist反例、連結族の障害、全生成判定 |
| `papers/rotation_models.tex` | 形式復元、étale局所実現、Sklyanin比較、外部積生成の全証明 |
| `research_notes.tex` | 研究ノートの正本 |
| `common.tex`, `references.tex`, `papers/*references.tex` | 共通設定と書誌情報・参照箇所 |
| `computations/` | 厳密計算と現行の小さな計算証明書 |
| `scripts/build.py` | PDFの再生成 |
| `scripts/verify_bundle.py`, `SHA256SUMS`, `validation.json` | 構成・参照・検証状態・整合性 |

外部文献PDF、旧原稿、ZIP、履歴、コンパイル中間物はこのツリーに含めない。配布用ZIPはこの現行ツリーから作る。

## 計算の再現

Python 3.9以降の標準ライブラリだけを使う。

```sh
python3 computations/verify_algebra.py
python3 computations/verify_rotation_obstructions.py
python3 computations/verify_geometry.py
```

中心元、点曲線、Hesseの特異条件、有限位数・無限位数の点、Koszul恒等式、Zhang twistの文字計算、完全交叉の数値を有理数・整数・有限体で検算する。浮動小数点を使わない。**これらは圏論的同値、生成性、変形理論の形式証明ではない。**

## PDFの再生成

LuaLaTeXと日本語TeX環境（`ltjsarticle`、LuaTeX-ja、`luaotfload`、HaranoAjiフォント等）、Pandoc、Python 3が必要。
通常のTeX Liveでは `texlive-luatex`, `texlive-lang-japanese`, `texlive-latex-extra`, `texlive-fonts-recommended` に相当する構成を使用する。
パッケージは `geometry, amsmath, amssymb, amsthm, mathtools, bm, booktabs, longtable, array, enumitem, xcolor, hyperref, fancyhdr, microtype, needspace`。

```sh
python3 scripts/build.py
```

全PDFを再生成する。特定の文書だけなら、たとえば `python3 scripts/build.py --only cubic_poisson_rotation`。
相互参照の安定を見ながら必要な回数だけコンパイルする。中間ファイルは一時ディレクトリに置き、未定義参照・引用、欠落文字、overfull boxが残れば失敗する。
研究方針のPDFはMarkdownから生成するため、そのためだけの重複したTeX正本は置かない。

```sh
python3 scripts/verify_bundle.py
```

計算証明書を再生成し、原稿入力・引用・ラベル・成果物・チェックサムを確認する。ソースを変更してPDFと検証状態を更新した後は `--write-hashes` を付けて現行チェックサムを作り直す。

## 状態の読み方

原稿の生成、数学の証明点検、有限計算、組版、PDFの表示確認、GitHubへの反映は別の状態として扱う。実行結果と限界は `validation.json` を参照する。外部査読とLean形式化は未実施。主要な外部定理の適用箇所と確認した版は文献表に記載している。

研究の区切りごとのbundle保存は再承認不要。一般研究原則と保存許可は研究方針に記載する。PR・GitHub Actionsを使わず、`main` の通常更新で現在の研究一式を管理する。

## 相対saturationの還元（v2）

公表用原稿の `papers/relative_saturation.tex` に、相対properな半直交分解での smoothness の同値、全超曲面圏の対角一本への有限証明書の還元、中心三次元の graded matrix factorization の `(1)^3 ≃ [2]` を証明した。gluingはOrlovの既知定理の相対版であり、新規性未確認。相対Beilinson仮定、実際の有限証明書、相対Orlov同値、可換復元の存在は未解決のまま区別する。

**組版状態**：更新したTeX原稿をGitHubに保存したが、GitHub上の既存PDF三点はv1からの再生成を今回行っていない。したがってPDFと現行TeXは一致しない。再生成は `python3 scripts/build.py`。今回独立にLuaLaTeX組版した相対saturationの3ページ補助PDFは会話の成果物として配布する。

相対gluingの議論には、残余圏がcompact generatorを持つという仮定を明記してある。今回対象とする相対proper模型では、研究ノートの命題によりgeneratorを構成する。
