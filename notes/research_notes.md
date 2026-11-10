# 研究ノート：可換復元の現在有効な知識と障害

**2026年11月10日・v26。GitHub mainだけを正本とする。** 最初に00_research_plan.mdを読む。証明全文は論文Cの現行input、局所rotation・SM・ERの詳細はnotes/reconstruction.mdと対応原稿に置く。

## 曲率付き絶対対角からの有限積と可換候補（v26）

**実際の非可換入力に対する計算結果、ただし残余rotation積との比較は未証明。** 混合族の λ=1 の指定中心対について、絶対曲率付き対角の閉自己準同型の合成を Q(h) 上で計算した。その対称積の核を積分すると
[
\widetilde F_h=(x^3+y^3+z^3)/3+v^3+h^2xyz/3+(1+h^6/54)uxy-h^4uz^2/18-h^2u^2z/12+(1+29h^6/648+h^{12}/4374)u^3
]
を得る。四変数の積は6×10行列、勾配変換の行列式は 1+h^6/27。これは有限の有理関数体上の計算であり、h=0で正則な中間ホモトピー・実際の残余圏との比較・一般λの式・generic rotation付き圏同値を証明したものではない。相対対角ではu³補正を検出できず、絶対対角を用いる必要がある。

**証明と再現：** papers/reconstruction/curved_diagonal_recovery.tex、computations/curved_diagonal.py、computations/absolute_diagonal.py、computations/verify_curved_diagonal.py、computations/curved_diagonal_certificate.json。研究上の障害は notes/curved_diagonal.md に整理。検算は `python3 computations/verify_curved_diagonal.py --output build/curved_diagonal_certificate.json`、出力と追跡中の証明書を照合する（重い厳密計算）。前回の検算記録と証明書を保持するが、この統合時点で長時間の完全再計算は未実施。

**次の課題：** (1) h=0で極を持つ中間ホモトピーと閉行列をDVR核飽和で正則化する。(2) 曲率付き絶対対角の積と残余dg圏の導来自然変換・rotation積との合成を保つ比較を証明する。(3) 比較が成立した後にgeneric可換模型と圏同値を検証する。SM/ERと指定生成子のgeneric生成性は独立した未解決課題として保持する。

## 有限代数的復元（現在の優先課題）

実際の非可換低rotation積と完成底比較の有限模型が第一の未解決課題である。条件付き代数化定理の証明全文はpapers/reconstruction/finite_algebraic_recovery.tex。局所飽和、可換候補の積表・判別式・実装上の注意は [finite_algebraic_recovery.md](finite_algebraic_recovery.md) を参照する。人工可換候補の厳密計算を実際のnc積と取り違えない。

## 目標と到達範囲

Poisson構造定理 thm:pg-normal と個々のPoisson構造の代数的量子化 thm:pg-quantization は論文Aに証明がある。各固定構造の量子化と、全Poisson係数方向を保つ一様相対量子化を区別する。一般の代数的generic可換復元は未完成。新規性の網羅的確認と全既存証明の独立再監査は完了していない。

現在は、一般の斉次中心三次形式変形について可換MF模型を構成し、全有限Artin切断で線束生成残余pairに移すところまで証明した。非零パラメータへの代数化、完備底からgenericへの生成性、実際の残余対角perfect性は別に残る。任意のAS-regular中心三次商の全点復元にはrotation付き反例がある。

## 全次数の混合同変正規形（現行の新しい補題）

証明全文：papers/reconstruction/mixed_equivariant_normal_form.tex。
非可換混合族の有限群H（αβγ=1、χ=αβδ、h↦χh）に、交換対合τ:(x,y,h)↦(y,x,−h)を加えたG=H⋊⟨τ⟩を使う。τは自由代数でr₁↦−r₁、r₂↦r₃、r₃↦r₂、Ω↦Ωを満たす。sorted PBW標識はH同変だが、τとは一般に可換しないため、標識の全G平均でG同変な加群同定を作る。Kontsevich affine formalityはGL同変であり、
全normalized Hochschild complexへの包含も同変。
有限群不変部分の完全性を用いてformalityのMaurer--Cartan比較と
一入力gaugeをG同変に選べる。中心のCasimir逆像W_hもG不変になる。
この比較は既存の二次jetを保持して行える。

