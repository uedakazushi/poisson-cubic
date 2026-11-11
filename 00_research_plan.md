# 研究方針：Poisson cubic論文Aの投稿品質確立と非可換cubicの可換復元

**2026年11月12日 / v44。再開時は最初に読む。GitHub uedakazushi/nc-cubic の main が唯一の正本。**
**現在の最優先課題は論文Aの公表水準への改訂。** 最新原稿は papers/paper_a.tex、
詳細な監査・未確認点・着手方法は notes/poisson_article_submission_audit.md。
関連文献は papers/support/papers/references_poisson_cubic.tex、独立検算は computations/verify_poisson_article_A.py と computations/verify_cubic_casimir_jet.py。
論文B/Cの有効な成果と証明を保持するが、当面はその新規拡張を優先しない。

## 最優先課題：論文Aを公表可能にする

**達成基準：** (i) Poisson正規形とBondal予想を含む主要定理の証明と仮定が独立に監査され、
(ii) 量子化の形式的中心元・PBW・代数化について一次資料と比較してギャップが解消され、
(iii) 新規性と既知結果の境界がIntroductionに明記され、
(iv) 全LuaLaTeX入力・引用・計算証明書を必要な範囲で再生成し目視検証できること。
これらを満たすまでは投稿準備段階と記し、投稿可能とは断定しない。

**すでに行った整備：** Abstract/Introductionを大幅改訂し、20件の専用bibliographyに分離。
文献キー・文書内label/refの静的整合性はPASS。二ブロックcubicのJacobi56成分と
Bondal joinの外積56成分を厳密計算でPASS。これは主定理の形式証明ではない。
A全体の組版、非楕円行列証明書全件の再実行、引用理論の全独立監査は未実施。

**新たに確立した低次結果：** 論文Aの lem:pg-center-parity と prop:pg-universal-casimir-jet により、三次中心元はWeyl表示でhの偶数次だけを含む形に選べる。全20係数を持つ任意の三変数以下三次式 f について、sym(f-h² det Hess_x f/12) は mod h⁵ で中心であることを普遍恒等式として確認した。厳密計算証明書は computations/verify_cubic_casimir_jet.py。これは全次数中心元の存在と区別する。Etingof–Ginzburg Prop.8.1.1(i)、Berger–Taillefer Thm.1.1(i) の原PDF該当箇所を確認した。現在の証明監査の残核は、複数中心変数への相対formalityと完成CY双加群分解の適用である。

**次に行う数学的作業：** まず lem:pg-formal-center の相対Kontsevich formality、
完備双加群分解からの絶対Calabi–Yau性、Dolgushev入力、prop:pg-PBWを
一次文献と逐語照合する。次に lem:pg-quadratic-lie（Bertini、可解根基、最高根）、
prop:pg-represent、lem:pg-linearizeの未監査部分を解消する。最後に全定理・検算・組版を査読可能に整理する。
滑らかなcubic threefoldのGrassmann記述は既知、Fano四・五次元のBondal予想も既知。
高次元cubicへの帰結や非楕円Poisson成分の新規性の網羅調査は未完了。
全Poisson係数で一様な量子化や中心商のqgr smoothnessは主張しない。

## 保持する論文A/B/Cの研究到達点

## Poisson構造定理の新たな帰結：Bondal予想（論文A）

**証明を追加。** n>=3の滑らかなcubic n-foldの任意のPoisson構造に対して、全j（2j<n）のD_{2j}は次元2j+1以上の既約成分を持つ。非零Poissonの正規形F=Σ f_s(x_s,u)、一般rank2kを使い、j<kならr=j+1個のブロック内の平面曲線C_s⊂{f_s(x_s,0)=0}のjoin J_rを構成する。J_r⊂X、dim J_r=2r−1。全ブロックのJacobian rank2ならEulerベクトルが像に入り射影化でrankが2下がり、いずれかrank0ならもとからrank≤2r−2。従ってJ_r⊂D_{2j}。π=0またはj>=kはD=X。全文 `papers/support/papers/sections/bondal_cubic.tex`、ノート `notes/bondal_cubic.md`。**正規形定理thm:pg-normalに依存し、その既存証明全体の独立再監査は未完了。** 2013年Fano4、2026年Fano5の既知定理との重複に注意し、新規性は未確定。正規形のLie代数補題を次に優先監査する。

## Point schemeの二パラメータ族とPoisson零点（論文C、証明あり）

**混合係数λの全滑らかな値へ拡張。** F_λ=(x³+y³+z³)/3+u³+v³+λuxy、λ³+3≠0、h⁶+27≠0。h≠0のB_{h,λ}のpoint module初期点の表現スキームは、λに依らないSklyanin Hesse楕円曲線 E_h: u=v=0, x³+y³+z³+h²xyz=0 と、u=1上の有限スキームS_{h,λ}の非交和。有限部分の可換商は x²+λy=y²+λx=z²=0, 1+v³+λxy/3+h²z(λ²/6−2xy/3)=0。基底 x^a y^b z^c v^d (a,b,c=0,1; d=0,1,2)によりλ,h同時に自由rank24。λ³+3≠0ならvは単元で、v'=v+h²z(λ²/6−2xy/3)/(3v²)によりS_{h,λ}はh方向に抽象的に自明。

