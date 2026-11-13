# nc-cubic — Poisson三次超曲面の量子化と一般点可換復元

2026-11-13 / v81。再開は [研究方針](00_research_plan.md) から。

| 現行論文 | 内容 |
| --- | --- |
| [論文A](papers/paper_a.tex)（A-v51） | 一般次元のPoisson幾何・代数的量子化・ambient復元 |
| [論文B](papers/paper_b.tex)（B-v56） | 任意のn>=3の中心三次変形の一般点可換復元と必要証明 |

論文Bの主要証明を公表の観点から再点検した。対称積の核・rotation付き一意性の定式化を正し、有限降下の核とcone、残余成分の随伴、graded stabilization、完備MF移送の有限rank性の証明を補った。Carqueville--Kay、Etingof--Ginzburgを含む先行研究との関係を序論に記載する。主定理の存在結論を弱める問題は今回の点検では見つかっていないが、組合せの新規性の確定・外部査読・形式検証は未了である。

必要証明は `papers/generic_recovery/` 内で自立する。[証明案内](notes/generic_recovery.md)、[監査と文献比較](notes/paper_b_proof_audit.md)、[実行した検証](validation_paper_b.json) を参照。今回Aおよび共有preambleの数学的内容は変更していない。

独立な点スキーム・Jacobian・一次変形・Artin・étale・相対模型の成果はnc-cubic2へ移管済みである。現在の入口と担当境界は [移管境界ノート](notes/paper_b_scope_and_transfer.md)。

```sh
python3 scripts/check_layout.py
python3 scripts/verify_bundle.py
python3 scripts/build.py --only paper_b
python3 scripts/verify_bundle.py --only paper_b --require-pdfs
```

Aは `python3 scripts/build.py --only paper_a` で組版できる。LuaLaTeX・LuaTeX-ja・latexmkを用いる。PDF・SyncTeX・中間物はbuild/で非追跡。GitHub mainに保存し、Actions・force pushを使用しない。LibraryはGitHub保存の実失敗時のみ緊急退避に使う。
