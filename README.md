# nc-cubic — Poisson三次超曲面の量子化と一般点可換復元

2026-11-13。GitHub mainが正本。再開は [研究方針](00_research_plan.md) から。

| 現行論文 | 内容 |
| --- | --- |
| [論文A](papers/paper_a.tex)（A-v51） | 一般次元のPoisson幾何・代数的量子化・ambient復元 |
| [論文B](papers/paper_b.tex)（B-v55） | 任意のn>=3の中心三次変形の一般点可換復元と必要証明 |

論文A `papers/paper_a.tex`（A-v51）、論文B `papers/paper_b.tex`（B-v55）、両者の再帰入力26ファイルと共通設定は変更していない。必要証明を外部参照だけで代用しない。

**論文Bから分離した現行独立成果の移管は完了。** nc-cubic2の [統合稿](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/relative_reconstruction_models.tex) と既存の点スキーム・Jacobian・一次変形・Artin・étale稿が正本。必要な証明・反例・計算を統合し、移管先の保存確認後に元側の専用142ファイルを整理した。全所在・保護対象・実行範囲は [移管境界ノート](notes/paper_b_scope_and_transfer.md)。新規性と全証明の独立監査は未了である。

Bは `papers/generic_recovery/` 内で自立する。既存の27頁組版記録は [validation_paper_b.json](validation_paper_b.json)。今回はA・Bを再組版せず、26入力の一致と参照を検査した。

```sh
python3 scripts/check_layout.py
python3 scripts/verify_bundle.py
latexmk papers/paper_a.tex
latexmk papers/paper_b.tex
```

LuaLaTeX・LuaTeX-ja・latexmkを使う。PDF・SyncTeX・中間物はbuild/で非追跡。Actions・force pushなし。LibraryはGitHub保存の実失敗時のみ緊急退避する。
