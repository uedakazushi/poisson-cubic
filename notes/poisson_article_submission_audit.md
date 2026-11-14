# 論文Aの公表準備：主張・依存・検証の範囲

**2026-11-14 / A-v59・B-v59・bundle nc-cubic-v92。** 再開時は `00_research_plan.md` を先に読む。
本文は `papers/paper_a.tex`、専用文献は `papers/support/papers/references_poisson_cubic.tex`。
以下の節ファイルはすべて `papers/support/papers/sections/` にある。
計算・組版・入力ハッシュの実行記録はルートの `validation_paper_a.json` に集約する。

## 現在の公表範囲

中心結果は、滑らかな三次超曲面上の全Poisson構造のJacobianブロック正規形、
全次元でのBondalの下界、全Poisson構造の代数的量子化、Fermatと相対Poissonモジュライの成分数である。
具体的な四次元の帰結として、一般階数四の構造の分離型分類、ambient Hessian階数軌跡による存在判定と純楕円退化因子を扱う。Hessianの可約性だけでは不十分な滑らかな例も含める。
中心元は固定した変数分解の全滑らかな係数空間上で同時選択できる。
さらにN>=5、全三次式Fが滑らか、Pが非零分解可能である全supportの係数空間について、
H_N=GL_N×Gmに共変な代数的中心元を、全零h切断を含む一つの開上に同時に選べる。
証明は古典核のBWB消滅、h冪厚化への持上げ、Stiefel開の正則関数の延長、
有限核のNoetherian完備化、還元的平均化を結ぶ。
gcd(N,3)=1なら、全階数二の被約Poisson層とh直線の積の零切断近傍へ
実際の次数付き代数・中心イデアル・中心商が降りる。N=5では全非零Poisson対を扱う。
零Poisson構造、全hへの延長、一意性、既存層別公式との一致はこの定理の範囲外である。

層別の明示的構成も保持する。
単一ブロックではreductive群に関して全係数空間上で同変に選べ、
三変数制限が滑らかな開と、節点・尖点の各軌道では、中心平行移動を含む群にも型ごとに拡張できる。
零制限ではPBW対称化したΩ=sym(f)が全パラメータの全G共変な正則中心元となり、
一般のG_0同変選択もこの零層の元に一致させられる。
線形群の商上の中心Gm-gerbeを同定し、gcd(m,3)=1では指標で次数線形化を補正して、
階数二のPoisson対の被約層内の開へ代数族を降ろす。
support平面がXに含まれる零制限層では、同じ指標による降下を全h直線上で行える。
節点・尖点層では唯一の特異点の直線束で次数重みを補正するため、gcd(m,3)=1を仮定せず、
本稿の範囲m>=2の全てでgerbeが中立となり、実際の次数付き代数と中心商が零h近傍へ降りる。
三次三様体での底の次元は節点型16、尖点型15である。
これらの層別の中心元と、新たに全supportで選ぶ中心元が一致するとは主張しない。
特に零制限の全h公式sym(f)と、その式に一致するG_0選択は別の強い範囲を持つ。
全f・η・hを用いても補空間を正則同変に選ぶことはできず、
中心平行移動Uの自由商は非アフィンである。中心核を直接扱う方法はこの障害と両立する。
ambientの二次包絡、偏極付き圏からの復元、三次三様体の条件付き導来復元は付録に収める。本文・付録を通じてambientはA、中心商はBとする。
要約・序論はこの依存順に整理し、Fermatのspace・固定stack・相対stackの三種類の成分数を区別する。
表示式には数値の式番号を付ける。

一般退化イデアル、critical cover、零点完全交叉は本文に必要な証明を保持する。
独立な六・七次元のprimary厚化（長さ8, 64, 49）と数値幾何は
`uedakazushi/nc-cubic2` の `papers/poisson_cubic_six_seven_geometry.tex` が現行入口であり、
Aの一般定理の証明を移管先へのリンクで代用していない。
移管先の独立公表価値とprimary分解の監査は、Aの検証とは別である。

## 主張の確実性と証明の所在

次の証明連鎖を本文と外部入力の適用条件に沿って点検している。
「点検」は独立な数学的読み直しを意味し、Lean等の形式検証や外部査読を意味しない。
既存の有効な証明監査を保持し、現改訂では全supportのBWB消滅、形式核への逐次持上げ、
有限Weyl開、有限核の完備化からの代数的持上げ、H_N平均化と次数補正による降下を独立に読み直した。
全fに依存する補空間選択の障害、U作用の自由性・非自明torsor・非アフィン商も点検した。
CMRのaccepted versionとの節点公式の対応は、本文の数学的読解と独立な厳密計算を分けて記録する。
節点・尖点の安定化群と左逆、軌道上の移送、特異点直線による降下、
不可約三次式全域での左逆の障害と層の次元については既存の有効な監査を保持する。
全次数PBWからAS条件・正則中心商への依存、rank/Cramer構成、Reynolds持上げ、
零制限の全パラメータ構成については既存の有効な監査を保持する。
既存の大きなHesse計算や、正規形・幾何・量子化の全証明を今回再実行・再監査したという意味ではない。
これは添付査読報告をすべて再実行・形式検証したという意味ではない。
主定理の記載済み証明、有限計算、初出の確認は区別する。

