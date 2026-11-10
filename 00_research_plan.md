# 研究方針：cubicのPoisson構造・量子化・可換復元

**2026年11月10日・v23。再開時は最初に本ファイルを読む。**

## 正本と現在の目標

**GitHub uedakazushi/nc-cubic の main を唯一の正本とする。** 次に notes/research_notes.md、論文C papers/rotation_cubic_reconstruction.tex を読む。旧ZIP・会話・Libraryを再開の前提にしない。

最優先の目標は、構成した非可換cubicの少なくとも幾何学的一般ファイバーについて、同じKuznetsov成分とrotationを持つ滑らかな可換cubicを構成すること。元の可換cubicへの復元を要求するのではなく、量子中心対から復元先の方程式を求める。全パラメータに一価の有理閉公式が存在するとは仮定しない。

現在の直接経路は、Kontsevich formalityの中心写像から可換Casimir W を取り出し、Wを曲率として保持したままPoisson項を消去する方法である。混合試験族の二次式と内部shift付きMF同値が得られ、Koszul次数論によって一般の斉次中心三次形式変形にも延びた。形式的MF復元とArtin底の射影残余模型との相対比較を証明し、非零パラメータへの代数化を次の核心として扱う。

一般の代数的可換復元は未完成。SM・ER・有限bar対角による存在経路も保持する。この方針変更は、形式的な可換模型を直接構成する経路が具体化したためであり、元のgeneric復元目標を放棄するものではない。

## 三つの目標と達成条件

\(X^n=V(F)\subset\mathbb P^{n+1}\)、\(n\ge3\)、\(N=n+2\) とする。周囲はN個の次数一生成元を持つ \(\mathrm{nc}\mathbb P^{n+1}\)。

1. **Poisson構造の構造定理。** 三変数Jacobianブロック正規形・逆構成・一般階数。論文A papers/sections/poisson_geometry.tex の thm:pg-normal に証明あり。全既約成分と交叉の完全分類を達成条件とはしない。
2. **各固定Poisson構造の代数的量子化。** \(0\in U\subset\mathbb A^1_h\) 上で、Koszul AS-regularな周囲 \(A_h\)、中心三次正則元 \(\Omega_h\)、次数別flatな商 \(B_h\)、\(B_0=\mathbb C[z]/(F)\) を構成する。同ファイルの thm:pg-quantization に証明あり。全Poisson係数方向を保つ一様相対量子化は、これより強い未解決問題。
3. **構成した量子化のgeneric可換復元。** 必要な有限分離拡大・étale被覆を明示して
   \[
   (\mathcal K(B_h),\rho_{B_h})\simeq(\operatorname{Ku}(Y_h),\rho_{Y_h})
   \]
   を構成する。一般混合型で未完成。Kuだけの同値と指定rotationを保つ同値を区別する。

任意のAS-regular中心三次商の全点復元にはZhang twistによるrotation付き反例があり、この範囲には広げない。「証明あり」は本文に証明があるという状態で、全既存結果の独立監査・外部査読・形式証明の完了ではない。

## 現在の主要な到達点

### 一般形式的MF復元

\(S=\mathbb C[z_1,\ldots,z_N]\)、\(F\in S_3\)、\(V(F)\)を滑らかとする。単位と内部次数を保つ結合形式変形 \(A_h\cong S[[h]]\) と、斉次中心三次元 \(\Omega_h\equiv F\bmod h\) を入力する。積が最初からbidifferentialであることは仮定しない。

formalityと全Hochschild cochainへの包含により、形式的斉次二次Poisson tensor \(\pi_h=O(h)\) と代数同型 \(\Phi_h\) を選ぶ。周期変数を入れる前のdegree −1の中心同型から、実際の三次Casimir \(W_h\) を
\[
\mathcal U^{\pi_h}(W_h)=\Phi_h(\Omega_h)
\]
で求める。

勾配Koszul複体の完全性と次数により、一意な定数係数trivector \(\Xi_h\in h\wedge^3\mathbb C^N[[h]]\) が存在し、
\[
\pi_h=[\Xi_h,W_h],\qquad[\Xi_h,\pi_h]=0.
\]
後者にはJacobi恒等式が必要である。rank4・係数次数1のKoszul cycleの原像はrank5・係数次数−1となるため消える。

