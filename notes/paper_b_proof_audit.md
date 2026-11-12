# 論文B：完備曲率付き比較と一般点可換復元

**2026-11-12 / B-v46。** 再開は `00_research_plan.md`。主定理は `papers/support/papers/reconstruction/general_dimension_recovery.tex`、形式比較の証明は `complete_curved_transport.tex`、局所比較は `three_object_window.tex`、基礎体降下は `generic_cubic_descent.tex`（同じディレクトリ）。

## 現在の結論と適用範囲

次数別有限自由な代数的中心三次対で、特殊ファイバーが多項式環と滑らかな三次式であるという入力から、局所比較(L)と完備形式比較(CF)を構成する。固定三対象への制限(CF_3)も結論となる。主定理にこれらを独立の追加仮定としては課さない。

この入力の一般点において、元の体K=C(h)上の滑らかな三次模型、有限拡大後のrotation・中心元由来周期付き全coherent残余圏同値、全n>=3での幾何学的一意性、BFKの生成段数上界2(n+2)(n+3)-1を得る。正則多変数局所基底の分数体にも同じ議論が通る。任意の抽象的nc cubic圏にこの表示があること、同値核のKへの降下、特殊点を含む代数的相対同値、全モジュライ上の接着は未証明。

本文の証明を構成し主要段階を点検したことと、原稿全体の全支持補題の独立再監査、計算機形式検証、外部査読、包括的新規性調査を区別する。今回の結論は指定された変形族の範囲でのものであり、「すべての非可換cubicの無条件分類」と呼ばない。

## 形式比較の論理と確認点

1. **曲率を入れる前に通常のformalityを使う**（`cft:lem:model`）。normalizedな全Hochschild cochainとpolydifferential cochainのHKR比較を、内部weightを保つbar/Koszul比較で行う。affine同変なKontsevich写像のweight零部分を使い、各Artin切断で既指定jetを保ってPoisson係数と一入力gaugeを持ち上げる。元の積がbidifferentialであることは不要。各斉次成分で極限を取ると、厳密なunital代数同型φ:A→(S⊗R,*π)を得る。
2. **中心元の逆像は有限行列で求める**（`cft:lem:center`）。C_π(f)=ΣU_(r+1)(f,π^r)/r! は三次式の有限自由加群上の1+O(m)であり、逆がある。W=C_π^{-1}φ(Ω)と置く。中心性と接写像のchain恒等式、vector場に対する最低次HKRの単射性から[π,W]=0をm進帰納で示す。ordinary curved Hochschild cohomologyとJacobian環を同一視する議論は使わない。
3. **三次の次数がPoisson項を消せる理由**（`cft:lem:primitive`）。勾配Koszulの係数次数ごとの完全性により、二次係数bivector πの原像は定数trivector Ξに一意に取れる。差の原像は次数−2を要求する。JacobiからD=[Ξ,π]もKoszul cycleとなり、その原像は次数−1を要求するためD=0。Casimir条件だけではこの最後の消滅は従わない。
4. **大きい曲率を冪零MC定理へ無断で入れない**（`cft:lem:arity`）。tの二重次数は(2,−3)、η=Ξ/t、α_s=−tW+(1−s)π。関数k個とbivectorの出力arityは2−2k、trivector一個を足すと3−2k。関数入力は高々一個、他の入力はmの倍数なので、mod m^(q+1)で全Taylor和が有限。L∞恒等式を有限和として適用し、∂_s b_s=[γ_s,b_s]を得る。γ_sのarityは1,3のみで単位入力に関してnormalized。
5. **実際のbar写像と逆写像**（`cft:lem:flow`）。非可換でs依存するγ_sの順序付き積分を用いる。mod m^(q+1)ではq因子で止まり、coalgebra性とF b_0=b_1 Fを微分方程式で確認する。逆も有限幾何級数。三入力をr回使うには少なくともm^rが掛かるため、F_(2r+1),H_(2r+1)∈m^r、偶数arityと零項は零。出力長ℓに対し入力長はℓ+2q以下なので、tensor長完備barにも各剰余で連続に作用する。
6. **冪零でないMF行列への代入**（`cft:thm:complete`）。Qがmの倍数または上三角であるとは仮定しない。各Artin商では対象像ΣF_r(Q,...,Q)と射の挿入公式がarity上界で有限。行列化したbar恒等式がMF方程式と全functor恒等式を与える。逆bar写像のtwistが実際の逆関手となる。固定cohomological/内部次数はtの冪とx次数を固定し、出力は有限自由加群内にあるので、m進極限が存在する。
7. **単位・shift・周期**。normalized flowはstrict unitを固定する。内部shiftは行列の次数ラベルを変えるだけで、R[t,t^{-1}]-多重線形性がtによる(3)≃[2]との整合を与える。任意の別のスカラー倍周期同型を保存するという主張ではない。三対象への制限は `cft:cor:CF3`。

