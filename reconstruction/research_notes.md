# 研究ノート：rotation・対角・局所可換実現

**2026年11月10日・v14。現在有効な知識を整理する。**

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

以下の表示は親論文A `tex/papers/nonelliptic_quantization.tex`（commit 4f2eb328a2249a173f0c658cdb744277f041ff1d）の入力を、再開に必要な形で記す。次数零は r,s、次数一は x,y,z,a,b,c,u。異なるブロックの生成元は可換、uは中心。

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

## 5. (ER)の一次資料比較

既存原稿Cの `rotation_models.tex` の `thm:etale` は、形式的可換モデルと同値核/intertwinerのmoduliからétale局所存在を主張する。本稿では(ER)を独立仮定として再掲した。全てのArtin変形の検出、rotationの同型の代数性、持上げのcoherenceを未確認のまま完了にしない。

2026年11月4日公開の Xun Lin–Shizhuo Zhang, *Categorical Torelli and Fourier–Mukai partners of hypersurfaces*, arXiv:2611.05915v1 を確認した。

- §2.1の設定は滑らかな射影族、smoothな底、相対admissible成分、perfectな射影核と底変更の両立である。
- Theorem 2.2は、幾何的変形からHH²への写像が全射のとき、一方の幾何的変形を固定して同値核の小拡大障害を他方の変形で消去する。
- Proposition 2.4は負のHH消滅等の下で代数的なsmooth correspondenceへ移す。
- これは本研究の非幾何的source dg族に対する(ER)を、そのまま引用できる定理ではない。障害理論の比較資料として重要である。

URL: https://arxiv.org/abs/2611.05915
確認した本文: https://arxiv.org/html/2611.05915v1, §§2.1–2.3。

その他の一次資料は原稿文献表を正本とする。Burke–Stevensonの有界section、Toënのfiltered-colimit降下、Toën–Vaquiéのperfect加群、Orlovの体上gluing判定の仮定を確認した。論文全体の独立再証明や包括的な新規性調査は未了。

## 6. 親プロジェクトとの接続

親mainの確認対象はcommit 4f2eb328a2249a173f0c658cdb744277f041ff1d。
論文A（Poisson・量子化）、B（17次元族・偏極付きambient）、C（rotation付き可換復元）と境界研究の構成を保持する。

本稿の結果を親Cへ統合する際は、`local_projective_model.tex` のrotation候補の命題を、trace・右mutationを使う自己同値定理へ置換する。残課題欄では、全coherent比較とfinite-type spreadを(SM)の帰結として整理する。(SM)・(ER)そのもの、全成分での量子化入力は未完成のまま残す。論文A/Bの既存証明や境界研究を削除しない。

今回の成果物は親全体の新しい第四論文を提案するものではなく、Cの現行部分を独立読解できる形にしたものである。親への実際の同期は未実行。
