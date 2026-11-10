# nc-cubic：Poisson構造・代数的量子化・可換復元

**2026-11-10・v26。正本はGitHub main。** 最初に [研究方針](00_research_plan.md)、次に [研究ノート](notes/research_notes.md) を読む。

## 曲率付き絶対対角からの有限積と可換候補（v26）

**実際の非可換入力に対する計算結果、ただし残余rotation積との比較は未証明。** 混合族の λ=1 の指定中心対について、絶対曲率付き対角の閉自己準同型の合成を Q(h) 上で計算した。その対称積の核を積分すると
[
\widetilde F_h=(x^3+y^3+z^3)/3+v^3+h^2xyz/3+(1+h^6/54)uxy-h^4uz^2/18-h^2u^2z/12+(1+29h^6/648+h^{12}/4374)u^3
]
を得る。四変数の積は6×10行列、勾配変換の行列式は 1+h^6/27。これは有限の有理関数体上の計算であり、h=0で正則な中間ホモトピー・実際の残余圏との比較・一般λの式・generic rotation付き圏同値を証明したものではない。相対対角ではu³補正を検出できず、絶対対角を用いる必要がある。

**証明と再現：** papers/reconstruction/curved_diagonal_recovery.tex、computations/curved_diagonal.py、computations/absolute_diagonal.py、computations/verify_curved_diagonal.py、computations/curved_diagonal_certificate.json。研究上の障害は notes/curved_diagonal.md に整理。検算は `python3 computations/verify_curved_diagonal.py --output build/curved_diagonal_certificate.json`、出力と追跡中の証明書を照合する（重い厳密計算）。前回の検算記録と証明書を保持するが、この統合時点で長時間の完全再計算は未実施。

**次の課題：** (1) h=0で極を持つ中間ホモトピーと閉行列をDVR核飽和で正則化する。(2) 曲率付き絶対対角の積と残余dg圏の導来自然変換・rotation積との合成を保つ比較を証明する。(3) 比較が成立した後にgeneric可換模型と圏同値を検証する。SM/ERと指定生成子のgeneric生成性は独立した未解決課題として保持する。

## 三つの目標

| 目標 | 内容 | 状態 |
|---|---|---|
| Poisson構造 | 滑らかなcubic n-fold (n≥3) のJacobianブロック正規形・一般階数 | 論文Aに定理・証明あり |
| 代数的量子化 | 各固定Poisson構造をKoszul AS-regularな周囲と中心三次商で実現 | 論文Aに定理・証明あり |
| 可換復元 | 構成した量子化のgenericを、同じKuとrotationを持つ可換cubicとして実現 | 形式MF・全Artin線束残余pairまで証明。generic代数化は未完成 |

証明の記載、独立点検、計算実行、外部査読・形式検証を区別する。個別量子化と全Poisson係数方向を保つ一様相対量子化は別問題。任意のAS-regular中心三次商の全点へのrotation付き復元には反例がある。

## 有限代数的復元（現行の最優先方針）

代数的な非可換中心対から残余dg圏の**実際の**低rotation導来自然変換の積を有限代数的複体で構成し、その核を局所飽和・線形可積分性・Euler積分で可換三次式に直接復元する。選択したformalityの無限級数そのものの代数性・収束を先行条件にしない。形式MF復元は完成底での積の比較と可積分性に利用する。

**証明全文：** [有限代数的復元](papers/reconstruction/finite_algebraic_recovery.tex)。Noether局所底で、完成底の滑らかな形式三次式と同じ勾配空間を持ち、任意の有限jetを保つ代数的三次式を構成する。DVRでの核の飽和・混合可換候補の積と滑らかさ式 $(L^3+3+3C^3)^2-12L^3C^3$ も記す。

**再現資産：** [finite_recovery.py](computations/finite_recovery.py)、[verify_finite_recovery.py](computations/verify_finite_recovery.py)、[有限計算証明書](computations/finite_recovery_certificate.json)、[研究ノート](notes/finite_algebraic_recovery.md)。実際の非可換低次数積はまだ計算されておらず、人工可換候補の検算と区別する。generic圏同値、指定生成子のgeneric生成性、SM/ERも別途未証明である。

