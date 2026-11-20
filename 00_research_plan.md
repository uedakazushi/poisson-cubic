# 研究方針：三次超曲面のPoisson構造と代数的量子化

2026-11-21 / v96。再開時は本ファイルを最初に読む。GitHub mainが正本。

## 現在の目標と達成基準

主公表原稿 `papers/poisson-cubic.tex`（旧論文A A-v61）は全次元Poisson正規形を中心に、その幾何学的帰結・代数的量子化を扱う。ambient復元と完全交叉の背景は付録に置く。完備MF移送・一般点可換復元（旧論文B）は `nc-cubic-n-fold` の主原稿へ必要な全証明と計算を統合した。公表の達成基準は、主要定理の仮定から結論までの証明が現行原稿内で閉じ、使用する既知定理の適用範囲と新規性が具体的に説明され、全文を再生成できることである。


## 到達点と証明の所在

AではEuler--Koszul表示、Jacobi条件のHessian線形化、Lie代数補題、全次元正規形、退化軌跡とBondalの次元下界、代数的中心三次元とPBW/AS性、固定・相対Poisson成分、ambient復元の証明を再点検した。本文の証明を追う監査と有限計算は別々に記録している。所在・仮定・一次資料の確認範囲は `notes/poisson_article_submission_audit.md`、実行状態は `validation_paper_a.json` を参照する。

査読の三要求に対する現行構成は、定理ごとの既知入力と追加内容の比較、版・頁を固定したPym比較、および幾何から量子化への依存順である。表現論の入力を集めた独立補題 `lem:pg-basepoint-free-lie` と、一般次数の滑らかな超曲面上の非連結中心に対する `prop:pg-triple-lifting-obstruction` を本文に置く。後者は任意の消失次数r>=2を扱い、超曲面の定義式と同じ次数dでの持上げ障害をH¹(I_C^{r−1})=C^{π₀(C)}/Cと同定する。全連結成分の正次元性が必要であり、連結なら障害消滅と持上げの一意性、分離型の二曲線ではr=3の非零障害を得る。任意のtwistに同じ群を使う主張ではない。

量子化の新規性は点ごとの中心元存在とは区別する。Etingof--Ginzburgの刊行版Theorem 3.3.2(ii), p.1385と§8.3, pp.1410–1411は既知の存在・特殊化を与え、§9, p.1414はRainsの公式を含む。Hesse係数tが可逆なら混合二次項を中心平行移動で既存表示へ移せる。本稿は固定係数環での無極な規格化、指定Casimirへの正則持上げ、特異・零の制限、全ブロック・多パラメータ・同変降下を制御する。旧目標の正規形・Bondal・量子化・成分数は保持され、階数二では全supportにわたる族を構成し、gcd(N,3)=1の全被約層への降下まで得た。階数二の三次Veroneseは全次元で降下し、元の次数一を線束補正で降ろす障害は位数gcd(N,3)のgerbeとして決定した。複数ブロックの一般の同変降下、固定非零変形での同型類像、および刊行版本文・初出の最終照合は残る。

相対Poisson空間から三次式のパラメータ空間への忘却射は有限型アフィン射であり、閉埋め込みではない。階数層の記述には (F,P)↦(aF,a^{-1}P) の同時スカラー作用と被約構造を明記した。三次三様体の導来復元には左右noetherian性を明示し、偶数Veroneseからの復元に必要な中心二変数上の自由性はambient PBWだけでは従わないと訂正した。最高active記号の正則性が十分条件となる。正規形・Bondal・全Poisson量子化・成分数の主要結論は保持している。

