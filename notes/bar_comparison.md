# 乗法的bar比較と実際のrotation積への残る条件

**2026-11-11 / v28。最初に00_research_plan.mdを読む。GitHub mainが正本。**

## 証明本文と状態

全文は `papers/reconstruction/multiplicative_bar_comparison.tex`。単独入口は `papers/multiplicative_bar_comparison.tex`。有界な同次射影対角分解Pと正規化barの同次special deformation retractionを明示的な入力とする。Koszulの場合はbar内の交叉空間が分裂し、商が項別射影で完全であることを使う。全次数の完全性を有限行列の検算で置換しない。

この入力の下で、曲率付き有限対角のYoneda積と有限支持Hochschild cup積の同定を証明した。Tuの曲率HPLで I,Pi,H を作り、deconcatenationの右cap作用 R_phi を用いる。J(phi)=Pi R_phi I に対し、次数零閉元では

`J(phi)J(psi)-J(phi cup psi)=-d(Pi R_phi H R_psi I)`。

有限対角側からの擬同型は `Q(a)=epsilon_P a Pi`。bar長を完成する一方、cochainはarity直和を保つ。tは線形係数で、t微分を導入しない。別の有限曲率化とは鎖長を上げる有限可逆行列で共役できる。証明の中でdg Lie同型から乗法性を推論していない。

有限支持cochainへのLowenのbrace挿入で、graded MFの内部shift付き導来自然変換への乗法的characteristic写像Thetaを構成した。これは同型性の主張ではない。線形N段対角では内部次数r、コホモロジー次数0の増大射成分は偶数p<=min(N,2r)に限られ、r=1,2の代表はarity<=2,4で取れる。

## 実際の圏との比較に必要な(BC)

R_m=C[h]/h^(m+1)、T_m=graded MF(A_m,Omega_m)とする。標的
`T_(r,m)=Hom_D(T_m^e)(Delta_m,Delta_m(r))`（r=1,2）について、自由rank5,10、自然なH^0剰余同型、Thetaとの両立を確認する必要がある。この条件を(BC)と呼ぶ。

(BC)が成り立てば、特殊fiberでの多項式倍/Jacobian同定と局所環上の単元行列式によりTheta_1,Theta_2は全Artinで同型となる。既存のArtin残余比較を入力すればrotation積へ移る。**(BC)の本研究の族での検証は未完成。** sourceの正則性、体上のBFK/Lin--Zhang公式、導来Homの底変更だけではH^0の底変更を結論しない。

次は既存の形式MF同値で標的を可換形式cubicへ移し、相対の対角kernel/sector複体をArtin底上で構成する。恒等sectorのgradient Koszul複体の相対完全性と非恒等sectorの次数を同時に確認し、その比較が内部shift・自然な剰余写像・Thetaを保つことを示す。可換体上での単なるrank比較では済ませない。

GHLRの包絡代数上の第二種理論とtwisted bimodule理論を同一視しない。外積生成条件・対角の本質像条件の全面解決とは別に、上の低次数条件を検証する経路を優先する。

## 計算済み候補の代数的正規化

v27で得たlambda=1の多項式G_h+v^3について、q=h^6とし
`u=a(q)U+h^2 b(q)Z, z=h^4 c(q)U+d(q)Z`
を使う。四本の多項式方程式は本文の mb:eq:algebraic-system と生成証明書にあり、初期値 `(1,1/36,25/432,1)` でJacobian行列式9。従って指定形式解はetale局所で代数的である。

正規形は
`(x^3+y^3+Z^3)/3+U^3+v^3+L(q)Uxy+h^2 C(q)Zxy`、
`L=1+(127/5184)q+O(q^2)`、
`C=13/36+(1613/1679616)q+O(q^2)`。

これは**計算済み候補の係数**である。元のformalityで選んだW_hの全次数係数と一致するという主張には(BC)と形式比較が必要。一般lambdaの公式、lambda^3=-12の高次係数、generic圏同値は未証明。

## 一次資料と再現

Negron arXiv:1304.0527v4 Theorem5.3（受け手は非曲率dg代数）、Tu arXiv:1009.4151v2 Appendix A Lemma A.1、Lowen arXiv:0707.2602 Propositions3.11,3.13、GHLR arXiv:2312.16645v5 Theorems4.7,6.14/Remark6.16、Lin--Zhang arXiv:2310.09927v2 Theorem3.5/Remark3.6、Stacks Tag00T7を一次資料で確認した。詳細書誌は `multiplicative_bar_references.tex`。既知のcap/HPL/brace原理の新規性を主張しない。

`python3 computations/verify_bar_comparison.py --output build/bar_comparison_certificate.json` は有限テスト代数で曲率144件、cap微分288件、cap積360件、有限SDRの乗法性ホモトピー30件を厳密検算する。うち25件では乗法性の差が非零であり、ホモトピー原像まで一致する。候補への直接座標代入、Jacobian9、最初の係数も再計算する。無限barの一般証明・categorical Nat・v27全行列の検証ではない。

`latexmk papers/multiplicative_bar_comparison.tex` で単独稿を再生成する。主論文Cへ同じ本文をinputし、重複した証明を保守しない。既存の正則対角コードと証明は保持する。
