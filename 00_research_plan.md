# 研究方針：論文A・Bの保持と独立成果の移管完了

2026-11-13 / v79。GitHub mainが正本。

## 現在の所在

論文A `papers/paper_a.tex`（A-v51）、論文B `papers/paper_b.tex`（B-v55）、両者の再帰入力26ファイルと共通設定は変更していない。必要証明を外部参照だけで代用しない。

論文Bは任意のn>=3の代数的中心三次変形の一般点可換復元を扱い、必要証明は `papers/generic_recovery/` 内で閉じる。一般点の同値、有限体拡大後の核、C(h)上の方程式、特殊点を含む相対同値を区別する。論文Aは一般次元のPoisson正規形・量子化・ambient復元を保持する。

独立な点スキーム・Jacobian・一次変形・Artin・étale・楕円多ブロック・対角/bar/Morita・混合jetはnc-cubic2の既存五稿と `papers/relative_reconstruction_models.tex` に統合し、移管先保存後に元の専用重複を整理した。正確な入口・検証・残る数学は [移管境界ノート](notes/paper_b_scope_and_transfer.md)。

## 今後の担当と研究課題

Chat側はAのPoisson正規形と量子化、Bの完備MF比較・一般点降下、一次文献と新規性を独立に監査・改善する。移管作業の完了を、全証明の独立監査や未解決比較の解決と数えない。一般研究の監査記録は `notes/poisson_article_submission_audit.md`、`notes/paper_b_proof_audit.md`、`notes/generic_recovery.md` に保持する。

## 再現と保存

`python3 scripts/check_layout.py`、`python3 scripts/verify_bundle.py` でA・Bの入力を検査し、`latexmk papers/paper_a.tex`、`latexmk papers/paper_b.tex` で組版する。今回A・Bは再組版せず、入力SHA-256一致と静的検査を行う。移管先統合稿は全文244頁の組版・表示概観、29有限検算を実行した。

日本語LuaLaTeXと現行.latexmkrcを使う。生成物はbuild/に置き非追跡。重要な証明・反例・再現入力を落とさず、証明記載・計算・独立監査・新規性を区別する。GitHub mainへ通常のfast-forward保存を行い、遠隔ref/blobを確認する。Actions・force push・不要なPR・旧版ZIPを作らない。LibraryはGitHub保存の実失敗時だけの緊急退避とする。
