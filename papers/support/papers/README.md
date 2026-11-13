# 現行A/Bの入力と文献

2026-11-14 / v89。論文AはA-v57、論文BはB-v58。全体の入口は[研究方針](../../../00_research_plan.md)。

[論文A](../../paper_a.tex)はこのディレクトリの `sections/` と専用参考文献を読み込む。[論文B](../../paper_b.tex)の必要証明・参考文献は [generic_recovery/](../../generic_recovery/) にあり、A/Bはここにある `common.tex` を共用する。

再生成はリポジトリルートから `python3 scripts/build.py --only paper_a` または `--only paper_b` で行う。`scripts/build.py` の `source_closure` が各入口の再帰的な全TeX入力を求め、`scripts/verify_bundle.py` がラベル・引用と必要な入力の整合性を確認する。再開用bundleにはこのA/B依存閉包を元のパスのまま収録する。

独立した点スキーム・Jacobian・Artin・étale・相対復元の現行原稿と担当境界は [専用ノート](../../../notes/paper_b_scope_and_transfer.md)、その研究の入口は [nc-cubic2の現行研究ノート](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/relative_reconstruction_models.md) にある。