三次単項式の指標空間は
- 1：x³,y³,z³,u³,v³,uxy（6次元）、Jacobian部分空間は5次元。
- χ：xyz,u²z（2次元）、関係はzF_u=λxyz+3u²z。
- χ²：uz²（1次元）、関係はuF_z=uz²。

よってJacobian商の各成分はC[uxy]、C[xyz]、0。両生成元はτ固定であり、H自明部分のτ反不変生成元はx³−y³=xF_x−yF_yでJacobianイデアルに属する。
h^r係数は指標χ^(-r)に属するとともに、x,y交換では固有値(-1)^rを持つ。
各次数のJacobian理想成分をG同変な一次線形vector fieldで除く
h進帰納法により、形式正規形
\[
W_h\sim F_{\lambda_*(h^6)}+h^2c_*(h^6)xyz,\quad
\lambda_*(0)=\lambda,\quad c_*(0)=1/3+\lambda^3/36
\]
が得られる。これは具体的な高次級数の決定、収束、SM、generic圏同値ではない。
最初の未計算係数はh⁶uxy方向a₁とh⁸xyz方向b₁。
h³,h⁴,h⁵のJacobian類は零だが、非同変表示で生の係数の零を意味しない。
λ³=−12ではc₀=0でもh⁶のa₁が残り得る。
厳密指標計算コード：computations/verify_mixed_characters.py。
同じ一般性での先行研究上の初出は未確認。

## 一般形式復元の機構

証明は papers/reconstruction/formal_cubic_mf_reconstruction.tex。S=C[z₁,…,z_d]、滑らかな射影三次式F、多項式環の単位・内部次数を保つ結合形式変形A_h、斉次中心三次元Ω_hを入力する。

1. T_poly→D_poly→全normalized Hochschild cochains のformalityを使い、A_hを形式的斉次二次Poisson tensor π_hの星積へ移す。既存の積がbidifferentialであるとは仮定しない。
2. 周期変数を導入する前に、degree −1の中心同型から実際の三次Casimir W_h を求める。このdegreeには境界が入らないので、中心のcohomology classだけの同定ではない。
3. 全偏微分のKoszul完全性により、π_h=[Ξ_h,W_h]となる一意の定数係数trivector Ξ_h を求める。Jacobi恒等式により[Ξ_h,π_h]はrank4・係数次数1のKoszul cycleとなり、その原像の係数次数が−1になるので零である。分解可能なΞや一ブロック性は不要。
4. deg t=(2,−3)で exp(ad(Ξ_h/t))(−tW_h+π_h)=−tW_h。curved gaugeのTaylor arityは1と3、flowはF_(2r+1)=O(h^r)。有限Artinでは有限和、次数別完備底では各固定成分内で収束する。
5. 有限rank twisting行列Qがhの倍数でなくても、対象・射への挿入和と逆写像が定義される。証明は curved_gauge_comparison.tex。これが(1)と(3)=[2]を保つ実際のMF同値を与える。

pure π_h=hπとcanonical中心U^(hπ)(F)を選んだ対は元のFへ戻る。しかし与えられた対称関係の代数と指定中心元については、π_h自体にも高次補正があり得る。半古典πだけで高次W_hを決めない。有限jetの代数同定はその後のformality持上げで保てる。

## 明示的二次式と混合族の積

対称二次関係 [z_i,z_j]=h sym(π^{ij}) とPBW性、中心元Ω=sym(F+h²C)を仮定した二次jetの公式は
\[
W_2=F+h^2\left(C-\frac1{48}Q_{ik}F_{ik}\right),
\qquad Q_{ik}=(\partial_l\pi^{ij})(\partial_j\pi^{kl}).
\]
全次数への延長を仮定しない有限jetの系である。一次の中心補正を含めないという入力条件がある。

