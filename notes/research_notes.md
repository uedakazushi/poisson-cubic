# 研究ノート：可換復元の現在有効な知識と障害

**2026年11月10日・v21。GitHub mainだけを正本とする。** 具体的復元・一次消滅の証明は論文Cの現行inputに、局所rotation・SM・ERの詳細は `notes/reconstruction.md` と対応原稿に置く。

## 三目標の区別と現状

構造定理 `thm:pg-normal` と個々のPoisson構造の代数的量子化 `thm:pg-quantization` は、論文A（`papers/sections/poisson_geometry.tex`）に証明が記載されている。後者は \(X^n\subset\mathbb P^{n+1}\) の各固定Poisson構造について、\(0\in U\subset\mathbb A^1_\hbar\) 上のKoszul AS-regular代数と中心三次商を与える定理であり、Poisson係数空間を同時に動かす一様族の存在定理ではない。新規性の網羅的監査と全外部入力の再証明は未実施。

三番目の目標は、こうして構成した非可換cubicのgenericファイバーをrotation付きの可換cubic Kuznetsov成分として実現すること。任意のAS-regular中心三次商全体の全点についての復元は要求しない。各成分のgeneric点への一様相対化は強化課題であり、個別量子化定理の欠落と混同しない。

## 具体的な方程式を得るための現在の知識

方程式抽出と圏同値存在を並行して進める。分離型に既に閉公式があるため、一般のSMを先に完成する経路だけに研究を限定しない。次の入力は三次元の本質的混合項lambda*u*x*yであり、分離点との二次比較を基準とする。

- **分離型の閉式。** 対称Jacobian量子化の多重線形化はM(v)=K(v)−h HessMatrix(f)/2。Mori–Smithの既知恒等式 det M=−3h(f+h² det HessMatrix(f)/24) を、本稿の量子化規約で初等的に証明した。滑らかな楕円中心商と独立な中心変数Pの仮定で、既存ブロック比較が可換模型 f+h²Hess(f)/24+P を与える。証明は papers/reconstruction/explicit_model_comparison.tex。
- **単純可換化の失敗。** Hesse型では復元先の二次類は +(1+t³)[xyz]/3、中心元の可換表示は −2(1+t³)[xyz]/3。差は非零。literal abelianizationはさらにactive三変数を冪零にし、Proj次元を3落とす。元のcubicへの全次数の同値を期待する根拠にはならない。
- **有限抽出。** V=Hom_dg(Id,rho)、W=Hom_dg(Id,rho²) の積が対称・全射で正しい次元を持つとき、K=ker(Sym²V→W)を求める。Kの基底qに対する可積分行列Aの線形系、det A≠0、共通射影零点なしを検査し、F=Σx_i(Aq)_i/3で積分する。滑らかな解は射影同型を除いて一意。Fermatでは積分解空間がN次元なのでscalar倍までの一意性は偽。証明は papers/reconstruction/explicit_jacobian_recovery.tex。
- **数値条件では不足。** mod5でq_i=x_i²+x_(i+1)x_(i+2)とすると共通零点は原点だけ、Hilbert級数は(1+t)^5だが、可積分線形系はrank25で核零。25次小行列式15872が証明書にある。この例がnc cubicから生じるとは主張しない。
- **三次元の一次消滅。** 純bivectorの通常HKR類はHH²(Ku)への制限で零。局所divergenceによりpi♯c1(K)=0を示してTodd補正を消し、JLLZのHochschild作用の単射性を適用する。pure Poisson KSと残余への制限の両立を確認し、可換族の存在を仮定すればF_h=F+O(h²)。証明は papers/reconstruction/poisson_first_order.tex。高次定数性・一般次元・SMは結論しない。
- **最小混合族の入力。** F_lambda=(x³+y³+z³)/3+u³+v³+lambda*u*x*yはlambda³≠−3で滑らか。papers/reconstruction/mixed_test_family.tex に三次中心元の閉式と、全パラメータ中心性を与える自由代数の3恒等式を全文記載した。全Artin切断でのmonic PBWと中心商の次数別flatnessも証明した。h²(lambda*u)²z/6を落とすと中心性が壊れる負例、sorted表示に現れる一次項と復元先の一次類を区別する注意も同節にある。非零hの全AS性、残余SM、rotation積、復元G₂はこの計算では得られていない。

これらの復元原理は既知のJacobian・symmetrizer理論を利用し、Hessian公式も既知である。具体的比較・検査器・一次消滅の帰結としての初出は未確認。計算コードは既知の可換多項式と二次関係を入力し、まだ一般nc残余圏のV,W,積を算出していない。二次の復元係数は、半古典Poisson括弧だけでなく選択した量子化の高次データに依存し得る。

### 混合族の二次係数：確定した方向と未検証の値

三乗根の対角作用 `(x,y,u,z,v) -> (alpha*x,beta*y,gamma*u,delta*z,epsilon*v)`、alpha*beta*gamma=1、chi=alpha*beta*delta、h->chi*hは量子族を保つ。三次Jacobian環のchi固有空間はC[xyz]、chi²固有空間は零。証明は papers/reconstruction/mixed_test_family.tex。従ってmarked同変復元の存在を仮定すれば、二次類は[G₂]=c(lambda)[xyz]である。これはc(lambda)の値や同変復元の存在を決定していない。

