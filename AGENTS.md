# nc-cubic 現行編集・再現指示

**2026-11-13 / v74。mainが正本。最初に00_research_plan.mdを読む。**

論文A `papers/paper_a.tex`（A-v51）とその入力はnc-cubicに保持し、変更・移管しない。論文B `papers/paper_b.tex`（B-v55）は任意のn>=3の一般点復元主定理と必要証明だけを読む。証明は `papers/generic_recovery/`、共有設定は `papers/support/papers/common.tex`。新しい研究より編集・独立成果の移管を優先する。

点スキーム、有限Jacobian復元、一次変形・Plücker障害はnc-cubic2の独立稿へ統合した。現行原稿はそれぞれ `papers/mixed_cubic_point_schemes.tex`、`papers/cubic_jacobian_recovery.tex`、`papers/cubic_first_order_deformations.tex`。詳しい状態と残件は `notes/paper_b_scope_and_transfer.md`。移管先で本文・文献・検算・組版・保存を確認した専用重複だけを整理し、全移管完了と混同しない。

一次変形稿に必要な双対数windowの証明を添えたことは、一般Artin理論全体の移管完了ではない。`artin_residual_mf_comparison.tex`、相対Artin/étale、Sklyanin/多ブロック、対角/bar/Morita、混合jetなどの未移管成果は保持する。Todd補正による別証明も保持する。元のfirst_order本文・2検算コードは移管先の同名現行ファイルが正本であり復活させない。

原稿に証明があること、独立監査、有限検算、組版、保存を区別する。方程式の基礎体と同値核の有限拡大を混同しない。特殊点込み相対同値、全射影化の導来同値、任意抽象nc cubicの表示を追加しない。

B-v55は27頁組版・全頁表示確認済みで今回未変更。検証はvalidation_paper_b.json。新しい独立一次変形稿は10頁、移管先のvalidation_cubic_first_order.jsonに実施範囲を記録した。全数学的証明の形式検証ではない。

日本語LuaLaTeX。PDF・中間物はbuild/で非追跡。Actions・force pushなし。main保存後に遠隔確認。Libraryは実際のpush失敗時のみ緊急退避し、既存Libraryを無断削除しない。
