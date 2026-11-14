# 研究方針：中心三次変形の量子化と一般点可換復元

2026-11-14 / v92。再開時は本ファイルを最初に読む。GitHub mainが正本。

## 現在の目標と達成基準

論文A `papers/paper_a.tex`（A-v59）は全次元Poisson正規形を中心に、その幾何学的帰結・代数的量子化を扱う。ambient復元と完全交叉の背景は付録に置く。論文B `papers/paper_b.tex`（B-v59）は、次数別有限自由な代数的中心三次変形の一般点可換復元を扱う。公表の達成基準は、主要定理の仮定から結論までの証明が現行原稿内で閉じ、使用する既知定理の適用範囲と新規性が具体的に説明され、全文を再生成できることである。

Bでは n>=3、R=C[h]_(h)、K=C(h) とし、A_R/hA_R が N=n+2 変数多項式環、中心三次元の剰余が滑らかな三次式であることを仮定する。可換方程式はK上、全coherent残余圏のrotation・指定三次周期付き同値はある有限拡大上に構成する。模型の一意性はrotation付きpairを実現する模型の幾何学的射影同型類についてである。K上のformの一意性・同値核のKへの降下・特殊点を含む代数的相対同値は結論に含めない。

## 到達点と証明の所在

AではEuler--Koszul表示、Jacobi条件のHessian線形化、Lie代数補題、全次元正規形、退化軌跡とBondalの次元下界、代数的中心三次元とPBW/AS性、固定・相対Poisson成分、ambient復元の証明を再点検した。本文の証明を追う監査と有限計算は別々に記録している。所在・仮定・一次資料の確認範囲は `notes/poisson_article_submission_audit.md`、実行状態は `validation_paper_a.json` を参照する。

査読の三要求に対する現行構成は、定理ごとの既知入力と追加内容の比較、版・頁を固定したPym比較、および幾何から量子化への依存順である。表現論の入力を集めた独立補題 `lem:pg-basepoint-free-lie` と、一般次数の滑らかな超曲面上の非連結中心に対する `prop:pg-triple-lifting-obstruction` を本文に置く。後者は任意の消失次数r>=2を扱い、超曲面の定義式と同じ次数dでの持上げ障害をH¹(I_C^{r−1})=C^{π₀(C)}/Cと同定する。全連結成分の正次元性が必要であり、連結なら障害消滅と持上げの一意性、分離型の二曲線ではr=3の非零障害を得る。任意のtwistに同じ群を使う主張ではない。

量子化の新規性は点ごとの中心元存在とは区別する。Etingof--Ginzburgの刊行版Theorem 3.3.2(ii), p.1385と§8.3, pp.1410–1411は既知の存在・特殊化を与え、§9, p.1414はRainsの公式を含む。Hesse係数tが可逆なら混合二次項を中心平行移動で既存表示へ移せる。本稿は固定係数環での無極な規格化、指定Casimirへの正則持上げ、特異・零の制限、全ブロック・多パラメータ・同変降下を制御する。旧目標の正規形・Bondal・量子化・成分数は保持され、階数二では全supportにわたる族を構成し、gcd(N,3)=1の全被約層への降下まで得た。未解決なのは複数ブロックの一般の同変降下、3|Nの別の降下、固定非零変形での同型類像、および刊行版本文・初出の最終照合である。

相対Poisson空間から三次式のパラメータ空間への忘却射は有限型アフィン射であり、閉埋め込みではない。階数層の記述には (F,P)↦(aF,a^{-1}P) の同時スカラー作用と被約構造を明記した。三次三様体の導来復元には左右noetherian性を明示し、偶数Veroneseからの復元に必要な中心二変数上の自由性はambient PBWだけでは従わないと訂正した。最高active記号の正則性が十分条件となる。正規形・Bondal・全Poisson量子化・成分数の主要結論は保持している。

Aの量子化は、全三次式の滑らかさ→active gradientのgcd=1→三次Casimir核の一定次元→普遍交換子小行列式の恒等的消滅→Cramer中心元、という有限代数的構成による。任意の三変数制限をHesse標準形へ帰着する系では滑らかさを仮定するが、全Poisson量子化定理には不要。Kontsevich--Dolgushevの形式理論は背景であって、この存在証明の入力ではない。純中心三次項の配分、相対PBW、中心正則性、AS-Gorenstein商まで本文に証明がある。階数二の型をまたぐ同変化には、以下の中心核のコホモロジーを用いた別の議論を加える。