「Artin同値が両立するから実際の完備関手がある」という宣言ではなく、同じ基礎行列上に関手・逆関手の収束する公式を構成した。一般点へは固定三対象のHomと高次積を先に構成してから局所化する。任意Laurent対象への無限Taylor和の評価は必要ない。

## 局所windowと一般点への接続

(L)の証明は `three_object_window.tex` に保持する。完備Homの摂動縮約から正則局所基底へproper性を降ろし、実際のdg section--windowのHom比較coneに導来Nakayamaを適用する。a=N−3、i=1−a、T_j=B(j)_{<i}の有限filtrationは、j=a,a+1,a+2に対してgr(T_j)=⊕_(r=0)^(j−a)B_r⊗R(j−r)。B_0=Rから三角的にK(a),K(a+1),K(a+2)を取り出し、三次周期性でK,K(1),K(2)へ移す。生成性を特殊ファイバーだけから持ち上げていない。

証明順序は、三対象window→完備曲率付き移送→固定Homの局所化→Eulerノルム2·3^(N−1)による非零性→代数閉包上のBFK生成→有限降下→coherent飽和→低Natの体拡大→勾配空間の積分によるG/K、である。

模型の方程式を元の体へ戻す際には、smooth proper性を先に得てから低Natの有限性と底変更を使う。低積の具体行列や(D)を一般存在の前提に戻さない。λ=1の明示多項式を復元先に指定するには(D)を別途照合する。従来の全Artin・相対・低jet・point scheme・Stevenson/regradingの有効な支持節は保持する。

## 一次変形の直接証明と接空間の位置付け

`first_order_poisson_kernel.tex` の `fpk:thm:infinitesimal` は全次数の完備曲率移送とは独立の双対数環での証明。一般の次数付き連結flat一次変形をHKRで多重微分の二次係数bivector πに正規化できる。中心性は[π,F]=0を与え、滑らかなcubicの勾配Koszul複体が唯一の定数trivector Ξを与える。η=ε HKR(Ξ)/t はarity3のunital curved gaugeで、実際のbar写像にはF1=Id,F3=ηのみが現れ、逆はF3=-η。Qがεの倍数でなくてもtwistingの評価は有限。HKR正規化の違いは線形導分T(F)なので、可換変形の一次係数は(S/J(F))_3に落ちる。Jacobianのdegree3次元はbinom(N+2,3)-N²：N=5で10、N=6で20。一般のPoisson一次変形はJacobiを満たす必要がなく、この一次消滅にはJacobi条件を使わない。二次以降の延長には[Ξ,π]を消すためのJacobi条件が必要。

nc-cubic2の17次元の非可換族から可換moduliへの微分を定義・計算していないので、7次元kernelと結論してはならない。特に可換Poisson零点の局所環はPlücker錐の頂点を含み、その錐自体の次元は7（Gr(2,5)の6次元に錐の1次元）だが、頂点のZariski接空間は全10次元。元の可換cubicの変形10次元と合わせると、局所モジュライの次元17に対し接空間20となる。従って可換点で「7次元だけ一次方向が見えなくなる」と言うのは不正確であり、今回直接消去した一次Poisson方向は10次元である。非零Poisson一般点の幾何学的7次元方向とは区別し、その接空間での圏論的微分の同定は未実施。現在言えるのは一次のMF変形が可換三次式のJacobian接空間へ因子化することのみ。これが既知の一般原理のどこまでの帰結かという初出調査も未完了。数値と可積分性だけで実際の変形functorの単射／全射を結論しない。

