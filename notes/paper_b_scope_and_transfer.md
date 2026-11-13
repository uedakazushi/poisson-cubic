# 論文Bの独立成果：移管完了と現在の所在

2026-11-13。現行の独立成果の移管と元側の専用重複整理を完了した。

論文A `papers/paper_a.tex`（A-v51）と論文B `papers/paper_b.tex`（B-v56）はnc-cubicに保持する。Bの必要証明は `papers/generic_recovery/` 内で自立し、外部参照だけで代用しない。公表向け数学監査の現状は `paper_b_proof_audit.md` と `../validation_paper_b.json` にまとめる。以下の移管時入力照合は `validation_transfer.json` が指定する移管時の版についての記録である。

## 移管先の現行入口

- [点スキーム](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/mixed_cubic_point_schemes.tex)
- [有限Jacobian復元](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/cubic_jacobian_recovery.tex)
- [一次変形とPlücker障害](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/cubic_first_order_deformations.tex)
- [有限Artin window](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/cubic_artin_windows.tex)
- [étale局所実現](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/relative_cubic_realization.tex)
- [相対復元・有限対角・明示模型](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/relative_reconstruction_models.tex)

最後の統合稿は残る41支持節、ノート固有の相対proper模型・PI生成子・有限bar判定・perfect性反例、普遍二次jetを論理順に収める。既存稿とArtin・étale・Hochschild・反例・混合中心式を同じTeXから共用する。`am:cor:formal-residual` は全次数MF存在の証明とともに保持し、条件付き移送だけで置き換えない。

## 検証と保存

統合稿244頁、54TeX入力、708ラベル、724参照、266引用、143文献項目。未解決・重複・文字欠落・overfullなし。全頁を描画してレイアウトを概観し、追加した末尾部分も表示確認した。29本の有限検算を実行し、対応する既存証明書は数学データが一致する。証明書の参照パスと末尾改行を正規化した。Artin稿も現行共有反例で再組版・有限dg検算を行った。

移管元の621数学的環境のうち612は空白・局所名前空間以外の本文を保持、9件は既存共有稿の参照整理・局所証明補足を照合した。これは全数学的証明の独立監査・形式検証・新規性の確定ではない。

先に移管先mainの内容コミット `8ca6ccae84413d88fcaa4fc7062f0b23750ddfc5` と遠隔blobを確認し、その後142専用ファイルを整理した。A・Bの26入力のSHA-256一致と参照閉包を再検査する。A/Bの検算、混合研究監査TeXが使う文献、保護対象と共有する計算は残す。旧候補資料は今回の現行B支持節の移管対象ではなく、既存の照合資料として保持する。

全対応は [manifest](https://github.com/uedakazushi/nc-cubic2/blob/main/validation_reconstruction_manifest.json)、今回の範囲は [validation](https://github.com/uedakazushi/nc-cubic2/blob/main/validation_relative_reconstruction_models.json)、再開は [専用方針](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/relative_reconstruction_models.md)。残るkernel比較・多ブロック生成・高次係数・新規性は数学の研究課題であり、移管未了とは分ける。