**再現方法**（リポジトリルートで実行）：
```sh
python3 computations/verify_finite_recovery.py --output build/finite_recovery_certificate.json
latexmk papers/finite_algebraic_recovery.tex
python3 scripts/verify_bundle.py
```
単独原稿7ページは組版済み。現行A/B/C全文の組版・receiptは未検査であり、PDFはGit追跡しない。

## 可換三次式を構成する

**斉次中心三次形式変形から、全次数の可換MF模型を構成する経路が得られた。**
滑らかな古典cubic F、markedな次数付き結合形式変形 A_h、中心三次元 Ω_h が入力である。formalityで対応する二次Poisson tensor π_h と実際の三次Casimir W_h を取り、勾配Koszul完全性と次数により
\[
\pi_h=[\Xi_h,W_h],\qquad[\Xi_h,\pi_h]=0
\]
を満たす一意の定数係数trivector Ξ_h を求める。
\[
\exp(\operatorname{ad}(\Xi_h/t))(-tW_h+\pi_h)=-tW_h
\]
を有限rankのgraded MFへ移すことで、内部shiftと三次周期性を保つ同値を得る。一ブロックや独立な中心一次変数は仮定しない。

全有限Artin切断では、相対特異圏とwindow (Rω−)_(≥4−d) により、この同値を線束生成残余pairへ移せる。可換側はsmooth cubicのperfect Kuznetsov成分である。次数別完備底上のMF同値も証明したが、非零の複素パラメータへの代数化とgeneric生成性は別に残る。

### 混合族の明示式

\[
F_\lambda=(x^3+y^3+z^3)/3+u^3+v^3+\lambda uxy,\qquad\lambda^3\ne-3.
\]
指定された中心元に対し、
\[
\widehat F_\lambda
=F_\lambda+h^2\left(\frac{xyz}{3}-\frac{\lambda^2u^2z}{12}\right)
\pmod{h^3}
\]
が実際の二次可換模型となる。
\[
[G_2]=\left(\frac13+\frac{\lambda^3}{36}\right)[xyz].
\]
係数1/36は星積と中心写像から計算した値であり、重みからの予測ではない。中心のWeyl記号と星積対称化との差を含めた結果である。MF pairおよび線束生成残余pairの低次数積も10×15行列として決定した。λ³=−12では二次類が零になるが、高次消滅は結論しない。

| 内容 | 証明全文 |
|---|---|
| 有限curved gaugeの有限rank MFへの延長 | [curved_gauge_comparison.tex](papers/reconstruction/curved_gauge_comparison.tex) |
| 混合族の明示二次式・低rotation積 | [kontsevich_second_jet.tex](papers/reconstruction/kontsevich_second_jet.tex) |
| 一般中心三次対の全次数形式MF復元 | [formal_cubic_mf_reconstruction.tex](papers/reconstruction/formal_cubic_mf_reconstruction.tex) |
| Artin底の相対stabilization・残余window・rotation | [artin_residual_mf_comparison.tex](papers/reconstruction/artin_residual_mf_comparison.tex) |
| 全Artin smoothでもgeneric非smoothとなる一般dg反例 | [artin_smoothness_obstruction.tex](papers/reconstruction/artin_smoothness_obstruction.tex) |
| 低次数積からの有限積分・射影的一意性 | [explicit_jacobian_recovery.tex](papers/reconstruction/explicit_jacobian_recovery.tex) |
| 純Poisson方向の一次消滅 | [poisson_first_order.tex](papers/reconstruction/poisson_first_order.tex) |
| 分離型Hessian模型・中心可換化との相違 | [explicit_model_comparison.tex](papers/reconstruction/explicit_model_comparison.tex) |
| 混合族の中心閉式・全Artin PBW | [mixed_test_family.tex](papers/reconstruction/mixed_test_family.tex) |