混合族は
\[
F_\lambda=(x^3+y^3+z^3)/3+u^3+v^3+\lambda uxy,\quad\lambda^3\ne-3.
\]
mixed_test_family.texの指定中心元・全Artin PBWを使うと、kontsevich_second_jet.texにより
\[
\widehat F_\lambda=F_\lambda+h^2\left(xyz/3-\lambda^2u^2z/12\right)
\quad\bmod h^3
\]
との内部shift付きMF同値が得られる。Artin相対比較を合成すると線束生成残余pairにも適用できる。

active Hessian H_act=8xyz−2λ²u²z、Q=−2 adj(Hessian)である。中心のWeyl記号はF−h²H_act/12だが、星積対称化はT(F)=F+h²H_act/8なので、実際の曲率はF+h²H_act/24となる。Ditoの星積eye項は非零、Shoikhetのboundaryのないtangent-wheel W₂は零であり、同じgraphとして扱わない。

\[
[G_2]=c(\lambda)[xyz],\quad c(\lambda)=1/3+\lambda^3/36,
\qquad G_2-c(\lambda)xyz=-\lambda^2z\,\partial_uF_\lambda/36.
\]
u′=u−h²λ²z/36で座標正規化できる。λ³=−12はsmoothだが二次変形類が零となる点であり、高次項を判別する入力になる。高次消滅は主張しない。u=0への単純な制限では、中心平面自体を動かすこの座標補正を捉えられない。

MFのR-linearなNat(Id,(1))は自由rank5、Nat(Id,(2))はrank10。相対対角Koszul/sector計算により後者はJ(\widehat F)_2で、全文の10×15積表と5×15勾配核が原稿にある。平方minorは9。このカテゴリカルな同定は本文の定理であり、検算scriptがnc Nat complexを直接構成したわけではない。

対角群のcharacterは二次方向をC[xyz]に制限するが、係数1/36は重みだけでは求まらない。λも動かす作用からc(ζλ)=c(λ)が従うという観察は、同変性の確認と高次項の候補削減に有用である。

### 二次変形類の内在的定義

Lを変形dg Lie代数、α=ha+h²bをMC元、一次類が零でa=dξとする。gauge exp(hξ)で一次項を消すと、
\[
\alpha'=h^2\left(b+\tfrac12[\xi,a]\right),\qquad
\kappa_2=\left[b+\tfrac12[\xi,a]\right]\in H^1(L)
\]
を得る。d b=−[a,a]/2、d[ξ,a]=[a,a]なので閉じている。別のξ′=ξ+z、dz=0では差は[ z,a ]/2=d[z,ξ]/2。一次項が零の代表間の恒等mod h gaugeも二次項を境界だけ変える。したがってκ₂は一次自明化の選択によらない。

L=CC•(K)[1]ならH¹L=HH²(K)。h↦χhの同変変形ではκ₂の重みはχ⁻²である。この議論自体は可換模型の存在を仮定しないが、入力の残余変形とそのKS同定は必要。新規性を主張する補題ではなく、方向制約を圏内部で使うための整理である。

## Artin底で射影残余pairへ移す

artin_residual_mf_comparison.tex のam:thm:comparison、am:prop:Gamma-basechange、am:cor:formal-residualを参照。絶対D_sg(B)ではなく、Res_A M∈Perf(A)を満たす複体による相対商を使う。Chenの加群論的入力とexact Frobenius圏のdg商を通してstabilizationを構成する。finite totalizationのcontractionも本文に明記した。

windowはi=4−d。線束sectionのこの切断は例外列を消し、残る三つの線束の像から三つのresidue stabilizationを得る。線束HomとMF Homを、特殊fiberのsplit contractionに対するnilpotent perturbationで有限free複体へ縮約し、自然なderived base changeを確認する。無界な自由複体を無条件にK-flatとする議論は使わない。