| 主張・所在 | 有効な仮定と結論 | 点検した内容 |
| --- | --- | --- |
| `lem:ci-low-twist-vanishing`、`complete_intersections.tex` | 滑らかな完全交叉、n>=2、1<=p<=n-1、t<=pならH⁰(Ω^p(t))=0 | Koszulによる線束消滅、穿孔錐のconormal外積分解、水平形式とCartan公式による独立証明。既知結果である |
| `prop:pg-represent`、`prop:pg-jacobi-extension`、`lem:pg-linearize`、`poisson_geometry.tex` | n>=3、Xが滑らかな三次。Poisson表示、Jacobi条件とHessian線形条件の対応 | Euler/Koszul、divergenceの係数、Hessianとの符号を追跡 |
| `lem:pg-basepoint-free-lie`、`lem:pg-quadratic-lie`、`thm:pg-normal` | 全非零Poisson構造が三変数Jacobianブロックへ分解 | 非退化形式の同時選択、可解根基、最高ウェイト、rank>=2単純因子の排除、混合項の消去 |
| `lem:pg-projective-rank`、`thm:pg-bondal`、`bondal_cubic.tex` | 全2j<nについてdim D_(2j)>=2j+1 | joinの次元、Euler線によるrank低下、ブロック数の端のケース |
| `prop:pg-deg-ideal`、`lem:pg-critical-cover`、`prop:pg-deg-support`、`prop:pg-zero-ci` | 一般退化イデアルは全正規形。critical coverと零点完全交叉には各純active三次の滑らかさが必要 | 正規形に基づく式と仮定の使い分け |
| `prop:pg-split-elliptic`、`cor:pg-cubic-fourfold-elliptic` | 滑らかな三次四様体の一般階数四の構造は全て(3,3)分離型で純楕円log symplectic。その存在はambient Hessian階数≤3軌跡が平面を含むことと同値 | join・Pfaffian・被約Poisson零点・modular場の既存直接証明を保持。BFP Theorem 3.4のn=5,k=2の照合を保持。Pym v1 Definition 4.2との適合を再読 |
| `ex:pg-reducible-hessian-no-rank-four` | F=x₀³+x₁³+Σzᵢ³−(Σzᵢ)³は滑らかでHessian可約だが(3,3)型に分解しない | 符号による滑らかさ、全点での定数symmetrizer E_F=diag(a,b,cI₄)、座標共役、階数三冪等元の不存在を独立に読解。QQ線形代数の検算は別記 |
| `prop:pg-triple-lifting-obstruction`、`cor:pg-split-lifting-obstruction`、`poisson_geometry.tex` | 滑らかな次数d超曲面内の滑らかな非空C、全連結成分が正次元。任意r>=2についてH¹(I_C^{r−1})=C^{π₀(C)}/C、次数d・r重消失の障害δ_r | ideal sheafの冪、正則局所方程式、余法束の全対称冪の切断消滅、全厚みの成分定数。連結時は存在・一意性。r=3の分離型でδ(g_X)≠0。全射性と任意twistへの拡張は未主張 |
| `prop:pg-PBW`、`lem:pg-center-parity`、`prop:pg-universal-casimir-jet`、`quantization_foundations.tex` | 一ブロックの相対PBW・偶性・有限jet | 既知PBW入力と係数環への拡張。全次数PBWを有限次数の中心性検算とは区別 |
| `thm:pg-universal-determinant`、`universal_casimir_determinant.tex` | 全体三次fが滑らかなら、active制限が特異・零でも、原点近傍に代数的中心三次元 | gcd、古典核、普遍行列、局所自由性、稠密Hesse開、Cramer規格化、偶性 |
| `lem:pg-det-divided-kernel`、`prop:pg-det-normalization-transition`、`thm:pg-det-global-coefficient-lift` | 固定変数分解の全係数空間×h内で、全零切断を含む開上の偶な中心元。遷移はΩ'=aΩ+c | 任意底変更、通常の中心との差、偶principal開、忠実平坦下降、UFD/Pic=0、単元補正、Hesseのイデアル不一致、covarianceを独立に再点検 |
| `thm:pg-equivariant-levi-center`、`equivariant_central_lifts.tex` | 全滑らかなfでG_0同変な偶中心元。定義開は零切断とg=0の全t層を含み、零制限ではsym(f)に一致 | stable idealへのReynolds平均、指標twist、Z₀=(t=0)∪(g=0)上の指定値の持上げ、商線束の零点除去 |
| `lem:pg-equivariant-singular-retractions` | 節点・尖点の各軌道上にδ_gの正則なL同変左逆。軌道の次元は9、8 | 方程式scale込みの全安定化群Gm×S₃、Gm²、明示σ、L/Hへの正則な移送。各型の標準形を係数比較で確認 |
| `thm:pg-equivariant-parabolic-center` | gが滑らかな開、節点軌道、尖点軌道のそれぞれで、零t切断全体を含む開上の全G同変中心元 | smooth gではaffine底の分裂、節点・尖点では軌道上のσを使用。B_fの変換則、fの滑らかさ、Q(f⁰,0)=1を保つ定義開の引戻し。これら層別の式と全supportの別の選択との一致は未主張 |
| `rem:pg-equivariant-stratumwise-centering` | 不可約ternary cubicの全開には、gだけに依存する単一の正則なδ_g左逆は存在しない | 可約式の錐の余次元2、正規性による行列成分の延長、g=0での矛盾。同変性なしでも成立し、中心元自体の貼合せ不存在は意味しない |
| `thm:pg-equivariant-zero-center` | g=0なら全t・全係数でPBW、Ω=sym(f)は全G共変。f smoothなら三次の割った交換子核はOΩ⊕C_m | 中心e₀を足したLie代数、monic PBW、対称化と交換子の厳密一致、全tの定階数核。中心性にはf smooth不要。一般のG_0族を(t=0)∪(g=0)上の指定値へ持ち上げる補強も点検 |
| `cor:pg-equivariant-central-quotient` | 線形群の商上の次数別平坦なAS-Gorenstein中心商族 | t=ηhでhを固定、domainと正則性、各次数の局所自由性、スカラーの重み |
| `prop:pg-equivariant-poisson-gerbe`、`cor:pg-equivariant-character-descent`、`rem:pg-equivariant-classical-family` | gcd(m,3)=1なら次数線形化を補正して階数二の被約Poisson層内の開へ降下。n=3で底は17次元 | GLの付随束表示、二つのスカラーの群完全列、fppf安定化群完全列、mr−3s=1の分裂、古典極限Sym(E_θ)と三次直線、相対Projを点検。大域中心生成元と固定h≠0での像の次元は未主張 |
| `prop:pg-equivariant-zero-stratum` | P(W_P)⊂Xのrank2層はm>=3でのみ非空、滑らか既約・余次元10。全hのgerbe族、gcd(m,3)=1なら層自体へ降下 | m個の法方向二次式、滑らかな例、共通incidence上のrank10制限束、Gbar商と次元D−m²−3m−18。m=3で指標法の適用は主張しない |
| `prop:pg-equivariant-singular-strata` | m>=2、節点・尖点の被約rank2層は非空・滑らか・既約、余次元c=1、2、次元D−m²−3m−8−c。全mでgerbe中立、零h近傍の次数付き代数が層自体へ降下 | 滑らかな全fの例、共通incidenceの局所閉制限、Gbar商。特異点直線ℓのpullback M⁻¹と重み−1、A_d⊗ℓ^d、frameによる中立化、重み零の積・中心イデアルの下降、古典Proj。n=3では16・15次元 |
| `lem:pg-rank-two-bott-vanishing`、`intrinsic_rank_two_center.tex` | N>=5、Gr(3,N)上のO(j)とSym³Q*⊗O(j)のH¹が全整数jで零 | BWB重みの重複・置換長、非零Plücker錐のGm-torsor、全twistの直和、アフィンな全F係数空間との積を独立に確認 |
| `thm:pg-intrinsic-rank-two-center` | 全smooth F・非零分解可能P・任意の制限型を扱い、全零h切断近傍でH_N共変な偶中心元、K=C⊕OΩ、次数別局所自由な正則中心商 | 局所核の任意底変更、形式持上げ、Stiefel開とSL3不変環、固定pivotによる有限Weyl開、Khat/hKhat≅K/hK、平均化、全次数PBW開への制限。形式級数全体の代数性やP=0での定階数性は仮定しない |
| `cor:pg-intrinsic-rank-two-descent` | gcd(N,3)=1なら全被約rank2層×A¹_hの零切断近傍へ実際の次数付き代数と中心商が降下。N=5では全非零Poisson対 | H_N/K_scによる商同定、Nr−3s=1、θ=(det L)^rλ^s、次数θ⁻ᵈによる重み除去。中心直線の生成元、零Poisson、全h、層別公式との一致は未主張 |
| `prop:pg-equivariant-global-centering-obstruction` | m>=1、全f・η・hに依存しても全零h切断近傍のG共変な補空間選択Bは存在しない。U商は非自明torsorかつ非アフィン代数空間 | Stiefel開の左逆R(A)A=I₃、余次元m+1の境界とA=0での矛盾。gradient正則列による自由性、U変換則を保つLevi平均、アフィン底の加法群torsor消滅。中心元そのものの不存在とは区別 |
| `rem:pg-cmr-nodal-comparison` | CMR既知のγ=0中心公式を節点Jacobian関係へ移し、t=0で正則かつ古典剰余fの中心元を得る | accepted v2の式(4.38)–(4.39)、別の同変左逆、q=p/s等の係数対応、Q=s⁵Ω_CMR/(6t)+κ、交換差−6A₃ℓ₃t³と純中心補正。既知の存在・公式と本稿の相対適用を区別 |
| `thm:pg-quantization`（`algebraic_quantization.tex`）、`thm:pg-ad-all-poisson` | 全Poisson構造について原点を含むZariski開上のAS-regular ambientと中心正則三次商 | 中心三次配分、PBW、Koszul tensor、中心元の正則性、AS-Gorenstein change of rings |
| `thm:pg-all-dimensions`、`cor:pg-ad-whole-pencil`、`prop:pg-ad-intrinsic-hessian` | 各純active三次が滑らかな場合は独立多変数底と短い多項式中心公式 | 係数環上の自由性、全パラメータでの多項式中心性、交差補正がないこと |
| `thm:pg-fermat-relative-count`、`fermat_relative_poisson_components.tex` | Fermat固定space、固定stack、全cubic相対stackの位相的既約成分 | Hessianによるブロック復元、有限群軌道、被約rank層、同時スカラー作用、閉包の非包含 |
| `ne:main`、`nonelliptic_poisson_components.tex` | 二つの固定された滑らかなcubic fivefoldに2次元の非楕円Poisson成分 | 現行コードによる整数証明書・直接Schouten線形化の検証結果、接空間から成分性への議論 |
| `thm:pg-ambient-recovery-general`、`thm:pg-ambient-recovery-polarized`、`ambient_recovery_general.tex` | 二次包絡と三次核。圏からの復元には本文のnoetherian・AS-Gorenstein条件 | 低次数積、section algebra、飽和のExt消滅 |
| `prop:pg-ambient-even`、`cor:pg-ambient-derived-threefold` | C上、二変数中心、中心上自由性、左右noetherian性、所定のSerre関手を仮定 | conicからの中心復元、局所化と交叉、次数の再設定、必要仮定の明示 |