固定したactive・中心変数の分解については、全滑らかな三次式の係数空間とh直線の積に、零切断全体を含む一つの開集合を取り、偶な中心元を同時に選べる。`thm:pg-det-global-coefficient-lift` は、割った交換子の定階数核、τ=h²への下降、factorialな係数環のPicard群消滅を用いる。通常の中心はh=0で次数三全体へ増えるため、この核の底変更と混同しない。規格化の変更は Ω'=aΩ+c（aは単元、cは純中心）であり、同じ古典極限でも中心イデアルは変わり得る。具体的Hesse例と同変な中心直線を選ぶ問題は `notes/universal_casimir.md` に整理した。

階数二の全supportにわたる族は `intrinsic_rank_two_center.tex` の `thm:pg-intrinsic-rank-two-center` にある。滑らかな全三次式Fと非零分解可能Pの積の上で、古典核は OF ⊕ Sym³(V/W_P)* である。Gr(3,N)の全整数twistについて純中心束とOのH¹が消えるため、Fを定階数核のh冪厚化へ順次持ち上げる。Stiefel開の補集合の余次元がN−2>=2なので、各Weyl係数は行列空間のSL3不変式環へ延長する。この環は有限生成である。次数三・四の有限Weyl行列の共通開を取り、有限中心核Kの完備化の完全性と Khat/hKhat=K/hK により、古典剰余Fを保つ代数的中心元を選ぶ。形式級数全体がその有理式に一致するという主張は不要である。GL_N×Gmで平均すると全座標群への共変性が得られ、AS/PBW・中心正則性の開へ制限して次数別局所自由な商族を得る。外部のformality定理や形式中心元存在定理を入力にする議論ではない。 ただし形式中心元の存在と所定古典剰余はEG Proposition 8.1.1(i), pp.1407–1408に既にあり、同証明は相対係数と還元群への対応も扱う。これら自体を新規成果とせず、全supportにわたる代数的な同時選択と降下を今回の追加として区別する。

`cor:pg-intrinsic-rank-two-descent` は gcd(N,3)=1 のとき、θ=(det L)^rλ^s、Nr−3s=1によって全被約階数二Poissonモジュライ×A¹_hの零切断近傍へ実際の次数付き代数と中心商を降ろす。N=5ではθ=(det L)²λ³を使い、三次三様体の全非零Poisson対が対象となる。底の次元は17であり、固定h≠0の同型類像の次元とは区別する。零Poisson構造、全hへの延長、一意性、各型で別に選んだ明示中心元との一致はこの主張に含まれない。全f・非零Poisson係数まで使っても補空間を正則同変に選ぶことはできず、中心平行移動Uの自由商は非アフィンである（`prop:pg-equivariant-global-centering-obstruction`）。この障害があるため、中心調整を経由せず中心核を直接扱う。

節点型の明示中心元はChekhov–Mazzocco–Rubtsov、Adv. Math.376(2021),107442、accepted arXiv:1905.02772v2のLemma4.6・式(4.39),p22に帰属する。本稿との関係式の対応、t=0での無極な規格化、安定化群共変にする純中心補正を `rem:pg-cmr-nodal-comparison` に記載した。独立な厳密検算は `verify_cmr_nodal_center.py`。既知の点ごとの公式と、全係数・全supportでの族の選択を区別し、後者の包括的な初出は未確定とする。

単一ブロックの層別の具体的構成は `equivariant_central_lifts.tex` に保持する。全滑らかなfについてはG_0=(GL3×GLm)×Gmに同変な中心元を、零切断全体を含む不変開上に選べる。g=f(x,0)も滑らかなら、方向微分δ_gの同変左逆から混合二次項の中心B_fを選び、B_f'=(MB_f−C)N^-1によって中心平行移動も含む全ブロック群Gと整合させられる。t=ηhとしてhを固定すると、対応する線形群の商上へ中心商族が降りる。純中心係数の固定と全平行移動の同変性は一般に両立しない。

g=0の場合には、active次数が二以下なので既知のPBW対称化の随伴同変性を直接適用でき、Ω=sym(f)が全tにわたる全G共変な正則中心元となる（`thm:pg-equivariant-zero-center`）。分母・例外パラメータ・中心係数の変更を要せず、割った交換子の三次核は全tでOΩ⊕C_mである。滑らかな全fの零制限層はm>=3のときに限り非空で、support平面P(W_P)⊂Xという階数二の層内の余次元10の条件に対応する。全hのgerbe上の族があり、gcd(m,3)=1なら同じ指標補正でこの層と全h直線の積へ代数族が降りる（`prop:pg-equivariant-zero-stratum`）。m=3ではこの指標法は適用しない。PBW原理自体の新規性は主張せず、全係数・同変族への適用として扱う。

