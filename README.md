# nc-cubic — Poisson三次超曲面の量子化と一般点可換復元

**2026-11-13 / v76。** GitHub mainが正本。再開は [研究方針](00_research_plan.md) から。

## 現行の二論文

| 原稿 | 内容 |
|---|---|
| [論文A](papers/paper_a.tex)（A-v51） | 一般次元のPoisson幾何・代数的量子化。本文と入力ソースを保持。 |
| [論文B](papers/paper_b.tex)（B-v55） | 任意のn>=3の代数的中心三次変形の一般点可換復元と必要証明。 |

Bの証明は [papers/generic_recovery/](papers/generic_recovery/) 内で自立する。局所模型、三対象window、完備MF比較、一般点生成・有限降下、coherent飽和、低rotation積と勾配空間、基礎体上の方程式を扱う。方程式をC(h)上に取れることと、同値の有限拡大を区別する。今回A・Bの本文・入力・設定は変更していない。

B-v55は27頁の全文組版・表示確認済み。11TeX入力、102ラベル、94参照、37引用、13文献で未解決・重複・文字欠落・overfullなし。これは数学的な全証明の独立監査ではない。状態は [validation_paper_b.json](validation_paper_b.json)、依存は [notes/generic_recovery.md](notes/generic_recovery.md)。

## 独立成果の現行所在

nc-cubic2に以下の独立原稿を整備した。各原稿と同名のnotesノート、validationファイルが再開と確認の入口である。

| 原稿 | 状態 |
|---|---|
| [点スキーム](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/mixed_cubic_point_schemes.tex) | 12頁。混合中心式と点加群、平坦閉包。4検算を保持し元の専用17ファイルを整理済み。 |
| [有限Jacobian復元](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/cubic_jacobian_recovery.tex) | 6頁。低積・可積分性・一意性・反例。元の専用3ファイルを整理済み。Bの必要証明は保持。 |
| [一次変形とPlücker障害](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/cubic_first_order_deformations.tex) | v2、13頁。直接MF比較、双対数window、Todd-HKR別証明。元の専用4ファイルを整理済み。 |
| [有限Artin基底上の残余圏とMF](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/cubic_artin_windows.tex) | v1、13頁。全有限一変数切断の比較、正則底からの変更、完備化の障害。独立稿の組版・検算・保存済み、元ソース整理は未完了。 |

新しい有限Artin稿はR_N=C[h]/h^(N+1)を扱い、任意の局所Artin環や全coherent圏の定理ではない。MF比較を別途与えた場合の可換残余圏への移送は述べるが、全次数MF比較の存在自体をこの稿で証明してはいない。既存反例の全文を保持した。7TeX入力・31ラベル・36参照・11引用・5文献の検査、全文組版・表示、4次元dg模型の有限検算を実行済み。全数学的証明の形式検証ではない。

**全移管は未完了。** 元のArtin比較の末尾の形式復元系と、mixed・formal等のam参照を整理するまで元の比較・反例を削除しない。形式/étaleの存在理論、Sklyanin/多ブロック、対角/bar/Morita、混合jet等も現行ソースに保持する。[現在の所在と残件](notes/paper_b_scope_and_transfer.md)を参照。

## 再現と保存

```sh
latexmk papers/paper_a.tex
latexmk papers/paper_b.tex
python3 scripts/verify_bundle.py --only paper_b
```

LuaLaTeX、LuaTeX-ja、latexmkを用い、.latexmkrcは変更しない。今回A・Bの再組版や全既存計算は実行していない。PDF・SyncTeX・中間物はbuild/で非追跡。Actions・force pushなし。Libraryは実際のGitHub保存失敗時のみ緊急退避する。