複数ブロックを含む全階数のモジュライへの一般の同変降下、3|Nの全rank2層での別の降下、
粗モジュライの構成、Poissonスキームの非被約構造の完全な決定、
全閉パラメータでのqgr滑らかさ、特殊点を含む相対残余圏同値はここでの定理ではない。
論文Bの一変数一般点での全coherent残余圏復元（同値は有限拡大後）とは区別する。

## 誤りを避けるための構造上の要点

### 相対Poisson空間

`poisson_moduli_stacks.tex` の相対Poisson空間は、
$\mathcal E=\Lambda^3V\otimes\mathcal O_{U_N}(-1)$ の全空間に閉埋め込みされる。
底 $U_N$ への忘却射自体は有限型アフィン射であり、一般には閉埋め込みではない。
固定F上にはPoisson構造を動かす非自明なファイバーがある。

相対Koszul複体は、被約底上で各次数のコホモロジー次元が一定であることから局所分裂し、任意底変更と両立する。
普遍三次式をアフィン錐で扱うときは $(F,P)\mapsto(aF,a^{-1}P)$ で割る必要がある。
被約rank層は $GL_N\times^{\operatorname{Stab}(P_k)}\mathcal F_{N,k}^{sm}$ から得られ、
射影化のための $\mathbb G_m$ が次元を1下げる。スタビライザーの次元は $8k+3km+m^2$。
この規約を落とすと相対次元と成分数の議論が不正確になる。
詳細は `notes/fermat_relative_poisson_components.md`。

### 全supportの中心核と代数的持上げ

S=T_smooth×C₃^×上でK₀=OF⊕Sym³(V/W_P)*である。
Gr(3,N)上の全整数twistのH¹消滅から、Fは局所定階数核の全h冪厚化へ整合的に持ち上がる。
ここで得る形式中心元の各Weyl係数は、Stiefel開の補集合の余次元N−2>=2と
SL3-torsorの関数降下により、有限生成環A_N=Γ(T_smooth,O)⊗C[Mat_(N,3)]^(SL3)に属する。
錐の射影正規性や全supportにわたる補空間選択は仮定しない。

有限次数三・四のWeyl同型が成立する不変principal開D(q)、q mod h=1上で、
R=A_N[h,q⁻¹]、K=ker MとするとKは有限R加群である。
完備化の完全性からKhat=ker Mhat、Khat/hKhat≅K/hKであり、
形式中心元の剰余類をKの元で代表してΩ mod h=Fを得る。
K/hK→(自由加群)/hの単射性を使う議論ではなく、包含と剰余写像の可換性を用いる。
指定した形式級数全体との一致は必要ない。P=0での核の階数跳躍もこの有限加群の操作を妨げない。
全次数PBWと正則中心商は、別に既存の局所PBW/AS開へ制限して得る。

全fに依存する中心調整Bを仮定すると、固定smooth FをStiefel開へ引き戻して
R(A)A=I₃を満たす正則左逆が得られる。その全行列空間への延長はA=0で矛盾する。
U作用が自由でも商がアフィンとは限らず、本件では非自明U-torsorの商Yは非アフィンである。
したがって自由商上のアフィン平均化に置き換える方法も使えない。
この障害は中心核を直接扱う上の存在証明とは両立する。

中心スカラーK_sc={(cI,c⁻³)}を除いた商は全rank2被約Poisson層である。
gcd(N,3)=1の指標θ=(det L)^rλ^s、Nr−3s=1により次数重みを除く。
降下する中心三次直線の一つの大域生成元が底上に存在するとは限らない。
N=5の底の次元17は固定h≠0の非可換同型類像の次元ではない。
各型で先に選んだ明示式との一致、特にg=0の全h公式sym(F)との一致は保証していない。

### 特異制限の軌道と中心スカラーの除去

