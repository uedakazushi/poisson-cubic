# 論文Aの投稿準備：現行の監査と再開点

**2026-11-12 / A-v50。** 最初に 00_research_plan.md を読む。
論文本文は papers/paper_a.tex、専用文献は papers/support/papers/references_poisson_cubic.tex。
本ノートは現在有効な知識・依存・課題を整理し、証明全文を重複させない。

## 論文Aの範囲と切り離した詳細幾何

一般次元のPoisson正規形、退化スキームの生成元と零点完全交叉、
Bondal予想、量子化、固定・相対moduli stacksを論文Aの中心に据える。
旧6/7次元専用節`sec:pg-six-seven`と
完全交叉の数値計算節`sec:pg-numerical`は
一般定理の証明の入力ではないため、現行論文Aから除外した。
専用節・数値節は完全なTeX本文として
`uedakazushi/nc-cubic2/papers/sections/`へ移し、
必要な一般退化イデアル・critical coverの証明も
同リポジトリに収録した。
主原稿Aでは`prop:pg-deg-ideal`、`lem:pg-critical-cover`、
`prop:pg-deg-support`、`prop:pg-zero-ci`を全文維持。
旧6/7次元のprimary厚化（長さ8,64,49）と
n=7のCalabi--Yau四次元のHodge数は
移管先の新しい独立草稿に保持されている。
この研究の独立公表価値・主要primary分解の独立監査は未確定。
Aの数学的な中核に必要な証明を外部の草稿へのリンクで代用していない。
最新Aの静的検査では全16入力ファイルに
239個のequation環境、6個のalign環境、210ラベル・225参照、
25文献項目・61引用があり、未解決参照・重複なし。
LuaLaTeX実組版・PDF目視は未実施。

## 任意次元の新しい主定理と検証の状態

論文Aに `general_dimension_universal_quantization.tex` を収録した。
`prop:pg-ad-compatible` は k個のJacobianブロックが相互Schouten可換で、
一般Poisson rankが2#{s:λ_s≠0}と示す。
`thm:pg-all-dimensions` は任意のN=3k+mで、
各純active三次g_s滑らかの下、独立なk変数η_sの
**中心元Ω_η=ΣΩ_{f_s,η_s}、ambient AS正則・中心商AS-Gorenstein、
内部次数ごとの多変数底平坦性**を証明する。
`cor:pg-ad-whole-pencil` は全λ線形族を
(λ,h)↦η_s=λ_s hによる一つの相対代数族で量子化。
`prop:pg-ad-relative-chart` はFのHesse表示係数も動かす。
`cor:pg-ad-hessian` は一般次元のHessian二次補正と四次補正の和。
これらの証明は以前に普遍恒等式を計算検証した
三変数Hesse中心元、相対PBW、Koszul tensor、中心正則性の
filtrationに依存。**本改訂で数学的証明を原稿に追加したが、
依存補題の全てを今回新たに独立再監査したとは限らない。**
適用範囲は固定正規形の一般smooth block locusと
その表示チャートであり、全Poissonモジュライの大域構成ではない。

`computations/verify_general_dimension_multiblock.py` と同じSymPyコードを
ローカルで実行し、滑らかな例
(k,m)=(1,2),(2,0),(2,2),(3,0),(3,3),(4,0)
（n=3,4,6,7,10）についてJacobiator計610成分、
F-Casimir計52成分、異なるブロック間のHessian交差成分を
独立なλ_sを保持した厳密計算で確認した。
`computations/build_general_dimension_center.py` と同等のコードを
ローカルで実行し、共通中心u,vを持つn=6,k=2の明示的な
Weyl中心symbolについてΩ_0=F、η_1η_2の補正なしを確認。
**いずれも全次元の中心性の計算証明ではない。**
GitHubへ保存したスクリプト自体をremoteで再実行したとは言わない。
今後は表示変換による相対族の降下、PBW/AS証明の独立監査、
LuaLaTeX全体組版と一次資料照合を優先し、
特異三次制限への拡張は保留する。

## 内在的な任意次元Hessian補正（最新の強化）

`prop:pg-ad-intrinsic-hessian` により
H(P,F)=(1/6)ΣP^{ijk}P^{abc}F_{ia}F_{jb}F_{kc} は
座標不変の次数三多項式となる。
一般正規形ではΣ_sλ_s²det Hess_{x_s}(f_s)。
全g_s滑らかなら中心三次の正規化を行い、
Ω_{P,h}=sym(F-h²H(P,F)/12+h⁴ K_{P,F}) を
**全次数で厳密な中心三次元**として選べる。
Hessian縮約の全次数・全次元数学的証明は
`papers/support/papers/sections/general_dimension_universal_quantization.tex` に記載。
6具体例でのSymPy独立検算は全てPASS。
h⁴項はHesse座標依存であり、単一座標不変式とは断定しない。
正規形Lie補題、相対AS/PBW入力、Bondal、文献新規性・
LuaLaTeX全組版の独立監査は未完了。

