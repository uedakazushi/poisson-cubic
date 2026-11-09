# 研究ノート：三論文の接続と独立した境界研究

**2026年11月9日・整理版v7。** 研究日誌ではなく、現在有効な主張・障害・証明の位置だけを記載する。

## 記法と三つの復元の区別

論文Bでは `B` をambient二次AS-regular代数、`G∈Z(B)_3` を中心三次元、`A=B/(G)` をcubicと書く。論文Cでは元の可換化研究に従いambientを `A_h`、中心商を `B_h=A_h/(Ω_h)` と書く。両者は同じ種類の対象で記号を反転している。

(1) `(qgr A,O,(1))` からsection Z-algebraを取り、二次包絡でambientを復元する**偏極付き復元**、(2) Serre関手から偶数Veroneseを取り奇数次数を下降する**構造対象付き条件付き復元**、(3) `(Ku(A),ρ_A)≃(Ku(Y),ρ_Y)` という**rotation付き可換復元**は異なる。Bの結果はCの一般存在を含意しない。

## A：Poisson構造と代数的量子化

Poisson正規形は三変数Jacobianブロックと中心変数。量子化は二次cyclic-potential関係式を明示し、中心三次元は形式持上げ・代数化を別々に扱う。滑らかなHesse型の三次中心元と点曲線パラメータは明示的だが、一般の本質的中心変数混合項は統一閉公式がない。Hesse側の各fiberの可換復元は論文Cに置き、Aには重複する圏同値の証明を置かない。

## B：一般17次元族の証明依存

三次式 `F(x,y,z,u,v)`、中心一次平面 `U=<u,v>`。41次元の中心三次対パラメータと一般PGL5軌道24次元から有理商次元17。正規形の31×31整数行列式は `−5538243375000`。実際の群軌道・PBW相対性・一定rank中心元が必要で、単なる次元数えでは同型類17次元を主張しない。

偏極付き復元では `A_1=B_1`, `A_2=B_2` から二次包絡 `Q(A)=T(A_1)/ker(A_1⊗A_1→A_2)=B`、三次の核 `ker(B_3→A_3)=CG`。section環の同定は別の入力であり、`O` や `(1)` を忘れてはならない。Serreからの強化はtails有限大域次元・中心二次・中心二変数上の自由性を仮定する。

全17次元に対する相対saturationとcanonicalな可換cubic模型は未解決。一般族のmoduliと `(Y,Λ,ξ)` の候補の次元一致17は証明ではない。

## BからCへの橋渡し：分離型の法線方向

論文B `tex/generic17_ambient_recovery.tex` の命題 `prop:split-codimension` と系 `cor:split-normal-directions` に証明を置く。中心一次平面 `U=⟨u,v⟩` を固定した35次元の三次係数空間において、分離型 `F=f(x+L(u))+g(u)` の像は20次元。座標変換群の一般軌道は18次元なので、17次元の全有理商の中で分離型の有理商は2次元、余次元15である。これは偏極付きPoisson中心三次対の有理商の次元であり、無標識導来圏のmoduliの次元ではない。

固定分離点の法線は `U⊗(Sym²W/⟨f_x,f_y,f_z⟩) ⊕ W⊗Sym²U`、各次元6と9。まず6方向の量子化と中心補正を追い、次に残り9方向の相対Orlov比較・saturationへ進む。有限計算 `computations/verify_split_codimension.py` は有理数体上で接空間階数20・軌道階数18を再現するが、一般の圏同値の証明ではない。

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