生成性はInd圏とR_N∈thick(k)により持ち上げる。rotationは(RωM)_(4−d)=RHom(O(d−4),M)=0から内部shiftと同定する。これらは全coherent圏の有限cohomological dimensionを仮定しない。可換側では線束がPerf(Y_N)を生成するため、perfect Kuznetsov成分への復元を得る。

Artin基底でMFと絶対特異圏を混同しないための例はR=C[ε]/ε²、A=R[x]、W=x。Q²=xの微分でMFは零だがD_sg(R)は零でない。全文証明はcurved_gauge_comparison.tex。

## 維持する具体的復元原理

- 分離型の点曲線 f+h² det Hess(f)/24 はMori–Smithの既知公式。適切な楕円中心商と独立な中心変数Pの仮定で既存ブロック比較に使える。explicit_model_comparison.texに証明とHesse特殊化を保持する。
- 低次数rotation積の核Kから可積分行列Aを解き、F=Σx_i(Aq)_i/3を求める。可逆性と共通射影零点なしが必要。射影的一意性は存在とは別で、Fermatの積分解空間はscalar一次元ではない。explicit_jacobian_recovery.texを参照。
- q_i=x_i²+x_(i+1)x_(i+2)（mod5）は正しい完全交差Hilbert級数を持つが可積分行列の核が零。rank25とminor15872が証明書にある。この例がnc cubicから生じるとは主張しない。
- cubic threefoldの純ordinary-HKR bivectorのHH²(Ku)への制限は零。Todd補正・JLLZの作用の単射性を扱った証明はpoisson_first_order.tex。pure Poisson KSと残余制限の両立が入力であり、高次定数性・一般次元・SMへ拡張しない。
- 中心のsorted PBW表示には一次項が現れても、可換復元の一次類とは別である。混合中心式のh²(λu)²z/6を落とすと中心性が壊れる。全パラメータ中心性と全Artin PBWの証明は保持する。

## 1. SM・ERによる存在証明の経路

所定の正則局所底上の次数別自由な中心三次量子化から、properな線束生成残余dg代数Γ_Rと、逆 `(-1)R_O` を持つ標準rotationが得られる。残余対角条件(SM)があれば全coherent残余圏との一致と有限型smooth proper pairへのspreadが従う。

étale局所実現(ER)は、実在するsmooth proper pairを入力とする定理として独立の証明を得た。従ってこの存在証明の経路では、量子化入力がある成分のgeneric可換復元の未解決条件はSMである。非楕円二成分の量子化は既存の具体的構成を使えるが、Poisson係数方向を保持した一様相対量子化は全成分で完成していない（各固定構造の代数的量子化の存在とは別）。

## 2. ERの実際の証明に必要な点

sourceの滑らかな幾何的変形族とtargetの実在するsmooth proper dg族を取る。同値双加群Pの小拡大障害はExt²(P,P)=HH²(source)に入る。両側に自己同値のliftがあり、還元上のintertwinerがあるため、障害の自然性からその類はrotation不変である。ここでintertwiner自体のliftはまだ仮定しない。

幾何的KSが不変HH²に全射なので、sourceのliftを修正して障害を消す。Pのperfect liftはunit/counitのconeにNakayamaを適用して同値となる。intertwinerの持上げ障害はHH¹であり、cubicでは零。最後にactual perfect対象と射のmoduliを使い、同値・同型が開条件であること、負HH消滅によるArtin性、無限小smoothness、pointed étale sectionを確認する。

この方法は抽象的なHochschild変形のactual性、HH³=0、formalityを使わない。自己同値一つのpairだけを扱い、選択した三次周期性のcoherenceは結論しない。親 `rotation_models.tex` の形式変形比較全体を再監査したことでもない。

一次資料と参照箇所は `papers/reconstruction/etale_references.tex`。Toën–Vaquié, arXiv:math/0503269v5, Theorem 3.6/Corollaries 3.15,3.17,3.19、Lowen, arXiv:0707.2602v1, Theorem 4.8を使う。Lin–Zhang, arXiv:2611.05915v1, §2.1/Theorem 2.2/Proposition 2.4は幾何的な両側projectorを仮定するため非幾何的targetへ直接引用しない。同じ障害消去原理との関係を本文に明記した。

