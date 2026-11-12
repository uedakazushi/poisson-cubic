# AGENTS.md — nc-cubic研究継続

**2026-11-12 / v49。GitHub mainが唯一の正本。** 最初に 00_research_plan.md を読む。

## 最優先指示：任意次元の同時量子化を論文Aの完成結果へ

まず `papers/support/papers/sections/general_dimension_universal_quantization.tex`
（`thm:pg-all-dimensions` と `cor:pg-ad-whole-pencil`、
`prop:pg-ad-relative-chart`、`cor:pg-ad-hessian`）を読む。
任意 n≥3、N=n+2=3k+m、F=Σf_s(x_s,u)、各純active三次g_s滑らかの下で、
k個のJacobian Poisson構造の線形族全体に独立η_sを与える。
Ω_{η}=Σ_sΩ_{f_s,η_s} は各ブロックのHesse普遍中心元の和で、
ブロック間の量子混合補正なしに厳密に中心。
共通u上のテンソルPBW、Koszul AS正則、中心正則性、
中心商AS-Gorenstein、各内部次数の多変数平坦性を原稿で証明している。
これは全Poisson pairモジュライの普遍量子化を主張しない。

数学的な次の優先は、表示係数も動く相対Hesseチャートの同変性、
ブロック入替え、Hesse座標変更、中心三次の分配に伴う
中心元・商の同型とモジュライ降下を検証すること。
次に既存PBW/正則性補題の全独立監査、正規形のLie補題、
Bondal予想、一次文献比較と全原稿のLuaLaTeX組版を進める。
滑らかでない三変数制限への拡張は、現在の優先課題ではない。
`notes/universal_casimir.md` を再開の現行ノートとする。
`computations/verify_general_dimension_multiblock.py` は
n=3,4,6,7,10の6具体例についてJacobi610成分とCasimir52成分を
厳密検算するが、一般次元定理の形式証明そのものではない。
`computations/build_general_dimension_center.py` は共有中心を持つ
2ブロックのWeyl中心symbolを構成する。
GitHub main正本、GitHub Actionsなし、PDFはGit追跡せず、
論文B/Cの数学的証明を保持する。

## 内在的な高次元Hessian補正
論文A prop:pg-ad-intrinsic-hessian はH(P,F)=Σ P^{ijk}P^{abc}F_{ia}F_{jb}F_{kc}/6 を座標不変に定義。正規形ではΣ λ_s² det Hess_{x_s}(f_s)となる。純中心三次の調整後、Ω= sym(F-h²H(P,F)/12+h⁴ K) という厳密中心元を取れる。h⁴ Kは各Hesseブロックの明示補正を合成し、まだ座標不変な短い式とは主張しない。一般次元の6具体例でHessian縮約の恒等式をSymPy厳密計算で確認。次はk変数Poisson pencilに沿う正規形表示の座標変換、Hesse chartの接着と相対モジュライへの降下を優先し、特異g拡張へ戻らない。

## 量子中心の現在の最重要到達点と残課題

論文A thm:pg-universal-hesse-mixed は一般Hesse t と全混合係数A,B,C,D,E,Hの**独立記号を保った普遍多項式の厳密中心性**を証明。検証コード`computations/verify_universal_hesse_mixed_center.py` はQ(h,t)上で自由語339、関係162、rank144、三交換子余り0とh=0でのrank144を計算する。Fermatはt=0、対角二次混合は中心平行移動で包含。任意のsmooth ternary cubicはHesse標準形経由で扱えるので、thm:pg-universal-determinant の形式中心存在仮定は不要になった。詳細は notes/universal_casimir.md。次は一般次元の正規形表示族の同変性と降下・PBW全仮定の監査、Poisson正規形とBondal証明の独立監査。全論文AのLuaLaTeX組版は未確認。

## 論文A：Bondal予想の帰結

全滑らかなcubic n-fold (n>=3) のPoisson構造についてBondalのD_{2j}次元下界を、正規形のJacobianブロックから選ぶ平面曲線のjoinで証明。`papers/support/papers/sections/bondal_cubic.tex` に証明全文、`notes/bondal_cubic.md` に次の監査点。現行の正規形 `thm:pg-normal` に依存する。旧正規形のLie代数補題と射影ランク低下の独立監査が次の優先事項。Fano4/5の既知結果と新規性を区別する。

## Point schemeの現行結果

混合族の全滑らかな係数λ（λ³+3≠0）に拡張。Sklyaninが滑らかなh⁶+27≠0、h非零でPoint(B)=E_h⊔S_{h,λ}。有限部分の環はmonicなx²+λy,y²+λx,z²,v³+1+λxy/3+h²z(λ²/6−2xy/3)で自由rank24。vは単元、明示せん断でh方向の抽象同型。h=0のflat schematic closureはPoisson零点の埋め込みスキーム。λ≠0で12二重点、λ=0で3八重点。証明 `papers/support/papers/reconstruction/point_scheme_lambda_family.tex`、ノート `notes/point_scheme_poisson_zero.md`。Sklyaninの点列scheme/translationは既知入力。特異λ³=−3・退化h⁶=−27と一般nc cubicは未解決。