## 二次のPlücker障害の独立証明

`first_order_poisson_kernel.tex` の `fpk:prop:tangent-pair` は、全次数formalityを用いず、HKRの一次正規形・中心性・次数付き導分のgaugeにより `T^1_pair ≅ Λ³V ⊕ Jac(F)_3` を示す。N=5で10+10=20。続く `fpk:thm:plucker-obstruction` は、滑らかなFなら `[ι_dF Ξ,ι_dF Ξ]=0` iff Ξ decomposable を直接示し、さらにJacobiatorの全係数が生成する二次イデアルが、Gr(3,5)の五つのPlücker二次式のイデアルに一致することを証明する。非分解可能ΞのGL5標準形e012+e034のJacobi方程式が `F_0i F_j−F_0j F_i=0` に一致する。Eulerの式から `3F F_0i=2F_0 F_i` を導き、Fの滑らかさ・既約性に矛盾。Grassmannianの二次イデアルとPfaffian写像の全射性でスキーム論的な同一性を得る。

二次`結合積`の延長障害はHH³で `[π,π]/2`、従ってPlücker錐を切り出す。これは二次障害の計算であり、全中心対の高次形式変形関手をこの錐と同一視したわけではない。Poisson構造のGrassmannian記述は既知（Mayanskiy）であり、直接の障害表示の初出は未確認。計算確認はFermat F=Σx_i³/3 と混合F=Σx_i³/3+x0x1x2/7の二例でJacobi係数がそれぞれ20本と56本、二次式空間の階数はいずれも5、Plückerの五式を合わせても階数5。これは一般Fの証明の代用ではない。

## 可換点の圏論的Kodaira--Spencer写像の正確な核

`fpk:thm:categorical-tangent` は、双対数上の中心三次対をMFへ送る一次比較を、既存のArtin基底上のenhanced Orlov/windowと合成する。滑らかなcubic threefoldでは `H¹(T_X)=Jac(F)_3`。JLLZ Theorem 4.4(2) は `η:H¹(T_X)→HH²(Ku(X))` の同型を与えるため、中心三次対の20次元一次接空間から基礎dg圏へのKS写像は `(Ξ,[G])↦η([G])`、核は `Λ³C⁵` の10次元、像はHH²の10次元全体。Artin windowのenhancementと第一次数MF比較を使うため、単なる次元差の推測ではない。これはrotation付きのmoduli stackの全構造や非零Poisson一般点の核7を証明しない。

一次資料のJLLZ `https://ajacovskis.github.io/hochschild_only_2.pdf` Theorem 4.4(2)（印刷p.15、web PDF画像確認）でηが同型、HH² Ku(Y₃)=k¹⁰を確認。刊行誌は *J. Pure Appl. Algebra* 227 (2023), 107418、doi 10.1016/j.jpaa.2023.107418。元の定理は既知で、本研究の接空間列への組合せの新規性は未確認。

## 一次文献と新規性

Kontsevich, *Deformation quantization of Poisson manifolds*, LMP 66 (2003),157–216, arXiv:q-alg/9709040。著者最終稿 `https://www.ihes.fr/~maxim/TEXTS/DefQuant_final.pdf` のTheorem4.6（PDF p.17）、Section4.6.2とLemma4.11（p.22）、Theorem6.3・affine同変性（p.30）を本文とページ画像で確認した。Sections6.2–6.4のグラフ表示・arityも本文で確認。適用は曲率を入れる前のMC対応と、曲率経路に対する有限Taylor恒等式に分ける。

