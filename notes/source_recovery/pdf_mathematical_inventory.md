# 外部に保全したPDFの数学的内容と未照合箇所（2026-11-12 / v2）

**現行状態：論文PDF5件をnc-cubic2に保持。旧資料8件は歴史的な対象数であり、研究ノート2件・Brill–Noether論文1件の追跡は解除済み。**
以前にPDF原本8件がnc-cubic2へ移管され、現在は論文PDF5件のみがnc-cubic2のmainで追跡される。nc-cubicのmainにはPDF追跡ファイルがない。
対応原本はLibrary内にある同一バイトサイズの版と照合し、目次を確認した。
内容の完全一致を主張するものではない。

| nc-cubic2で保全中のPDF | 対応した原本（2026-11-01） | ページ数 | TeXの現状 |
|---|---|---:|---|
| [`papers/pdf-only/ambient/central_cubic_technical.pdf`](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/ambient/central_cubic_technical.pdf) | `nc_cubic_p4_paper_ja_20261101_v5.pdf` | 61 | 第28節 pp.43–44の中心正則性をTeX化 |
| [`papers/pdf-only/ambient/central_pair_formal_moduli.pdf`](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/ambient/central_pair_formal_moduli.pdf) | `nc_cubic_unified_paper_V_ja_20261101_v16.pdf` | 60 | 量子化、中心三次対、全Artin比較の関連TeXあり、一致未了 |
| [`papers/pdf-only/boundary/central_quotient_singularities.pdf`](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/boundary/central_quotient_singularities.pdf) | `nc_cubic_unified_paper_VI_ja_20261101_v1.pdf` | 61 | 第15節 pp.25–27の中心曲面判別式をTeX化。Azumaya等は未移植 |
| [`papers/pdf-only/boundary/pfaffian_contact.pdf`](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/boundary/pfaffian_contact.pdf) | `nc_cubic_unified_paper_III_ja_20261101_v2.pdf` | 89 | 包括TeXのPfaffian節にかなりの重複あり。全証明一致未了 |
| [`papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf`](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/pdf-only/quantization/sklyanin_mixed_quantization.pdf) | `nc_cubic_unified_paper_II_ja_20261101_v16.pdf` | 195 | 包括TeX・Sklyanin節との部分重複。全混合族は未照合 |

## 今回確実にソース化した内容


- `notes/source_recovery/dg_perfectness_counterexamples.tex`：特殊・Artin perfect性は相対perfectnessを含意しないこと、非開性、Hom有限性。原本p.26–31。
- `papers/support/papers/source_recovery/central_cubic_generic_smoothness.tex`：二つの中心チャートの貼合せによるperfectnessとvery-general中心三次商の正則性。比較原稿p.43–44。
- [nc-cubic2の中心曲面判別式TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/central_fiber_discriminant.tex)：中心曲面の完全判別式、特異点の全列挙、混合因子への帰結。原論文VI p.25–27。有限恒等式は [nc-cubic2の記号検算コード](https://github.com/uedakazushi/nc-cubic2/blob/main/computations/verify_central_fiber_discriminant.py) でも検査する。

## この比較で特に失ってはならない成果

- 論文VI：正確なtails判別式 `(α³+9)(28α³+243)`、中心上のAzumaya locus、Brauer指数6、21中心特異点と3つのhomological singularity、spherical twist。
- 論文II：全21混合方向の量子補正、標識付き全Artin比較、点加群スキーム、非自明な臨界層と局所特異点。
- 論文V：中心三次対の41次元incidence/17次元商、全Artin形式局所比較、偏極付き復元。
- 旧論文III：Pfaffian接触商と普遍非線形接触分類。旧§23–24のHessian局所不変量・Pfaffian graph解消は [現行TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/sections/pfaffian_hessian_geometry.tex) に復元済み。他の重要な主張は未完全照合。

## TeXへの完全復元の厳格な条件

そのPDFに固有の数学的主張と重要な証明・反例・再現資産が現行TeXに統合されたことを確認し、
必要なLuaLaTeXと計算検証を行った上で、nc-cubic2の追跡PDFの解除を判断する。見出し類似や断片的なTeX化だけでは解除しない。
参照 TODO：[照合一覧](pdf_source_checklist.md)。


**Reye原論文77ページ・専用ソース・検証コードの移行先：** https://github.com/uedakazushi/reye （移行先の同一PDF blob SHA検証済み）。

## 分離先（現在有効）

独立のPfaffian・Brill–Noether技術原稿（全TeX）および中心ファイバー判別式TeX・検算コードは [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) へGit blob一致で移管した。当初移転したPDF8本のうち、現行mainには独自の証明を含む論文PDF5本のみが残る。移転、内容確認、TeX化と削除は別々の工程である。

- `notes/sm_bar_and_spreading.tex`：第18--21節（pp.23--25）の有限bar-skeleton対角判定、Artin底での検出、generic spreading、smoothnessを未証明のまま残す必要性。相対smoothnessそのものは未証明。旧34ページ全体の逐語復元ではないが、公表価値のある有限正則性・偏極付き復元の内容はnc-cubic2の現行ノートに整理済み。
