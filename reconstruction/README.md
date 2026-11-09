# 可換復元：局所rotation・saturation・étale実現

**2026-11-10・v16。研究全体の正本はGitHub main。最初にルートの00_research_plan.mdを読む。**

このディレクトリは論文Cの現行証明を独立組版する入口であり、第四の主論文ではない。旧bundleやLibraryを取得せず再開できる。既存の局所rotation・Serre関手・full coherent比較・spreadの全証明を保持した。

## 数学的状態

`tex/rotation_saturation_reduction.tex` は局所模型と還元を記し、`tex/etale_realization.tex` を直接inputする。後者は親論文Cからも同じファイルを読む。

実在するsmooth proper dg族と可逆perfect双加群が、一点でsmooth cubicのKuとrotationに一致すれば、étale局所的に可換cubic族となることを、実際の同値双加群の障害消去で証明した。負HH消滅、HH¹=0、幾何的KSのrotation不変HH²への全射を使う。原稿に証明を記載して点検したが、外部査読・Lean形式検証ではない。新規性の包括的確認は未了。

所定の局所量子化がある成分のgeneric復元に残る仮定は残余対角perfect性(SM)である。SM自体、全成分での量子化入力、全点の復元、大域降下は未完成。35係数sliceの計算はSMも復元係数の閉公式も証明しない。

## 再現（リポジトリルートから）

Python 3.10以上、SymPy、LuaLaTeX、LuaTeX-ja/ltjsarticle、標準数学パッケージを用いる。

```sh
python3 -m pip install -r reconstruction/requirements.txt
python3 reconstruction/computations/verify_nonelliptic_inputs.py --output /tmp/nc-cubic-center.json
python3 reconstruction/computations/verify_etale_inputs.py --output /tmp/nc-cubic-tangent.json
python3 reconstruction/scripts/build.py
python3 reconstruction/scripts/verify.py
```

PDFは `reconstruction/pdf/rotation_saturation_reduction.pdf` に生成される。buildは全TeX inputをハッシュ化し、verifyはinput閉包・ラベル・引用・source/PDFの対応と二つの厳密計算証明書を確認する。日付を固定して組版するが、別バージョンのTeXエンジンでのPDFのバイト同一性は保証しない。PDFや中間生成物はGitで重複管理しない。

中心検算はQ(r,u)上のDiamond重なりと中心交換子を、変形slice検算は整数・有理数上の84×49行列と35次元補空間を扱う。これらを圏同値や残余smoothnessの計算機形式化と呼ばない。

親三論文全体の再組版は別の検証であり、今回の独立組版成功から推論しない。生成・検証・GitHub登録・遠隔確認の実際の状態を区別する。Libraryはpush実失敗時だけの緊急避難である。