Căldăraru–Tu, *Curved A∞ algebras and Landau–Ginzburg models*, NYJM19 (2013),305–342、`https://nyjm.albany.edu/j/2013/19-16v.pdf`。Section2、Remark2.8、Theorem2.12の本文を確認した。webのPDFページ画像取得は失敗しており、画像確認とは記録しない。同文献のtwisted complex/MF記述は、今回必要な無限arity関手の完備収束まで自動的に保証する引用ではない。その部分は本稿で証明する。

局所windowのBurke–Stevenson、Chen、Crainicと、生成/TorelliのBFK、Lin–Zhangについては既存の文献位置を支持節に保持するが、今回は全てを再調査していない。一般理論そのものの新規性は主張せず、この組合せの初出・公表価値の包括的調査は未完了。

## 有効な障害・反例

**CasimirとJacobiは別。** F=Σ_(i=0)^4 x_i³/3、Ξ=∂_0∧∂_1∧∂_2+∂_0∧∂_3∧∂_4としπ=[Ξ,F]と置くと[π,F]=0だが、[Ξ,π]=4x_0∂_1∧∂_2∧∂_3∧∂_4≠0、[π,π]≠0。二回目のゲージ作用の消滅にはPoisson条件を必ず使う。

**特殊生成性だけの持上げは偽。** P¹上のcone(O(−1) --hs--> O)の例は有効。ここでは有限filtrationと、一般点の非零性・rotation軌道という追加構造を使う。

**基礎体上のformと幾何学的一意性は異なる。** C(h)上のΣx_i³とh x_1³+Σ_(i>1)x_i³は同じ勾配空間だがK上では射影非同型。Hessian超平面配置とh進付値による `gcd:ex:forms` を保持する。これは同値核の降下障害が非零である例とは主張しない。

**有限可積分性は圏同値を証明しない。** 低積からの模型抽出には先に幾何学的な圏同値の存在を使う。pure Poissonとcanonical中心元の場合、形式模型をFに取れるが、一般の中心元の選択や高次Poisson補正を一次項だけから決めてはならない。

## 次の課題

最優先は現在の定理の証明を別の経路から独立に監査すること。特にnormalized全Hochschild比較のweight零への制限、曲率入りグラフ恒等式の符号、三次周期比較、generic有限降下の同値核とcoherent飽和の接続を対象とする。新しい一般化を先に積み増さず、指定仮定の範囲での信頼性を高める。

その次に実際の非可換入力でV,U,μの有限表示を作りG/Kを有効化する。有限拡大の必要性・次数、同値核行列、特殊点を含む正則模型、全モジュライでの接着は未解決として分ける。Aの正規形・PBW/AS・全中心恒等式の監査も継続する。

## 実行した検算と組版

`computations/verify_first_order_curved_kernel.py` は5変数・6変数の明示的三次式と定数trivectorで、曲率挿入の8恒等式およびJacobian次数3の階数を厳密に検査する補助コード。一般のA∞関手やnc圏の計算証明ではない。

`python3 computations/verify_complete_curved_transport.py --output build/complete_curved_transport_checks.json` を実行。5/7変数のSchouten恒等式と定数trivector contractionのrank10/35、上のnegative controlを確認。tensor長9・パラメータ次数4の非自律・非可換coalgebra flowで10本の逆行列係数恒等式、2750本のcoproduct係数恒等式、odd arity/位数評価、冪零でない対象変数への両側逆代入を厳密検証した。

これらは有限代数・組合せの検算であり、Kontsevichグラフ積分、非可換MFの実際のHom、高次積、全圏同値の計算機検証ではない。以前のwindow・勾配積分コードは保持するが今回は再実行していない。

`latexmk papers/support/papers/complete_curved_transport.tex` で5頁の日本語証明抜粋を再生成する。本文外参照はラベル名で表示する。今回の抜粋はLuaLaTeXで組版・表示確認した。論文B全文の再組版、全入力の静的再監査、全既存計算の再実行は未実施。正確な状態とハッシュは `validation_paper_b.json`。

GitHub main正本、Actions・force pushなし。Libraryは実際のGitHub保存失敗時のみ緊急退避する。