節点・尖点では、方程式scaleを含む安定化群に同変な明示左逆を標準形で作る。
σ_{(M,λ)g_*}=Mσ_*ρ₂(M,λ)⁻¹は右安定化群作用に不変なので、
軌道L/H上の正則な写像へ降りる。各gの標準形への座標変換を大域的に選ぶ必要はない。
このσを中心調整に使うと、各係数層の全零切断を含む不変principal開が得られる。
各軌道での分裂と、不可約三次式全域での単一の分裂は区別する。
後者は可約式の錐の余次元2による正則関数の延長とδ_0=0に反する。

各gの唯一の特異点は、軌道上の正則な同変射O_γ→P(W)を与える。
そのtautological直線ℓの点の順方向の写像はMだが、代数のΦと同じ向きの引戻しデータはM⁻¹である。
従ってℓの中心スカラー重みは−1であり、A_d⊗ℓ^d、J⊗ℓ³、B_d⊗ℓ^dの重みが零になる。
重み+1の双対線束をLと書くなら同じ補正はA_d⊗L⁻ᵈである。
積と中心イデアルも整合して降りるため、代数そのものの降下である。
重み一の線束にframeを付けたスタックが底とfppf局所的に同型となる直接証明から、gerbeも中立となる。
この方法は群の指標による分裂と異なり、mに合同条件を課さない。

support平面とXの交わりが節点・尖点曲線である条件は、support平面そのものがXに含まれる零制限条件とは異なる。
節点・尖点層の余次元1・2および底の次元16・15は、固定したh≠0での非可換同型類の像の次元ではない。
これら層別の式の全hへの延長、全supportの別の選択との一致、
降下後の大域中心生成元の存在は主張しない。
接線とconicの軌道でのδの同変非分裂は `notes/universal_casimir.md` §2(VIII) に独立な障害として記録する。
これらの障害は中心調整の方法に関するものであり、
中心核を直接扱う全supportのH_N共変中心元定理とは両立する。

### 中心二変数とambient復元

$S=\mathbf C[u,v]$、$D=S^{(2)}=\mathbf C[a,b,c]/(ac-b^2)$ とする。
$D_1$ のconicのgraded自己同型は $GL_2/\{\pm1\}$ から来る。
偶数Veroneseを元の次数の2倍に戻してからSとtensorし、uとvの局所化を取る。
$S[u^{-1}]=D[(u^2)^{-1}]\oplus uD[(u^2)^{-1}]$ と奇数部分の記述、
S自由基底に関する交叉から元の代数を回復する。
このため商代数自身のS自由性が必要である。

**ambientのPBW性だけでは商のS自由性は従わない。** 例えば $A/(u^3)$ はS-torsionを持つ。
active filtrationに関して中心三次元Gの最高記号 $g_3$ が正則で、
$\operatorname{gr}A=S_{f_3}\otimes S$ なら
$\operatorname{gr}(A/(G))=(S_{f_3}/(g_3))\otimes S$ となり、斉次基底の持上げでS自由性を得る。
これは `eq:pg-ambient-quotient-symbol` の十分条件である。
導来復元の系にはAの左右noetherian性を明示し、BのAS-Gorenstein injective dimension 4からsection algebraを回復する。

### 正規形とBondalの下界

$K(P)$ の基点自由性からVとsupport Wの両方に非退化なBを取るには、二つの非空開集合の交叉を使う。
可解根基の作用が既約加群上スカラーとなるだけでは零とはいえず、$W=[W,W]$ によるtrace零性を併用する。
最高根が単純根ではないことは、隣接単純根のroot stringを使って正当化する。

半単純性を得た後の二次形式の核はDerdzinski--Gal Theorem Bの直接の帰結でもある。
本稿の追加の還元は、Hessianの基点自由性から可解根基を排除する段階である。
Cartan三形式によるブロックの復元も同論文Lemma 7.1(a)で述べられるが、
公開PDFの補助主張(e)の最小像の説明にはsl₂⊕sl₂の混合rank 1+2による反例がある。
これはLemma 7.1(a)の結論への反例ではなく、本稿は`ne:blocks`の独立証明を用いる。
詳細と一次資料の所在は `notes/bondal_cubic.md` に整理する。

rank 2rの二重ベクトルを一次元Lで割ったときのrankは、
$L\subset\operatorname{im}b$ なら2r-2、それ以外なら2rである。
この線形代数補題を明示して、join上でEuler線が像に入ることとBondalのrank評価を結ぶ。
本文の一般証明と一具体例の外積計算は別である。詳細は `notes/bondal_cubic.md`。

### 分離型三次四様体、Hessian判定と持上げ

Bricalli–Favale–Pirolaの刊行Theorem 3.4は、滑らかなcubicの(k+1,n−k)分離型と、ambient Hessian階数≤k+1軌跡内のP^kの存在を同値にする。n=5,k=2を本稿の正規形に合わせるとrank4 Poissonの存在を方程式Fだけから判定できる。平面はX内ではなくambient P⁵内にある。Theorem AのHessian可約性・非正規性の条件は全サイズの分離を含むため、(3,3)条件とは区別する。

反例 `ex:pg-reducible-hessian-no-rank-four` の定数symmetrizerはdiag(a,b,cI₄)である。その冪等元の階数は0,1,2,4,5,6だけなので、座標に依存しない(3,3)分解の障害になる。E_Fの条件はHessianの全係数に対する恒等式であり、一点の行列に関する自己共役性ではない。既知Hessian判定そのものの新規性は主張しない。

F=f(x)+g(y)ではD=V(f,g)が正規な(3,3)完全交叉で、
特異集合は互いに素な楕円曲線E_f、E_gとなる。
E_f近傍でπ=A∂w∧E_v+q_g、(1/2)π²=3Agν⁻¹、
modular場はE_f上で−3A∂w≠0である。
Poisson零点スキームは被約だが、Dの特異スキームは各曲線の横断方向に長さ8を持つ。
Pym arXiv:1507.05668v1 Definition 4.2の全条件を満たす。

同版Theorem 1.3のcubic非存在、Proposition 5.7の非正規性とは両立しない。
Lemma 5.5の証明が使うH¹(I_C)=0はC=E_f⊔E_gでは誤りで、H¹(I_C)=H¹(I_C²)=Cとなる。
g|_Xのambient liftはλf+(1+λ)gで、E_fでの三重消滅はλ=0、E_gではλ=−1を要求する。
IをP⁵内、JをX内のCのイデアルとすると、
0→I²→I³(3)→i_*J³(3)→0の境界類δ(g|_X)は非零で、H¹(I²)を生成する。
比較対象はこのv1に限定する。刊行版の書誌とOxford accepted manuscript登録は確認したが、
刊行本文・accepted本文は取得できず、訂正状況の確定も未了である。
独立な反例証明と一般階数四の分類は本文に保持し、未取得資料の内容を推測しない。