Aの量子化は、全三次式の滑らかさ→active gradientのgcd=1→三次Casimir核の一定次元→普遍交換子小行列式の恒等的消滅→Cramer中心元、という有限代数的構成による。任意の三変数制限をHesse標準形へ帰着する系では滑らかさを仮定するが、全Poisson量子化定理には不要。Kontsevich--Dolgushevの形式理論は背景であって、この存在証明の入力ではない。純中心三次項の配分、相対PBW、中心正則性、AS-Gorenstein商まで本文に証明がある。階数二の型をまたぐ同変化には、以下の中心核のコホモロジーを用いた別の議論を加える。

固定したactive・中心変数の分解については、全滑らかな三次式の係数空間とh直線の積に、零切断全体を含む一つの開集合を取り、偶な中心元を同時に選べる。`thm:pg-det-global-coefficient-lift` は、割った交換子の定階数核、τ=h²への下降、factorialな係数環のPicard群消滅を用いる。通常の中心はh=0で次数三全体へ増えるため、この核の底変更と混同しない。規格化の変更は Ω'=aΩ+c（aは単元、cは純中心）であり、同じ古典極限でも中心イデアルは変わり得る。具体的Hesse例と同変な中心直線を選ぶ問題は `notes/universal_casimir.md` に整理した。

階数二の全supportにわたる族は `intrinsic_rank_two_center.tex` の `thm:pg-intrinsic-rank-two-center` にある。滑らかな全三次式Fと非零分解可能Pの積の上で、古典核は OF⊕Sym³(V/W_P)* である。Gr(3,N)の全整数twistのH¹消滅により、普遍二次jet Θ=F−h²H(P,F)/12 をK/h³Kの初期切断として形式中心元へ持ち上げる。Stiefel開の正則関数は有限生成のSL3不変式環へ延長し、有限中心核の完備化 Khat/h³Khat=K/h³K により、この指定jetを保つ代数解を選べる。全GL_N×Gmと偶性について平均してもjetは保たれ、Ω=sym(F−h²H/12+O(h⁴))となる。AS/PBW・中心正則性の開へ制限すると次数別局所自由な商族を得る。形式級数全体の代数性は不要である。形式中心元の存在・指定古典剰余・相対的または還元群に対応した形式構成はEG Proposition 8.1.1(i)の既知の内容と区別する。

`cor:pg-intrinsic-rank-two-descent` は gcd(N,3)=1 のときθ=(det L)^rλ^s、Nr−3s=1で全被約階数二Poissonモジュライ×A¹_hの零切断近傍へ元の次数付き代数と中心商を降ろす。N=5では全非零Poisson対が対象で、底の次元は17である。一般のNでも `cor:pg-intrinsic-third-veronese-descent` により A^[3]_d=A_(3d)⊗λ^d と中心商が降下し、Ωは新次数一の大域中心元になる。古典Projは元の普遍三次族、新偏極は各fiber上のO(3)である。元のAS-regular性をVeroneseへそのまま移さず、qgr同値は左右noetherianな閉fiberについて述べる。Smithの訂正文が要求するTor¹のtorsion条件も本文で直接確認する。

中心変数が残らない満support層N=3kでも、`full_support_quantization.tex` の `thm:pg-intrinsic-full-support-center` により、ブロックの順序を底に加えずに指定Hessian二次jet付きの共変な代数的中心元を選べる。三重ベクトルからのブロック復元を有限étale被覆として相対化し、安定化群(SL3)^k⋊S_kが還元的なので軌道も適合する滑らかな係数空間もアフィンとなる。割った交換子の階数kの核へ、法h³の切断を直接持ち上げ、Reynolds平均と偶平均でjetを保つ。各ブロック成分を非零にすると、一ブロック次数によるfiltrationから正則性が従い、次数別局所自由な中心商を得る。`cor:pg-full-support-veronese-descent` は A^[3]_d=A_(3d)⊗λ^d、中心線J⊗λ≃Oを用いて新次数一の大域中心元と商を実際の被約Poisson層へ降ろす。全零h切断を含む開近傍での存在であり、全hや一意性は主張しない。底の次元は2k、三次四様体のrank4では4である。固定h≠0での同型類像の次元は未決定である。アフィン商にはArzhantsevのMatsushima基準の公開原稿§2を一次資料として用いる。

