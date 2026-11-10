# 研究ノート：rotation・対角・局所可換実現

**2026年11月10日・v17。現在有効な知識を整理する。**

## 1. 今回の中心となる有限データ

R-properな局所dg圏 C、T=(1)、O_i=T^i O、特殊ファイバー Perf(X^n)、a=n−1 とする。

L=RHom(O_a,O[n]) は剰余が k[0] のR-perfect複体なので R[0] と同型。trace L→R を一つ選び、合成から

RHom(M,O[n]) → RHom(O_a,M)^∨

を作る。そのconeはR-perfectで剰余が零なので零。従って ^⊥O = O_a^⊥ である。

この一つの直交同定が逆rotationを閉じる。N∈K に右mutationを施した Q=R_O N は ^⊥O に入り、従って O_a^⊥ にも入る。他の O_i（1≤i<a）への直交は三角と例外性から従う。よって T^−1 Q∈K。逆同型はmutation三角から実際に得られ、特殊ファイバーの同型を勝手に持ち上げていない。

十分な証明は原稿第2–3節。smoothnessはここには使わない。任意のproper関手の随伴存在も使わない。

## 2. smoothness後の論理

### 全coherent圏

Eから全twistを生成でき、RHom(E,M)が全coherent MについてR-perfectであれば、REnd(E)のsmoothnessからM自体がthick(E)に入る。加群のpseudo-perfect→perfect性と、弱生成性で証明する。

残余と有限例外列のgluingは、基礎R複体としてperfectな交差双加群で行う。成分がsmoothならこの双加群は包絡代数上perfectである。三角代数の対角三角を明記すれば、体上の既知定理を無条件に相対化したことにせず証明できる。原稿第6節。

### 有限型spread

R=(R0)_m は主開集合の座標環のfiltered colimit。Gammaがsmooth properならToënの降下定理でGammaを降下できる。可逆rotation双加群Pとその逆Qは、smoothnessの下でGamma^e-perfectなので、P,Q、二つの逆同型を有限段階で降下できる。原稿第7節。

従って「全高次積を有限型開集合へ一斉にspreadする」問題を(SM)の後にも独立の難問として残す必要はない。properだけではこの議論を使っていない。

## 3. 非楕円二成分の具体的入力

以下の表示は親論文A `papers/sections/nonelliptic_quantization.tex`（commit 4f2eb328a2249a173f0c658cdb744277f041ff1d）の入力を、再開に必要な形で記す。次数零は r,s、次数一は x,y,z,a,b,c,u。異なるブロックの生成元は可換、uは中心。

第一ブロック：

- 尖点型 C： [y,z]=r(z²+2ux), [z,x]=3ry², [x,y]=r(xz+zx)。
- 節点型 N： [y,z]=(r/2)(yz+zy)+2rux, [z,x]=(r/2)(zx+xz)+3ry², [x,y]=(r/2)(xy+yx)+3rz²。

第二ブロック：

[a,b]=s(3c²+2uc), [b,c]=s(3a²+2ua), [c,a]=s(3b²+2ub)。

第一ブロックの中心三次式は、積を表示順で読むと

Gamma_C = z²x+y³−3rzy²+ux²−6r²uyx−6r³uzx+12r⁴uy²,

Gamma_N = z³+((2−r)/(2+r))³y³+(r²+12)zyx/[3(2+r)²]+(r²+12)ux²/[6(2+r)]−24r²uzy/(2+r)²−24r³u²x/(2+r)²。

alpha=a+u/3, beta=b+u/3, gamma=c+u/3 として、第二ブロックの中心式は

Gamma_F = alpha³+beta³+gamma³−3s² sum_{6 permutations} alpha beta gamma −(u²/3)(alpha+beta+gamma)+2u³/9。

Omega_epsilon=Gamma_epsilon+Gamma_F+u³、B_epsilon=A_epsilon/(Omega_epsilon)。尖点型の係数環は C[r,s]、節点型では 4−r² を反転する。可換点での局所環は共に R=C[r,s]_(r,s)。N=7,n=5,a=4。

### 今回実行した厳密なチェック

`computations/verify_nonelliptic_inputs.py` は第一ブロックのmonic書換えを使う。normal word は z^i y^j x^k。一意な重なり xyz の二経路と、Gamma_epsilon と x,y,z の交換子を、Q(r,u)上の有理関数恒等式として検証する。r,uの有限特殊化ではない。