\(\deg t=(2,-3)\) とすれば
\[
\exp(\operatorname{ad}(\Xi_h/t))(-tW_h+\pi_h)=-tW_h.
\]
これを全有限Artin切断 \(R_r=\mathbb C[h]/(h^{r+1})\) で有限階数graded MFへ移す。bar写像は \(F_{2j+1}=O(h^j)\)、arity≤2r+1で、逆も有限である。内部shiftと三次周期性を保持する。一ブロック、独立中心変数、事前の残余SMを入力に加えない。

証明は papers/reconstruction/curved_gauge_comparison.tex と formal_cubic_mf_reconstruction.tex。固定内部次数の成分内で収束を取れば、次数別完備な \(\mathbb C[[h]]\) 上の有限rank graded MFにも同値を得る。ただし非零の複素数hへの特殊化や、任意の対象を持つgeneric MF圏への比較は別に確認する。

### 明示的な二次公式と混合族

対称関係 \([z_i,z_j]=h\,\mathrm{sym}(\pi^{ij})\)、PBW性、中心元 \(\Omega=\mathrm{sym}(F+h^2C)\) を仮定すると、h³=0で
\[
W_2=F+h^2\left(C-\frac1{48}\sum_{i,k}Q_{ik}F_{ik}\right),
\quad
Q_{ik}=\sum_{j,l}(\partial_l\pi^{ij})(\partial_j\pi^{kl})
\]
が内部shift付き可換MF模型である。一次の中心補正を含めないという仮定を明示する。この有限jetの系は、入力が全次数へ延長できることを必要としない。

混合入力
\[
F_\lambda=(x^3+y^3+z^3)/3+u^3+v^3+\lambda uxy,\qquad\lambda^3\ne-3
\]
について、指定中心元は \(a=\lambda u\)、Tをxyzの六語の和として
\[
\Omega=\frac{x^3+y^3+z^3}{3}-\frac{h^2}{9}T
+\frac a2(xy+yx)+\frac{h^2a^2}{6}z+\frac{h^4a}{18}z^2+u^3+v^3.
\]
全パラメータ中心性と全Artin切断PBWは mixed_test_family.tex に証明がある。

kontsevich_second_jet.tex では
\[
\widehat F_\lambda
=F_\lambda+h^2\left(\frac{xyz}{3}-\frac{\lambda^2u^2z}{12}\right)\pmod{h^3}
\]
とのMF同値を構成した。中心元のWeyl記号は \(F-h^2H_{\rm act}/12\)、星積への対称化補正は \(+h^2H_{\rm act}/8\) なので、結果は \(H_{\rm act}/24\)。Ditoのeye項とShoikhetのtangent-wheel消滅を区別する。

