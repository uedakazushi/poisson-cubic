# nc-cubic 現行編集・再現指示

**2026-11-13 / v73。** GitHub mainが正本。最初に `00_research_plan.md` を読む。

論文A（A-v51）はnc-cubicに残し、本文と入力ソースを移管・変更しない。論文B（B-v55）は任意のn>=3の一般点可換復元主定理と必要証明のみ。支持ソースは `papers/generic_recovery/` の9本、共有preambleは `papers/support/papers/common.tex`。中心元の次数3と超曲面の次元nを混同しない。必要証明を移管先への参照だけで代用しない。

## 移管の現在の状態

正本は `notes/paper_b_scope_and_transfer.md`。点スキームはnc-cubic2の `papers/mixed_cubic_point_schemes.tex` に統合・検証・保存し、元の専用17ファイルを除外済み。有限Jacobian復元は `papers/cubic_jacobian_recovery.tex` に全証明・例・反例・文献・検算を備えて統合した。元の専用本文・コード・再生成可能証明書3ファイルを除外する一方、主定理に必要な低次数同定と一意性は `gradient_recovery.tex` に残し、共有文献断片は他の移管まで維持する。

一次変形・Plücker障害は全文保存済みだが統合未完。次はcft:*、am:*等の依存と計算を解決し、17次元モジュライ研究と照合する。その後、Artin/étale、Sklyanin/多ブロック、対角/bar/Morita、混合jetを同じ手順で移管する。`mixed_test_family.tex` とその検算には未移管の独立結果があるので削除しない。

各単位で証明・入力・文献・コードを保存し、必要範囲の組版・計算と遠隔mainを確認してから元の重複を整理する。旧コミットや旧ZIPへのリンクで数学的内容を保持したとはしない。新研究の拡張より原稿編集と移管完了を優先する。

## 検証と保存

B-v55は27頁で全文組版・表示確認済み。今回その原稿は変更・再組版していない。状態は `validation_paper_b.json`、依存は `notes/generic_recovery.md`。独立稿の実施範囲は移管先の各validationを参照する。有限計算・組版と全数学的監査を区別する。

`latexmk -r .latexmkrc papers/paper_b.tex` で再生成する。日本語LuaLaTeX、PDF・中間物はbuild/で非追跡。Actions・force push禁止。区切りでmainへfast-forward保存し遠隔確認する。Libraryは実際のpush失敗時のみ緊急退避、既存Libraryの無断削除は禁止。
