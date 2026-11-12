# nc-cubic 現行編集・再現指示

**2026-11-12 / v71。GitHub mainが正本。** 最初に `00_research_plan.md` を読む。

## ユーザーの指定

論文A（`papers/paper_a.tex`、A-v51）はnc-cubicに残す。論文Aとその入力ソースを変更・移管しない。論文B（`papers/paper_b.tex`、B-v55）は、任意の n>=3 の一般点可換復元主定理と必要な証明だけを収録する。新しい研究結果の追加より、論文の焦点、完全な証明、参照と組版の整合を優先する。

Bの支持ソースは `papers/generic_recovery/` の9ファイル。共有preambleは従来の `papers/support/papers/common.tex`。主定理の証明はnc-cubicだけで読め、nc-cubic2の未公表証明を取得することを前提にしない。中心三次元の次数3と超曲面の次元nを混同しない。

## 独立成果の移管は未完了

`notes/paper_b_scope_and_transfer.md` に現行の分担と残件を記す。nc-cubic2に全文保存した6節だけで移管全体を完了扱いにしない。既存のモジュライ・明示量子化原稿へ統合し、必要な補題・文献・コードを揃え、照合と組版を確認する。未移管のソースを削除せず、旧コミットへのリンクだけで有効な結果を保持したとしない。

古い支持節・検算スクリプトにはBの旧配置への参照がある。主論文Bからは読まないが、独立成果の再開に必要な現行資産として残している。移管先の動作確認後に必要なコードと参照を整理する。Aが読む節と計算をその作業に巻き込まない。

## 証明状態と検証

現在の定理には証明が記載されているが、今回の編集は全補題の独立再証明ではない。一般点の有限拡大と方程式の基礎体を区別する。特殊点込み相対同値、任意の抽象的nc cubicの表示、全射影化の導来同値を結論に加えない。

`latexmk -r .latexmkrc papers/paper_b.tex` で全文を組版する。B-v55は実際に27頁で組版し、全頁表示確認、未解決参照・引用・文字欠落・overfullは0。静的な11入力の参照照合と数学の独立監査は別。状態は `validation_paper_b.json`、証明の依存は `notes/generic_recovery.md`。

日本語LuaLaTeX。PDF・中間物はbuild/で非追跡。GitHub Actions・force pushなし。mainへの保存後に遠隔HEADとファイルを確認する。LibraryはGitHub pushの実失敗時のみ緊急退避し、既存Libraryファイルを無断削除しない。