一般次数の持上げ命題では、全連結成分が正次元なら
余法束→Ω¹_P|C→O_C(-1)^{N+1}の部分束埋込みの対称冪から、全j>=1でH⁰(I^j/I^{j+1})=0となる。
全ての厚みの大域関数は成分定数だけなので、任意r>=2でH¹(I^{r−1})=C^{π₀(C)}/Cである。
0→I^{r−1}→I^r(d)→i_*J^r(d)→0によりr重消失の持上げ障害を得る。
ここでd=deg Xに固定することが重要であり、次数eなら障害群はH¹(I^{r−1}(e−d))となる。
正次元という仮定は不可欠な証明入力であり、点を含む中心へ無条件に拡張しない。
独立命題は文献比較から切り離され、連結時の存在・一意性も明示する。

確認した版の番号・頁は、Theorem 1.3 p.4、Definition 4.2 p.17、
Lemma 5.5 pp.28–29、Proposition 5.7 p.30である。
2026-11-14の確認ではCambridgeの公式PDF経路はabstractページへ移り、
Oxfordの2016年受理原稿の本文は取得できなかった。訂正文の不存在は結論しない。
公開v1: https://arxiv.org/pdf/1507.05668v1
刊行書誌: https://doi.org/10.1112/S0010437X16008174
受理原稿登録: https://ora.ox.ac.uk/objects/uuid:a457621f-f733-41b0-99c7-fa475b8e807e


## 代数的中心元の証明の依存

1. `lem:pg-det-gradient-coprime`：全体fの滑らかさから $\gcd(f_x,f_y,f_z)=1$。
   共通因子と中心偏微分を同時に消す非零点がKrullの高さ定理から生じれば、全勾配の零点となって矛盾する。
2. `lem:pg-det-classical-kernel`：三次古典Casimirは $\mathbf C f+\mathbf C[u]_3$。
   分数体上の比例係数はgcd=1により多項式で、斉次次数から定数となる。
3. `lem:pg-det-universal-rank`：有限表示の次数別行列は被約な係数底上で一定階数を持ち、局所自由な商を与える。
   各固定fのh曲線上で、滑らかなactive制限に対するHesse中心公式から小行列式の消滅を得る。
   その後fを動かして普遍恒等式とする。Hesse座標の代数的な同時選択は仮定しない。
4. `thm:pg-universal-determinant`：古典rankの非零小行列を局所化し、Cramer法で $\Omega_0=f$ を規格化する。
   語の反転と $h\mapsto-h$ により係数は $h^2$ の有理関数となり、分母は原点で消えない。
5. `thm:pg-det-global-coefficient-lift`：固定した全係数空間の零切断全体を含む偶principal開へ縮める。
   割った交換子行列をτ=h²へ降ろし、factorial係数環のPic=0と特殊化の単元補正で全係数に正則な中心元を得る。
   規格化変更のaffine遷移は同じ中心イデアルを保証しない。実例と同変降下の条件は `notes/universal_casimir.md`。
6. `thm:pg-equivariant-levi-center`、`thm:pg-equivariant-parabolic-center`：
   affine底上でReynolds平均を定義開・中心元・方向微分の左逆へ適用する。
   滑らかなgではこの左逆を、節点・尖点では`lem:pg-equivariant-singular-retractions`の軌道上の左逆を用いる。
   混合二次項からB_fを作り、B_f'=(MB_f−C)N^-1を用いて全G同変に戻す。
   純中心係数の固定は全平行移動との同変性に一般には両立しないため、この規格化を外す。
   g=0は`thm:pg-equivariant-zero-center`のPBW対称化で全tの全G共変性を別途証明する。
   G_0選択では指定閉部分を(t=0)∪(g=0)として、この標準元への一致も保てる。
   節点・尖点層のモジュライ降下は、特異点直線による重み補正を別途用いる。
   同変な中心元の選択、gerbe上の族、底のPoisson層への代数の降下はそれぞれ区別する。
7. `lem:pg-central-splitting-smooth`：純中心三次を各ブロックへ配分する。
   $u=0$ は全体Xの滑らかさ、$u\ne0$ は基点自由な線形系のBertiniを用いる。
   射影線形系のうち元のブロックの係数が非零のchartで係数を1に規格化し、必要なアフィン配分空間に戻る。
8. `thm:pg-quantization`、`thm:pg-ad-all-poisson`：各中心元の和、共有中心上のPBW/Koszul性、
   一つのactive blockのfiltrationによる正則性から、全Poisson構造と固定正規形のpencilを量子化する。
   非可換domainのtensor積が常にdomainである、という一般には誤る命題は使わない。
9. `thm:pg-intrinsic-rank-two-center`：全supportの古典核のH¹消滅から形式持上げを行う。
   Stiefel開・Hilbert有限生成・有限Weyl行列を介し、Noetherian完備化の完全性で
   同じ古典剰余の代数的中心元を得てH_Nで平均する。外部formalityを存在入力には用いない。
   形式中心元存在自体と相対・還元群への対応はEG Proposition 8.1.1(i)に既にある。
10. `cor:pg-intrinsic-rank-two-descent`：全rank2被約Poisson層の商表示と、
    gcd(N,3)=1の重み一指標による次数補正を用いる。
    中心線の選択・gerbe上の族・rigidification後の代数の降下を区別する。

任意の滑らかなactive制限に対する短い多項式公式はHesse標準形への帰着で得る。零制限はPBW対称化が全tで適用でき、非零の特異な一般制限はCramer構成で扱う。個別の非零特異例には別途明示式がある。
普遍Hesse証明書は独立混合係数を保持した有理関数体上の恒等式であり、数値特殊化による推測ではない。
内在的な二次補正は $H(P,F)=\frac16\sum P^{ijk}P^{abc}F_{ia}F_{jb}F_{kc}$、
正規形では $\sum_s\lambda_s^2\det\operatorname{Hess}_{x_s}(f_s)$。
四次補正を一つの座標不変式と断定しない。
詳しい公式、例、Dolgushevによる代替形式ルートの制約は `notes/universal_casimir.md` を参照する。

## 一次文献と本稿の位置づけ