Gamma_epsilon|_(u=0)+ux² という素朴な持上げは、両型とも x,y,z 全てについて非零交換子を持つ。混合補正を捨ててはならない。

このコードは第一ブロックの全次数PBWを支えるDiamond overlapを確認するが、第二ブロックの全次数flatnessやambient AS性の全面的な独立検算ではない。それらは親論文Aの構成を入力とする。圏のsmoothnessや同値は計算していない。

### 可換特殊ファイバーの滑らかさの直接証明

f_C=xz²+y³、f_N=xyz+y³+z³ とし、

F_epsilon=f_epsilon+ux²+a³+b³+c³+u(a²+b²+c²)+u³。

u=0で勾配が零なら、第二ブロックからa=b=c=0。尖点ではF_x=z²,F_y=3y²よりz=y=0、F_u=x²よりx=0。節点ではyz=0、xz+3y²=0、xy+3z²=0よりy=z=0、F_u=x²よりx=0。射影点はない。

u≠0ならu=1とする。各a,b,cは0または−2/3であり、a²+b²+c²=4j/9（j=0,1,2,3）。尖点ではy=0、xz=0、z²+2x=0からx=z=0。F_u=3+4j/9≠0。

節点ではx=−yz/2。y,zの一方が零なら両方零であり、同じF_uが非零。両方非零ならy=z²/6、z=y²/6からyz=36、x=−18を得る。F_u=327+4j/9≠0。従って両Fは滑らかなcubic fivefoldを定める。

この消去証明は複素点全体を扱う。コードが確認する整数27+4j,2943+4jはこの証明中の非零性であり、ランダムな点検査ではない。

## 4. 対角に向けた使える障害と作業方法

(SM)は Gamma ∈ Perf(Gamma^op⊗^L_R Gamma) である。GammaがR-perfect、またGamma_kがsmoothであるだけを使って、対角の有限分解が自動的に持ち上がったとは言わない。本稿はその一般命題の真偽を決着していない。

実際のP∈Perf(Gamma^e)と射P→Gammaが作れれば、Gamma properよりPもR-perfect。特殊ファイバーが擬同型ならconeはR-perfectかつ剰余零なので、局所底上で既に擬同型になる。従って対角証明書は、有限複体だけでなく増大射と微分・homotopyの整合を含む。

着手方法は、特殊ファイバーの対角を外部線束の有限twisted complexとして記述し、その差分・高次homotopyを量子関係から構成すること。周囲Aの対角分解をBで両側テンソルするだけでは、Bや残余の対角にならない。中心自己交叉から生じる周期的部分を射影化・windowで制御する必要がある。

中心変数uについて、通常のpartial_uを非可換代数の導分として使ってはならない。例えば尖点関係 [y,z]−r(z²+2ux)=0を、u↦1、x,y,z↦スカラーの次数−1導分で微分しu=0とすると、−2r(x+partial_u(z)z)=0となり、r≠0でPBWに反する。節点でも同様。中心方向の可換Jacobian計算をそのまま量子式へ代入する方法は止まる。

Serre関手の存在はsmoothnessを含意しない。Perf(k[epsilon]/epsilon²)は対称FrobeniusによりSerre=idだが、単純加群の無限分解から非smoothである。原稿最後の命題に証明がある。この例は今回の量子化の反例ではなく、証明方法の境界を示す。

## 5. étale局所実現の証明と一次資料

証明全文は `papers/reconstruction/etale_realization.tex`。対象は実在するsmooth proper pairであり、properだけの残余模型にはまだ適用できない。

小拡大での同値双加群の障害はHH²に入る。両側の自己同値のliftと還元上のintertwinerに対する障害の自然性により、その類はrotation不変となる。幾何的KSの全射でsourceを修正して障害を消し、HH¹=0でintertwinerを持ち上げる。actual perfect対象と射のmoduli、unit/counitの消滅開条件、無限小smoothness、étale sectionまで確認する。これでERを独立仮定として残す必要はない。

HH³=0、Hochschild cochainのformality、抽象的Hochschild変形が全てactualであることは使わない。選択したrho³=[2]のcoherenceはpairのデータに含めない。親rotation_models.texの形式変形比較を全て再監査したとの主張でもない。

一次資料：Toën–Vaquié, math/0503269v5, Theorem 3.6/Corollaries 3.15,3.17,3.19、Lowen, 0707.2602v1, Theorem 4.8。BFK Theorem 5.39、Huybrechts–Rennemo Lemma 2.19/§3.3、JLLZ Theorem 4.4(2)、Huybrechts Proposition 3.12でcubicの入力を確認。正確な書誌とリンクは papers/reconstruction/etale_references.tex。

