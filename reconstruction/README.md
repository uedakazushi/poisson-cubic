# 可換復元：局所rotation・saturation還元（現行論文Cの独立組版入口）

2026-11-10・v14。**研究全体の正本はこのGitHubリポジトリの `main` であり、最初にルートの `00_research_plan.md` を読む。**

このディレクトリは論文Cの現行の新しい証明を、そのまま読んで再生成できる最小の構成である。古いZIPやChatGPT Library、過去の会話、外部の補助ファイルを必要としない。三論文A/B/Cの古い証明は削除していない。`tex/rotation_saturation_reduction.tex` は10ページの独立組版入口で、新たな第四論文ではない。今後の論文C本体への統合では証明全文を移し、このソースへの依存がなくなったことを検証してから冗長物を整理する。

## 数学的状態

- 原稿に証明あり（独立した査読・形式証明ではない）：局所proper残余模型におけるrotationの逆 `(-1)◦R_O`、smoothness仮定下のfull coherent残余比較と有限型spread。
- 条件付き：任意のPoisson成分のgeneric可換復元には相対smoothness (SM) と局所実現原理 (ER) の監査済み実証が必要。
- 未完成：非楕円二成分の残余対角perfect性、全次元・全成分の相対量子化、ERの全面的確認。
- 新規性：網羅的な文献比較は未了。

## GitHubをcloneした状態からの再現

ルートから以下を実行する（Python 3、SymPy、LuaLaTeX、LuaTeX-ja/ltjsarticle、amsmath等が必要）。

```sh
python3 reconstruction/computations/verify_nonelliptic_inputs.py --output /tmp/nc-cubic-input-checks.json
python3 reconstruction/scripts/build.py
python3 reconstruction/scripts/verify.py
```

`verify.py` は検算を再実行し、生成したPDFとソースのbuild receipt、TeX内部参照と引用、数式計算の固定された証明書を確認する。PDFは `reconstruction/pdf/rotation_saturation_reduction.pdf` に再生成される（Gitには生成物を追加しない）。コマンドの成功は**圏論の完全な形式検証ではない**。

`validation.json` の検証履歴はbundle作成時の結果。GitHub反映の成否はGitHub commit/refを別途確認する。
