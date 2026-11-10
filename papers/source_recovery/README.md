# 段階的な PDF → TeX 回復

各ファイルは追跡中の原PDFから**一部の定理と証明だけ**を復元した独立原稿である。原PDFを完全に再生成できるとは主張しない。

- `notes/source_recovery/dg_perfectness_counterexamples.tex`：`notes/pdf-only/finite_smoothness_notes.pdf` 第23節 pp.26–31 の非連結dg加群の反例・補題・適用限界。
- `papers/source_recovery/central_cubic_generic_smoothness.tex`：`papers/pdf-only/ambient/central_cubic_technical.pdf` に相当する比較稿第28節 pp.43–44 の中心二チャートによる判定とvery-general正則性。

他の数学的成果も失われないよう、各原PDFは全章・全証明との照合が済むまではGitで保持する。全体の進捗と残作業は `TODO_PDF_SOURCES.md` に記す。

- `papers/source_recovery/central_fiber_discriminant.tex`：原論文VI（`central_quotient_singularities.pdf`）第15節 pp.25–27 の中心曲面の判別式と特異点の分類。検証コードは `computations/source_recovery/verify_central_fiber_discriminant.py`。Azumaya・Brauer・非可換tailsの残りはPDFに保持。

- `papers/source_recovery/reye_stationary_core.tex`：原論文IV（`reye_stationary.pdf`、77ページ）の §2–3 と §4.1–4.4 の中核を証明付きで復元。275停留点・Hessian pencil・長さ2・275本のReye三次曲線を扱う。`computations/source_recovery/verify_reye_275.py` はChern・Hesseの有限恒等式を検証。**このTeXは原PDF全体の代替ではない**。

- `papers/source_recovery/reye_full_monodromy.tex`：原論文IVの第13節（普遍275点被覆、二点付きincidenceの全相対位置、分岐conormalの唯一の特異直線、単一transposition、monodromy `S_275`、double symmetroidの550本の対角作用）を独立のLuaLaTeX原稿として再構成。原論文第3・10節の存在・網羅性・法束結果を入力とする。検証コードは `computations/source_recovery/verify_reye_two_point_ranks.py` と `verify_reye_fold_conormal.py`。前者は一般相対位置の厳密数値特殊化であり、全特殊層の普遍証明ではない。

- `reye_deformations_degree_one.tex`：原論文IV第5・9・10節の法束・全Artin比較、定階数Hessian直線、550本の全次数1曲線とGW仮想数550の主要証明。第3・4節の一般275点とregularityを明示的入力とする。
- `reye_length_three_cusp_jet.tex`：原論文IV第12節の長さ3停留点の四次消去と二変数versal cuspの有限jet計算。射影ordered族の全域regularity・PT仮想寄与を無条件に主張しない。
- 有理数体上の有限検算：`computations/source_recovery/verify_reye_cusp_jet.py`、`verify_reye_pencil_cases.py`。