## 主張の確実性と所在

1. Poisson正規形（thm:pg-normal、papers/support/papers/sections/poisson_geometry.tex）：全非零構造の三変数Jacobianブロック分解。n>=3、X smooth。証明は記載済みだが、核心のLie代数補題 lem:pg-quadratic-lie を含め、今回の全面的独立監査は未完了。
2. Bondal予想（thm:pg-bondal、papers/support/papers/sections/bondal_cubic.tex）：全 2j<n について dim D_{2j}>=2j+1。j<k で j+1 個のブロック上の平面曲線joinを構成し、Euler線の射影化でrankが2低下する。正規形定理に依存。scheme-theoretic primary分解を与える主張ではない。高次元での新規性調査は未完。
3. 退化スキーム（prop:pg-deg-ideal）：任意の正規形に適用できる。critical cover と零点の完全交叉（lem:pg-critical-cover、prop:pg-zero-ci）には各 f_s(x_s,0) が滑らかな平面三次という追加仮定が必要。
4. **全Poisson量子化（thm:pg-quantization、thm:pg-universal-determinant、thm:pg-ad-all-poisson）**：全ての滑らかなcubic上のPoisson構造について原点を含む一変数Zariski開上にAS-regular ambientと中心正則三次商を代数的に構成。三変数制限が特異・零でも全体三次のactive gradient gcd=1、古典Casimir核一定、普遍量子交換子行列のminor恒等式とCramer、中心三次の配分Bertiniによって証明。**形式的中心元・formality・Dolgushevを量子化定理の存在証明に使わない。** 相対PBWとAS条件・正規形は従来の入力で全独立監査が必要。モジュライ全係数上の大域的同変量子化やqgr smoothnessは未証明。
5. 非楕円Poisson成分（ne:main）：固定した二つの滑らかなcubic fivefoldのPoisson schemeで2次元成分を示す。35列の線形化Jacobi行列がrank33という整数証明書に依存する。今回全行列を再実行したわけではない。全cubicを動かすrelative成分性を主張しない。
6. Hesse中心元（thm:explicit-hesse-center）：既知Sklyanin公式のPoissonパラメータへの翻訳。基本中心公式の新規性は主張しない。

## 正則三次超曲面のambientの周期性（論文Aに統合）

- **証明済み（仮定付き）**：標準型 (1,5,10,10,5,1) の5次元Koszul AS正則Z代数が、次数3の左右正則な正規族を持つとき、ambientは1周期的。より一般に次元・AS parameter N の対象に次数dの正則正規族があれば、最小周期は gcd(N,d) を割る。**本文の証明**：`papers/support/papers/sections/ambient_periodicity.tex`（定理 `thm:pg-ambient-gcd`、系 `cor:pg-cubic-ambient-periodic`、正規性判定命題 `prop:pg-cubic-normal-criterion`）。主論文入力は `papers/paper_a.tex`。正規族の消去が d 周期、局所Frobenius/Koszul双対性が N 周期を与える。N=5,d=3 なら 2×3−5=1。
- **論文Aとの接続**：定理 `thm:pg-quantization` の量子化は最初からgraded ambientと中心三次元を構成するため、その族の1周期性は自明。新しい帰結は、最初からgradedと仮定せず正則正規三次超曲面を持つZ代数ambientへ拡張する点。非1周期的な一般AS正則Z代数と矛盾しない。
- **未証明**：この構成による任意の1周期同型が三次商イデアルを保つこと、商の同時1周期化、中心化・CY化、任意の抽象的nc cubicの超曲面表示の存在は主張しない。既知の一般論からの系で、結論自体の新規性は未確認。
- **文献**：Bondal--Polishchuk, *Homological properties of associative algebras: the method of helices*, Russian Acad. Sci. Izv. Math. 42 (1994), 219--260, Proposition 4.1 と §5, DOI 10.1070/IM1994v042n02ABEH001536。Chan--Nyman, *Noncommutative linear systems and noncommutative elliptic curves*, arXiv:2211.12465, Definition 8.6。引用キーは `PBondalPolishchukHelices`、`PChanNymanNormalFamily`。
- **検証状態**：数学的証明を論文Aに書き、今回一次資料の文献情報と定義を照合。本文の全独立監査、形式検証、外部査読、論文A全体の組版とは区別する。既存の論文A公表準備優先順位は維持。

## 全Poisson構造の代数的中心三次元：証明済みの核心と依存

