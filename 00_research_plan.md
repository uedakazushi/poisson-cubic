# 研究方針：滑らかなcubicのPoisson moduli stacksと量子化

**2026年11月12日 / v54。再開時は必ず最初に読む。GitHub uedakazushi/nc-cubic のmainが唯一の正本。**
最上位目標は論文A（papers/paper_a.tex）を投稿可能な水準へ仕上げること。
現在の数学的最優先課題は、**全次元のsmooth cubicの全Poisson構造に対する
代数的中心三次元と量子化定理を、形式的中心元の存在定理に依存せず完成させること**。
一般のPoisson space・固定stack・relative stackの構造定理と
その成分数も論文Aの主要成果として維持する。
三変数制限が特異な場合まで**代数的存在は解決**したが、
短い単一多項式閉公式・モジュライ上の同変な接着は未解決。
旧論文Bのambient復元は一般次元化して論文Aに統合し、モジュライ部分はnc-cubic2へ移管する。論文Cの結果と証明は保持する。

## 一般次元ambient復元とBの再編

`papers/support/papers/sections/ambient_recovery_general.tex` を論文Aに統合。二次ambientの次数$d\ge3$の超曲面商から、低次数の乗法によりambientと方程式直線を復元する。noetherian AS Gorenstein条件で偏極付き圏からの復元も証明。Serre関手のみでの復元は三次三様体の追加条件付きで、一般次元については未証明。旧Bの41次元中心三次対、17係数正規形、分離型余次元15、忘却核7と関連証明・計算コードはnc-cubic2の `papers/nc_cubic_threefold_moduli.tex` および研究ノートに統合した。構成した17次元族のnc cubic moduli内の既約成分性は未証明。標準5次元AS正則$\mathbb Z$-代数の正則正規三次族からの1周期性は`nc-cubic2/papers/sections/ambient_periodicity.tex`に証明を保持し、非可換三次三様体のモジュライ原稿に統合する。論文AはPoisson構造と量子化を中心とし、一般次元のquadratic envelope復元は引き続き論文Aに保持する。主リポジトリの公表原稿はAとCの二つ。

## 現行の研究入口と主なファイル

- 公表原稿：papers/paper_a.tex（A-v50、日本語LuaLaTeX）
- 二つのスタックの定義と代数性：papers/support/papers/sections/poisson_moduli_stacks.tex
- Fermat／relative成分公式：papers/support/papers/sections/fermat_relative_poisson_components.tex
- 現行知識ノート：notes/fermat_relative_poisson_components.md
- 全Poisson量子化の核心証明：papers/support/papers/sections/universal_casimir_determinant.tex、
  papers/support/papers/sections/poisson_geometry.tex、
  papers/support/papers/sections/general_dimension_universal_quantization.tex
- 現行の中心元研究ノート：notes/universal_casimir.md
- 投稿監査：notes/poisson_article_submission_audit.md、validation.json
- 厳密計数再現：computations/verify_poisson_stack_component_counts.py
- 特異三次制限の独立検算：computations/verify_singular_cubic_classical_kernel.py
- 式番号・引用の静的検査：scripts/verify_article_a_numbering.py

## 論文C：一般次元の中心三次非可換超曲面の可換復元

