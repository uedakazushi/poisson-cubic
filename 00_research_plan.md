# 研究方針：非可換cubicの一般点復元

**2026年11月11日 / v39。再開時は最初に読む。GitHub `uedakazushi/nc-cubic` の `main` が唯一の正本。**
次は `notes/bondal_cubic.md`、`notes/coherent_residual_saturation.md` と `notes/rotation_orbit_generic_reconstruction.md`。具体式は `notes/curved_diagonal.md`、形式比較は `notes/geometric_rotation_basechange.md`。完備底全体の別経路は `notes/one_sided_morita.md`。一般背景は論文A/B/Cと `notes/research_notes.md`。旧ZIP・会話を再開条件にしない。

## Poisson構造定理の新たな帰結：Bondal予想（論文A）

**証明を追加。** n>=3の滑らかなcubic n-foldの任意のPoisson構造に対して、全j（2j<n）のD_{2j}は次元2j+1以上の既約成分を持つ。非零Poissonの正規形F=Σ f_s(x_s,u)、一般rank2kを使い、j<kならr=j+1個のブロック内の平面曲線C_s⊂{f_s(x_s,0)=0}のjoin J_rを構成する。J_r⊂X、dim J_r=2r−1。全ブロックのJacobian rank2ならEulerベクトルが像に入り射影化でrankが2下がり、いずれかrank0ならもとからrank≤2r−2。従ってJ_r⊂D_{2j}。π=0またはj>=kはD=X。全文 `papers/sections/bondal_cubic.tex`、ノート `notes/bondal_cubic.md`。**正規形定理thm:pg-normalに依存し、その既存証明全体の独立再監査は未完了。** 2013年Fano4、2026年Fano5の既知定理との重複に注意し、新規性は未確定。正規形のLie代数補題を次に優先監査する。

## Point schemeとPoisson零点（混合lambda=1）

**スキーム論的にも証明（論文C新節）。** 非零一般h（h^6!=-27）のB_h=A_h/(Omega_h)のpoint moduleの初期点集合はE_h⊔Σ。E_hはu=v=0のSklyaninのHesse曲線 x³+y³+z³+h²xyz=0、Σはu!=0の固定点12点。Poisson零点の台はE_0⊔Σで、E_0はFermat曲線。h=1の(1,1,-1,0,0)はpoint scheme上だがX0上でない。Poisson零点のΣ部分はスキーム長24（12点、各横断長2）。point schemeの孤立12点もそれぞれ長さ2で総長24。Poisson零点の孤立厚化と抽象的には同型だが、射影空間での接方向は異なる。明示同型はv'=v+h²z(1/6−2xy/3)/(3v²)。E_h方向の中心変数の余分な厚化はSklyanin shiftの非自明平行移動と中心性から排除。全文 papers/reconstruction/point_scheme_thickening.tex。論文Cの `papers/reconstruction/point_scheme_poisson_zero.tex` と `notes/point_scheme_poisson_zero.md` を参照。これは一般のnc cubicのpoint scheme分類ではない。

## 最終目標と現在の結論

構成した代数的nc cubicの幾何学的一般点について、全coherent残余圏を滑らかな可換cubicのKuznetsov成分から、指定rotationと三次周期性を保って復元する。存在、方程式、同値核の明示化を区別する。

**既存入力(L),(CF)下の一変数量子化では、有限拡大K'/C(h)上で全coherent残余pairの可換復元が得られる。** (L)は局所proper/window模型とHom底変更、(CF)は次数別完備底上の実際の有限rank MF A∞同値であり、互換なArtin同値の列だけではない。明示的なlambda=1の多項式を復元先に取るには既存の有限対角比較(D)も使う。これらの既存証明を今回全部独立再監査したという意味ではない。

今回、中心三次商のGorenstein条件から全coherent対象に対する線束Homの有限性と検出性を得て、線束生成部分がsmoothなら全coherent導来圏に一致することを証明した。既存の一般点同値から残余smoothness、有限例外成分との貼合せから線束部分smoothnessが従う。したがってK^linと全coherent残余圏の差は、この一般点・AS-regular入力の範囲では残条件でなくなった。

全Db(qgr B)と可換Db(coh Y)の同値は主張しない。残余同値でも例外成分との貼合せは異なり得る。Bそのものの有限global dimensionも主張しない。特殊点を含む相対同値、有限拡大次数・同値行列、多変数の全モジュライ方向は未完成。

## 現在の最短証明経路

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

## 次の優先課題

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