| 文献 | 確認した所在・適用範囲 | 本稿との関係 |
| --- | --- | --- |
| Bondal, MPIM 93-67 (1993) | §4、印刷pp.11–12の無番号Lemma/Theorem | 射影Poissonの一意な斉次divergence-free持上げは既知。本稿はcubic上のJacobiatorの延長へ適用 |
| Derdzinski–Gal, DOI 10.1007/s12188-013-0085-z、arXiv:1304.2801 | 著者PDF (1.4) p.2、Theorem B p.3・§5、Lemma 7.1(a) p.10 | 式の符号・係数まで同じ核計算。半単純性への還元は別。ブロック復元は本稿の独立証明を使用 |
| Bricalli–Favale–Pirola, Forum Math. Sigma 13 (2025), e80, DOI 10.1017/fms.2025.36、arXiv:2406.12024 | 刊行Theorem A p.2、Theorem B p.3、Theorem 3.4 p.10・証明pp.11–12 | Hessian階数軌跡による分離型判定は既知。本稿はn=5,k=2をrank4 Poisson存在に結び付ける |
| Pym, DOI 10.1112/S0010437X16008174、arXiv:1507.05668v1 | 確認したv1 Definition 4.2、Theorem 1.3、Lemma 5.5、Prop.5.7 | 分離型例との不整合と非連結曲線の持上げ障害。刊行版本文・訂正状況は未確認 |
| Loray--Pereira--Touzet, arXiv:1112.3871v3 | Theorems 7.1, 9.1 | 三次三様体の分類は既知。本稿は高次元の複数Jacobianブロックを扱う |
| Mayanskiy, arXiv:1303.5916 | Theorem 1 | GrassmannスキームのJacobi方程式による記述とPoisson cohomology |
| Gualtieri--Pym, DOI 10.1112/plms/pds090 | Theorem 7.13 | Fano四次元のBondal予想は既知 |
| Druel--Pereira--Pym--Touzet, arXiv:2606.03424v1 | Theorem 1.2、Corollary 1.3、著者PDF | 奇数次元のsubmaximal退化軌跡とFano五次元。本稿はcubicというクラスで全次元・全rank |
| Darío Martín Aza, arXiv:2604.07217v1 | Theorem 1.3, p.2、証明p.10 | 隣接退化軌跡の真包含の下での選言。全Bondal予想の証明とは扱わない |
| Etingof, MIT 2024 lecture notes | Cor.13.7–13.8 p.75、Prop.16.9 p.88、Def.21.13/Lem.21.14 p.114、Thm.25.17 p.137、§32.2 p.173 | PBW対称化の随伴同変性、可解根基、最高ウェイト、最高根の既知入力 |
| Mori--Smith, Math. Z. 287 (2017), 215--241, DOI 10.1007/s00209-016-1824-5 | 本文確認はarXiv:1502.07403v2。Thm.1.4 p.5、Cor.2.7 p.11/2.9 p.12、Thm.4.2 pp.16–17、Lemma 7.1/Thm.7.2 pp.23--24 | standard性、AS-regular/3-CY、滑らかな平面三次で全パラメータの判定、point curve |
| Berger--Taillefer, JNCG 1 (2007), 241--270, DOI 10.4171/JNCG/6 | 刊行PDFのThm.1.1(i) p.242、Thm.3.1 p.246、Thm.3.6 p.251 | 低次数potentialからのPBW変形。(ii)の逆向き分類の追加条件は使わない |
| Le Bruyn--Smith--Van den Bergh, Math. Z. 222 (1996), 171--212 | 著者PDF、Thm.2.6/Cor.2.7、Thm.3.1.3 | 中心正則拡大。Fermatブロックのパラメータ代入を本文で明示 |
| Smith--Tate; De Laet--Le Bruyn | 後者arXiv:1405.1158v1 §2 p.3 | 純Sklyanin中心公式は既知。本稿は固定係数環の無極な規格化、普遍恒等式、Cramer構成を扱う。表示の誤植注意は中心ノートに記載 |
| Etingof--Ginzburg, JEMS 12 (2010), 1371–1416, DOI 10.4171/JEMS/235 | 刊行Thm.3.3.2(ii) p.1385、Prop.8.1.1(i) p.1407・証明pp.1407–1408、§8.3 pp.1410–1411、§9 p.1414 | 一ブロックの中心元存在・特殊化・Rains公式に加え、指定古典剰余を持つ形式中心と相対・還元群に対応した形式性も既知。本稿の追加は動く全support上の同時代数的選択と被約層への降下 |
| Chekhov–Mazzocco–Rubtsov, Adv. Math. 376 (2021), 107442, DOI 10.1016/j.aim.2020.107442 | 本文確認はaccepted arXiv:1905.02772v2。式(4.38) p.21、Lemma 4.6・式(4.39) p.22、Table 5 p.41 | γ=0の場合の節点型中心元は既知。本稿は一般混合二次項からの移送、対称Jacobian関係への係数対応、t=0の規格化と安定化群共変な純中心補正を明示 |
| Guo–Lu–Sharpe, arXiv:1605.01410v2 | [本文](https://arxiv.org/pdf/1605.01410v2)、§2.2 Thm.2.3 pp.5–6、Thm.2.4の証明 | Grassmann多様体上のBWBの重み規約と負の最高重みを確認。全整数twistのH¹消滅への適用は本稿で計算 |
| Lurie, *A proof of the Borel–Weil–Bott theorem* | [著者公開ノート](https://www.math.harvard.edu/~lurie/papers/bwb.pdf)、Thm.5と証明 p.3。PDF内に刊行年の記載なし | BWB一般定理の確認に使用。Bott原論文・Weyman原書を直接読了したとはしない |
| Derksen, Advances in Mathematics 141 (1999), 366–384 | [著者公開刊行PDF](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.4.pdf)、Thm.2.1 pp.368–369、Reynoldsの性質p.369 | Hilbert有限生成とstable部分加群を保つReynolds射影は既知。SL3不変環のNoetherian性、不変開・有限中心核の平均に適用 |
| Stacks Project [00MA](https://stacks.math.columbia.edu/tag/00MA)・[00MB](https://stacks.math.columbia.edu/tag/00MB) | Lemmas 10.97.1–10.97.2 | Noetherian有限加群の完備化の完全性・テンソル積との一致。形式中心の古典剰余を有限核から代数的に持ち上げる |
| Stacks Project [06PH](https://stacks.math.columbia.edu/tag/06PH)・[03OY](https://stacks.math.columbia.edu/tag/03OY) | Lemma 80.11.7、§59.22のThm.59.22.4 | flat・局所有限表示群の自由作用の代数空間商とfppf torsor、準連接層のfppf/Zariskiコホモロジー比較。U商の非アフィン性へ適用 |
| Milne, *Algebraic Groups*, CUP 2022 | [著者PDF](https://www.jmilne.org/math/Books/iAG2022.pdf)、Props.7.12, 7.17 pp.142–143 | 軌道L/Hと忠実平坦な軌道写像は既知。標準形での同変左逆を軌道上へ正則に移送するために用い、軌道のaffine性を追加仮定しない |
| Bergh–Schnürer, Doc. Math. 26 (2021), 1465–1500, DOI 10.4171/DM/846 | [刊行PDF](https://ems.press/content/serial-article-files/26626?nt=1)、Prop.4.10 p.1487 | gerbe上の重み零の準連接層の降下は既知。次数付き代数・積・中心イデアルへ適用。重み一の直線によるgerbe中立化は本文のframeを用いる直接証明であり、同命題へ誤帰属しない |
| Dolgushev, Selecta Math. 14 (2009), 199--228, DOI 10.1007/s00029-008-0062-z | 本文確認はarXiv:math/0612288v3 Prop.1 p.9、Thm.3 pp.15--16 | 条件は全形式Poisson classのunimodularity。本稿の代数化の証明には用いない |
| Fu--Hwang, arXiv:1608.00846v2 | Lemma 4.1 p.13：完全交叉Zで1<=r<=dim Z-1、p<=rならH^0(Ω_Z^r(p))=0 | Brückmann型消滅の明示的定理文と適用条件を確認 |
| SGA 2 XII Cor.3.7、Stacks Tags 06FI/0BCH/06PD/06WT、Artin--Zhang | Picard群、商stack、UFDのPic=0、gerbe判定、同変準連接層の降下、section algebra | モジュライ・係数空間上の中心元・偏極付き復元の既知の一般原理 |

Hesse表示の混合二次項Axy+Byz+Czxは、t可逆なら
x=X−B/t、y=Y−C/t、z=Z−A/tで消える。残る低次項は各一変数の多項式で、
q=(1+ht/2)/(1−ht/2)、μ=h/(1−ht/2)によりEG§9の交換関係へ移る。
全残余係数と自由語の関係は `rem:pg-hesse-eg-translation` と
`computations/verify_hesse_translation.py` に明示した。
この座標変換がt=0で使えないことから、全ての座標変換による既知公式への帰着不能を結論しない。
混合係数を含むことだけを初出の根拠にせず、指定した係数環・古典極限・正則性を比較する。
EG刊行本文: https://ems.press/content/serial-article-files/31746

EG Proposition 8.1.1(i), p.1407は、正の重みa,b,c、d=a+b+cについて
Φ=xyz−yxz+Σ_(j≥1)h^jΦ_j、deg Φ_j≤dという三生成元potentialに、
古典剰余(Φ₁)^abを持つ次数d以下の形式中心元を与える。
孤立特異点は同命題(ii),(iii)の追加仮定であり、(i)には不要である。
証明pp.1407–1408はR=C[u]を基底とする相対構成を用い、
還元群作用に対応するKontsevichの形式性とその相対版も明記している。
従って指定古典剰余の形式中心元存在、相対・同変な形式構成、
形式解から有限条件を取り出す一般原理だけを本稿の新規性とはしない。
現行稿では、全smooth Fと全非零supportの係数底に一つの代数的中心元を同時に選び、
全H_N共変性と被約Poisson層への代数族の降下まで制御する主張を区別する。

CMRとの具体対応は、f°=x³+y³+xyz+ΣA_i x_i²+Σℓ_i x_i+κに対し、
p=1+t/2、s=1−t/2、q_CMR=p/s、α=β=3t/s、γ=0、
(a₁,b₁,c₁)=−2t(A₁,A₂,A₃)/s、(a₂,b₂,c₂)=−t(ℓ₁,ℓ₂,ℓ₃)/sである。
Q=s⁵Ω_CMR/(6t)+κの係数はt=0で正則、古典極限はf°となり、
x,y交換とt↦−tの差−6A₃ℓ₃t³をQhat=Q−3A₃ℓ₃t³で補正する。
任意の二次混合項への移送を含む詳細は `rem:pg-cmr-nodal-comparison` と
`notes/universal_casimir.md` §2(VIII)にある。
CMRの刊行書誌とaccepted versionの本文確認を区別し、刊行レイアウトを照合したとはしない。

文献URL・DOIと現在の引用キーは専用参考文献にある。
Brückmannの1976年論文はMath. Nachr.71,203--210、DOI 10.1002/mana.19760710116で書誌を確認した。
1977年続編はFu--Hwangの書誌でMath. Nachr.77,307--318。
**原証明（1976年Satz 3、1977年Satz 6）は未取得であり、読了と報告しない。**
必要な低twist範囲には本文`lem:ci-low-twist-vanishing`で独立証明を与えたので、
現行の完全交叉の存在判定は未取得の原証明に依存しない。
高次元の正規形・Bondalのjoin証明・相対成分数・量子化の包括的結論と同一の先行定理は調査範囲で確認できていないが、初出は未確定である。
節点・尖点層についても、軌道への移送と重み零降下の原理自体は既知として扱う。
本稿の明示的な左逆、係数族の中心調整、特異点直線を用いた中心商族の下降という包括的な適用の初出は未確定である。
全supportのBWB計算・有限核の完備化・還元的平均を結んだ同時代数的選択についても、
一般原理と本稿の適用を区別し、包括的な初出は未確定とする。
刊行書誌を確認したことと、その刊行版の定理番号・証明全文を再照合したことも区別する。

## 実行済みの厳密計算と限界

今回の新しい実行対象は `verify_cmr_nodal_center.py` の一本であり、PASSした。
出力 `build/verify_cmr_nodal_center.json` はSymPy 1.14.0での独立QQ係数の厳密計算を記録する。
記録されたコードSHA-256
`f3ca63fcf5e5f66ed6d7aad45c2c853bd162c86074980a8b1e915ee998d3a503`は現行ファイルと一致した。
節点・尖点の中心調整、零制限、Hesse等を含む他の十三件は、
既存の実行証拠とコード・証明書のハッシュ照合を保持し、今回の再実行とは区別する。
添付査読報告の独立実装そのものは添付されておらず、再実行したとは扱わない。
実行対象、以前の検算の適用可能性、現在の入力ハッシュは `validation_paper_a.json` に集約する。

| スクリプト（computations/） | 結果と範囲 |
| --- | --- |
| `verify_cmr_nodal_center.py --json` | 本改訂でPASS。独立QQ係数でCMR γ=0関係の唯一のzyx重なり、三中心交換子、Jacobian関係への係数対応、Qのt=0正則性・古典極限、交換差とQhatの純中心補正、スカラー・μ₃重みを検算。sp≠0での計算でありt=±2のPBW・平坦性、Weyl偶性、安定化群の完全分類・軌道移送・モジュライ降下は対象外 |
| `verify_singular_orbit_centering.py --json` | 実施済み結果を引継ぎ、今回未再実行。独立10係数と3並進係数、nodeの全生成子・cuspの対角torusでσδ=id、B_fと中心調整式の共変性を検算。接線とconicでは左逆・Lie同変性の線形系のrank18/拡大rank19、torus制限後rank4/拡大rank5。二つの拡張例の勾配イデアルへの純冪の所属をQQ Groebnerで確認。安定化群の完全分類、一般GLの軌道移送、quantum中心性・モジュライ降下の計算機証明ではない |
| `verify_zero_restriction_center.py --json` | 実施済み結果を引継ぎ、今回未再実行。QQ上の独立10係数とt、独立3並進係数でzyxの重なり、全3中心交換子、関係式と中心元の並進共変性が恒等的に零。数値特殊化・t打切り・分母なし。一般線形変換・AS条件・幾何・降下の検算ではない |
| `verify_hessian_split_obstruction.py` | 実施済み結果を引継ぎ、今回未再実行。単一の具体例でHessian行列・行列式を照合。QQ上90方程式・36未知数のrank33、核dim3、冪等元の可能rank0,1,2,4,5,6。滑らかさ・一般分解判定・Poisson分類の証明ではない |
| `verify_hesse_translation.py` | 実施済み結果を引継ぎ、今回未再実行。独立全係数で平行移動後の三次式を定数項まで照合し、三つの交換関係を自由語の有理係数で照合。中心性・PBW性の検証ではない |
| `verify_equivariant_centering.py` | 実施済み結果を引継ぎ、今回未再実行。25混合係数を記号のまま保持。二組の座標変換で左逆、B_fの変換、中心調整した三次式、三つのJacobian括弧がPASS。Reynolds存在や全群定理の計算機証明ではない |
| `verify_split_cubic_fourfold.py` | 実施済み結果を引継ぎ、今回未再実行。分離型Fermat例のambient 20 Jacobi成分とCasimir、射影10括弧・10 Jacobi・接性、暗黙消去後の4 Jacobi、Pfaffian、modular場の二通りの計算がPASS |
| `verify_poisson_article_A.py` | 実施済み結果を引継ぎ、今回未再実行。滑らかな一具体例、56 Jacobi成分と56 Euler外積成分が厳密に零 |
| `verify_nonelliptic_components.py --direct` | 実施済み結果を引継ぎ、今回未再実行。nodal/cuspidal両例でHessian線形化と直接Schouten線形化のrank 33。保存した整数小行列証明書を照合 |
| `verify_poisson_stack_component_counts.py` | 実施済み結果を引継ぎ、今回未再実行。n=3,...,10の三種類の成分数、全8行一致 |
| `verify_universal_hesse_mixed_center.py` | 実施済み結果を引継ぎ、今回未再実行。339基底語、162関係倍数、rank 144。Q(h,t)上で独立な6混合係数を保持し、3交換子が恒等的に零 |
| `verify_cubic_casimir_jet.py` | 実施済み結果を引継ぎ、今回未再実行。20自由係数。x,y,z各交換子の125個の語・次数係数が零。有限jetの検算であり、任意次数の中心性を単独で証明しない |
| `verify_singular_cubic_classical_kernel.py` | 実施済み結果を引継ぎ、今回未再実行。active制限0の滑らかな例で378×56行列のrank 45、核次元11 |
| `verify_nonelliptic_quantization.py` | 実施済み結果を引継ぎ、今回未再実行。二つのmonic Diamond系と重なり、六普遍中心交換子、h=0極限、potential syzygy、分母範囲、二つのnegative control、17項Fermat恒等式がPASS。実行時の再計算は保存JSON全体と厳密一致 |

非楕円例の33次小行列式は nodal: $8916100448256=2^{24}3^{12}$、
cuspidal: $-4565043429507072=-2^{33}3^{12}$。
その非零性と既知の2次元pencilにより接空間次元2を得る。
元のPoissonスキームは有限型Cスキームなので、正則局所環から該当点での滑らかさを結論できる。

独立多ブロックの補助例・別のminor等のコードも保持しているが、
上表にない計算を今回再実行済みとは扱わない。
有限例のJacobi/rank検算は全次元正規形や成分定理の一般証明の代わりではない。
普遍係数での恒等式検証と有限例への特殊化を区別する。
BWB消滅、有限核の代数的持上げ、U商の非アフィン性とモジュライ降下は本文の一般証明であり、
上表の有限計算がこれらを形式検証したとはしない。

## 再現と残る課題

```sh
python3 scripts/check_layout.py
python3 scripts/build.py --only paper_a
python3 scripts/verify_bundle.py --only paper_a --require-pdfs
python3 computations/verify_cmr_nodal_center.py --json --output build/verify_cmr_nodal_center.json
python3 computations/verify_singular_orbit_centering.py --json
python3 computations/verify_zero_restriction_center.py --json
python3 computations/verify_equivariant_centering.py
python3 computations/verify_split_cubic_fourfold.py
python3 computations/verify_hesse_translation.py
python3 computations/verify_hessian_split_obstruction.py
python3 computations/verify_poisson_article_A.py
python3 computations/verify_nonelliptic_components.py --direct
python3 computations/verify_poisson_stack_component_counts.py
python3 computations/verify_universal_hesse_mixed_center.py
python3 computations/verify_cubic_casimir_jet.py
python3 computations/verify_singular_cubic_classical_kernel.py
python3 computations/verify_nonelliptic_quantization.py
```

大きな記号行列のスクリプトは一つずつ実行する。
組版の成功、PDF表示の確認、数学的証明の監査、遠隔保存は別々に記録する。
上の一覧は再現手順であり、全コマンドを本改訂で実行したという記録ではない。
A-v59の組版・参照検査・視覚確認は `validation_paper_a.json` に記録する。
bundle生成・整合性検証・Library保存は配布時にそれぞれ確認し、本文の検証状態と区別する。

優先課題は、Pym刊行本文・訂正状況の照合、包括的な結果の初出照合、
複数ブロックの分解・配分を忘れた同変構成、および3|Nの全rank2層での別の降下である。
階数二の任意の制限型を含む全supportのH_N共変な代数的中心元と、
gcd(N,3)=1の全被約層への降下は本文で証明した範囲として扱う。
次は `notes/universal_casimir.md` §3の中心核の射影束とdilatationから、
古典核の自然な線・純中心束のコホモロジー・ブロック置換を調べる。
全supportの選択と層別の明示式との一致、全hへの延長、短い共変多項式表示、
固定h≠0の非可換同型類像の次元は別に残る。
滑らか・節点・尖点の中心調整、g=0の全パラメータPBW中心元と、それに整合するG_0平均も保持する。
節点・尖点層では特異点直線により、mの合同条件なしでgerbeの中立性と零h近傍の次数付き代数の下降を得た。
滑らか・零の層ではgcd(m,3)=1の指標補正による降下を得ており、これらの層の3|mの場合は別の課題である。
不可約全域でのσの貼合せ、接線・conic軌道でのσの分裂、全fに依存する大域中心調整には障害がある。
自由なU商をアフィンと仮定する経路も使わない。全モジュライでのカテゴリーの降下はさらに区別する。
Brückmann原証明の入手は帰属の補充として残るが、本文の消滅証明の未解決箇所ではない。
相対残余圏と全閉パラメータの滑らかさは独立の研究課題として扱い、原稿Aの確立した結果の仮定へ曖昧に混ぜない。
公表価値は主要結果の正確さと既知結果との差から判断し、形式検証・外部査読・初出確定が済んだとは断定しない。

GitHub mainが正本。節目の保存に追加承諾は不要。現在の利用者指示に従い、現行版の研究継続用bundleもLibraryへ保存する。既存ファイルの削除は行わない。