節点・尖点の各軌道では、基準形の安定化群に同変なδ_gの左逆を明示し、軌道商上へ正則に移すことで全G同変な中心元を得た（`lem:pg-equivariant-singular-retractions`、`thm:pg-equivariant-parabolic-center`）。それぞれの層は階数二のPoisson層内で余次元1,2であり、三次三様体では底が16,15次元となる。唯一の特異点のtautological直線ℓ_gは、代数の引戻し線形化と同じ規約で中心スカラーの重み−1を持つ。A_d⊗ℓ_g^d、中心線J⊗ℓ_g^3を使うと重みが消え、全mでPoisson層自体の零h切断近傍へ代数族が降りる（`prop:pg-equivariant-singular-strata`）。これは定数群指標を使わない方法で、対応するgerbeも中立になる。既知の軌道商と重み零の層の降下を適用した結果であり、その一般原理の新規性は主張しない。

階数二のPoisson対の被約層内でgが滑らかな開について、この線形群の商は実際のPoissonモジュライ上の中心Gm-gerbeである。gcd(m,3)=1ならmr−3s=1を満たす整数を選び、θ=(det N)^rλ^sで次数dの線形化をθ^-dだけ補正すると、中心スカラーの作用が消えて次数付き代数と中心商がPoissonモジュライへ降りる（`prop:pg-equivariant-poisson-gerbe`、`cor:pg-equivariant-character-descent`）。特に三次三様体ではm=2、θ=(det N)^2λであり、17次元のPoisson対の被約モジュライの稠密開とh直線の積の零切断近傍に量子化族を得る。17は底の次元であり、固定h≠0での非可換代数の同型類の像の次元は未解決である。3|mではこの指標による方法が使えないことだけを示しており、別の降下の不存在は結論しない。方程式の代表を変える自由なスカラーと、係数を固定する中心スカラーは `eq:pg-equivariant-effective-group-sequence` で区別する。指標補正後の次数一束E_θと三次直線の古典商、その相対Projが元の普遍三次族であることは `rem:pg-equivariant-classical-family` に明記する。中心直線の降下は底上での大域生成元の存在を主張しない。

三次四様体の一般階数四の構造は、二つの滑らかな平面三次の分離型F=f+gに限られ、全てpurely elliptic log symplecticとなる。退化因子は正規なjoin、Poisson零点スキームは被約な二本の楕円曲線の非交和である。`prop:pg-split-elliptic` は正規形に依存しない直接証明、`cor:pg-cubic-fourfold-elliptic` は正規形からの分類を与える。Pym arXiv:1507.05668v1のTheorem 1.3・Proposition 5.7とは両立せず、同版Lemma 5.5が非連結曲線で成立しないH¹(I_C)=0を用いることを具体化した。刊行版本文・訂正文との照合は未了で、比較を公開v1に限定する。Definition 4.2はp.17、Theorem 1.3はp.4、Lemma 5.5はpp.28–29、Proposition 5.7はp.30に固定する。

三次四様体については、Bricalli–Favale–Pirolaの刊行版Theorem 3.4（Forum Math. Sigma 13 (2025), e80, pp.10–12; DOI 10.1017/fms.2025.36）により、上の(3,3)分離型と、周囲のP⁵のHessian階数≤3軌跡が平面を含むことが同値になる。この既知判定とPoisson正規形を結んだのが `cor:pg-cubic-fourfold-elliptic` である。平面はX内でなく周囲の空間内である。Hessianの可約性だけでは不十分であり、`ex:pg-reducible-hessian-no-rank-four` の滑らかな(1,1,4)型の例では定数symmetrizerがdiag(a,b,cI₄)で階数三の冪等元を持たない。一般の証明と、この例のQQ線形代数を確認する `verify_hessian_split_obstruction.py` を区別する。

既知部分の帰属も明確にした。Bondal 1993のdivergence-free持上げ、Derdzinski--Gal Theorem Bの半単純Lie代数上の核計算と、本稿のHessian基点自由性からの根基排除を区別する。完全交叉の低twist消滅には `lem:ci-low-twist-vanishing` で穿孔錐とKoszul分解による独立証明を与えた。Brückmann原証明は未取得だが、現行の存在判定の証明依存からは外れている。

Bの証明は `papers/generic_recovery/` だけで完結する。`local_model.tex` と `window.tex` が局所proper模型と三対象window、`curved_transport.tex` が実際の完備A_infty比較、`generic_descent.tex` がEuler非消滅・BFK生成・有限降下、`coherent_saturation.tex` が全coherent圏への飽和、`gradient_recovery.tex` と `field_model.tex` が勾配空間の積分と方程式の基礎体降下を与える。

