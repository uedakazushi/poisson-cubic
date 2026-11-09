# 研究ノート：三論文の接続と独立した境界研究

**2026年11月9日・整理版v9。** 研究日誌ではなく、現在有効な主張・障害・証明の位置だけを記載する。

## 記法と三つの復元の区別

論文Bでは `B` をambient二次AS-regular代数、`G∈Z(B)_3` を中心三次元、`A=B/(G)` をcubicと書く。論文Cでは元の可換化研究に従いambientを `A_h`、中心商を `B_h=A_h/(Ω_h)` と書く。両者は同じ種類の対象で記号を反転している。

(1) `(qgr A,O,(1))` からsection Z-algebraを取り、二次包絡でambientを復元する**偏極付き復元**、(2) Serre関手から偶数Veroneseを取り奇数次数を下降する**構造対象付き条件付き復元**、(3) `(Ku(A),ρ_A)≃(Ku(Y),ρ_Y)` という**rotation付き可換復元**は異なる。Bの結果はCの一般存在を含意しない。

## 一般次元・全Poisson既約成分の計画

固定滑らかなcubic $X^n$（$n\ge3$）のPoissonスキーム $\operatorname{Pois}(X)=\{\pi:[\pi,\pi]=0\}$はアフィン錐。既約成分への$\mathbb G_m$作用は連結性により不変なので全ての成分に零が属する。可換cubicを動かす場合も同じ議論。これにより、成分ごとの一つの滑らかな可換点から相対量子化へ進む構成が可能となる。

**条件付きgeneric復元**：既約成分の零Poisson点のZariski近傍上に、PBW・中心正則商がflatで、残余dg圏がsmooth properかつ代数的rotationを持つ族が存在すれば、論文Cの既存étale局所復元で稠密開上の可換模型が存在する。存在条件の成分横断的検証は未完成。各一点に対応する形式量子化があるだけでは代数的な相対族にはならない。

**次元別rotation**：$S\simeq\rho^{1-n}[n]$と$\rho^3\simeq[2]$から、$3a+(1-n)b=1$を満たす$a,b$があれば$\rho\simeq S^b[2a-nb]$。よって$n\not\equiv1\pmod3$ではこの必要関係を満たすrotationはSerreとshiftから決まり、$n\equiv1\pmod3$ではSerreは$[(n+2)/3]$に退化し、別のrotation不変量が必要。既存の$n=4$のZhang twist反例はこの区別を示す。

**一般位置でのrank**：現行論文AのPoisson正規形では$n+2=3k+m$として三変数Jacobianブロック$k$個と中心変数$m$個で表示される。一般階数$2k$ごとの層は重要だが、各$k$が既約成分と一対一対応することは主張しない。同じrankでも異なる既約成分の可能性を残す。個々の既約成分の成分スキーム構造と、一様中心規格化・法線方向の接着は引き続き調査事項。

**非可換モジュライ全体との差**：任意のAS-regular中心三次商の各点で可換模型が存在するという命題は既存Zhang twist反例で偽。しかし反例点の存在だけでは、可換点に接続しない任意の非可換既約成分の一般点が非幾何的だとは結論できない。Poisson全成分と非可換全成分は別問題。

詳細な補題・証明は論文Cの `tex/papers/all_poisson_components.tex` を参照。

## A：Poisson構造と代数的量子化

Poisson正規形は三変数Jacobianブロックと中心変数。量子化は二次cyclic-potential関係式を明示し、中心三次元は形式持上げ・代数化を別々に扱う。滑らかなHesse型の三次中心元と点曲線パラメータは明示的だが、一般の本質的中心変数混合項は統一閉公式がない。Hesse側の各fiberの可換復元は論文Cに置き、Aには重複する圏同値の証明を置かない。

## B：一般17次元族の証明依存

三次式 `F(x,y,z,u,v)`、中心一次平面 `U=<u,v>`。41次元の中心三次対パラメータと一般PGL5軌道24次元から有理商次元17。正規形の31×31整数行列式は `−5538243375000`。実際の群軌道・PBW相対性・一定rank中心元が必要で、単なる次元数えでは同型類17次元を主張しない。

