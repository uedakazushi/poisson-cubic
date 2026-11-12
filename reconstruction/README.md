# 可換復元：局所rotation・saturation・étale実現

**2026-11-12・v23。研究全体の正本はGitHub main。最初にルートの00_research_plan.mdを読む。**

このディレクトリは論文Bの補助証明を独立組版する入口であり、第四の主論文ではない。過去のbundleやLibraryを取得せず再開できる。既存の局所rotation・Serre関手・full coherent比較・spreadの全証明を保持した。

## 数学的状態

`papers/support/papers/reconstruction/rotation_saturation_reduction.tex` は局所模型と還元を記し、`papers/support/papers/reconstruction/etale_realization.tex` と `papers/support/papers/reconstruction/hochschild_obstructions.tex` を直接inputする。後者は親論文Bからも同じファイルを読む。

実在するsmooth proper dg族と可逆perfect双加群が、一点でsmooth cubicのKuとrotationに一致すれば、étale局所的に可換cubic族となることを、実際の同値双加群の障害消去で証明した。負HH消滅、HH¹=0、幾何的KSのrotation不変HH²への全射を使う。原稿に証明を記載して点検したが、外部査読・Lean形式検証ではない。新規性の包括的確認は未了。

この存在証明の経路で、所定の局所量子化がある成分のgeneric復元に残る仮定は残余対角perfect性(SM)である。SM自体、全成分での量子化入力、全点の復元、大域降下は未完成。35係数sliceの計算はSMも復元係数の閉公式も証明しない。

## 再現（リポジトリルートから）

Python 3.10以上、SymPy、LuaLaTeX、LuaTeX-ja/ltjsarticle、標準数学パッケージを用いる。

```sh
python3 -m pip install -r reconstruction/requirements.txt
python3 reconstruction/computations/verify_nonelliptic_inputs.py --output /tmp/nc-cubic-center.json
python3 reconstruction/computations/verify_etale_inputs.py --output /tmp/nc-cubic-tangent.json
python3 reconstruction/computations/verify_hochschild_sectors.py --output /tmp/nc-cubic-hh.json
python3 reconstruction/scripts/build.py
python3 reconstruction/scripts/verify.py
```

PDFは `build/rotation_saturation_reduction.pdf` に生成される。buildは全TeX inputをハッシュ化し、verifyはinput閉包・ラベル・引用・source/PDFの対応と三つの厳密計算証明書を確認する。日付を固定して組版するが、別バージョンのTeXエンジンでのPDFのバイト同一性は保証しない。PDFや中間生成物はGitで重複管理しない。

中心検算はQ(r,u)上のDiamond重なりと中心交換子を、変形slice検算は整数・有理数上の84×49行列と35次元補空間を扱う。BFK sector整数検算は既知の公式から導かれた次数・次元・非自明固有値の算術を検証する。これらを圏同値や残余smoothnessの計算機形式化と呼ばない。

親二論文全体の組版は独立SM/ER入口とは別の検証である。各補助原稿の組版の実際の状態はルートvalidation.jsonを参照する。生成・検証・GitHub登録・遠隔確認の実際の状態を区別する。Libraryはpush実失敗時だけの緊急避難である。

## パス移動後の実行方法

TeX原稿は `papers/support/papers/reconstruction/`、ノートは `notes/reconstruction.md`、生成PDFはルート `build/` に統一した。Gitに生成PDFは登録しない。

```sh
latexmk papers/support/papers/reconstruction/rotation_saturation_reduction.tex
python3 reconstruction/scripts/build.py
python3 reconstruction/scripts/verify.py
```

SMの有限bar対角・generic spreadingの証明は `notes/sm_bar_and_spreading.tex`（根拠原本：[有限正則性の現行TeX](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/ambient_finite_smoothness_and_recovery.tex) 第18--21節）。今回の補題はSM自体を証明しない。


## 具体的な方程式の抽出と二次比較（親論文B）

親Bは従来の有限積分・一次消滅・分離型Hessian式・混合中心とPBWに加え、curved_gauge_comparison.tex、kontsevich_second_jet.tex、formal_cubic_mf_reconstruction.tex、artin_residual_mf_comparison.tex、artin_smoothness_obstruction.texを読む。全次数の形式MF復元、全Artinの線束残余比較、混合二次係数1/3+lambda³/36、低rotation積、およびgenericへの移行を妨げる一般dg反例を記載する。これらはSM/ERの独立入口とは別のinput閉包に属する。

```sh
python3 computations/verify_explicit_jacobian_recovery.py --output /tmp/nc-cubic-jacobian.json
python3 computations/verify_explicit_model_comparison.py --output /tmp/nc-cubic-explicit-model.json
python3 computations/verify_mixed_test_family.py --output /tmp/nc-cubic-mixed.json
python3 computations/verify_kontsevich_second_jet.py --output build/kontsevich_second_jet_certificate.json
python3 scripts/build.py
python3 scripts/verify_bundle.py
```

第一計算は有理数上でFermat・混合smooth cubic・積分不可能な二次完全交差を判定し、第二計算は一般十係数三次式のHessian恒等式、Hesse特殊化、二次Jacobian類の相違を検算する。一般nc残余圏の導来自然変換・圏同値・SMの計算機形式化ではない。純Poisson一次消滅は一次文献を用いた本文の証明であり、計算コードで証明したものではない。

混合族の証明書は `python3 computations/verify_mixed_test_family.py` で再生成できる。自由代数の三つの多項式恒等式を有理数演算で検算し、中心性を全パラメータで証明する。有限h-jetによる独立検算と、非零hのAS性・圏同値とは区別する。

主論文のbuildはbuild/<paper>.receipt.jsonへ全inputのハッシュ、PDFハッシュ、エンジン、組版警告を記録する。verify_bundleはreceiptがある原稿についてsource/PDF対応を検査し、既存三つの具体計算証明書を再生成して照合する。二次Kontsevich計算は一時JSONへ再生成して恒等式・行列を検算し、未確認のJSONを手で復元したものとは照合しない。A/Bを再組版しない場合は、そのPDFが現行だと報告しない。


## 検証の射程と再開

公開コードの二次検算はPASSした。旧版の原稿について133頁の組版・表示確認を記録しているが、現在の論文Bの新入口については未組版であり、独立SM/ERも組版・receipt・検算がPASSした。各原稿の詳細はルートvalidation.jsonを参照する。共通bibliographyも更新したため、古い原稿名のreceiptが残る環境では現行A/Bを再組版してからverify_bundleを実行する。コードはgraph積分、formality、圏同値を形式証明するものではない。詳しい状態はルートvalidation.jsonを読む。