**新しい最重要結果**：
`universal_casimir_determinant.tex`（定理`thm:pg-universal-determinant`）で、
`f∈C[x,y,z,u]_3`の**全体**が滑らかなcubicを定める限り、
三変数制限g=f(x,y,z,0)の特異性を問わず、
Jacobian量子代数に`Omega_h∈Z(A_{f,h})_3`、
`Omega_0=f`となる**厳密な代数的中心三次元**を構成。
係数は原点で分母が消えないh²の有理関数で、
計算は次数3・4の有限交換子行列とCramer法に尽きる。
形式的中心元の一般存在補題は不要である。

**証明の依存関係（論文Aに全文あり）**：
1. `lem:pg-det-gradient-coprime`：全体fの滑らかさから
   gcd(f_x,f_y,f_z)=1。共通因子h=0と残るm中心偏微分の
   非零共通零点がKrullの高さ定理から存在して矛盾。
2. `lem:pg-det-classical-kernel`：
   次数三古典Jacobian CasimirはC f+C[u]_3。
   これにより古典交換子行列のrankは
   r=binom(m+5,3)-binom(m+2,3)-1と一定。
3. `lem:pg-det-universal-rank`：
   滑らかな全体fの係数空間の稠密開（g smooth）で
   Hesse型の厳密代数中心が存在する。
   PBW/Weyl自由基底上の量子交換子行列の
   全(r+1)小行列式は稠密開で零、故に係数空間上の
   **正則関数恒等式として普遍的に零**。
   g特異・零への特殊化でもrank≤rを保つ。
   これは中心元そのものの無条件な特殊化ではない。
4. `thm:pg-universal-determinant`：
   原点で非零のr×r小行列でCramer中心元を構成。
   古典Casimir核により正確にOmega_0=f。
   語の反転とh→−hで係数はh²の有理関数。
5. `lem:pg-central-splitting-smooth`：
   正規形F=Σ tilde f_s(x_s,u)+c(u)の純中心三次を
   c=Σc_sへ一般に分配する。
   u=0での滑らかさはX smooth、u≠0は中心三次の
   基点自由線形系へのBertini、
   配分空間の既約性により全f_sを同時にsmooth化。
   active微分は変わらず元のPoisson構造を保持。
6. `thm:pg-quantization` と`thm:pg-ad-all-poisson`：
   各blockの中心元の和と共有中心u上のPBW/Koszul/AS議論で
   **全Poisson構造**と固定正規形のk次元Poisson pencilを
   同時に代数的量子化する。
   Hesse制限の場合は短い有限多項式、特異制限はCramer有理式。

**独立計算**：
`f=u x²+v y²+w z²+u³+v³+w³`は
`f(x,y,z,0,0,0)=0`だが全体はsmooth。
古典交換子行列378×56をSymPy有理数演算で
実際にrank45と確認し、核次元11=
C f+C[u,v,w]_3を確認。
`computations/verify_singular_cubic_classical_kernel.py`。
さらに当該例ではf自身が厳密な量子中心元である。
有限の検算は一般定理の代わりではない。

**先行研究との関係・未完了事項**：
Etingof–Ginzburg, arXiv:0709.3593v4 §8.3の
potentialのrank一定・特殊化議論を原PDFの
当該ページで確認した。今回の方法は
smoothな全体fからのactive gradient gcd、
古典Casimir一定次元、普遍minorとCramerによる
**原点の規格化も含む代数的構成**を用いる。
先行研究上の完全な新規性確認はまだない。
Hesse型の普遍全係数恒等式証明書
`computations/verify_universal_hesse_mixed_center.py`、
Mori–Smithのrank判定、Berger–TailleferのPBW、
全Poisson正規形のLie補題、中央拡大とAS正則性の
全独立監査と全LuaLaTeX組版・PDF目視は未完。
相対Poisson moduli stackへのグローバルな量子化の降下は
まだ未解決。

**形式的中心元について**：
従来のKontsevich–Dolgushev/絶対CY経由の構成は
考え得る代替手段だが、その相対化・完備双加群の全条件の
独立監査を終えていない。
**今回の完成した全Poisson量子化定理には使用しない。**
`notes/universal_casimir.md`に現行の核心と再現方法を整理し、
原稿に不要な旧形式的証明を付録として蓄積しない。

## Lie代数補題の検査点