Lin–Zhang, *Categorical Torelli and Fourier–Mukai partners of hypersurfaces*, arXiv:2611.05915v1 (2026-11-04), §§2.1–2.3は重要な比較資料である。同論文Theorem 2.2/Proposition 2.4は幾何的な両側のsmooth projective familyとrelative admissible component、perfect projectorを仮定する。本稿は同じ障害消去原理を非幾何的targetに使えるMorita双加群で定式化し、rotation不変性とintertwinerを別々に証明する。同論文を仮定未確認で直接適用しない。新規性は未確定。

## 6. 非楕円例の35係数slice

第3節のF_C,F_Nについて、84個の三次単項式の空間の中で49個の z_j partial_i F の係数行列を取る。`computations/verify_etale_inputs.py` が有理数上の階数49と、35個の単項式補空間を確認する。採用小行列式はCで2^15·3^26、Nで−2^6·3^25。SymPyの計算と独立した整数Bareiss消去の結果が一致する。商への射影が座標変換方向を消し、35単項式には恒等であることも確認する。

35単項式の全リストは原稿の er:prop:slice と computations/etale_input_checks.json に保持する。これをsourceとすれば各小拡大の障害を35係数で消せる。ただし実際の障害類や量子パラメータ(r,s)からその係数への関数は未計算。SMの証明にもなっていない。

## 7. 親プロジェクトと次の核心

A（Poisson・量子化）、B（17次元族・ambient）、C（rotation付き復元）と境界研究の構成を保つ。この独立組版はCの一部であり、親Cはétale実現節と文献を同じソースから読む。局所rotation・Serre・gluing・spreadの証明全文はこの原稿に保持する。

所定の局所量子化に対しては、SMから全coherent比較とspread、ER、generic復元が従う。残る最優先課題は第4節の有限残余対角証明書。全成分での量子化、全点の復元、大域降下、既存の全証明の独立監査は未了。

GitHub mainだけを正本とし、研究の区切りに全文と再現資産をpushして遠隔確認する。Libraryはpushが実際に失敗した場合の緊急退避だけに使う。

## Hochschildの奇数次sectorと形式的障害

BFK Theorem 5.39に従えば、非自明μ₃-sectorは3|Nの場合にq=N/3に限り二次元で、そのrotation固有値はζ,ζ²。恒等sectorは偶数次のみ。従って`HH³(Ku(X))^rho=0`は全cubic n≥3で成立し、n=5では`(dim HH⁰,...,dim HH⁴)=(1,0,35,0,7)`。n=7の場合のみHH³自体は二次元。通常の第一Morita変形障害が消えることは、残余対角SMの実在的な証明書を与えることではない。本文`papers/reconstruction/hochschild_obstructions.tex`と検算`computations/verify_hochschild_sectors.py`を参照する。

## 線束生成子を使う新しいSM実装経路

有限例外列の左右admissibilityから、`Gamma_R` のsmoothnessと `Lambda_R=REnd(⊕O(i))` のsmoothnessが同値になる。Perryの相対半直交分解定理(Lemma 4.15(3))を現在のproper局所模型に適用する。残余mutation対象のEndの具体係数を先に求めなくてもよい。

`H^0(Lambda)` は順序つき線束間の `B_{j-i}` を成分とする有向代数、`H^n(Lambda)` は `B_{i-j-(n-1)}^∨` を成分とするsquare-zero双加群。最小模型では$m_k$が `k=2 mod n` に限られる。fivefoldの$m_7$の対象指数列は出力H0側2478、H5側303通り、うちRスカラー出力は7巡回配置。これは各Hom空間内の基底数でなく、許容対象の並びの整数計算である。

$m_7$は初期Hochschild cocycleを定めるが、次の$m_{12}$に$[m_7,m_7]$が現れる。指数列だけでは二次障害は消えない。実際の非可換量子化に対する$m_7$の係数計算と有限bar右逆は**未実行・未完成**。

証明は `papers/sections/minimal_ainfty_arity.tex`、再現は `python3 computations/verify_minimal_ainfty_arity.py --output /tmp/nc-cubic-arity.json`。Perry (2019) の既知の半直交smoothness判定、Petersen (2020)・Burke (2018) のhomotopy transferと、本研究の対象への具体的指数制約を区別する。
