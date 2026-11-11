# 混合nc cubicのpoint schemeとPoisson零点

**2026-11-11 / v42。最初に00_research_plan.mdを読む。GitHub mainが正本。**

## 現行の主要結果

二パラメータ族 F_λ=(x³+y³+z³)/3+u³+v³+λuxy、λ³+3≠0、h⁶+27≠0 において、h≠0のpoint moduleの初期点スキームは楕円曲線 E_h と有限スキーム S_{h,λ} の非交和。E_h は u=v=0、x³+y³+z³+h²xyz=0でλに依存しない。Sはu=1チャートの可換化で表す。

有限環は R[x,y,z,v]/(x²+λy,y²+λx,z²,1+v³+λxy/3+h²z(λ²/6−2xy/3))、R=C[λ,h,(λ³+3)^(-1),(h⁶+27)^(-1)]。x^a y^b z^c v^d（a,b,c=0,1;d=0,1,2）を基底とする自由rank24。t=xy, t²=λ²t、(1+λt/3)^(-1)=1−λt/(3+λ³)よりvは単元。v'=v+h²z(λ²/6−2xy/3)/(3v²)によりh方向の抽象的同型が得られる。

h=0で E0⊔S0 はXλ上のPoisson零点スキームD0に**射影空間内の埋め込みスキームとして**一致し、h≠0のpoint schemeのflat schematic closure。Hilbert多項式3t+24。h=0のB自身のpoint schemeはXλ全体である点を保持。

λ≠0ではx,yの4個の単純点と各3個のv根があり、12個の長さ2点。λ=0ではx²=y²=z²=0、v'^3+1=0により3個の長さ8の点に合体。各局所環はC[x,y,z]/(x²,y²,z²)、Hilbert関数(1,3,3,1)。λ³=−3とh⁶=−27は一般定理の適用外。

## 証明と依存

- **直接証明**：可換化のmonic Gröbner基底、24の自由基底、vの可逆性、明示shear、平坦性、12→3支持衝突。全文は `papers/reconstruction/point_scheme_lambda_family.tex`。
- **既知入力**：三次元Sklyaninの滑らかなpoint schemeと非自明translation、中心三次元が点モジュールを消すこと。これによりE_hとその冪零横断方向が決まる。参考文献は現行Cのpoint-scheme節を参照。
- **計算**：`python3 computations/verify_lambda_point_scheme.py --output build/lambda_point_scheme_certificate.json`。λ=0,1,2,-1、h=0,1,2の12個の有理パラメータでGröbner長さ24、二変数多項式恒等式、shearのz²-倍数性を確認。これはSklyanin定理やpoint functorの形式検証ではない。

## 特異境界で得た有限代数的結果

判別式λ³=-3では可換cubicが特異になり、smooth Poisson零点との一致は述べない。しかし有限componentの環はC[λ,h]上自由rank24。λ0³=-3でx=y=0の枝は3二重点、非零x,yの各3枝にh≠0でC[v]/v^6という曲線的六重点。h=0ではC[v,z]/(v³,z²)となり、長さ6を保ちながら埋め込み次元が変わる。δ=λ³+3、x=-λζ、y=-λζ²なら非零hの局所模型は(v³+δ/3)²=0。境界を挟む3二重点→1六重点の衝突を表す。全文 `papers/reconstruction/point_scheme_discriminant_boundary.tex`。全体のSklyanin楕円曲線はh⁶≠-27の既知定理に依存。

## 次の研究課題

この族の結果を一般k=1三変数Jacobianブロックの量子化・多中心変数へ拡張するため、中心一次元のmultilinearized commutationによる定数列の局所模型、非定数列の楕円曲線運動、半古典臨界スキームの埋め込み一致条件を分離して調べる。複数activeブロックのpoint schemeや全nc cubicへの一般化は未証明。λ³=−3特異境界、h⁶=−27退化Sklyaninも別問題として保持。

抽象scheme同型と射影埋め込みの同一性を区別し、既知結果と本研究の寄与、新規性未確認を明記する。
