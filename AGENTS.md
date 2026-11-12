# nc-cubic 現行編集・再現指示

**2026-11-13 / v72。GitHub mainが正本。** 最初に `00_research_plan.md` を読む。

## ユーザーの指定

論文A（`papers/paper_a.tex`、A-v51）はnc-cubicに残す。論文Aとその入力ソースを変更・移管しない。論文B（`papers/paper_b.tex`、B-v55）は、任意の n>=3 の一般点可換復元主定理と必要な証明だけを収録する。新しい研究結果の追加より、論文の焦点、完全な証明、参照と組版の整合を優先する。

Bの支持ソースは `papers/generic_recovery/` の9ファイル。共有preambleは `papers/support/papers/common.tex`。主定理の証明はnc-cubicだけで読め、nc-cubic2の未公表支持節の取得を前提にしない。中心元の次数3と超曲面の次元nを混同しない。

## 独立成果の移管状態

`notes/paper_b_scope_and_transfer.md` が現在の所在と残件の正本である。点スキーム4節はnc-cubic2の `papers/mixed_cubic_point_schemes.tex` に統合・検証・保存し、対応する元の17専用ファイルを除外した。必要な中心式の全文証明、文献、4検算コード、現行ノートは移管先にある。古いpoint_scheme専用入口・検査スクリプトを復活させない。

一次変形・Plücker障害と有限Jacobian復元の2節は移管先に全文保存済みだが統合未完。Artin・étale理論、Sklyanin/多ブロック、相対対角・bar・Morita、混合族のjet・同変性等は移管が残る。`mixed_test_family.tex` と検算は点スキーム以外の結果も含むため保持する。

各移管単位は、定理・証明・必要補題・文献・コードを現行原稿に統合し、参照・組版・必要計算・移管先main保存を確認してから元の配置を整理する。未移管のソースを削除せず、旧コミットへのリンクだけで有効な結果を保持したとしない。Aが読む節と計算を巻き込まない。

## 証明状態と検証

原稿に証明があることと、全補題の独立再証明は異なる。一般点の有限拡大と方程式の基礎体を区別する。特殊点込み相対同値、任意の抽象的nc cubicの表示、全射影化の導来同値を結論に加えない。

`latexmk -r .latexmkrc papers/paper_b.tex` で全文を組版する。B-v55は27頁で組版・全頁表示確認済みで、未解決参照・引用・文字欠落・overfullは0。その検証対象の本文は今回変更していない。状態は `validation_paper_b.json`、依存は `notes/generic_recovery.md`。点スキームの計算・組版の実施範囲は移管先の `validation_mixed_cubic_point_schemes.json` を参照する。

日本語LuaLaTeX。PDF・中間物はbuild/で非追跡。GitHub Actions・force pushなし。mainへの保存後に遠隔HEADとファイルを確認する。LibraryはGitHub pushの実失敗時のみ緊急退避し、既存Libraryファイルを無断削除しない。