偏極付き復元では `A_1=B_1`, `A_2=B_2` から二次包絡 `Q(A)=T(A_1)/ker(A_1⊗A_1→A_2)=B`、三次の核 `ker(B_3→A_3)=CG`。section環の同定は別の入力であり、`O` や `(1)` を忘れてはならない。Serreからの強化はtails有限大域次元・中心二次・中心二変数上の自由性を仮定する。

全17次元に対する相対saturationとcanonicalな可換cubic模型は未解決。一般族のmoduliと `(Y,Λ,ξ)` の候補の次元一致17は証明ではない。

## BからCへの橋渡し：分離型の法線方向

論文B `tex/generic17_ambient_recovery.tex` の命題 `prop:split-codimension` と系 `cor:split-normal-directions` に証明を置く。中心一次平面 `U=⟨u,v⟩` を固定した35次元の三次係数空間において、分離型 `F=f(x+L(u))+g(u)` の像は20次元。座標変換群の一般軌道は18次元なので、17次元の全有理商の中で分離型の有理商は2次元、余次元15である。これは偏極付きPoisson中心三次対の有理商の次元であり、無標識導来圏のmoduliの次元ではない。

固定分離点の法線は `U⊗(Sym²W/⟨f_x,f_y,f_z⟩) ⊕ W⊗Sym²U`、各次元6と9。まず6方向の量子化と中心補正を追い、次に残り9方向の相対Orlov比較・saturationへ進む。有限計算 `computations/verify_split_codimension.py` は有理数体上で接空間階数20・軌道階数18を再現するが、一般の圏同値の証明ではない。

## Bと可換Jacobian変形の接空間比較

分離cubic `F=f(x)+g(u)` のJacobian環は分離テンソル積で、三次変形空間の次元は `1+6+3=10`。17次元のPoisson中心三次対の係数/放物型軌道の接空間から10次元の通常の可換cubicのJacobian変形空間へは全射で、核7次元。
分離型の商2次元は可換cubic変形へ1次元に写り、法線15次元は9次元に写って6次元が核になる。これを `17=10+6+1` の幾何模型の示唆として扱う。ただしこの忘却対象は最初の可換三次式であって、量子化後のrotation付き復元による可換モデルとは未同定である。本文命題 `prop:jacobian-forgetful-tangent` と `computations/verify_split_codimension.py` 参照。

## Poissonスカラー7次元核の完全な解釈と固定基底の障害

論文B `prop:vertical-seven` に、分離点の短完全列
`0→C[f]⊕Hom(U,W)→T_(F,U)(17)→Jac(F)_3(10)→0`
を記載。中心形式の部分空間 `U=⟨u,v⟩` が指定する平面の移動が `Hom(U,W)`。その接写像は `ℓ_u(x)g_u+ℓ_v(x)g_v` で、Jacobian方向では零。残る `[f]` はPoissonスカラー。放物型軌道18次元と垂直7次元を合わせるとJacobianイデアル25次元と一致することを有理数体上で検算。これは非可換cubicの全てのファイバーがsmoothである証明ではない。

固定 `(X,Λ)` のスカラー `G_m` と `Pic⁰(X∩Λ)` の間に非定数一価有理写像がないことを論文B `prop:poisson-picard-obstruction` で証明した。前者は有理曲線、後者は種数1。有限多価対応や量子化後に可換側の `Y` を動かす復元は排除しない。形式的変形では局所同定があり得るため、これを形式復元に対する反例と誤解しない。

## 中心量子化の独立検算と一次持上げの一意性

既存技術稿§14.3のFermat混合15方向の中心三次元について `computations/verify_mixed_center.py` を追加。標数1009、5つのh、各3組の混合係数の15特殊化で三交換子が次数四の関係イデアルに属することを厳密に確認（イデアル階数555）。`h²A²z/6` を省いた式は中心でないという負例を保持する。**有限特殊化の検査は普遍的な中心性の証明ではない。** 本文 `rem:full-mixed-center` と既存技術稿の全係数証明、Etingof–GinzburgのRains型公式を参照。

命題 `prop:mixed-center-jet-unique` は `Z(S_h)_2=0` と平方零の中心変数に対する次数別PBW自由性の下で一次中心持上げの一意性を証明する。二つの持上げの差 `uQ+vR` が中心なら `Q,R∈Z(S_h)_2=0`。h=0の可換特殊化には適用しない。