lambdaも動かす場合、全mu₃⁵についてkappa=alpha*beta*gamma、lambda->kappa⁻¹lambdaとすれば量子族全体が同変になる。この作用まで復元が両立する場合にはc(zeta*lambda)=c(lambda)であり、lambda=0の周りの形式的係数はC[[lambda³]]に入る。既知のc(0)=1/3を合わせると、最初の未知混合補正はlambda³h²の係数に現れる。これは同変性を仮定した重みの帰結であり、係数の計算ではない。

**未検証の作業仮説。** active三変数のHessian行列式は
\[
H_{\rm act}=8xyz-2\lambda^2u^2z.
\]
構成した中心元の対称表示を可換にしたとき、h²係数は正確に−H_act/12となる。分離型との類推から、可換復元先に対してH_act/24という候補が自然に浮かぶ。Jacobian関係3u²+lambda*xy=0を用いると、候補類は
\[
[G_2^{\rm Hess}]=\frac{12+\lambda^3}{36}[xyz].
\]
これはlambda=0の既知値1/3と一致するが、一般lambdaでは圏データからの検証を一切行っていない。中心元の係数から復元係数を推定する推論を証明として使わない。次の計算ではこの式を結論として組み込まず、rotation積から独立にc(lambda)を求めて比較する。特にlambda³=−12でも古典cubicは滑らかであり、この候補が二次で零になる点は有用な判別試験になる。

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

`reconstruction/README.md` の計算、build、verifyを実行する。参照とハッシュは全TeX inputを含む。計算的確認と圏論的証明は別である。最優先の次作業は、構成した三次元混合試験族について、純Poisson KSと残余制限の両立を確認し、rotationの低次数積と復元先の二次類を計算すること。有限残余対角証明書による存在経路と、非楕円fivefoldでの一般次元への検証を並行する。

GitHubへ全文と再現資産を保存し遠隔確認する。Libraryはpushが実際に失敗した場合だけの緊急退避とする。

## Hochschildの第三次数障害（現行の確定した整理）

滑らかなN変数三次F（n=N−2≥3）に対するBFK Theorem 5.39の恒等sectorは偶数次 q=2r にJ(F)_{3r}を与え、μ₃の非自明二sectorは3|Nなら次数q=N/3に各一次元を与える。二sectorのrotation固有値はζ,ζ²。したがってHH³はN=9の場合だけC²で、全N≥5でHH³のrotation不変部分は零。具体的検証は`papers/reconstruction/hochschild_obstructions.tex` と同じディレクトリの整数証明書を参照。形式変形の一次障害の消滅と有限型でのSMを混同しない。

## SMの回復済み反例から分かること

`notes/source_recovery/dg_perfectness_counterexamples.tex` は、原PDF [nc-cubic2のfinite_smoothness_notes.pdf](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/pdf-only/finite_smoothness_notes.pdf) の第23節（pp.26–31）をTeXで復元したもの。例えば `R=k[[h]]`、`Lambda=R⊕R eps⊕R eta`（`|eps|=|eta|=1`、積零）上の `d(e)=h e eps` で定まるdg加群 `M` は、`R`-perfect、特殊ファイバー `M_k\simeq Lambda_k` はperfect、さらに全Artin切断 `M/(h^a)` もperfectだが、一般ファイバーでnonperfectとなる。したがって `M` 自体は相対的にnonperfect。**この例の特殊ファイバー代数 `Lambda_k` はsmoothではない**ため、`Gamma_R` のSMを否定する反例ではない。

回復稿には `R=k[[h]]` で特殊化 `P_k` がperfect、`N` が底上perfectなら `RHom_Gamma(P,N)` は底上perfectとなるという補助結果もある。しかし **Hochschild cochainsの底上有限性は対角perfectnessではない**。今後は有限cell/retractの実際の底上持上げ、増大射およびホモトピーの有限個の整合式を構成する。単なるすべてのArtin切断での成功を証明書の代用にしない。

## 有限bar段階によるSMの直接判定

回復原稿 `notes/sm_bar_and_spreading.tex` は、`Gamma_R ∈ Perf(R)` なら相対二側bar解消の有限skeleton `P_d` は `Gamma_R^e`-perfectで、`hocolim_d P_d ≃ Gamma_R` となり、**SMと「あるdで `P_d → Gamma_R` が導来右逆を持つ」は同値**であることを証明する。特殊ファイバーの右逆だけで底上の右逆を得ることはできない。

また `R` noetherian整域でproperなdg模型のgeneric fiberがsmoothなら、perfect dg加群のfiltered-colimit descentとconeのgeneric消滅から、ある非空局所化で相対smoothになる。ただしspecial smoothnessだけではgeneric smoothnessはまだ得られない。以上は [nc-cubic2のfinite_smoothness_notes.pdf](https://github.com/uedakazushi/nc-cubic2/blob/main/notes/pdf-only/finite_smoothness_notes.pdf) の第18--21節（pp.23--25）の有効な補題・証明を整理したもので、元の34ページ全体のTeX化ではない。この存在証明経路の核心は、実際の有限bar右逆（または同等の有限対角証明書）を非楕円二成分で構成することである。現在の全体方針では、三次元混合族からの方程式抽出も同時に進める。