K(P)の基点自由性からBertiniを用いて、V上もsupport W上も非退化な対称形式 B in K(P) を取る。
[x,y]=P(B^flat x,B^flat y) はB不変なLie括弧で、W=[W,W]、Z(W)=0。
可解根基が非零なら最後の非零導来イデアルに含まれる極小W-イデアルIを取る。
Iは可換な既約W-加群。可解根基の作用は既約表現上スカラーであり、W=[W,W]のtrace零性からその作用は零。
Z(W)=0 よりIは半単純商の非自明な表現なので、最高ウェイトとsl2関係を用いて
H([a,b],[c,d])+H([b,c],[a,d])+H([c,a],[b,d])=0
に代入すると、全Hに共通の等方方向が存在して基点自由性と矛盾する。
半単純Wのrank2以上の単純因子も最高根の正根分解から同様に排除する。
従ってWはsl2の直和となる。
**一次資料で確認した範囲：** Etingof, *Lie Groups and Lie Algebras* 原PDFの p.88 Proposition 16.9（可解根基のスカラー作用）、p.114 Definition 21.13 / Lemma 21.14（非単純正根の正根和）、p.137 Theorem 25.17（最高ウェイト）、p.173 §32.2（最高根の設定）を本文・ページ画像で確認し、論文Aの最高根の証明記述を明確化した。これは外部入力の参照監査であって、基点自由からの全Lie補題の形式検証ではない。
Euler列からのPoisson表現（prop:pg-represent）、Jacobiのdivergence（prop:pg-jacobi-extension）、Hessian（lem:pg-linearize）も独立再監査の対象として残す。

## 独立検算と限界

computations/verify_poisson_article_A.py は
F=(x^3+y^3+z^3+a^3+b^3+c^3+u^3+v^3)/3+uxy+vab
を対象とし、Poisson Jacobiatorの56成分、および二つの平面三次曲線のjoinでEuler wedge pi^2が消える56成分を理想で割った余りとして検査する。最初の独立実行でそれぞれPASS。
現行のGitHub版はgradient理想の零次元性によるsmoothnessチェックを追加したため、GitHub版そのものの再実行は未確認。
これは一具体例の厳密計算であり、一般次元の証明を形式検証するものではない。

2026-11-12の最新静的検査では、論文A入力閉包の22 bibliography keys、56 citation uses、175 labels、184 ref/eqrefに、未解決引用・重複bibitem・未解決ref・重複labelがない（コンパイル検証ではない）。
A全体のLuaLaTeXコンパイル・PDF表示確認・非楕円成分の全行列証明書の再計算は未実施。

## 一次文献の位置づけ

- Loray–Pereira–Touzet, arXiv:1112.3871、および Mayanskiy, arXiv:1303.5916：滑らかなcubic threefoldでのGrassmann記述は既知。
- Gualtieri–Pym, DOI:10.1112/plms/pds090：Bondal予想とFano四次元の既知結果。
- Druel–Pereira–Pym–Touzet, arXiv:2606.03424 (2026)：Fano五次元での全結果、高次元一般Fanoでの部分結果。
- Mori–Smith, arXiv:1502.07403、Berger–Taillefer, arXiv:math/0610112、Kontsevich, arXiv:q-alg/9709040、Dolgushev, arXiv:math/0612288、Etingof–Ginzburg, arXiv:0709.3593、Smith–Tateは量子化の既知入力。
- **Dolgushev一次資料の確認（2026-11-12）：** arXiv:math/0612288v3 の Proposition 1（PDF印刷p.9；不変形式でのunimodularity判定）と Theorem 3（印刷p.15；dualizing bimoduleが自明であることとunimodularityの同値）を原PDF本文・ページ画像で照合した。Theorem 3の仮定は滑らかな複素アフィン多様体、標準束自明、形式星積である。論文Aにおける絶対Calabi–Yau性の示し方、相対係数・完備双加群・形式星積への適用の全仮定は未監査。
- Brueckmann消滅のFu–Hwang経由の引用は原論文へ遡って条件を監査する。
これらは調査・比較した文献であり、全ての引用定理を今回一次PDFから再検証したという意味ではない。
高次元cubicの正規形・Bondal結論の包括的新規性照合は未完成。

## 次の具体的な着手順

1. 最優先は今回の全Poisson代数中心定理の**全依存監査**。
   稠密Hesse開→普遍minor恒等式の証明と
   全体fのactive gradient gcd、中心三次配分のBertiniを
   数学的に独立に点検する。
   特異g=0の古典rank検証コードと
   普遍Hesse係数不定元の検証コードを再実行する。
2. 全次元`thm:pg-normal`のLie補題、
   PBW/AS正則性、中心正則性のfiltrationと
   AS-Gorenstein change of ringsを一次資料と照合。
3. relative moduli stackの構造・成分数・
   Cramer中心のHesse表示チャート間の同型と
   moduliへの降下可能性を研究する。
4. 論文Aの全表示式の数値式番号、TeX参照・bibitem、
   LuaLaTeX全組版、PDF目視を確認してから投稿可否を判定する。
   先行研究上の新規性・全依存監査が未完のため
   投稿可能であるとはまだ断定しない。

GitHub mainが正本。Libraryはpushが実際に失敗した時だけ緊急退避。
