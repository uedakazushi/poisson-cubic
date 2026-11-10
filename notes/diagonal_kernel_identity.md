# 相対stabilized diagonalの恒等作用と(KF)の残る部分

**2026-11-11 / v30。最初に `00_research_plan.md` を読む。正本は GitHub main。**

## 現在確実な結果

任意の可換環 R、三次斉次 W∈R[z]、有限自由 graded MF M(y) に対し、差分商で定義した stabilized diagonal \(\mathscr D(W(x)-W(y))\) の畳込みが M(x) に自然な**強ホモトピー同値**となる。R の正則性・完備性・h 冪零性を要しない。これは MF の全忠実性や一般 kernel theorem ではなく、対角 kernel の **unit** の構成である。

形式的には s_i=y_i−x_i、a_i=(W(x_1,…,x_i,y_{i+1},…)-W(x_1,…,x_{i-1},y_i,…))/s_i、d₀=Σs_iι_i、δ=tΣa_i(e_i∧−) と置く。Koszul 収縮 h₀ は y_i−x_i の多項式差分商だけで定義する。M の微分を加えた p_M に対し h₀p_M は外積次数を一つ以上上げるから (h₀p_M)^(n+1)=0。従って

`i_M=Σ_{j=0}^n(-h₀p_M)^j i₀`, `H_M=Σ_{j=0}^n(-h₀p_M)^j h₀`

は有限和であり、πD=d_M(x)π、Di=i d_M(x)、πi=1、DH+HD=1−iπ が成り立つ。自然な評価射 π は MF 射とも厳密に可換する。内部shift、µ₃スカラー作用、全Artin底変更が成立する。全文：`papers/reconstruction/diagonal_kernel_identity.tex`。

## 計算と既知の枠組み

`computations/verify_diagonal_identity.py` は t=1 で n=1 の W=y³、n=2 の混合 W=y₁³+y₂³+2y₁²y₂ と rank2/rank4 Koszul型 MF を用い、計606件の有理係数恒等式を確認する。自然なスカラー積、曲率、収縮、包含、射影を検査する。一般証明の代用ではない。生成証明書は `computations/diagonal_identity_certificate.json`。

既知文献：Tu *Matrix factorizations via Koszul duality* (2014), Appendix A, Lemma A.1（曲率付きHPL）；Ballard–Favero–Katzarkov *A category of kernels for equivariant factorizations...* (2014), Theorem 5.22 と Remark 5.21（体上のkernelとfunctor、基底環を一般化したときはderived tensorが必要）；Dyckerhoff *Compact generators...* (2011), §5。既知の一般原理そのものを新規と称さない。一次資料は BFK の該当定理・仮定を今回確認した。相対の明示的 unit formula の初出は未調査。

## (KF) の未解決核心と新しい障害

相対 kernel Hom から実際の導来自然変換 Hom への

`κ_r: Hom_MF(Δst,Δst(r)) → RHom_(T^e)(Δ_T,Δ_T(r))`

が、同一の dg enhancement で定義され、特殊ファイバーで BFK の**全忠実な写像そのもの**になり、導来 Hom を計算する bar 模型が R_m の底変更に両立することは未証明。unit が自然なホモトピー同値だからといって、κ_r の全忠実性を結論してはならない。

特に **項別自由/平坦 != K-flat**。R=k[ε]/ε² 上の両側無限周期複体 `⋯ --ε--> R --ε--> R --ε--> ⋯` は非輪状だが、k への剰余は零微分で非輪状でない。従って、v29 での二側 bar の「各項が R_m-平坦」という確認だけでは、任意の derived tensor のモデルになっていると結論できない。

今後は、指定した graded MF 生成子 G_m=stab(k)⊕(1)⊕(2) に対して **cofibrant（または同等のh-projective）な相対二側bar置換**を与え、κ_r の chain map と本当に同じ BF​​K comparison の特殊化を記述する。これが完成するまで (KF),(BC)、非可換 finite diagonal = actual rotation、formality W との全次数一致、generic圏同値はすべて未証明。
