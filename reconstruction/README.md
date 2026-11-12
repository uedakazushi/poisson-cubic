# 独立の相対rotation・saturation・étale実現

**2026-11-13 / v24。最初にルートの00_research_plan.mdを読む。GitHub mainが正本。**

このディレクトリは、移管が残る相対理論の独立組版・検証の入口である。現在の論文B（B-v55）は `papers/generic_recovery/` に主定理と必要証明を集約しており、この入口を直接入力しない。元の相対rotation・Serre関手・全coherent比較・spreadの有効な証明は、移管が確認されるまで現行ソースに保持する。

## 数学的内容と主定理との区別

`papers/support/papers/reconstruction/rotation_saturation_reduction.tex` は局所模型と還元を記し、`etale_realization.tex` と `hochschild_obstructions.tex` を読む。

実際のsmooth proper dg族と可逆perfect双加群が一点でsmooth cubicのKuとrotationに一致する場合、étale局所的な可換族の実現を、同値双加群の障害消去によって扱う。負HH消滅、HH¹=0、幾何的KSのrotation不変HH²への全射が入力である。本文の証明と、外部査読・形式検証・包括的新規性調査を区別する。

この相対的経路では残余対角のperfect性(SM)を実際に確認する必要がある。全成分の量子化入力、全パラメータでの相対復元、大域降下を無条件には結論しない。これは指定代数的中心三次対の一般点を扱う論文Bの主定理とは別の問題である。35係数sliceの有限計算はSMや復元係数の閉公式を証明しない。

## 再現（リポジトリルートから）

Python 3.10以上、SymPy、LuaLaTeX、LuaTeX-jaと標準数学パッケージを使う。

```sh
python3 -m pip install -r reconstruction/requirements.txt
python3 reconstruction/computations/verify_nonelliptic_inputs.py --output /tmp/nc-cubic-center.json
python3 reconstruction/computations/verify_etale_inputs.py --output /tmp/nc-cubic-tangent.json
python3 reconstruction/computations/verify_hochschild_sectors.py --output /tmp/nc-cubic-hh.json
python3 reconstruction/scripts/build.py
python3 reconstruction/scripts/verify.py
```

生成先は `build/rotation_saturation_reduction.pdf`。buildはTeX入力、PDF、エンジン、組版警告のreceiptを作り、verifyは参照とsource/PDFの対応および三つの厳密計算を検査する。異なるエンジン版でのPDFのバイト一致は保証しない。今回これらの相対原稿・コードを再実行してはいない。

中心検算はQ(r,u)上のDiamond重なり・中心交換子、変形slice検算は84×49行列と35次元補空間、Hochschild sector検算は既知公式からの次数・次元・固有値を扱う。圏同値やSMの計算機形式化ではない。

TeXは `papers/support/papers/reconstruction/`、ノートは `notes/reconstruction.md` に置く。SMの有限bar対角・generic spreadingの議論は `notes/sm_bar_and_spreading.tex` と、nc-cubic2の現行 `notes/ambient_finite_smoothness_and_recovery.tex` 第18--21節を参照する。この還元だけでSMを証明するものではない。

## 有限方程式復元の移管先

有限Jacobian復元は **nc-cubic2/papers/cubic_jacobian_recovery.tex** へ統合した。必要十分条件、射影的一意性、積分不可能な完全交差、有限検査器と全証明を保持する。元の専用コードと証明書は移管先の `computations/verify_explicit_jacobian_recovery.py` で再生成する。移管先での検算入口は `python scripts/check_cubic_jacobian_recovery.py --calculations`。

## 移管が残る具体模型と有限jet

`explicit_model_comparison.tex`、`mixed_test_family.tex`、`curved_gauge_comparison.tex`、`kontsevich_second_jet.tex`、`formal_cubic_mf_reconstruction.tex`、`artin_residual_mf_comparison.tex`、`artin_smoothness_obstruction.tex` に、分離型Hessian式、混合中心とPBW、形式MF比較、相対Artin比較、混合二次係数1/3+lambda³/36、rotation積および一般dg障害例を保持する。現在の主論文Bがこれらを全て直接読むという構成ではない。

```sh
python3 computations/verify_explicit_model_comparison.py --output /tmp/nc-cubic-explicit-model.json
python3 computations/verify_mixed_test_family.py --output /tmp/nc-cubic-mixed.json
python3 computations/verify_kontsevich_second_jet.py --output build/kontsevich_second_jet_certificate.json
```

前者は一般十係数三次式のHessian恒等式・Hesse特殊化・二次Jacobian類の相違を検査する。混合族は自由代数の3恒等式と有限h-jetを分けて検査し、全非零hでのAS性や圏同値を結論しない。二次Kontsevich検算もgraph積分やformalityの形式検証ではない。純Poisson一次消滅は文献と本文の証明に基づく。

全体の現在の分担は `notes/paper_b_scope_and_transfer.md`、主論文Bの組版状態は `validation_paper_b.json`。相対原稿の過去の実行記録を現在の主論文の検証と混同しない。生成物はbuild/に置きGit追跡しない。GitHub Actions・force pushは使用せず、Libraryは実際のpush失敗時だけの緊急退避とする。
