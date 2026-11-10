# 追跡中PDFの数学的内容保全監査（2026-11-10）

**状況：８本・計574ページ。原PDFの完全なTeX置換が確認できたものはまだ0本。**
GitHub `main` が正本で、既存PDFは数学的な情報が失われないよう例外的に追跡する。
対応原本はLibrary内にある同一バイトサイズの版と照合し、目次を確認した。
内容の完全一致を主張するものではない。

| Gitで追跡中のPDF | 対応した原本（2026-11-01） | ページ数 | TeXの現状 |
|---|---|---:|---|
| `notes/pdf-only/categorical_boundary_notes.pdf` | `nc_cubic_unified_notes_ja_20261101_v1.pdf` | 16 | 関連ノートあり、11節の完全照合未了 |
| `notes/pdf-only/finite_smoothness_notes.pdf` | `nc_cubic_p4_notes_ja_20261101_v4.pdf` | 34 | 第23節 pp.26–31のdg反例をTeX化 |
| `papers/pdf-only/ambient/central_cubic_technical.pdf` | `nc_cubic_p4_paper_ja_20261101_v5.pdf` | 61 | 第28節 pp.43–44の中心正則性をTeX化 |
| `papers/pdf-only/ambient/central_pair_formal_moduli.pdf` | `nc_cubic_unified_paper_V_ja_20261101_v16.pdf` | 60 | 量子化、中心三次対、全Artin比較の関連TeXあり、一致未了 |
| `papers/pdf-only/boundary/brill_noether.pdf` | `nc_cubic_unified_paper_I_ja_20261101_v2.pdf` | 58 | 大部な包括TeXと部分重複。相対gluing等は未照合 |
| `papers/pdf-only/boundary/central_quotient_singularities.pdf` | `nc_cubic_unified_paper_VI_ja_20261101_v1.pdf` | 61 | 第15節 pp.25–27の中心曲面判別式をTeX化。Azumaya等は未移植 |
| `papers/pdf-only/boundary/pfaffian_contact.pdf` | `nc_cubic_unified_paper_III_ja_20261101_v2.pdf` | 89 | 包括TeXのPfaffian節にかなりの重複あり。全証明一致未了 |
| `papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf` | `nc_cubic_unified_paper_II_ja_20261101_v16.pdf` | 195 | 包括TeX・Sklyanin節との部分重複。全混合族は未照合 |

## 今回確実にソース化した内容


- `notes/source_recovery/dg_perfectness_counterexamples.tex`：特殊・Artin perfect性は相対perfectnessを含意しないこと、非開性、Hom有限性。原本p.26–31。
- `papers/source_recovery/central_cubic_generic_smoothness.tex`：二つの中心チャートの貼合せによるperfectnessとvery-general中心三次商の正則性。比較原稿p.43–44。
- `papers/source_recovery/central_fiber_discriminant.tex`：中心曲面の完全判別式、特異点の全列挙、混合因子への帰結。原論文VI p.25–27。有限恒等式は `computations/source_recovery/verify_central_fiber_discriminant.py` でも検査する。

## この比較で特に失ってはならない成果

- 論文VI：正確なtails判別式 `(α³+9)(28α³+243)`、中心上のAzumaya locus、Brauer指数6、21中心特異点と3つのhomological singularity、spherical twist。
- 論文II：全21混合方向の量子補正、標識付き全Artin比較、点加群スキーム、非自明な臨界層と局所特異点。
- 論文V：中心三次対の41次元incidence/17次元商、全Artin形式局所比較、偏極付き復元。
- 論文I・III：相対gluingとPfaffian接触商の独立した高次証明。

## 追跡解除の厳格な条件

そのPDFのすべての定理・仮定・証明・反例・計算資産が現行TeXから再現可能であること、
LuaLaTeXと再現計算を確認すること、関連原稿が自立していることを確認した上で
`git rm --cached`を行う。見出し類似や断片的なTeX化だけでは解除しない。
参照 TODO：[`TODO_PDF_SOURCES.md`](TODO_PDF_SOURCES.md)。


**Reye原論文77ページ・専用ソース・検証コードの移行先：** https://github.com/uedakazushi/reye （移行先の同一PDF blob SHA検証済み）。