現行稿は `papers/paper_c.tex` (C-v40)、主定理と証明依存は
`papers/support/papers/reconstruction/general_dimension_recovery.tex`。
$n\ge3$、$N=n+2$ とし、一変数代数的flat中心三次対で局所window/proper (L) と
実際の完備graded MF同値 (CF)、一般点のnoetherian Koszul AS-regular条件が
成立すれば、有限拡大 $K'/\mathbb C(h)$ 上で
$(\mathcal K^{\mathrm{coh}}_{B_{K'}},\rho_B)\simeq
(\operatorname{Ku}(Y),\rho_Y)$（$Y/K'$滑らかなcubic $n$-fold）。
三shift生成、Eulerノルム $2\cdot3^{N-1}$、有限perfect核の降下、
smoothnessからのcoherent飽和は全次元の既存証明を合成する。
可換模型の一意性は $n>3$ で Pirozhkov のTorelliを使用（代数閉包後）。
五変数混合族の閉公式には追加で(D)を使用する。

(L),(CF) の全依存の独立監査は未完成であり、原稿記載の証明が
無条件に一般の全非可換三次超曲面へ適用できるとは扱わない。
多変数全体の同時可換復元、計算済み模型の一般次元閉公式、
有限拡大次数、具体同値核、特殊点込みの同値も未完成。
現行の検証入口：`notes/general_dimension_categorical_reconstruction.md`。
次は (CF) の内部次数付き曲率比較と (L) の相対window/stabilization を
独立監査し、論文Aの各量子化線に適用する。

## 論文Aの範囲：一般次元に集中する

論文Aの本体は、任意次元の滑らかな三次超曲面について
Poisson正規形、退化スキームの一般的生成元とcritical covers、
Bondal予想、代数的量子化、固定・相対moduli stacksを扱う。
六・七次元に特化した退化スキームの詳しいprimary分解、
階数二・四・六の個別表、Hodge/Chern/種数の計算は
この本体の論理に必要なく、全体の焦点をぼかすので、
独立草稿として`uedakazushi/nc-cubic2`の
`papers/poisson_cubic_six_seven_geometry.tex`へまとめた。
移管先には、主論文の一般退化イデアル・finite flat critical coverと
零点完全交叉の補題の**証明全文**も持たせてある。
このため主論文Aの一般定理を移管先参照で代用せずに保持する。
詳細な現行知識は`nc-cubic2/notes/poisson_cubic_six_seven_geometry.md`。
七次元rank6のprimary分解・embedded長8,64,49は
独立研究価値の候補だが、先行研究上の新規性と局所イデアル証明の
独立監査は未完成。標準的な完全交叉の数値計算だけでは
論文Aの主定理とは独立に公表価値を主張しない。

本文の移管元を取り除いた後も、一般退化スキームの
`prop:pg-deg-ideal`、`lem:pg-critical-cover`、
`prop:pg-deg-support`、`prop:pg-zero-ci`と
その証明は論文Aに残っている。
またn=6,7の一般次元量子化への**適用**は
`general_dimension_universal_quantization.tex`にそのまま残す。
研究再開ではまず現在の論文Aを読み、
移管先の副次研究に新しい最優先を勝手に変更しない。

## Poissonのspace・固定stack・relative stack

（1）space of Poisson structuresは、Jacobi二次式の閉アフィン零スキーム
Pois(X)=Z([pi,pi]) in H^0(X,Λ²T_X)である。
Poisson双ベクトルのスカラーを割らず、零構造とnilpotentスキーム構造を含む。

（2）moduli stack of Poisson structuresは
PoisStack(X)=[Pois(X)/Aut(X)]。
各点の安定化子はPoisson automorphism群Aut(X,pi)。
n>=3の滑らかなcubicではSGA2のPicard定理とgradientの
一次syzygy消滅からAut(X)は有限エタール。
従ってPoisStack(X)は有限型Deligne--Mumford代数的スタック。
既約成分はPois(X)の成分のAut(X)軌道と対応し、spaceと個数が違い得る。

（3）relative moduli stack of Poisson structuresは
PoisRel_n=[P_n/PGL(V)]、N=dim V=n+2。
滑らかな三次式の開U_N in P(Sym³V*)上で
P_n in Tot(Λ³V⊗O_U(-1))はrelative Jacobi二次式の閉零スキーム。
FをaFに替えると三重ベクトルPをP/aに替える。
PGL(V)は滑らかであるから、Stacks Project Theorem 97.17.2
（Tag 06FI）によって代数的有限型。
幾何学的安定化子Aut(X,pi)は有限エタールなのでDM。
cubicのmoduli stackへの忘却射を持つ。
Xを枠付けた2-fiberはPois(X)、同型類のresidual gerbe上ではPoisStack(X)。

## 全次元の既約成分数：Fermatとrelative

Fermat X_N=V(Σ_i z_i³)、N=n+2について、
添字集合{1,...,N}の各大きさ>=3の非順序ブロック分割Bごとに
Z_B=Σ_{B_s in B} cone(Gr(3,C^{B_s})) in Λ³C^N
がspace Pois(X_N)の被約既約成分である。
従ってspace成分数は、各部分が3以上の集合分割数
Σ_{k=1}^{floor(N/3)} S_>=3(N,k)である。
Hessian判別式∏_i z_iによりFermatの自己同型は
(μ_3^N/μ_3)⋊S_Nというmonomial群。
座標置換で同じサイズ多重集合のブロック分割が同一視されるため、
固定stackの成分数は整数分割数
p_>=3(N)=[q^N]∏_{b>=3}(1-q^b)^(-1)である。
relative stackは一般階数2kごとに一成分で
floor((n+2)/3)個。

n=3,4,5,6,7,8,9,10について
spaceの個数は1,11,36,92,491,2557,11353,60105、
固定stackは1,2,2,3,4,5,6,9、
relative stackは1,2,2,2,3,3,3,4。
一般の滑らかなcubicではspaceと固定stackは既約。
よって固定stackの成分数は複素構造に依存する。
Fermatが最大になることは未証明。
各成分公式の証明は論文Aに掲載しているが、
正規形のLie代数補題を含む全依存の独立監査は未完了。

## 解決した最優先の中心三次元定理（全Poisson構造）

**確立した数学的構造と証明の所在：**
任意の滑らかな全体三次式
\`f(x,y,z,u)\` に対して、三変数制限
\`g=f(x,y,z,0)\`の滑らかさを課さず、
Jacobian量子化代数\`A_{f,h}\`に
\`Omega_h in Z(A_{f,h})_3\`、\`Omega_0=f\`となる
**代数的な中心三次元**がある
（\`thm:pg-universal-determinant\`）。
係数は有限個の次数三Weyl単項式に掛かるh²の有理式で、
原点で分母は非零。Hesse型の\`g\`がsmoothなら
既存のh⁴までの短い多項式公式が使える。

**新しい証明の4点（形式的中心元は一切使わない）：**
1. 全体fの滑らかさから\`gcd(f_x,f_y,f_z)=1\`。
   共通因子hがあれば\`h=f_{u_1}=...=f_{u_m}=0\`の
   非零射影解がKrull高さ定理により生じ、
   全偏微分の共通零点になって矛盾。
2. UFDと同次数性から、古典次数三Casimir核は
   \`C*f + C[u]_3\`（\`lem:pg-det-classical-kernel\`）。
   すなわち古典交換子行列のrankは
   \`r=binom(m+5,3)-binom(m+2,3)-1\`で**滑らかな全体fなら一定**。
3. 滑らかな全体fの係数空間は既約で、
   gが滑らかな稠密開では普遍Hesse式から量子中心元がある。
   PBW/Weyl基底の普遍交換子行列\`D_{f,h}\`の
   全(r+1) minorはこの開上で零、よって
   **係数空間上恒等的に零**。gが特異・零でもrank≤r。
4. 原点でrank=rのため非零r×r minorを取り、
   Cramerのdet比から量子中心元を構成。
   順序反転+\`h→-h\`で係数はh²の有理式。
   古典Casimir核から特殊化が正確にfとなる。
   **中心元そのものを特異gへ無条件に特殊化するのではなく、
   minor恒等式を特殊化する**ことが論理の要点。

**任意次元の全Poisson構造：**
正規形\`F=Σ_s tilde f_s(x_s,u)+c(u)\`において
純中心三次c(u)を\`c_1+...+c_k\`へ配分し、
全ての\`f_s=tilde f_s+c_s\`を
滑らかな全体三次式へできる
（\`lem:pg-central-splitting-smooth\`）。
u=0ではXの滑らかさ、u≠0では基点自由な中心三次系へのBertini、
配分パラメータ空間の既約性を使用。
配分はactive偏微分を変えないのでPoisson構造も同じ。
各f_sにCramer中心を構成し和\`Omega=Σ_sOmega_s\`を取れば
**全ての滑らかなcubic上の全Poisson構造**の代数的量子化を得る
（\`thm:pg-quantization\`）。
各fiberのambientはKoszul AS-regular（gldim N=n+2、
Hilbert \`(1-z)^(-N)\`）、中心元は左右正則、
中心商はAS-Gorenstein（injdim N−1、
Hilbert \`(1-z³)/(1-z)^N\`）。
さらに独立パラメータeta_sで
一般の**k次元Poisson線形族の全方向**を
同時に代数的量子化（\`thm:pg-ad-all-poisson\`）。
形式的量子化・Kontsevich・Dolgushevはこの証明の入力から除外した。
これは**全モジュライにわたる大域的同変量子化**という意味ではない。

**独立に計算した特異制限の具体例：**
\`f=u x²+v y²+w z²+u³+v³+w³\`は
\`g=f(x,y,z,0,0,0)=0\`だが全体三次は滑らか。
古典交換子行列は378×56、rank45、
核は\`C f + C[u,v,w]_3\`（次元11）。
SymPyによる有理数行列の厳密rank計算を実際に実行してPASS。
\`computations/verify_singular_cubic_classical_kernel.py\`を登録。
さらにこの具体例ではf自身が量子代数の厳密中心元。
一般の特異gについての新しい定理はこの有限計算に依存せず、
普遍minor恒等式とCramer証明による。

**保留する問題：**
正規形\`thm:pg-normal\`のLie代数補題・普遍Hesse計算証明書・
PBW/AS正則性の全依存を独立再監査する。
全係数上の短いGL3同変多項式中心元、
Hesse/行列式チャートの同型とmoduli stackへの降下、
全Poisson moduliの大域的量子化、qgrのsmoothness、
非可換Kuznetsov復元は未解決。
一般次元の内在的Hessian二次補正
\`H(P,F)=ΣP^{ijk}P^{abc}F_{ia}F_{jb}F_{kc}/6\`
は引き続き有効。
既知のEtingof--Ginzburg §8.3のrank・特殊化法と
今回の固定次数の独立したminor証明を一次資料と照合したが、
全研究の初出・新規性調査は未完了。

## 投稿の達成基準と次の研究課題

1. 定義・代数性と成分数の式を維持し、
   特にthm:pg-normal、lem:pg-quadratic-lie、Fermat component theorem、
   relative rank層・Bondal予想の依存を独立に精査する。
2. Poisson pair moduliの境界・scheme構造と、
   高次元量子化族の表示チャート間の同変性・降下を調べる。
3. Stacks Project、SGA2、Matsumura--Monsky等の一次資料を照合し、
   既知と本研究の貢献の関係をIntroductionで明確にする。
4. 論文Aの全表示式を自動的な数字の式番号に統一済み。
   数学的検算とは別にLuaLaTeX全組版・PDF目視・引用・
   厳密計算証明書の必要な範囲の再現を確認する。
   全てが済むまで投稿可能と断定しない。

## 保持する論文A/Cとnc-cubic2の研究到達点

## Poisson構造定理の新たな帰結：Bondal予想（論文A）

**証明を追加。** n>=3の滑らかなcubic n-foldの任意のPoisson構造に対して、全j（2j<n）のD_{2j}は次元2j+1以上の既約成分を持つ。非零Poissonの正規形F=Σ f_s(x_s,u)、一般rank2kを使い、j<kならr=j+1個のブロック内の平面曲線C_s⊂{f_s(x_s,0)=0}のjoin J_rを構成する。J_r⊂X、dim J_r=2r−1。全ブロックのJacobian rank2ならEulerベクトルが像に入り射影化でrankが2下がり、いずれかrank0ならもとからrank≤2r−2。従ってJ_r⊂D_{2j}。π=0またはj>=kはD=X。全文 `papers/support/papers/sections/bondal_cubic.tex`、ノート `notes/bondal_cubic.md`。**正規形定理thm:pg-normalに依存し、その既存証明全体の独立再監査は未完了。** 2013年Fano4、2026年Fano5の既知定理との重複に注意し、新規性は未確定。正規形のLie代数補題を次に優先監査する。

## Point schemeの二パラメータ族とPoisson零点（論文C、証明あり）

**混合係数λの全滑らかな値へ拡張。** F_λ=(x³+y³+z³)/3+u³+v³+λuxy、λ³+3≠0、h⁶+27≠0。h≠0のB_{h,λ}のpoint module初期点の表現スキームは、λに依らないSklyanin Hesse楕円曲線 E_h: u=v=0, x³+y³+z³+h²xyz=0 と、u=1上の有限スキームS_{h,λ}の非交和。有限部分の可換商は x²+λy=y²+λx=z²=0, 1+v³+λxy/3+h²z(λ²/6−2xy/3)=0。基底 x^a y^b z^c v^d (a,b,c=0,1; d=0,1,2)によりλ,h同時に自由rank24。λ³+3≠0ならvは単元で、v'=v+h²z(λ²/6−2xy/3)/(3v²)によりS_{h,λ}はh方向に抽象的に自明。

**scheme-theoretic平坦極限。** E_h⊔S_{h,λ}は二パラメータで平坦、h=0の埋め込みスキームはX_λ上のPoisson零点D_0(π)。Hilbert多項式は3t+24。h=0の非可換代数そのもののpoint schemeはX_λ全体であり、平坦閉包とは区別する。

**λ=0の衝突。** λ≠0ではSは12個の長さ2の非被約点。λ=0では3個の長さ8の点へ衝突し、各局所環は C[x,y,z]/(x²,y²,z²)、Hilbert関数(1,3,3,1)。全長24は保存。λ³=−3では元のcubicが特異、h⁶=−27ではSklyaninが退化するため適用外。

証明全文は `papers/support/papers/reconstruction/point_scheme_lambda_family.tex`、再生成可能な単独LuaLaTeX入口は `papers/support/papers/point_scheme_lambda_family.tex`、現行研究ノートは `notes/point_scheme_poisson_zero.md`、厳密検算は `computations/verify_lambda_point_scheme.py`。前段のλ=1非被約・平坦極限の証明は `point_scheme_thickening.tex` に保持。3D Sklyanin point-scheme定理は既知入力。一般のnc cubicに対する同一結果や全先行研究上の新規性は未確認。

## 特異な混合係数境界でのpoint scheme（論文C）

**証明済みの有限平坦モデル。** 特殊値 λ³=-3 では元の可換cubicが特異となりPoisson多様体の零点定理の適用外だが、既存の中心座標u=1における有限point-module可換化環は C[λ,h] 上で自由rank24（基底 x^a y^b z^c v^d、a,b,c=0,1; d=0,1,2）。これは λ,h の分母を使わず、判別式境界やh=0にも代数的に延長する。**h=0のこの環はB_0自身のpoint schemeではない。**

λ³=-3、h≠0では支持が6点：x=y=0から3個の二重点、非零x,yの3枝に各局所環C[v]/(v^6)の曲線的六重点。h=0では同じ3枝の局所環はC[v,z]/(v³,z²)となり、長さ6は同じでも埋め込み次元は1から2へ変化。δ=λ³+3を境界の局所パラメータとすると非零枝で hλ≠0 の模型は (v³+δ/3)²=0で、一般λの3二重点が判別式上で1六重点に合体する。証明: `papers/support/papers/reconstruction/point_scheme_discriminant_boundary.tex`、単独LuaLaTeX `papers/support/papers/point_scheme_discriminant_boundary.tex`、有限検算 `computations/verify_lambda_discriminant.py`。

有限部分の全パラメータ平坦性と、**滑らかなPoisson零点との平坦極限の同定**は異なる。後者はλ³≠-3のv41定理の範囲に保ち、特異境界では無条件に主張しない。h⁶=-27のSklyanin退化も未調査。

## 最終目標と現在の結論

構成した代数的nc cubicの幾何学的一般点について、全coherent残余圏を滑らかな可換cubicのKuznetsov成分から、指定rotationと三次周期性を保って復元する。存在、方程式、同値核の明示化を区別する。

**既存入力(L),(CF)下の一変数量子化では、有限拡大K'/C(h)上で全coherent残余pairの可換復元が得られる。** (L)は局所proper/window模型とHom底変更、(CF)は次数別完備底上の実際の有限rank MF A∞同値であり、互換なArtin同値の列だけではない。明示的なlambda=1の多項式を復元先に取るには既存の有限対角比較(D)も使う。これらの既存証明を今回全部独立再監査したという意味ではない。

今回、中心三次商のGorenstein条件から全coherent対象に対する線束Homの有限性と検出性を得て、線束生成部分がsmoothなら全coherent導来圏に一致することを証明した。既存の一般点同値から残余smoothness、有限例外成分との貼合せから線束部分smoothnessが従う。したがってK^linと全coherent残余圏の差は、この一般点・AS-regular入力の範囲では残条件でなくなった。

全Db(qgr B)と可換Db(coh Y)の同値は主張しない。残余同値でも例外成分との貼合せは異なり得る。Bそのものの有限global dimensionも主張しない。特殊点を含む相対同値、有限拡大次数・同値行列、多変数の全モジュライ方向は未完成。

## 論文Cにおける現行の最短証明経路（保持）

1. (L)によりK_R=stab(R)、T_R=K_R⊕K_R(1)⊕K_R(2)が線束生成残余圏を表すproper生成代数Gamma_Rを与える。
2. (CF)を固定三対象に制限し、各固定Hom次数の通常の完備係数写像としてからhを反転する。任意のLaurent対象へ無限Taylor和を新しく評価しない。
3. special stabilizationのEulerベクトル `chi_r=Σ_(s+r=0 mod3)(-1)^s binom(N,s)` の二乗和 `2*3^(N-1)` とproper性から一般点の像が非零と分かる。
4. Stevensonのaffine hypersurface分類と次数の再付与・compact局所化から、非零像の三shiftが可換graded MF全体を生成する。これでLaurent体上の同値を得る。
5. 体上でcompactとなる核とrotation比較を有限表示性で有限型部分代数へ降ろし、非空開の閉点を取って有限拡大K'/K上の同値を得る。全文は `rotation_orbit_generic_reconstruction.tex`。
6. **全coherentへの拡張。** B=A/(w)はGorensteinでchiと有限cohomological dimensionを持つ。任意MのRHom(O(j),M)は体上perfect、全twistが零を検出する。smoothな線束生成代数LambdaではN_M=RHom(G,M)がLambda-perfect。評価のconeが全twistと直交するため零。C_lin=Db(qgr B)、K_lin=K_cohを得る。有限拡大からのsmoothnessは対角のrestriction/retractで降下する。全文は `coherent_residual_saturation.tex`。

完備底全体のcompact逆核、一般MF核全忠実性(KF)、特殊点の生成性を一般点へ持ち上げる命題を前提にしない。旧反例は有効なまま。

## 明示式と保持する成果

混合lambda=1の式は
`G_h+v^3=(x^3+y^3+z^3)/3+v^3+h^2xyz/3+(1+h^6/54)uxy-h^4uz^2/18-h^2u^2z/12+(1+29h^6/648+h^12/4374)u^3`。
(D)と可換projected kernelによる全Artin低Nat底変更からW_hと形式GL5同型になる。この変換はLaurent体上では通常の変換となり、Gを固定して降下できる。勾配変換det=1+h^6/27、正則行列分母(h^3-1)(h^6+162)、q=h^6の正規形L=1+127q/5184+O(q^2)、C=13/36+1613q/1679616+O(q^2)を保持する。行列分母をsmoothness判別式と呼ばない。

論文Aの一般Poisson正規形・固定方向の代数的量子化、一般次元ambient復元は論文Aに統合し、41次元中心三次対・17係数slice・分離型余次元15・忘却核7はnc-cubic2のモジュライ原稿に保持する。全nc cubic分類や全係数の一様量子化と混同しない。

論文Cの形式MF、相対window、有限積分、全16積、bar/cup/characteristic比較、幾何学的BC、片側Morita/Popescu、相対sector、対角unit、中心対称性、純Poisson一次消滅、分離Hessian、非楕円fivefold、35係数slice、A∞arity、SM/ERおよび反例を保持する。有効な証明を容量削減のため要約・削除しない。

## 論文Cの残る課題（一般次元稿の独立監査と適用）

1. **残る依存の独立監査。** 今回はStevensonの適用範囲、次数再付与、固定HomのLaurent局所化を点検した。次に(CF)の曲率formality・coherent inverseの全構成と、(L)の通常導来stabilization/window、明示式への(D)を順に監査する。証明の記載と独立監査を区別する。
2. **有効化。** 三shift生成の有限cell、同値核の行列、有限拡大次数を明示する。今回、線束生成代数の対角のq段表示があれば全coherent対象もq段で生成されることを示したが、qは未計算。
3. **範囲拡張。** 一般lambdaの明示式、独立中心変数のない成分、多変数基底・全Poissonモジュライ一般点への適用を検討する。一変数の結果から無条件に一般化しない。
4. 特殊点を含む相対同値には、保持した片側compact形式核・Popescu・SM経路を使う。今回の有限体拡大降下は形式分枝全体の再現ではない。

## 証明・計算・再現の状態

新定理の証明と一次資料を確認：Burke–Stevenson1507.00830v1 Prop4.18/Lemmas6.1–6.2/Thm6.4、Toën–Vaquié0503269v5 Lemma2.8(2)、Perry Lemma4.15(3)。Stevenson1105.4698v3 Thm6.13とDyckerhoff0904.4713v5 §2.4を原PDFで再確認した。一般原理の新規性は主張せず、包括的新規性調査・外部査読・形式証明は未実施。

`python3 scripts/verify_coherent_residual_assets.py --rerun-orbit` は新原稿の参照とCへの統合を点検し、既存64 Eulerベクトルと32×32行列41恒等式を再実行する。今回、既存コードおよび生成証明書のGit blob SHAが正本と完全一致した。新しい飽和定理の形式証明やnc全行列の再計算ではない。

`latexmk papers/paper_c.tex` で新単独稿を生成する。単独稿5頁の組版と表示を確認。現行A/Cとnc-cubic2の移管原稿全体の組版、CF全構成と全既存計算の再検証は未実施。正確な状態をvalidation.jsonに記す。

## 研究一般の原則と保存許可

以下は研究固有の計画とは別の一般原則である。
1. 数学的重要性、新規性、理解、応用、正確性、実現可能性を総合して価値を最大化する。方針は現行の理由・到達点・未解決事項として書き直し、履歴を蓄積しない。
2. 証明済み、追加仮定付き、未完成、予想、計算観察を区別する。仮定・依存・証明所在を記し、記載・今回の監査・計算・外部査読・形式証明を分ける。誤りは依存する記述も修正する。
3. 重要文献は一次資料を確認し、未確認の内容・書誌・新規性を補作しない。外部PDFや検索結果を大量収録しない。
4. 価値ある数学と十分な証明を日本語LuaLaTeXで保持する。ノートは有効な知識・例・反例・障害を整理し、作業日誌や重複証明にしない。
5. **区切りごとに承認を求めず、方針・ノート・論文全文・必要なコード/証明書・再現手順をmainへ通常のfast-forwardで反映する。** remote変更を保持し、force push・無断PR・GitHub Actionsは禁止。refと変更blobを照合する。
6. **Library保存は実際のGitHub反映失敗時のみの緊急避難。** 未同期と復帰手順を示し、既存Libraryファイルを無断削除しない。
7. 最新一式から再開できる構成とし、旧ZIP・旧稿・ログ・cache・重複を追加しない。数学・検証可能性を固定容量のため削らない。独立境界/未照合PDFはnc-cubic2、Reyeはreyeに保全。
8. 日付・版・参照を揃え、生成・計算・組版・保存・遠隔確認を分けて報告する。PDFはGit追跡せずlatexmkでbuild/へ生成する。