命題 `prop:relative-scalar-picard` はPoisson pencilのGrassmann開部分に相対化する。関数体上の一般スカラー繊維がG_mであり、P¹から楕円曲線への非定数射がないため、相対Picardへの有理写像はスカラー方向に定数。幾何学的一般スカラー繊維の連結有限étale被覆もG_mなので同様。分岐被覆や動く可換cubicを通じた復元を否定しない。

## C：rotation付き可換復元と障害

形式的marked復元、一定のsmooth proper代数的dg族の下でのétale局所復元、一楕円ブロックのファイバーごとの可換同値を得る。Hesse係数 `θ(h,t)=[t+h²(1+t³/4)/3]/[1-h²t²/4]`。固定tで可換模型のmarkedな二次変形は非自明。θ一定の代数曲線上で非可換代数が動いても各fiberの残余pairが同じ可換模型となる。底上の相対同値は証明していない。

Calabi–YauなZhang twist反例は広いAS-regular中心三次商の**普遍的な存在定理**を否定するが、可換点を含む指定量子化族の全ファイバーについての反例ではない。二つ以上の無限位数Sklyaninブロックの全生成も未解決。

## 独立した境界研究と未整備な証明書

Brill–Noether / Pfaffian：評価核・接錐・接触商・形式正規形の証明を技術TeXに保持する。原稿内の全次数消滅や高次接触は独立再検証していない。
Reye / 停留平面：275停留平面・550曲線、monodromy、非被約局所模型について原PDFに詳しい主張・証明がある。PDFのみの部分は編集可能なLuaLaTeXソースが欠けるため、証明を推測で再作成しない。
中心三次商の正則性・特異圏：有限中心、Azumaya locus、Brauer指数の議論は独立原PDFへ譲る。仮定と一般係数での適用は追加検証が必要。

境界研究の各原稿は独立性と詳細な計算証明の有無により分割する。古い抽出TXTは正式な数式の証明資料ではない。保持したPDFを一次原稿として参照する。

## 先行研究の入口

Artin--Zhang（偏極付きsection algebra、`doi:10.1006/aima.1994.1087`）、Mori--Smith（三変数Jacobian代数、`arXiv:1502.07403`）、Etingof--Ginzburg（中心・PBW、`arXiv:0709.3593`）、Lin--Zhang（polarized categorical Torelli、`arXiv:2310.09927`）、Toën--Vaquié（dg圏の対象のmoduli、`arXiv:math/0503269`）。正確な箇所・仮定・既知主張と本研究の区別は各論文の文献表を参照。新規性の包括的監査は未完了。

## 一楕円ブロックの相対化に固有の核心

固定した滑らかなHesse係数tについて `R=ℂ[h,(UbΔ)^{-1}]` 上の相対THCR表示から開始する。Burke–Stevenson（arXiv:1507.00830、Definition 5.1とTheorem 6.4）を使うには左右noetherian性、相対Gorenstein性、window、底変更、relative perfect部分でのdg比較を別々に検証する。相対楕円曲線の線束 `O(p-o)` は平行移動を共役する候補だが、相対rotationと三次周期性を含む同値をまだ構成していない。二次変形のJacobian類の非零性を示すことと、残余pair変形の相対Kodaira–Spencer写像の核を求めることも別問題。

## 現行のPDF-only資料の扱い

`pdf/ambient/` は中心対・有限次数正則性の技術的原PDF、`pdf/quantization/` は一般混合SklyaninとPoisson二次ジェット、`pdf/boundary/` はBrill–Noether・Pfaffian・Reye・特異圏の独立原稿である。編集可能なTeXが存在しない部分については、既存のPDFを唯一の証明として保存し、PDF抽出テキストを正本としない。可換復元の論文Cにその証明を無断で移植しない。

## 再開時の作業

まずA–C各論文の仮定と用語を整合させ、Bの相対中心とCの相対Beilinson仮定を比較する。次にgeneric `(Y,Λ,ξ)` に対する実際のgluing対象とrotationを構成し、中心三次対との有限型対応・降下を証明する。補助計算が成立しただけでは大域復元の完成とは扱わない。
