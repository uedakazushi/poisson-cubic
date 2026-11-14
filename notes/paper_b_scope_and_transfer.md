# 現行A/Bと独立成果の所在・担当境界

2026-11-14 / v94。論文AはA-v61、論文BはB-v59。再開は[研究方針](../00_research_plan.md)から。

## nc-cubicで扱う研究

[論文A](../papers/paper_a.tex)はPoisson正規形・退化軌跡・代数的量子化・固定相対モジュライを扱い、ambient復元を付録に置く。[論文B](../papers/paper_b.tex)は中心三次変形の一般点可換復元を扱う。Bの必要証明は `papers/generic_recovery/` 内で完結し、A/Bの主張を読むために独立原稿の取得を必要としない。

現行A/Bの編集・公表準備では、本文とその再帰入力、専用ノート、必要な計算・証明書を一体として更新する。Aの確認範囲は[投稿準備監査](poisson_article_submission_audit.md)と [validation](../validation_paper_a.json)、Bは[証明監査](paper_b_proof_audit.md)と [validation](../validation_paper_b.json)を参照する。

## nc-cubic2に置く独立成果

- [点スキーム](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/mixed_cubic_point_schemes.tex)
- [有限Jacobian復元](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/cubic_jacobian_recovery.tex)
- [一次変形とPlücker障害](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/cubic_first_order_deformations.tex)
- [有限Artin window](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/cubic_artin_windows.tex)
- [étale局所実現](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/relative_cubic_realization.tex)
- [相対復元・有限対角・明示模型](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/relative_reconstruction_models.tex)

相対復元の統合稿には、相対proper模型、PI生成子、有限対角、有限bar判定、perfect性の反例、普遍二次jet、および楕円ブロックの明示模型を収める。Artin・étale・Hochschildの比較と全次数MF存在の証明を保持し、各構成の追加仮定を区別する。これらの成果を追究するときは、同リポジトリの[現行研究ノート](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/relative_reconstruction_models.md)を読む。

## 担当と未解決の核心

nc-cubicではAの正規形・量子化とBの完備比較・一般点降下を進め、nc-cubic2では上記独立成果の公表向け構成と証明を整える。各リポジトリの本文と必要証明をその現在の入口に維持し、共有する主張の仮定や参照を変更するときは両側への影響を確認する。

独立構成で追究する課題には、有限模型からのrotation積・比較核の有効な計算、同変な高次係数、有限bar右逆、二つ以上の無限位数ブロックの生成性、Artinから完備底へのperfect性の制御がある。一般点で得られる同値と全閉パラメータでの相対同値は別の主張であり、これらの個別課題をBの一般点存在定理の未証明部分として扱わない。

各主張の証明記載・独立点検・有限検算・新規性は、対応する現行原稿と専用ノートで確かめる。A/Bの再開用bundleは、研究方針、上記の専用ノート、A/Bの全TeX入力と再現資産から構成する。