全非零階数2kの被約層で、中心スカラーgerbeの位数はgcd(N,3)である（`prop:pg-intrinsic-all-rank-gerbe`）。3|NのFermat点で、安定化群の二元の交換子が中心の三乗根になるため、全ての同変可逆層の中心重みは三の倍数となる。指標による上界と合わせたこの証明はPicard群の消滅を要しない。階数二のPic(S_N)=0を用いる既存証明は `prop:pg-intrinsic-gerbe-period` に保持する。3|Nでは全零切断近傍にも重み±1の可逆層がなく、既存の次数一の族を可逆層の次数冪で補正して降ろす方法は不可能である。これは別ambient・Morita模型・カテゴリーの不存在でも、任意の稠密開や一般点でのperiod決定でもない。

零制限層Z_Nでの標準中心直線O sym(F)への一致には、`prop:pg-intrinsic-zero-matching-obstruction` の別の障害がある。任意の大域偶中心元は二次係数を −H/12+aF+c と書けるが、全supportの純中心束CにはP重み2の大域切断がない。一方Z_N上のHは純中心で非零になり得るため、N>=6ではOΩをO sym(F)へ全層で一致させられない。相対障害は0≠∂(H|Z/12)∈H¹(S_N,I_Z C)_2である。指定ambient下の中心ideal不一致と、商の抽象非同型・qgr非同値は区別する。全係数の補空間の同変選択も不可能で、中心平行移動Uの自由商は非アフィンである。

節点型の明示中心元はChekhov–Mazzocco–Rubtsov、Adv. Math.376(2021),107442、accepted arXiv:1905.02772v2のLemma4.6・式(4.39),p22に帰属する。本稿との関係式の対応、t=0での無極な規格化、安定化群共変にする純中心補正を `rem:pg-cmr-nodal-comparison` に記載した。独立な厳密検算は `verify_cmr_nodal_center.py`。既知の点ごとの公式と、全係数・全supportでの族の選択を区別し、後者の包括的な初出は未確定とする。 Veronese同値、重み零のgerbe降下、底の線束による次数別twistは既知の原理としてSmith（訂正文を含む）、Bergh–Schnürer、Van den Berghに帰属する。

単一ブロックの層別の具体的構成は `equivariant_central_lifts.tex` に保持する。全滑らかなfについてはG_0=(GL3×GLm)×Gmに同変な中心元を、零切断全体を含む不変開上に選べる。g=f(x,0)も滑らかなら、方向微分δ_gの同変左逆から混合二次項の中心B_fを選び、B_f'=(MB_f−C)N^-1によって中心平行移動も含む全ブロック群Gと整合させられる。t=ηhとしてhを固定すると、対応する線形群の商上へ中心商族が降りる。純中心係数の固定と全平行移動の同変性は一般に両立しない。

g=0の場合には、active次数が二以下なので既知のPBW対称化の随伴同変性を直接適用でき、Ω=sym(f)が全tにわたる全G共変な正則中心元となる（`thm:pg-equivariant-zero-center`）。分母・例外パラメータ・中心係数の変更を要せず、割った交換子の三次核は全tでOΩ⊕C_mである。滑らかな全fの零制限層はm>=3のときに限り非空で、support平面P(W_P)⊂Xという階数二の層内の余次元10の条件に対応する。全hのgerbe上の族があり、gcd(m,3)=1なら同じ指標補正でこの層と全h直線の積へ代数族が降りる（`prop:pg-equivariant-zero-stratum`）。m=3ではこの指標法は適用しない。PBW原理自体の新規性は主張せず、全係数・同変族への適用として扱う。