**scheme-theoretic平坦極限。** E_h⊔S_{h,λ}は二パラメータで平坦、h=0の埋め込みスキームはX_λ上のPoisson零点D_0(π)。Hilbert多項式は3t+24。h=0の非可換代数そのもののpoint schemeはX_λ全体であり、平坦閉包とは区別する。

**λ=0の衝突。** λ≠0ではSは12個の長さ2の非被約点。λ=0では3個の長さ8の点へ衝突し、各局所環は C[x,y,z]/(x²,y²,z²)、Hilbert関数(1,3,3,1)。全長24は保存。λ³=−3では元のcubicが特異、h⁶=−27ではSklyaninが退化するため適用外。

証明全文は `papers/support/papers/reconstruction/point_scheme_lambda_family.tex`、再生成可能な単独LuaLaTeX入口は `papers/point_scheme_lambda_family.tex`、現行研究ノートは `notes/point_scheme_poisson_zero.md`、厳密検算は `computations/verify_lambda_point_scheme.py`。前段のλ=1非被約・平坦極限の証明は `point_scheme_thickening.tex` に保持。3D Sklyanin point-scheme定理は既知入力。一般のnc cubicに対する同一結果や全先行研究上の新規性は未確認。

## 特異な混合係数境界でのpoint scheme（論文C）

**証明済みの有限平坦モデル。** 特殊値 λ³=-3 では元の可換cubicが特異となりPoisson多様体の零点定理の適用外だが、既存の中心座標u=1における有限point-module可換化環は C[λ,h] 上で自由rank24（基底 x^a y^b z^c v^d、a,b,c=0,1; d=0,1,2）。これは λ,h の分母を使わず、判別式境界やh=0にも代数的に延長する。**h=0のこの環はB_0自身のpoint schemeではない。**

λ³=-3、h≠0では支持が6点：x=y=0から3個の二重点、非零x,yの3枝に各局所環C[v]/(v^6)の曲線的六重点。h=0では同じ3枝の局所環はC[v,z]/(v³,z²)となり、長さ6は同じでも埋め込み次元は1から2へ変化。δ=λ³+3を境界の局所パラメータとすると非零枝で hλ≠0 の模型は (v³+δ/3)²=0で、一般λの3二重点が判別式上で1六重点に合体する。証明: `papers/support/papers/reconstruction/point_scheme_discriminant_boundary.tex`、単独LuaLaTeX `papers/point_scheme_discriminant_boundary.tex`、有限検算 `computations/verify_lambda_discriminant.py`。

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

論文Aの一般Poisson正規形・固定方向の代数的量子化、論文Bの41次元中心対・17係数slice・ambient復元・分離型余次元15・忘却核7を保持する。全nc cubic分類や全係数の一様量子化と混同しない。

論文Cの形式MF、相対window、有限積分、全16積、bar/cup/characteristic比較、幾何学的BC、片側Morita/Popescu、相対sector、対角unit、中心対称性、純Poisson一次消滅、分離Hessian、非楕円fivefold、35係数slice、A∞arity、SM/ERおよび反例を保持する。有効な証明を容量削減のため要約・削除しない。

## 論文Cの保留課題（論文Aの投稿準備を優先）

1. **残る依存の独立監査。** 今回はStevensonの適用範囲、次数再付与、固定HomのLaurent局所化を点検した。次に(CF)の曲率formality・coherent inverseの全構成と、(L)の通常導来stabilization/window、明示式への(D)を順に監査する。証明の記載と独立監査を区別する。
2. **有効化。** 三shift生成の有限cell、同値核の行列、有限拡大次数を明示する。今回、線束生成代数の対角のq段表示があれば全coherent対象もq段で生成されることを示したが、qは未計算。
3. **範囲拡張。** 一般lambdaの明示式、独立中心変数のない成分、多変数基底・全Poissonモジュライ一般点への適用を検討する。一変数の結果から無条件に一般化しない。
4. 特殊点を含む相対同値には、保持した片側compact形式核・Popescu・SM経路を使う。今回の有限体拡大降下は形式分枝全体の再現ではない。

## 証明・計算・再現の状態

新定理の証明と一次資料を確認：Burke–Stevenson1507.00830v1 Prop4.18/Lemmas6.1–6.2/Thm6.4、Toën–Vaquié0503269v5 Lemma2.8(2)、Perry Lemma4.15(3)。Stevenson1105.4698v3 Thm6.13とDyckerhoff0904.4713v5 §2.4を原PDFで再確認した。一般原理の新規性は主張せず、包括的新規性調査・外部査読・形式証明は未実施。

`python3 scripts/verify_coherent_residual_assets.py --rerun-orbit` は新原稿の参照とCへの統合を点検し、既存64 Eulerベクトルと32×32行列41恒等式を再実行する。今回、既存コードおよび生成証明書のGit blob SHAが正本と完全一致した。新しい飽和定理の形式証明やnc全行列の再計算ではない。

`latexmk papers/coherent_residual_saturation.tex` で新単独稿を生成する。単独稿5頁の組版と表示を確認。現行A/B/C全体の組版、CF全構成と全既存計算の再検証は未実施。正確な状態をvalidation.jsonに記す。

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