\[
[G_2]=\left(\frac13+\frac{\lambda^3}{36}\right)[xyz],
\qquad
G_2-\left(\frac13+\frac{\lambda^3}{36}\right)xyz
=-\frac{\lambda^2z}{36}\partial_uF_\lambda.
\]
係数1/36は重みからの予測ではなく計算結果である。u′=u−h²λ²z/36で \(F_\lambda(x,y,z,u',v)+h^2(1/3+\lambda^3/36)xyz\) に直せる。λ³=−12では二次類が零になるが、高次の消滅は結論しない。MF pairの低rotation積は本文の10×15行列で完全に指定した。

### 混合族の全次数同変正規形

新しく papers/reconstruction/mixed_equivariant_normal_form.tex に、
混合族の有限対角群 H と指標 χ を使って、同変formalityの選択と
全次数の形式的線形正規形を証明した。
三次Jacobian商の三指標成分は
\(J(F_\lambda)_3^H=\mathbb C[uxy]\)、
\(J(F_\lambda)_3^\chi=\mathbb C[xyz]\)、
\(J(F_\lambda)_3^{\chi^2}=0\)。
H不変な可換模型は、H同変な形式GL_5座標変換により
\[
W_h\sim F_{\lambda_*(h^3)}+h^2c_*(h^3)xyz,\quad
\lambda_*(q)=\lambda+O(q),\quad
c_*(0)=\frac13+\frac{\lambda^3}{36}
\]
にできる。これは二つの形式級数への\textbf{全次数の還元}であり、
その高次係数を計算したものでも、非零hでの代数化でもない。
\(\lambda^3=-12\)では二次項が消えるが、h³のλ方向はなお許される。
character商の有限行列は computations/verify_mixed_characters.py。
Kontsevichの線形同変性は既知、中心元からの同変化と正規化は本文で証明する。
この一般性での先行研究上の初出は未確認。

### Artin底の射影残余比較

papers/reconstruction/artin_residual_mf_comparison.tex の am:thm:comparison と am:cor:formal-residual に証明があり、独立に点検した。d個の変数、a=d−3について、周囲でperfectな相対特異圏を介した
\[
\Psi=\operatorname{stab}\circ(\mathbf R\omega -)_{\ge4-d}
\]
が、線束生成残余圏 \(\mathcal K_B^{\rm lin}\) と有限rank graded MFを同定し、\(\Psi\rho\simeq(1)\Psi\) を与える。Homの自然な底変更・nilpotent perturbation・Ind圏での生成性を個別に示した。am:prop:Gamma-basechange は既存の正則局所模型Γ_Rの非正則Artin商への底変更を扱う。

したがって全有限Artin切断で、同じW_hにより、非可換の線束生成残余pairを可換cubicのperfect Kuznetsov成分へ復元できる。非正則底の全有界coherent圏をperfect圏と同一視しない。

### 形式的smoothnessからgenericへ進めない明示的反例

papers/reconstruction/artin_smoothness_obstruction.tex の四次元free dg模型Γは、R=C[[h]]上properで、特殊fiberと全Artin切断がsmoothだが、generic fiberは非smoothである。既知のP¹上の生成子退化例を用い、genericの外積dg代数に無限Torを持つaugmentation加群を構成する。これは一般的な持上げ原理の反例であり、本研究のnc cubicに指定されたΓの反例ではない。反例のcohomologyはh-torsionを持つ。現行線束模型Λの有限自由なH⁰⊕Hⁿという追加条件下の持上げは否定していない。特殊fiberのsmoothnessと全Artin同値だけからSMを結論する経路は使わない。

### 維持する既存成果

- 分離型の点曲線 \(f+h^2\det\operatorname{Hess}(f)/24\) はMori–Smithの既知公式。適切な楕円中心商と独立中心変数Pの仮定で既存のブロック比較を使う。式の恒等式だけで圏同値を結論しない。
- rotation次数一・二の自然変換の積から勾配空間Kを求め、可積分行列Aを解き、\(F=\sum_i x_i(Aq)_i/3\) で候補を抽出する。共通射影零点なし・可逆解が必要。候補の射影的一意性と存在を区別する。
- cubic threefoldの純ordinary-HKR bivectorはHH²(Ku)への制限で零。pure Poisson KSと残余制限の両立を確認した上で適用する。一般次元・全次数定数性・SMには拡張しない。
- 非楕円fivefoldの節点・尖点成分、全次数PBW、35係数slice、有限bar右逆判定、A∞arity制約、論文Bの17次元族・余次元15・核7等の有効な証明を保持する。
- BFK sectorによりHH³のrotation不変部分は全n≥3で零。形式的障害消滅はSMそのものではない。
- \(q_i=x_i^2+x_{i+1}x_{i+2}\)（mod5）は正しい完全交差Hilbert級数を持つが積分不能。Hilbert級数やHom階数だけで復元を判定しない。

## 未解決の核心と次の着手

1. **完備底・genericへの比較。** Artin残余比較は証明した。次は次数別完備MF同値が、既存Γの指定生成子を可換側の生成子へ送ることを、特殊fiberだけに頼らず示す。失敗例は artin_smoothness_obstruction.tex。実際の有限cone/retract表示、または指定生成子の像の明示的計算を優先する。Λの対象の添字・内部次数・積の向きから、対角の持上げが有限filtrationを保つかを調べる。有限rankのA∞双加群を作るだけでは有限cell性を結論しない。通常の有限自由代数へMorita帰着できる場合の十分条件と証明は研究ノートに置く。
2. **高次の具体式。** 同変正規形を用い、まずh³のλ方向係数a₁、次にh⁵のxyz方向係数b₁を計算する。h⁴のJacobian類は零だが、生のh⁴係数が零とは限らない。結合積のPoisson逆像、中心tangent map、gaugeを順に計算し、λ³=−12を判別点とする。
3. **代数化とgeneric。** 完備底上の実際のgraded MF同値から、指定残余生成子・generic base change・有限型へのspreadを追う。Artinでのkのdescendabilityは \(\mathbb C[[h]]\) では使えない。可換smooth proper族でも生成子の性質は一般に開条件ではない。全有限jetの成功だけでSMを結論しない。
4. **SM・ER経路。** 実際のproper残余dg代数Γの有限perfect対角と増大射、または有限bar-skeletonの右逆を構成する。ERには実在するsmooth proper pairを入力する。周囲の対角やSerre関手は代用にならない。
5. **全Poisson成分。** スカラーchartと必要な有限分離・étale底変更を使い、係数方向を保つ相対量子化を確認する。rank層と既約成分を同一視しない。

反例 \(\mathrm{MF}(R[x],x)=0\ne D_{\rm sg}(R)\)、\(R=\mathbb C[\epsilon]/\epsilon^2\) を保持する。非正則Artin底で絶対特異圏との比較を流用しない。

## 検証と再開

新しい同変正規形の証明を本文に記載した。指標商の係数行列は別途記号計算で照合したが、formalityと圏論的部分の外部査読・形式証明は未実施。外部査読・Lean形式証明・包括的な新規性確認は未実施。Kontsevich、Dito、Shoikhet、Căldăraru–Tu、Tu、Chen等の一次資料と適用箇所をbibliographyに記録する。

二次星積・tensor・積行列の厳密検算は公開コードでPASSした。論文Cの従前のソースは133頁・32 TeX inputsで組版・検査済み。今回追加した同変正規形の節を含む現行v23の全論文Cは未組版・未検証である。既存三つの具体計算証明書、arity証明書、独立SM/ERの三証明書も再生成して照合した。計算のJSONを手で復元したものは収録しない。各原稿の正確な状態はvalidation.jsonを読む。

再開時はvalidation.jsonの各原稿の状態を確認する。計算と全inputの参照・引用検査は公開コードで再実行した。既存の計算資産と証明全文はmainに保持する。独立SM/ER節とA/Bの組版は別状態として記録する。

## 研究一般の原則と保存規則

1. 数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究価値を最大化する。重要な方針変更の理由・達成点・残る問題は現行方針として書き直し、時系列の履歴を蓄積しない。
2. 証明済み、条件付き、未完成、予想、計算的観察を分け、仮定・依存・証明所在を示す。証明の記載、独立監査、計算実行を区別し、誤りが判明した場合は依存する主張と要約も更新する。
3. 重要文献は一次資料を確認し、未確認の書誌や新規性を補作しない。外部PDF・検索結果は大量収録しない。
4. 公表価値のある成果と証明全文を日本語LuaLaTeXで保持し、既存成果を削らず論理的に統合する。ノートは着想・例・反例・障害・必要な文献比較を整理し、作業日誌や重複証明にはしない。
5. **研究の区切りごとに承認を求めず、方針・ノート・論文の証明全文・必要なコード/入力/証明書/再現手順をmainへ通常のfast-forwardで反映する。** remote変更を保持し、force push・無断PR・GitHub Actionsは使わない。反映後にremote refと主要blobを再取得する。
6. **Library保存はGitHub反映が実際に失敗した場合だけの緊急避難。** 成功時には二重保存しない。退避時は未同期と復帰手順を明示し、既存Libraryファイルは明示指示なしに削除しない。
7. 最新一式だけで研究を再開できる構成とする。旧ZIP・旧稿・変更履歴・作業ログ・キャッシュ・バックアップ・重複物を収録しない。軽量化のために有効な数学的内容や必要な証明を削らない。
8. 日付・版・参照を揃え、生成・計算・組版・保存・遠隔確認を別々に報告する。LuaLaTeXはルート.latexmkrcからbuild/へ生成し、PDFをGit追跡しない。未実行・失敗・再現上の制約を明示する。