節点・尖点の各軌道では、基準形の安定化群に同変なδ_gの左逆を明示し、軌道商上へ正則に移すことで全G同変な中心元を得た（`lem:pg-equivariant-singular-retractions`、`thm:pg-equivariant-parabolic-center`）。それぞれの層は階数二のPoisson層内で余次元1,2であり、三次三様体では底が16,15次元となる。唯一の特異点のtautological直線ℓ_gは、代数の引戻し線形化と同じ規約で中心スカラーの重み−1を持つ。A_d⊗ℓ_g^d、中心線J⊗ℓ_g^3を使うと重みが消え、全mでPoisson層自体の零h切断近傍へ代数族が降りる（`prop:pg-equivariant-singular-strata`）。これは定数群指標を使わない方法で、対応するgerbeも中立になる。既知の軌道商と重み零の層の降下を適用した結果であり、その一般原理の新規性は主張しない。

階数二のPoisson対の被約層内でgが滑らかな開について、この線形群の商は実際のPoissonモジュライ上の中心Gm-gerbeである。gcd(m,3)=1ならmr−3s=1を満たす整数を選び、θ=(det N)^rλ^sで次数dの線形化をθ^-dだけ補正すると、中心スカラーの作用が消えて次数付き代数と中心商がPoissonモジュライへ降りる（`prop:pg-equivariant-poisson-gerbe`、`cor:pg-equivariant-character-descent`）。特に三次三様体ではm=2、θ=(det N)^2λであり、17次元のPoisson対の被約モジュライの稠密開とh直線の積の零切断近傍に量子化族を得る。17は底の次元であり、固定h≠0での非可換代数の同型類の像の次元は未解決である。この層別の系と、全階数二層におけるgerbeの位数の命題は区別する。方程式の代表を変える自由なスカラーと、係数を固定する中心スカラーは `eq:pg-equivariant-effective-group-sequence` で区別する。指標補正後の次数一束E_θと三次直線の古典商、その相対Projが元の普遍三次族であることは `rem:pg-equivariant-classical-family` に明記する。中心直線の降下は底上での大域生成元の存在を主張しない。

三次四様体の一般階数四の構造は、二つの滑らかな平面三次の分離型F=f+gに限られ、全てpurely elliptic log symplecticとなる。退化因子は正規なjoin、Poisson零点スキームは被約な二本の楕円曲線の非交和である。`prop:pg-split-elliptic` は正規形に依存しない直接証明、`cor:pg-cubic-fourfold-elliptic` は正規形からの分類を与える。Pym arXiv:1507.05668v1のTheorem 1.3・Proposition 5.7とは両立せず、同版Lemma 5.5が非連結曲線で成立しないH¹(I_C)=0を用いることを具体化した。刊行版本文・訂正文との照合は未了で、比較を公開v1に限定する。Definition 4.2はp.17、Theorem 1.3はp.4、Lemma 5.5はpp.28–29、Proposition 5.7はp.30に固定する。

三次四様体については、Bricalli–Favale–Pirolaの刊行版Theorem 3.4（Forum Math. Sigma 13 (2025), e80, pp.10–12; DOI 10.1017/fms.2025.36）により、上の(3,3)分離型と、周囲のP⁵のHessian階数≤3軌跡が平面を含むことが同値になる。この既知判定とPoisson正規形を結んだのが `cor:pg-cubic-fourfold-elliptic` である。平面はX内でなく周囲の空間内である。Hessianの可約性だけでは不十分であり、`ex:pg-reducible-hessian-no-rank-four` の滑らかな(1,1,4)型の例では定数symmetrizerがdiag(a,b,cI₄)で階数三の冪等元を持たない。一般の証明と、この例のQQ線形代数を確認する `verify_hessian_split_obstruction.py` を区別する。

既知部分の帰属も明確にした。Bondal 1993のdivergence-free持上げ、Derdzinski--Gal Theorem Bの半単純Lie代数上の核計算と、本稿のHessian基点自由性からの根基排除を区別する。完全交叉の低twist消滅には `lem:ci-low-twist-vanishing` で穿孔錐とKoszul分解による独立証明を与えた。Brückmann原証明は未取得だが、現行の存在判定の証明依存からは外れている。

