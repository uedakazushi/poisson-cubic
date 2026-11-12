# nc-cubic 現行編集・再現指示

**2026-11-13 / v76。mainが正本。最初に00_research_plan.mdを読む。**

論文A `papers/paper_a.tex`（A-v51）と入力はnc-cubicに保持し、変更・移管しない。論文B `papers/paper_b.tex`（B-v55）は任意のn>=3の一般点復元主定理と必要証明だけを読む。証明は `papers/generic_recovery/`、共有設定は `papers/support/papers/common.tex`。新しい研究結果の追加より編集・独立成果の移管を優先する。

点スキーム、有限Jacobian復元、一次変形・Plücker障害とTodd-HKR別証明はnc-cubic2の現行原稿に統合し、専用重複を整理した。本文入口は `papers/mixed_cubic_point_schemes.tex`、`papers/cubic_jacobian_recovery.tex`、`papers/cubic_first_order_deformations.tex`（v2、13頁）。元の移管済み本文・専用コードを復活させない。共有文献断片は未移管支持節のため保持する。

有限Artin比較と完備化の障害を `nc-cubic2/papers/cubic_artin_windows.tex`（v1、13頁）に独立原稿化し、必要な正則局所の証明、反例全文、文献・検算を保存した。ただし元の `artin_residual_mf_comparison.tex` と反例は削除しない。元の末尾の `am:cor:formal-residual` とそのMF存在入力、他のmixed/formal/window原稿のam:*依存がまだ未整理である。新稿の `ar:cor:conditional` はMF同値を入力する系であり、元の存在を含む結果の置換・弱化ではない。

現在の所在は `notes/paper_b_scope_and_transfer.md`。次はrelative_formal_models・relative_etale_modelsの存在理論と、その入力・am参照を統合する。Sklyanin/多ブロック、対角/bar/Morita、混合jet等も現行ソースに保持する。各単位の自足性・必要な検証・移管先保存・他原稿の依存解消を確認してから元の重複を削除する。部分の抽出を全移管完了としない。

証明の記載、独立監査、有限検算、組版、保存を区別する。方程式の基礎体と同値核の有限拡大を混同せず、特殊点込み同値、全射影化の可換導来同値、任意の抽象的nc cubicの表示を追加しない。

B-v55は27頁で既存の組版・全頁表示確認を維持し、今回原稿未変更。新しい有限Artin稿は7TeX入力・31ラベル・36参照・11引用・5文献で組版・全頁表示とdg模型の有限検算を実行した。詳細は各リポジトリの対応validationファイル。有限検算を圏同値やsmoothnessの形式証明としない。

日本語LuaLaTeX。PDF・中間物はbuild/で非追跡。Actions・force pushなし。main保存後に遠隔HEADとblobを確認し、同時更新を保持する。Libraryは実際のpush失敗時のみ緊急退避し、既存Libraryを無断削除しない。
