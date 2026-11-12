# nc-cubic — Poisson三次超曲面の量子化と一般点可換復元

**2026-11-12 / v71。** GitHub `main` が正本。再開は [研究方針](00_research_plan.md) から。

## 現行の二論文

| 原稿 | 対象と現行構成 |
|---|---|
| [論文A](papers/paper_a.tex)（A-v51） | 一般次元のPoisson幾何・代数的量子化。本文と支持ソースは今回変更していない。 |
| [論文B](papers/paper_b.tex)（B-v55） | 任意の n>=3 における代数的中心三次変形の一般点可換復元と、その証明に必要な結果のみ。 |

論文Bは [papers/generic_recovery/](papers/generic_recovery/) に主定理と必要な証明を集約した。本文の順序は、局所代数的模型、三対象window、完備曲率付きMF比較、一般点への移行と有限降下、全coherent残余圏への飽和、低rotation積と勾配空間、方程式の基礎体降下である。主定理は三次三様体に限らず任意の n>=3 を扱う。方程式は元の体 C(h) 上、圏同値は有限拡大後という区別を保つ。

## 編集と検証の状態

論文Bの全文をLuaLaTeX/latexmkで組版し、27頁を表示確認した。主原稿、共通設定、9個の本文・文献ファイルの計11ファイルを使用する。静的検査は102ラベル・94参照・37引用・13文献項目で、未解決・重複はない。最終ログの未解決参照・引用、文字欠落、overfull boxは0。これは組版と参照の検証であり、全数学的証明の新たな独立監査ではない。正確な状態は [validation_paper_b.json](validation_paper_b.json)、証明の依存は [notes/generic_recovery.md](notes/generic_recovery.md)。

## 独立成果の移管は未完了

一般次元の主定理に不要な変形論、相対Artin・étale理論の独立結果、明示量子化、point scheme等は論文Bの入力から外した。その数学的内容は削除していない。

[nc-cubic2の移管先](https://github.com/uedakazushi/nc-cubic2/tree/main/papers/reconstruction_extensions) に、一次変形・Plücker障害、有限Jacobian復元、point schemeに関する6節の全文を保存した。移管先の独立原稿への統合、参考文献・必要計算コードの移管、残る支持節の移管はまだ終わっていない。未移管または統合未確認の本文は本リポジトリの現行支持ソースに保持し、旧コミットへの参照だけで代用しない。本文の集約完了と、リポジトリ間の移管完了を混同しない。

詳細は [現行の分担と移管残件](notes/paper_b_scope_and_transfer.md)。論文Aの移管は行わず、Aとその支持ソースを維持する。

## 再現

```sh
latexmk papers/paper_a.tex
latexmk papers/paper_b.tex
python3 scripts/verify_bundle.py --only paper_b
```

LuaLaTeX、LuaTeX-ja、latexmkを用いる。既存の `.latexmkrc` は変更していない。PDF・SyncTeX・中間物は `build/` に生成しGit追跡しない。今回実行したのは論文Bの全文組版と専用の静的照合であり、論文Aの再組版と全既存計算の再実行は未実施。

GitHub Actions・force pushは使用しない。Libraryは実際のGitHub保存失敗時のみ緊急退避し、既存Libraryファイルを無断削除しない。
