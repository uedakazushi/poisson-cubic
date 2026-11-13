# nc-cubic — Poisson三次超曲面の量子化と一般点可換復元

2026-11-13 / v83。再開は [研究方針](00_research_plan.md) から。

| 現行論文 | 内容 |
| --- | --- |
| [論文A](papers/paper_a.tex)（A-v52） | 一般次元のPoisson正規形・Bondal予想・代数的量子化・固定相対モジュライ・ambient復元 |
| [論文B](papers/paper_b.tex)（B-v57） | 任意のn>=3の中心三次変形の一般点可換復元と必要証明 |

論文Aの主要証明を公表の観点から再点検し、要約と序論を結果の依存順に整理した。相対Poisson空間の忘却射をアフィン射へ訂正し、相対階数層の同時スカラー作用、Koszul表示のbase change、普遍中心元の階数一定の議論を明記した。三次三様体の導来ambient復元には左右noetherian性を明示し、中心二変数上の自由性を保証する最高次記号の条件を加えた。正規形・Bondalの下界・全Poisson構造の代数的量子化・Fermat成分数の主要結論は保持している。

[Aの監査と文献比較](notes/poisson_article_submission_audit.md) に仮定と証明の所在を、[Aの検証記録](validation_paper_a.json) に組版・厳密計算・確認範囲をまとめた。新規性の網羅的な確定・外部査読・形式検証は未了である。Brückmann消滅の原論文本文は未取得で、現在はFu--Hwangの明示的定理文と原文献への帰属を確認している。

論文Bの証明は `papers/generic_recovery/` 内で完結する。可換方程式は関数体上、全coherent残余圏のrotation・指定三次周期付き同値は有限拡大上に構成する。固定勾配空間の積分は有限étaleなsymmetrizer代数で記述し、幾何学的に分解不能なら方程式は基礎体上でスカラー倍まで一意である。同値核の基礎体への降下は別の問題である。[Bの証明案内](notes/generic_recovery.md)、[Bの監査](notes/paper_b_proof_audit.md)、[Bの検証記録](validation_paper_b.json) を参照。今回のA改訂ではB-v57の全入力と共通preambleを変更していない。

独立な点スキーム・Jacobian・一次変形・Artin・étale・相対模型の成果はnc-cubic2へ移管済みである。現行の入口と担当境界は [移管境界ノート](notes/paper_b_scope_and_transfer.md)。

```sh
python3 scripts/check_layout.py
python3 scripts/verify_bundle.py
python3 scripts/build.py --only paper_a
python3 scripts/verify_bundle.py --only paper_a --require-pdfs
python3 scripts/build.py --only paper_b
python3 scripts/verify_bundle.py --only paper_b --require-pdfs
```

LuaLaTeX・LuaTeX-ja・latexmkと `requirements.txt` のPython依存を用いる。厳密計算のコマンドは各論文のvalidationに記載し、大きな記号計算は一つずつ実行する。PDF・SyncTeX・中間物はbuild/で非追跡。GitHub mainに保存し、Actions・force pushを使用しない。LibraryはGitHub保存の実失敗時のみ緊急退避に使う。