Kontsevich、Dito、Shoikhet、Căldăraru–Tu、Tu、Chen等の既知結果と、本文で直接証明する比較を区別する。この一般性での新規性の包括的確認は未実施。

### 全次数の同変正規形（混合族）

有限対角群Hと交換対合τ:(x,y,h)↦(y,x,−h)、および古典Jacobian商の指標分解から、
G=H⋊⟨τ⟩同変な形式模型を形式的な線形座標変換で
\[
W_h\sim F_{\lambda_*(h^6)}+h^2c_*(h^6)xyz,\qquad
\lambda_*(q)=\lambda+O(q),\quad c_*(0)=\frac13+\frac{\lambda^3}{36}
\]
に整理できる。**全次数で未知となる形式級数は二つ**に限るが、
正規形の最初の未知係数はh⁶のλ方向とh⁸のxyz方向。その値、代数性、generic可換復元は未解決。
詳細証明は [mixed_equivariant_normal_form.tex](papers/reconstruction/mixed_equivariant_normal_form.tex)。
指標ごとの三次単項式とJacobian行列は
`python3 computations/verify_mixed_characters.py` で再現できる。

## generic復元に残る問題

全Artin切断での成功から、相対残余対角のperfect性(SM)は自動的には従わない。P¹上の既知の生成子退化例から、特殊fiberと全Artin切断がsmoothなのにgenericが非smoothなrank4のproper dg模型を明示した。これは本研究のnc cubicに指定されたΓの反例ではない。またその反例のcohomologyは底上flatではなく、現行線束模型の追加構造を否定しない。

まず実際のnc低rotation積と完成底比較を構成し、有限積分を行う。その後、指定生成子の像、有限cone/retract、generic base changeと圏同値を確認する。実在するsmooth proper pairからのétale実現ER、有限bar右逆によるSM判定、非楕円fivefoldと全成分の相対化も維持する。

## 原稿と再現

| 論文 | 入口 |
|---|---|
| A：Poisson・量子化 | papers/poisson_cubic_quantization.tex |
| B：17次元族・ambient復元 | papers/generic17_ambient_recovery.tex |
| C：rotation付き可換復元 | papers/rotation_cubic_reconstruction.tex |

Python 3.10以上、SymPy、LuaLaTeX、LuaTeX-ja/ltjsarticleと標準数学パッケージを用いる。リポジトリルートから実行する。

    python3 computations/verify_kontsevich_second_jet.py --output build/kontsevich_second_jet_certificate.json
    python3 scripts/build.py
    python3 scripts/verify_bundle.py
    python3 reconstruction/scripts/build.py
    python3 reconstruction/scripts/verify.py

詳細は [reconstruction/README.md](reconstruction/README.md) と [validation.json](validation.json)。
PDFとbuild receiptはGit対象外のbuild/へ生成する。主論文receiptは全TeX inputを含む。

**v26の検証状態：** 既存の二次星積・tensor・積行列の厳密検算はv22ソースでPASS。新しい指標商と交換対合の自由代数恒等式も別途SymPyで厳密検算した。現行v26の論文A/B/Cは新節追加後にまだ全体組版・receipt検査していない（従前は133頁・32 inputsを組版済み）。既存の具体計算証明書と独立SM/ERの検算も再実行した。A/Bを含めた詳細はvalidation.jsonを参照。これらは圏論的証明の形式検証や外部査読ではない。

## 資料の配置と保存

mainだけを正本とし、LibraryはGitHub反映が実際に失敗した場合の緊急退避に限る。通常のfast-forwardで反映し、GitHub Actions、force pushは使わない。PDFはGit追跡しない。

独立Pfaffian・Brill–Noether・中心判別式研究と未照合原PDF8件は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2)、Reye研究は [reye](https://github.com/uedakazushi/reye) に保全されている。PDF移転とTeX完全照合は別の状態である。参照先は [TODO_PDF_SOURCES.md](TODO_PDF_SOURCES.md)、[SOURCE_RECOVERY_AUDIT_20261110.md](SOURCE_RECOVERY_AUDIT_20261110.md)。
