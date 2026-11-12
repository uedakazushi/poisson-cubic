# nc-cubic — Poisson三次超曲面の量子化と一般点可換復元

**2026-11-13 / v72。** GitHub `main` が正本。再開は [研究方針](00_research_plan.md) から。

## 現行の二論文

| 原稿 | 対象と現行構成 |
|---|---|
| [論文A](papers/paper_a.tex)（A-v51） | 一般次元のPoisson幾何・代数的量子化。本体と入力ソースは保持する。 |
| [論文B](papers/paper_b.tex)（B-v55） | 任意の n>=3 における代数的中心三次変形の一般点可換復元と、その証明に必要な結果のみ。 |

論文Bは [papers/generic_recovery/](papers/generic_recovery/) に主定理と必要な証明を集約した。本文の順序は、局所代数的模型、三対象window、完備曲率付きMF比較、一般点への移行と有限降下、全coherent残余圏への飽和、低rotation積と勾配空間、方程式の基礎体降下である。主定理は三次三様体に限らず任意の n>=3 を扱う。方程式は元の体 C(h) 上、圏同値は有限拡大後という区別を保つ。今回の移管整理ではA・Bの本文を変更していない。

## 編集と検証の状態

B-v55はLuaLaTeX/latexmkで全文27頁を組版・表示確認済み。主原稿、共通設定、9個の本文・文献ファイルの計11ファイルを使用する。静的検査は102ラベル・94参照・37引用・13文献項目で、未解決・重複はない。最終ログの未解決参照・引用、文字欠落、overfull boxは0。これは組版と参照の検証であり、全数学的証明の独立監査ではない。状態は [validation_paper_b.json](validation_paper_b.json)、証明の依存は [notes/generic_recovery.md](notes/generic_recovery.md)。

## 独立成果の移管

点スキームの4節は [nc-cubic2の独立原稿](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/mixed_cubic_point_schemes.tex) に、必要な中心式の証明・文献・4本の検算コードと共に統合した。全文12頁の組版・表示、参照検査、4本の検算を実行済み。元の2ノートの固有内容は [移管先ノート](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/mixed_cubic_point_schemes.md) に整理した。保存確認後に点スキーム専用の元本文・組版入口・コード・再生成できる証明書など17ファイルを除外し、残る文献入力を修正した。論文A・現在の論文Bの入力には影響しない。

**移管全体は未完了。** 一次変形・Plücker障害、有限Jacobian復元の2節は移管先に全文保存済みだが、独立原稿への統合と依存の整理が残る。Artin・étale理論、Sklyanin/多ブロック模型、相対対角・bar・Moritaの別構成、混合族の二次jet等も、未移管部分を本リポジトリの現行支持ソースに保持する。点スキームに必要な中心式を抽出したことを、混合族全体の移管完了とは扱わない。

詳細は [現行の分担と移管残件](notes/paper_b_scope_and_transfer.md)。新結果の追加より、移管単位ごとの証明・参照・再現性の整備を優先する。旧コミットや旧ZIPだけを成果の保存場所にしない。

## 再現

```sh
latexmk papers/paper_a.tex
latexmk papers/paper_b.tex
python3 scripts/verify_bundle.py --only paper_b
```

LuaLaTeX、LuaTeX-ja、latexmkを用いる。`.latexmkrc` は変更していない。PDF・SyncTeX・中間物は `build/` に生成しGit追跡しない。今回の計算・組版は移管先の点スキーム稿で実施し、A・Bの再組版と全既存計算の再実行はしていない。

GitHub Actions・force pushは使用しない。Libraryは実際のGitHub保存失敗時のみ緊急退避し、既存Libraryファイルを無断削除しない。