## 特異境界の有限点の局所型

判別式λ³=-3を越えて孤立point-module可換化環のC[λ,h]自由rank24が証明された。境界h≠0で3×2 +3×6、六重点はC[v]/(v^6)、h=0ではC[v,z]/(v³,z²)。hλ≠0で局所一変数式(v³+(λ³+3)/3)²=0。論文Cの `point_scheme_discriminant_boundary.tex` を使用。Sklyanin部分の退化h⁶=-27と、特異cubicのPoisson零点定理は別扱い。h=0の代数的延長をB0のpoint schemeと同一視しない。証明原稿と有限計算証明書を残す。

## 現行の結論と依存

(L)局所proper/windowと(CF)実際の完備MF同値下の一変数量子化について、有限拡大K'/C(h)上の全coherent残余pairの可換復元を得る。lambda=1の明示式には(D)も必要。既存全依存を独立再監査した意味ではない。

一般点では非零像の三shiftが生成するためLaurent体上の同値が得られ、compact核の有限表示性で有限体拡大へ降下する。完備底全体の逆核を先に作る課題へ戻らない。

新節coherent_residual_saturation.texは、B=A/(w)のGorenstein/section条件から任意MのRHom(O(j),M)が体上perfectであることと全twistによる検出を示す。smoothな線束生成代数の対角によりRHom(G,M)はその代数上perfectとなり、評価coneの直交からC_lin=Db(qgr B)。残余smoothnessと有限例外貼合せで適用し、K_lin=K_cohを得る。一般点以外で無条件の一致を宣言しない。

## 次に進めること

(CF)の曲率formality/coherent inverse全構成、(L)の通常導来stabilization/window、(D)の乗法的比較を独立監査する。今回点検済みなのはStevenson Thm6.13の適用範囲、次数再付与、固定HomのLaurent局所化と、新しい飽和証明。

同値核の行列・有限拡大次数・三shift生成の有効なcell上界は未計算。全Db(qgr B)と可換Db(coh Y)の同値は主張しない。残余同値では貼合せが残る。多変数族・全モジュライ一般点・特殊点を含む相対同値は別課題。

## 保持・検証

論文A/B/Cの有効な証明・コード・必要証明書・反例を保持する。一般KFは未解決だが現行経路の前提でない。項別自由性だけの生成子持上げは偽のまま。smoothness・perfect性・通常導来底変更を区別する。既知の飽和原理を新規成果としない。

`python3 scripts/verify_coherent_residual_assets.py --rerun-orbit` と `latexmk papers/paper_c.tex`。前者はsource参照と旧64 Euler/41 MF恒等式の再現確認であり新定理の形式検証でない。今回新単独稿5頁を組版・表示確認、A/B/C全体は未組版。検証状況はvalidation.jsonに分離する。

## 保存

区切りごとに承認を求めず、証明全文・研究方針・ノート・必要ソースをmainへ通常のfast-forwardで反映する。全文の代わりに要約だけを保存しない。remote headと既存変更を保持し、force push・無断PR・GitHub Actions禁止。refと変更blobを照合する。

成功時はLibraryへ二重保存せず、実際のGitHub失敗時のみ緊急退避する。既存Libraryファイルを無断削除しない。日本語LuaLaTeX、PDFはGit追跡せずbuild/へ生成。旧版ZIP・ログ・cache・重複は追加せず、数学的内容と再現性を容量制限のため削らない。

## papers/の配置規則
papers/直下に置くファイルはpaper_a.tex、paper_b.tex、paper_c.texのみ。補助TeX・参考文献・短い独立原稿はpapers/support/papers/以下に配置する。主原稿はpapers/support/をinput探索先として使用する。新たなpapers/直下のファイルを作らない。

## 量子中心三次元の現行結果と作業順
論文A thm:pg-fermat-mixed-universal（六つの独立中心係数のFermat混合中心元）は、computations/verify_universal_fermat_mixed_center.pyによりQ(h)上の339列・162関係・階数144・三交換子剰余0とh=0の同階数を厳密検証済み。形式的中心存在を仮定しない。中心平行移動で対角二次混合を含む。論文A thm:pg-universal-determinantは任意の滑らかな三変数制限gに対するCramer決定式で、形式中心存在補題に依存する。検算はcomputations/verify_universal_casimir_minor.py。研究ノート notes/universal_casimir.md をまず参照し、Hesse一般tの短い普遍式探索と形式中心補題の完全監査を続ける。数学的に価値のある既存のFermat式を単に有限特殊化候補と呼び直さない。一般の特異gまで一つの式で覆うとは主張しない。