## 3. cubicのHochschild入力と具体的slice

N=n+2≥5に対し、HH<0=0、HH0=C、HH1=0。HH2はJ(F)_3、ただしn=4では二つの追加方向を持つ。BFKのsector公式で非恒等sectorは3|Nかつcohomological degree N/3に各一次元となる。四次元の追加二方向はrotation固有値ζ,ζ²を持ち、不変部分は常にJ(F)_3で、次元はbinom(N,3)。幾何的KSとの同定にはn≥4でHuybrechts–RennemoのLemma 2.19と§3.3、n=3でJLLZ Theorem 4.4(2)を用いる。単なる次元一致だけでKS同型を結論しない。

節点・尖点の滑らかなcubic fivefold
F=f+ux²+a³+b³+c³+u(a²+b²+c²)+u³、f_C=xz²+y³、f_N=xyz+y³+z³
について、84個の三次単項式と49個の z_j partial_i F からなる整数行列を構成した。コード `reconstruction/computations/verify_etale_inputs.py` は階数49、表示された35単項式の商基底、射影の二恒等式を厳密検算する。採用49行の小行列式は尖点で2^15·3^26、節点で−2^6·3^25。SymPyの有理演算と独立な整数Bareiss消去で照合した。

これによりF+Σt_m mという具体的35係数source族が得られる。量子パラメータ(r,s)からt_mへの閉公式は未計算であり、SMを検算したわけではない。証明書には単項式の順序、全基底、採用行を収録する。

## 4. 各成分を扱う支配的chart

`papers/sections/all_poisson_components.tex` のスカラーchart定理は、非零被約既約アフィン錐Zを滑らかな S=T×A¹_h で支配する。h≠0では稠密開への同型、h=0では零点へ縮約する。Tは射影化の滑らかな稠密アフィン開で、スカラー代表を一座標で規格化する。

generic復元のために特異な頂点への量子化の降下を先に解く必要はない。幾何学的一般点のブロック正規形を有限分離拡大へ移し、分母と判別式を除いて有限étale被覆上で固定する。これは正規形の存在を入力とする帰結である。一つのPoisson方向だけの形式弧では成分のgenericを扱えず、係数方向Tを保つ必要がある。

## 5. 中心元の有限jet代数化

有限行列M(h)の形式核ベクトルは、係数整域の縮小とq(h)の反転（q(0)可逆）によって、任意の指定有限jetを保つ代数的核ベクトルに置換できる。一定rankは仮定しない。K[h]_(h)→K[[h]]の忠実平坦性を有限余核へ用いる。

次数3,4の自由PBW模型があれば、中心三次元は z↦h^−1[z,x_i] の有限行列で扱える。未知数binom(N+2,3)、方程式N binom(N+3,4)。形式中心の存在は入力であり、指定無限級数全体の一致を主張しない。これは全次数PBW性・AS性・残余対角の代数化を証明しない。

## 6. 非楕円成分とsmoothnessへの障害

固定した滑らかなcubic fivefold上に、一般点で節点型または尖点型の純三次ブロックを持つ二次元Poisson既約成分がある。`papers/sections/nonelliptic_poisson_components.tex` のne:mainに証明、全Jacobi接行列35列の階数33、整数小行列式（節点2^24·3^12、尖点−2^33·3^12）の証明書を保持する。support内の縮約二形式の平方零スキームからブロックの内在性を示す。

従って楕円Sklyaninだけでは全成分を覆えない。一般化Jacobianは節点でG_m、尖点でG_aであり、楕円Picardへの有理写像障害をそのまま適用しない。これは可換復元の反例ではない。

SMに必要なのは、特殊ファイバーの有限対角ではなく、実際の底上のP∈Perf(Γ_R^e)と射P→Γ_Rである。Γ_RがproperならPのconeも底上perfectで、一ファイバーで擬同型なら局所Nakayamaを使える。各Artin切断のsmoothnessやHom階数だけでこの持上げを置換しない。

