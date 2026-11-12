# Codex実行指示 — nc-cubic

2026-11-13 / v78。最初に `00_research_plan.md` と `notes/paper_b_scope_and_transfer.md` を読む。GitHub mainが正本。

## 完了した移管と担当境界

論文Bから独立した現行成果の移管は完了。nc-cubic2の `papers/relative_reconstruction_models.tex` と既存五稿、専用ノート・validation・manifestが正本。完了した専用ソースを再導入しない。移管先の既存研究や別担当の更新を上書きしない。

Chat側の担当はAのPoisson正規形・量子化、Bの完備MF比較・一般点降下、一次文献・新規性の独立監査と改良。移管完了と全数学的監査の完了を混同しない。

## 厳格な保護

- 今回の移管で `papers/paper_a.tex`（A-v51）、`papers/paper_b.tex`（B-v55）、両者の再帰的な全入力、`papers/generic_recovery/`、`papers/support/papers/common.tex`、共通設定を編集・削除していない。以後の移管整理でも保護する。必要証明を移管先へのリンクだけで代用しない。
- パスだけで移管可否を決めず、input/include・論理参照・引用・ノート・コードの実依存を確認する。共有する文献・証明書・検算を消さない。
- 数学的問題は具体的な仮定・反例・依存先とともに監査ノートへ記し、主定理を迂回して強化・弱化しない。
- 全次数MF存在と条件付き移送、全coherentと線束生成圏、有限Artinと一般Artin、形式と代数的同値、相対smooth properの仮定を区別する。

## 検証と保存

変更前・push前に最新mainを取得する。通常のfast-forward pushと遠隔ref/blob確認を行い、force push・Actions・不要なPR・旧版ZIP・バックアップ複製を作らない。生成PDF・中間物はbuild/で非追跡。Libraryは実際のGitHub保存失敗時だけの緊急退避。節目のmain保存に追加承諾は不要。

重要な証明・例・反例・書誌・再現入力を落とさず、移管先へ統合して参照・必要な全文組版・厳密計算・保存を確認してから元の真の重複を除く。旧ZIP・旧PDF・旧コミットを現行証明の代用にしない。有限体での零を特性零の恒等式の証明と混同しない。証明記載・有限検算・独立監査・形式検証・新規性を区別する。

日本語LuaLaTeXと現行.latexmkrcを使い、研究方針・現在有効なノート・必要最小限のvalidationを更新する。数学的重要性・正確性・理解・応用・実現可能性を重視し、歴史ログや重複した論文を増やさない。
