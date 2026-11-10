# nc-cubic：Poisson構造・代数的量子化・可換復元

**2026-11-10・v23。正本はGitHub main。** 最初に [研究方針](00_research_plan.md)、次に [研究ノート](notes/research_notes.md) を読む。

## 三つの目標

| 目標 | 内容 | 状態 |
|---|---|---|
| Poisson構造 | 滑らかなcubic n-fold (n≥3) のJacobianブロック正規形・一般階数 | 論文Aに定理・証明あり |
| 代数的量子化 | 各固定Poisson構造をKoszul AS-regularな周囲と中心三次商で実現 | 論文Aに定理・証明あり |
| 可換復元 | 構成した量子化のgenericを、同じKuとrotationを持つ可換cubicとして実現 | 形式MF・全Artin線束残余pairまで証明。generic代数化は未完成 |

証明の記載、独立点検、計算実行、外部査読・形式検証を区別する。個別量子化と全Poisson係数方向を保つ一様相対量子化は別問題。任意のAS-regular中心三次商の全点へのrotation付き復元には反例がある。

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

有限対角群Hの線形同変性と古典Jacobian商の指標分解から、
同変形式模型を形式的な線形座標変換で
\[
W_h\sim F_{\lambda_*(h^3)}+h^2c_*(h^3)xyz,\qquad
\lambda_*(q)=\lambda+O(q),\quad c_*(0)=\frac13+\frac{\lambda^3}{36}
\]
に整理できる。**全次数で未知となる形式級数は二つ**に限るが、
h³以降の係数の値、代数性、generic可換復元は未解決。
詳細証明は [mixed_equivariant_normal_form.tex](papers/reconstruction/mixed_equivariant_normal_form.tex)。
指標ごとの三次単項式とJacobian行列は
`python3 computations/verify_mixed_characters.py` で再現できる。

## generic復元に残る問題

全Artin切断での成功から、相対残余対角のperfect性(SM)は自動的には従わない。P¹上の既知の生成子退化例から、特殊fiberと全Artin切断がsmoothなのにgenericが非smoothなrank4のproper dg模型を明示した。これは本研究のnc cubicに指定されたΓの反例ではない。またその反例のcohomologyは底上flatではなく、現行線束模型の追加構造を否定しない。

次は、完備MF同値による指定生成子の像、実際の有限cone/retract表示、generic base changeと代数化を確認する。実在するsmooth proper pairからのétale実現ER、有限bar右逆によるSM判定、非楕円fivefoldと全成分の相対化も維持する。

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

**v23の検証状態：** 既存の二次星積・tensor・積行列の厳密検算はv22ソースでPASS。新しい指標商も別途記号計算で検算した。現行v23の論文Cは新節追加後にまだ全体組版・receipt検査していない（従前は133頁・32 inputsを組版済み）。既存の具体計算証明書と独立SM/ERの検算も再実行した。A/Bを含めた詳細はvalidation.jsonを参照。これらは圏論的証明の形式検証や外部査読ではない。

## 資料の配置と保存

mainだけを正本とし、LibraryはGitHub反映が実際に失敗した場合の緊急退避に限る。通常のfast-forwardで反映し、GitHub Actions、force pushは使わない。PDFはGit追跡しない。

独立Pfaffian・Brill–Noether・中心判別式研究と未照合原PDF8件は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2)、Reye研究は [reye](https://github.com/uedakazushi/reye) に保全されている。PDF移転とTeX完全照合は別の状態である。参照先は [TODO_PDF_SOURCES.md](TODO_PDF_SOURCES.md)、[SOURCE_RECOVERY_AUDIT_20261110.md](SOURCE_RECOVERY_AUDIT_20261110.md)。