中心変数uの通常微分は量子代数の導分にならない。ambientの対角を中心商で両側テンソルしたものは残余対角ではない。Serre自己同値の存在もsmoothnessを含意しない（対称Frobenius代数C[epsilon]/epsilon²）。詳細な障害と具体式は `notes/reconstruction.md`。

## 7. 他の有効な成果と依存範囲

論文Aは一般次元のPoisson正規形・退化・量子化、Bは中心三次対の41次元incidence、17係数族、構造対象と次数シフト付きambient二次包絡復元、Cはrotation付き可換復元と障害を扱う。BではambientをB、商をAと書き、CではambientをA、商をBと書く。

Bの分離型は余次元15、法線は中心変数一次6方向と二次9方向。元の可換cubicのJacobian変形への17次元接写像の核は平面移動6とPoissonスカラー1。これは量子化後の可換模型への写像ではない。固定cubic・固定平面のG_mから滑らかな楕円Picardへの有理写像は定数だが、分岐対応や動くcubicは排除しない。

混合15方向の中心式と一次持上げの一意性は独立節に保持する。有限体特殊化の成功を普遍中心性の証明としない。`fermat_center_certificate.json` の15項整数恒等式は混合なし三変数Fermat中心式の証明書である。

Cの一楕円ブロックの良い複素ファイバーでの比較、有限位数条件付き多ブロック比較、形式復元の既存証明は保持する。一般混合項の全点復元、二つ以上の無限位数ブロックの全生成、元の底への一意降下は未解決。独立Pfaffian/Brill–Noether技術原稿と中心曲面の判別式・検算は [nc-cubic2](https://github.com/uedakazushi/nc-cubic2) に全文をGit blob一致で移管した。対応するPDF原本8件もnc-cubic2へGit blob一致で移転済み。TeXとの完全照合は未了。Reye研究は専用リポジトリ https://github.com/uedakazushi/reye に原PDF・TeX・検証コードを移行して保持する。PDF-only資産の全面的TeX再構成と全過去計算の再監査は未了。

## 8. 再現と次の着手

`reconstruction/README.md` の計算、build、verifyを実行する。参照とハッシュは全TeX inputを含む。計算的確認と圏論的証明は別である。最優先の次作業は実際のnc低rotation積の有限模型を構成し完成底比較を証明すること。指定残余生成子のgeneric生成性は圏同値についての後続課題である。混合族の同変正規形でまずh⁶のa₁とh⁸のb₁を計算し、λ³=−12も判別点として調べる。指標空間とτの自由代数恒等式をSymPyで厳密検算した。現行v26の論文Cは未組版で、旧入力閉包での組版・表示確認とは区別する。各原稿の詳細な検証状態はvalidation.jsonを確認する。

GitHubへ全文と再現資産を保存し遠隔確認する。Libraryはpushが実際に失敗した場合だけの緊急退避とする。

## Hochschildの第三次数障害（現行の確定した整理）

滑らかなN変数三次F（n=N−2≥3）に対するBFK Theorem 5.39の恒等sectorは偶数次 q=2r にJ(F)_{3r}を与え、μ₃の非自明二sectorは3|Nなら次数q=N/3に各一次元を与える。二sectorのrotation固有値はζ,ζ²。したがってHH³はN=9の場合だけC²で、全N≥5でHH³のrotation不変部分は零。具体的検証は`papers/reconstruction/hochschild_obstructions.tex` と同じディレクトリの整数証明書を参照。形式変形の一次障害の消滅と有限型でのSMを混同しない。

## SMの回復済み反例から分かること

`notes/source_recovery/dg_perfectness_counterexamples.tex` は、原PDF [nc-cubic2のfinite_smoothness_notes.pdf](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/pdf-only/finite_smoothness_notes.pdf) の第23節（pp.26–31）をTeXで復元したもの。例えば `R=k[[h]]`、`Lambda=R⊕R eps⊕R eta`（`|eps|=|eta|=1`、積零）上の `d(e)=h e eps` で定まるdg加群 `M` は、`R`-perfect、特殊ファイバー `M_k\simeq Lambda_k` はperfect、さらに全Artin切断 `M/(h^a)` もperfectだが、一般ファイバーでnonperfectとなる。したがって `M` 自体は相対的にnonperfect。**この例の特殊ファイバー代数 `Lambda_k` はsmoothではない**。特殊fiberがsmoothである場合も一般の持上げ原理は偽であり、次の独立な例で確認する。どちらも、本研究のnc cubicに指定されたΓ_RのSMを否定したものではない。

回復稿には `R=k[[h]]` で特殊化 `P_k` がperfect、`N` が底上perfectなら `RHom_Gamma(P,N)` は底上perfectとなるという補助結果もある。しかし **Hochschild cochainsの底上有限性は対角perfectnessではない**。今後は有限cell/retractの実際の底上持上げ、増大射およびホモトピーの有限個の整合式を構成する。単なるすべてのArtin切断での成功を証明書の代用にしない。

## 有限bar段階によるSMの直接判定

回復原稿 `notes/sm_bar_and_spreading.tex` は、`Gamma_R ∈ Perf(R)` なら相対二側bar解消の有限skeleton `P_d` は `Gamma_R^e`-perfectで、`hocolim_d P_d ≃ Gamma_R` となり、**SMと「あるdで `P_d → Gamma_R` が導来右逆を持つ」は同値**であることを証明する。特殊ファイバーの右逆だけで底上の右逆を得ることはできない。

また `R` noetherian整域でproperなdg模型のgeneric fiberがsmoothなら、perfect dg加群のfiltered-colimit descentとconeのgeneric消滅から、ある非空局所化で相対smoothになる。ただしspecial smoothnessだけではgeneric smoothnessはまだ得られない。以上は [nc-cubic2のfinite_smoothness_notes.pdf](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/pdf-only/finite_smoothness_notes.pdf) の第18--21節（pp.23--25）の有効な補題・証明を整理したもので、元の34ページ全体のTeX化ではない。この存在証明経路の核心は、実際の有限bar右逆（または同等の有限対角証明書）を非楕円二成分で構成することである。現在の全体方針では、三次元混合族からの方程式抽出も同時に進める。


## 全Artin切断がsmoothでもgenericが非smoothとなる例

全文証明は papers/reconstruction/artin_smoothness_obstruction.tex。P¹_R上の
P_h=[O(−1) --hs→ O]を使う。特殊fiber O⊕O(−1)[1] は生成子、genericは点のskyscraperで生成子でない。この幾何的退化例はSashaの2016年MathOverflow回答にある既知例で、一次資料と参照先をbibliographyに記録した。

Γ_R=RHom(P_h,P_h)にはrank4のstrict dg模型がある：
Γ⁰=Re_-⊕Re_+、Γ¹=Rs⊕Rt、d(e_-)=hs、d(e_+)=−hs。
R-perfect、特殊fiberと全Artin切断はsmoothだが、genericはE=K[ε]/ε²、|ε|=1へquasi-isomorphicである。augmentation Kのsemifree分解Q=⊕_(n≥0)E u_n、|u_n|=0、du_n=εu_(n−1)から、K⊗^L_E Kはdegree0に無限次元となる。よってEはnon-smooth。

したがって「特殊fiber smooth＋全Artin同値＋proper」だけではSMもgeneric smoothnessも出ない。smooth properな可換幾何の中に対象を実現しても生成性の持上げは自動的ではない。今回の形式的MF同値について、Γの指定生成子が可換側の生成子を実際に生成するという追加の証明、または有限対角証明書が必要となる。この反例の存在は、nc cubicの目標そのものの反例ではない。


### cohomology-flatな線束模型に残る具体課題

上の反例ではH¹にh-torsionがあり、cohomology-flatな場合を否定しない。現行Λ_RのH⁎=H⁰⊕Hⁿは両成分が有限自由で、SMΓとSMΛの同値によりΛ側で検討できる。固定有限自由加群上のminimal A∞族について、特殊fiberのsmoothnessから少なくともgeneric smoothnessを導けるかを確認する。具体的には、特殊fiberの対角の有限cell表示を、Artin次数によらないcell数とshiftの上界を保って持ち上げられるかを調べる。各次数で別々の有限表示があるだけでは足りない。この追加flatness下で適用可能な一般定理は今回の一次文献調査から確証できておらず、未解決の補題として扱う。

minimal $A_\infty$模型の対角をHPLで持ち上げる際は、「基礎加群が有限rank」と「有限cellである」を区別する。後者には有限filtrationを保つ上三角性が必要である。現行$\Lambda_R$の対象の添字・内部次数・積の向きが、このfiltrationを全次数で保つかを次に調べる。正次数$H^n$があるため、通常の有限次元代数の射影分解の議論をそのまま流用しない。

### 通常の有限自由代数へ帰着できる場合の十分条件

次は標準的な持上げ議論であり、新規性を主張しない。$R=\mathbb C[[h]]$、$A$を有限自由な通常の$R$-代数とし、$A_0=A/hA$が$\mathbb C$上homologically smoothなら、$A$は$R$上homologically smoothである。

**証明。** $B=A^{\mathrm{op}}\otimes_R A$と置き、対角$A_0$の有限射影$B/hB$-分解$\overline P_\bullet\to A_0$を取る。$B$は有限$R$-加群として$h$進完備なので、行列冪等元を持ち上げて各$\overline P_j$を有限射影$B$-加群$P_j$へ持ち上げられる。$P_0$の射影性でaugmentationを$P_0\to A$へ持ち上げると、余核は有限$R$-加群で剰余が零だからNakayamaにより全射である。$A$は$R$-自由なのでこの全射は$R$-分裂し、核$K_1$は有限自由で、その剰余は特殊分解の核と一致する。同じ操作を$P_j\twoheadrightarrow K_j$に繰り返し、各核の自由性と正しい剰余を保つ。最後の$\overline P_\ell\simeq K_\ell/hK_\ell$を持ち上げた全射$P_\ell\to K_\ell$の核も$R$-自由で、剰余が零だからNakayamaにより零である。従って対角$A$に有限射影$B$-分解ができる。特にgeneric fiberもsmoothである。$\square$

この十分条件は、族がこのような通常代数に$R$-linear Morita同値となるtilting模型を持つ場合にも使える。現行$\Lambda_R$の指定線束生成対象は正次数の自己Extを持つのでtiltingではなく、この条件を満たす別の模型があるとは未証明である。

## Cartier自己交差の係数付き分裂を仮定しない

閉埋込みj:Y→Pについて、Lj*j_*O_Yのformalityと、任意のperfect Mに対するO_Y-linearな分裂は別である。生成の証明ではStacks Project Tags 0BQT, 09M1のcompact生成を用いる。

具体的にSegre quadric Y=P¹×P¹⊂P³、M=O_Y(1,0)を取る。座標行列 (X_ij) による分解は
\[
0\to O_{\mathbf P^3}(-1)^2\to O_{\mathbf P^3}^2\to j_*M\to0.
\]
したがってLj*j_*M=[O_Y(-1,-1)^2→O_Y²]。RHom_Y(M,−)の二項はO_Y(-2,-1)^2とO_Y(-1,0)^2の導来切断で、両者とも全cohomologyが零である。一方、M⊕M(-2,-2)[1]ならHom(M,M)=Cが残る。従ってそのような分裂は、Mが線束であっても成立しない。

一般の障害との関係はArinkin–Căldăraru, *When is the self-intersection of a subvariety a fibration?*, arXiv:1007.1671v2, §§2.1–2.2, Propositions 2.6, 2.10（https://arxiv.org/abs/1007.1671）を参照。この反例そのものの検証は上の二項複体計算で完結する。