Bの公表上の核心は、任意の完備noetherian局所C代数上での実際の有限rank graded MF移送（`cft:thm:complete`）と、それを代数的一般点の全coherent残余pairへ結ぶ存在定理である。前者は逆関手・固定rank・内部shift・t-relativeな指定周期を保ち、底の正則性を要求しない。正則局所底のwindowとの区別、曲率付きbar写像のarity評価とMF関手のTaylor成分の区別を序論で明示する。

`tw:eq:comparison-diagram` はdg商・余核・totalization・section切断・mutationを集約し、`tw:eq:period-extension` と `tw:eq:rotation-period-square` が指定周期を追跡する。提供された独立査読報告の主要結論を踏まえ、比較図式と文献帰属の整理を保持する。今回の独立点検は具体例の二次jet・全次数Hesse係数・相対楕円比較と固定模型への降下を対象とした。未変更の全証明を今回改めて一から監査した、あるいはLean等で形式検証したとはしない。正確な範囲は `notes/paper_b_proof_audit.md` と `validation_paper_b.json` に置く。

一次資料の比較では、EGが既に有限rank graded MFと楕円曲線を結んでいること、CKの結果が第二種変形複体の比較であることを区別する。Pirozhkov Theorem 1.2の三次の場合はn>3、Lin--Zhangの低積計算とpair Torelliは三次三様体も扱う。BFKの数値上界、Toën--Vaquié/Perryの有限性・飽和、Hwang等の勾配空間の構造は既知の入力である。本稿の一般点存在結論と明示的移送の包括的な初出は引き続き未確定である。

具体的な非可換Hesse--Sklyanin族では、生成元を固定するharmonic-angle比較から W_rec=F+h xyz+(h²/3)xyz+O(h³) を得た。中心元のWeyl表示の二次係数−2/3と、星積への比較の補正+1を分け、inner二輪の重み零を使う。さらに全次数のHesse正規形 W_H=F+λ(h)xyz を取り、λ(h)=(h+h²/3+h⁵/12)/(1−h⁴/4) と厳密に同定した。したがってK上の可換模型は (4−h⁴)(x³+y³+z³+u³+v³)+(12h+4h²+h⁵)xyz=0 と明示できる。証明は `explicit_example.tex` にあり、正規化中心商の相対THCR表示、三変数a=0のdg比較、Perf模型の分数体への底変更、楕円曲線のjと形式分枝の比較を用いる。五変数のrotation・指定周期同値は元の完備MF比較から固定したこのK模型へ有限降下する。全次数の有理式同定は本文の圏的証明であり、有限計算の外挿ではない。

方程式の積分には、Hwangの理論の基本的帰結として有限étaleなsymmetrizer代数E_Fを用いる。可積分行列空間の次元は最細の幾何学的Sebastiani--Thom分解のブロック数に等しく、幾何学的に分解不能なら固定した勾配空間からの方程式は基礎体上でもスカラー倍まで一意である。証明は `ej:lem:symmetrizer-algebra`、`gcd:prop:integrability-symmetrizer`、`gcd:cor:indecomposable-equation`。これは同値核の基礎体降下を意味しない。

独立な点スキーム・Jacobian・一次変形・Artin・étale・相対模型の成果はnc-cubic2へ移管済みである。現在の入口は `notes/paper_b_scope_and_transfer.md`。Bの必要証明を移管先へのリンクだけで代用しない。

## 優先する次の課題