## 優先する次の課題

1. Aの公表上の中心を全次元正規形・Bondal・全Poisson代数的量子化・相対成分数に置き、三次四様体の純楕円分類を具体的帰結として示す。Pym論文の刊行版または著者のaccepted manuscriptを通常の公開経路で入手し、v1との該当箇所・訂正状況を最優先で照合する。Oxfordの登録メタデータは確認できたが本文は取得できていない。独立な反例証明は現行本文にある。Bondal・Derdzinski--Gal・LPT/Mayanskiy・Gualtieri--Pym等との比較を踏まえ、包括的な正規形・成分定理の初出も引き続き調べる。
2. 階数二の全supportと、中心変数のない満support層N=3kでは、指定二次jetを持つ共変中心元と三次Veroneseの降下が得られた。全非零階数層のgerbeの位数もgcd(N,3)と決定した。次の存在問題は中心変数を残すm>0、k>=2の層に絞る。`notes/universal_casimir.md` §3の自然な完全列 0→Sym³(V/W_P)*→K_0→E_perm→0 から始め、古典Fの対角切断、H¹と有限アフィン模型への延長を調べる。補空間と純中心配分の大域的分裂は仮定しない。三重ベクトルの軌道の非アフィン性だけから係数incidenceの非アフィン性や中心元不存在を結論しない。零制限標準中心直線への全support一致はN>=6で不可能であり、次は中心商の抽象的同型・Morita/qgr比較や基底変更との関係を調べる。3|Nでは三次偏極の族を基準に別ambient表示を比較する。全hへの延長、短い共変多項式表示、固定h≠0での同型類像、全閉パラメータでのqgr滑らかさは別の課題とする。

## 一般原則と保存許可

以下は個別の研究課題と区別した継続原則である。数学的重要性・新規性・理解・応用・正確性・実現可能性を総合し、方針は現在有効な内容へ書き直す。証明済、仮定付き、未完成、予想、有限計算を区別する。誤りがあれば依存先・要約も修正する。必要な証明・例・反例・再現入力を軽量化のために削らず、履歴と重複を整理する。先行研究は一次資料で仮定・適用箇所を確認し、初出未確認は明記する。原稿・ノートは研究の経緯ではなく現在の数学を理解する順に構成する。

本研究はGitHub mainへの節目ごとの保存が継続して許可されており、追加承諾を求めない。保存前に最新mainを確認し、期待する親SHAを指定したfast-forward更新と遠隔ref/blob照合を行う。force push、GitHub Actions、不要なPR、旧版ZIPは作らない。GitHub管理後はLibraryへの定常的な二重保存やZIP作成を行わない。pushに失敗した場合の緊急保存または明示的な指示がある場合に限りLibraryを使用する。生成PDF・中間物はGitで追跡せず、既存Libraryファイルは明示的な指示なしには削除しない。

## 再現手順

- 主原稿：`papers/poisson-cubic.tex`（日本語LuaLaTeX、本文と全必要証明を保持）。
- ソース・引用検証：`python3 scripts/check_layout.py`、`python3 scripts/verify_bundle.py`、`python3 scripts/verify_article_a_numbering.py`。
- 組版：`latexmk papers/poisson-cubic.tex` または `python3 scripts/build.py --only poisson-cubic`。PDFとSyncTeXは`build/`。
- 主な数値・厳密計算の依存と既存検証：`validation_paper_a.json`。改名後の稿はこの更新では再組版していない。旧検証記録のハッシュを改名後の検証と同一視しない。
- 外部の可換復元結果は [nc-cubic-n-fold](https://github.com/uedakazushi/nc-cubic-n-fold) 内で完結する。本repoはPoissonの論文Aを正本とする。
