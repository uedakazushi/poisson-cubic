# 段階的な PDF → TeX 回復

各ファイルはnc-cubic2で保全されている原PDFから**一部の定理と証明だけ**を復元した独立原稿である。原PDFを完全に再生成できるとは主張しない。

- `notes/source_recovery/dg_perfectness_counterexamples.tex`：`notes/pdf-only/finite_smoothness_notes.pdf` 第23節 pp.26–31 の非連結dg加群の反例・補題・適用限界。
- `papers/support/papers/source_recovery/central_cubic_generic_smoothness.tex`：`papers/pdf-only/ambient/central_cubic_technical.pdf` に相当する比較稿第28節 pp.43–44 の中心二チャートによる判定とvery-general正則性。

他の数学的成果も失われないよう、各原PDFは全章・全証明との照合が済むまではGitで保持する。全体の進捗と残作業は [PDF照合一覧](../../../../notes/source_recovery/pdf_source_checklist.md) に記す。

- [nc-cubic2の中心曲面判別式TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/central_fiber_discriminant.tex)：原論文VI（`central_quotient_singularities.pdf`）第15節 pp.25–27 の中心曲面の判別式と特異点の分類。検証コードは [nc-cubic2の記号検算コード](https://github.com/uedakazushi/nc-cubic2/blob/main/computations/verify_central_fiber_discriminant.py)。Azumaya・Brauer・非可換tailsの残りはPDFに保持。




Reye に属する部分復元 TeX・原PDF・計算コードは [uedakazushi/reye](https://github.com/uedakazushi/reye) に移行した。

この中心判別式の独立TeX・検算コードは [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) にGit blob一致で移管した。主研究に必要な中心チャートのgeneric正則性 `papers/support/papers/source_recovery/central_cubic_generic_smoothness.tex` はここに残す。
