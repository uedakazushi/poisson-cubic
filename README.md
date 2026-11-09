# nc-cubic — 三つの中心論文と独立した境界研究

**2026年11月9日・整理版v9**

再開時は [研究方針](00_research_plan.md) を最初に読み、[研究ノート](research_notes.md) を確認する。

## 中心となる三つの公表用論文

| 論文 | 現行LuaLaTeXソース | 内容 |
|---|---|---|
| A | `tex/poisson_cubic_quantization.tex` | Poisson正規形・退化・完全交叉・量子化・Hesse中心元 |
| B | `tex/generic17_ambient_recovery.tex` | 一般17次元中心三次対、偏極付きambientの二次包絡復元 |
| C | `tex/rotation_cubic_reconstruction.tex` | 形式復元・楕円ブロック・Zhang twist障害・相対saturation |

詳細な証明は従来からの `tex/papers/` 内のコンポーネントに残し、
AとCが別々に `\input` する構成。二つの本文間に未定義の `\ref` を残さない。
論文Bは独立した公表用原稿を移し、証明内容を維持する。

## 独立した境界研究

- `tex/boundary/pfaffian_brill_noether_technical.tex`：Brill–Noether・Pfaffian接触・高次形式理論の技術的な証明。公表可能な論文への分割・証明書の再監査は別途必要。
- `pdf/boundary/`：停留平面・Reye曲線、Pfaffian、中心商の特異圏などの原PDF。TeX原稿のない結果は再生成制約を `research_notes.md` に記録。
- `pdf/ambient/`、`pdf/quantization/`：一般族・Poisson量子化に固有の追加計算や詳細な原PDF。歴史保存ではなく、主要論文に未移植の唯一の証明を保持するための資料。
- `computations/`：厳密計算と証明書。外部査読・Lean形式化は未実施。

## PDFと再生成

`tex/` と `pdf/` を分離。原稿は日本語LuaLaTeX。主に `scripts/build.py` を使って独立論文のPDFを生成する。
PDFのソース一致が実際に確認できなければ、最新PDFとして扱わない。
現在のGitHubで未再組版のA/C PDFは生成済みと表示せず、PDF-only境界資料は元の証明のために残す。
`scripts/verify_bundle.py` でソース参照の閉包を点検できる。計算コードは必要な依存を入れて実行する。
古い原稿・PDF抽出TXT・旧ZIP・中間ファイル・バックアップは現行bundleへ入れない。

## 数学的な主張の状態

Bの偏極付きambient復元とCのrotation付き可換復元は別の主張。
一般17次元族の可換モデル、smooth properな相対残余dg族、一般混合項に対する比較は未解決。
広いAS-regular中心三次商の普遍的rotation付き可換復元はZhang twist反例により偽。
既存原稿の証明記載と今回の再検証範囲は `validation.json` で区別する。

### 現行の論文PDFの状態

- 論文A：ソースの相互参照・文献を静的検証済み。PDFは新ソースから未組版。
- 論文B：既存の対応する原PDFを `pdf/generic17_ambient_recovery.pdf` に配置。TeXは独立組版で13ページを確認済みだが、GitHub上のPDFとの完全ハッシュ一致は未確認。
- 論文C：ソースの相互参照・文献を静的検証済み。PDFは新ソースから未組版。
- 独立した境界研究：全ての元原PDFを分類し、編集可能なソースがあるものは明示。高次計算の全再検証は未完了。

### 分離型の余次元15と再現

論文Bの命題 `prop:split-codimension` と系 `cor:split-normal-directions` は、分離した一楕円ブロックの有理商次元が2であり、一般17次元族には本質的混合方向が15あることを証明する。法線は中心変数一次の6方向と二次の9方向に分かれる。検算は `python3 computations/verify_split_codimension.py`。最新の論文Bは15ページのPDFをローカルで組版・目視確認済みだが、GitHub上のPDFへの同期は別途検証する。A/Cの現行PDFは未再組版。

通常の可換cubicへのJacobian忘却の接空間（論文B命題 `prop:jacobian-forgetful-tangent`）も計算した：17→10は全射・核7、法線15→9・核6。これは量子化後の可換復元写像の構成ではない。厳密計算を同じ検証スクリプトに含めた。

### 17次元族の新しい幾何的障害（v8）

論文Bに `prop:vertical-seven`（17→10の核は平面移動6とPoissonスカラー1）、`prop:poisson-picard-obstruction`（元のcubicと平面を固定すると非零PoissonスカラーのG_mから楕円Picardへ非定数一価有理写像はない）を追加。第一優先課題は混合6方向に沿い量子化後の可換模型も変える相対的な復元の構成。日本語LuaLaTeX論文Bは16ページに再組版しLibraryへPDFと現行bundleを保存済み。GitHubへのPDFバイナリ同期は未実施。

### 混合中心の検算と相対Picardの障害（v9）

論文Bは `tex/papers/mixed_center_picard.tex` を読み込み、既存の全15混合方向の中心式、一次持上げの一意性、Grassmann族の相対Picardへのスカラー方向の有理写像の障害を扱う。厳密有限体検査は `python3 computations/verify_mixed_center.py`（Python標準ライブラリのみ）。全係数の普遍的中心性を今回独立に再証明したとは扱わない。独立部分研究用19ページPDFと自己完結v9 ZIPはLibraryに保存済み。GitHub上の論文B PDFはまだ旧版で、現行TeXから再生成する必要がある。