1. Aの公表上の中心を全次元正規形・Bondal・全Poisson代数的量子化・相対成分数に置き、三次四様体の純楕円分類を具体的帰結として示す。Pym論文の刊行版または著者のaccepted manuscriptを通常の公開経路で入手し、v1との該当箇所・訂正状況を最優先で照合する。Oxfordの登録メタデータは確認できたが本文は取得できていない。独立な反例証明は現行本文にある。Bondal・Derdzinski--Gal・LPT/Mayanskiy・Gualtieri--Pym等との比較を踏まえ、包括的な正規形・成分定理の初出も引き続き調べる。
2. 階数二の型をまたぐ共変な中心元と、gcd(N,3)=1での全被約層への降下は本文に証明した。次は複数ブロックの分解・純中心配分を忘れた同変構成を調べる。`notes/universal_casimir.md` §3の中心核の射影束とdilatationから再開し、古典核の自然な線と純中心束のコホモロジー、ブロック置換作用を確認する。3|Nの場合は指標だけでは次数重みを除けないが、節点・尖点層は特異点直線で処理済みなので、全階数二層上で利用できる重み一線束の有無を調べる。新しい全supportの選択と零制限の全h明示式・既存層別公式の一致、短い共変多項式表示、固定h≠0での同型類像、全閉パラメータでのqgr滑らかさは別の課題とする。補空間の大域選択と自由なU商のアフィン性は否定されたので、この経路を再度仮定しない。
3. Bでは二次補正と、このHesse--Sklyanin例の全次数の有理K方程式が決定したため、次は比較核と低rotation積の有効化に進む。rotation核Pと対角Deltaの有限表示から V=H^0RHom(Delta,P)、U=H^0RHom(Delta,P^2)、積を算出する。まずstabilization模型の有限Homと三対象dg代数へ戻り、どの構造写像がV,Uに寄与するかを特定し、得られた核を既知の明示方程式の勾配空間と照合する。一般点の固定模型への核の有限降下は証明済みだが、核の具体行列と拡大次数は未計算である。楕円曲線を用いた方程式の同定を、非可換圏から低積全体を直接抽出したことの代用にしない。
4. 公表上の貢献を、完備比較と相対windowの具体的構成、および包括的な一般点復元に絞る。既知の一般原理と本稿の適用条件の対照は監査ノートにある。新たな引用が必要になれば一次資料で範囲を確かめ、同一の定理の初出が判明すれば序論・方針を修正する。
5. 同値核のGalois降下を調べる。E_F=kという方程式の一意性と、rotation付き同値核の降下を分け、まずその自己同値群・自己同型群を同定する。`gcd:ex:forms` は特殊ファイバーも完備化も一致するがK上非同型の例である。TsenによるBrauer群消滅や形式点の存在だけでK'=Kを結論しない。

## 一般原則と保存許可

以下は個別の研究課題と区別した継続原則である。数学的重要性・新規性・理解・応用・正確性・実現可能性を総合し、方針は現在有効な内容へ書き直す。証明済、仮定付き、未完成、予想、有限計算を区別する。誤りがあれば依存先・要約も修正する。必要な証明・例・反例・再現入力を軽量化のために削らず、履歴と重複を整理する。先行研究は一次資料で仮定・適用箇所を確認し、初出未確認は明記する。原稿・ノートは研究の経緯ではなく現在の数学を理解する順に構成する。

本研究はGitHub mainへの節目ごとの保存が継続して許可されており、追加承諾を求めない。保存前に最新mainを確認し、期待する親SHAを指定したfast-forward更新と遠隔ref/blob照合を行う。force push、GitHub Actions、不要なPR、旧版ZIPは作らない。現在の利用者指示に従い、研究の区切りでは現行の方針・ノート・原稿・必要な再現資産だけからなる軽量bundleも、承諾を求めずLibraryへ保存する。生成PDF・中間物はGitで追跡しない。Library上の既存ファイルの削除はこの許可に含めない。

## 再現手順

```sh
python3 scripts/check_layout.py
python3 scripts/verify_bundle.py
python3 scripts/build.py --only paper_a
python3 scripts/verify_bundle.py --only paper_a --require-pdfs
python3 computations/verify_zero_restriction_center.py --json
python3 computations/verify_singular_orbit_centering.py --json
python3 computations/verify_cmr_nodal_center.py --json
python3 computations/verify_equivariant_centering.py
python3 computations/verify_split_cubic_fourfold.py
python3 computations/verify_hesse_translation.py
python3 computations/verify_hessian_split_obstruction.py
python3 scripts/build.py --only paper_b
python3 scripts/verify_bundle.py --only paper_b --require-pdfs
python3 computations/verify_complete_curved_transport.py --output build/verify_complete_curved_transport.json
python3 computations/verify_three_object_window.py --output build/verify_three_object_window.json
python3 computations/verify_generic_cubic_descent.py --output build/verify_generic_cubic_descent.json
python3 computations/verify_recovery_example.py --output build/verify_recovery_example.json
```

`scripts/check_layout.py` はGit checkoutでの追跡対象検査であり、Git管理情報のない再開用ZIPでは省略する。その他のソース・組版検査はZIPの展開先でも実行できる。

日本語LuaLaTeX、LuaTeX-ja、latexmk、Pythonと `requirements.txt` の依存を用いる。Aの厳密計算は `validation_paper_a.json` のコマンドで再現する。大きな記号行列を扱うスクリプトは一つずつ実行する。PDF・SyncTeX・中間物・再生成可能な出力はbuild/で非追跡。生成、検証、遠隔保存を別の状態として記録し、有限検算を一般定理や圏同値の計算機証明とは報告しない。本改訂はA-v59を対象とし、B-v59の全TeX入力・専用検証記録と共通preambleを保持する。Bの再組版・再監査は今回の実行範囲に含めない。
