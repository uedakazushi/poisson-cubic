# 論文B：証明監査・先行研究・有効な障害

2026-11-14 / B-v58。最初に `../00_research_plan.md` を読む。主定理は `papers/generic_recovery/main_result.tex` の `gdr:thm:generic`。本ノートのファイル名は、特に指定しない限り `papers/generic_recovery/` 内を指す。全稿入口は `papers/paper_b.tex`。

## 主張の状態と監査の結論

指定された次数別有限自由な中心三次対について、局所window (L) と完備MF比較 (CF) を本文で構成し、主定理の追加仮定として課していない。一般点での全coherent残余pairの可換模型は有限体拡大後に存在し、方程式は元のK=C(h)上に取れる。幾何学的一意性はrotationを保つ模型の範囲で述べる。

提供された独立査読報告（2026-11-14 / v1）は、主要証明を支持し、核心となる移送の提示・文献帰属・具体例・限定の整理を求めている。今回の改訂では追加した比較図式と二拡張の周期、非可換入力の一次jetの証明を独立に読み、CK・EG・Pirozhkov・Lin--Zhang・Sklyanin文献の該当箇所を確認した。主定理の入力や存在結論は変更していない。未変更の証明全体を今回一から再監査した、計算機形式検証した、正式な投稿査読で採択された、包括的な初出を確定したとは述べない。本文の証明、提供された査読の判定、今回の読解、有限計算は別の状態として扱う。

## 査読の要求と現在の本文

| 要求 | 現行の対応箇所 | 状態と範囲 |
| --- | --- | --- |
| 核心定理と比較図式 | `gdr:thm:complete-intro`, `cft:thm:complete`, `tw:eq:comparison-diagram`, `tw:eq:period-extension`, `tw:eq:rotation-period-square` | 完備底上の実MF関手・逆・rank・t-relative性を明示し、余核からrotationまで指定周期を追跡。新しい図式と型を独立読解 |
| 既知結果との差分 | 序論の定理別比較表、`references.tex` | Pirozhkovの三次範囲n>3を明記。EGの有限rankとCKの変形複体の範囲を確認。BFKの上界・Jacobian Torelliは既知の帰結 |
| 非可換な具体例 | `explicit_example.tex`, `gre:prop:input`, `gre:prop:jet` | 全次数自由性・中心性・非可換性を証明し、形式的potentialの非零一次jetを算出。一般点K-modelや低rotation積の全行列は未計算 |
| 限定の集約 | `gdr:subsec:scope` | K/K'、幾何学的一意性/form、線束/coherent、通常局所化/torsion Morita、特殊化の範囲を保持し、後続節から参照 |

## 正確な定式化と証明の所在

### 対称積の核と一意性

`prop:ej-geometric-low-degree` の勾配空間は **Sym^2 V→U の核** である。V⊗V→Uの核にはΛ^2Vも含まれる。原稿では `ej:eq:symmetric-product` を明記し、後続の `gcd:eq:gradient-data` と一致させた。

`gcd:thm:field-model` の第三項と主定理の一意性は **pair (C,rho) のrotation付き模型** に限定する。証明で使うV、U、積はrhoに依存する。圏のみのTorelliを全次元で別途示したことにはしない。K上のformの一意性まで強められない理由は本文の `gcd:ex:forms` に示す。

### 積分空間と有限étale代数

`ej:lem:symmetrizer-algebra` は、滑らかな三次式Fのsymmetrizer代数E_Fが有限étaleで、その形成が体拡大と可換であることを示す。代数閉包上の原始冪等元が最細のSebastiani--Thom分解を与え、dim E_Fがそのブロック数である。これはHwangの基本的結果を任意の標数零体上で使うために整理したもので、新しいJacobian Torelliとは扱わない。

`gcd:prop:integrability-symmetrizer` は、固定勾配空間Qを含む勾配を持つ三次式の線形空間I_Q、可積分行列空間L_Q、E_Fの線形同型を与える。勾配空間がちょうどQとなる式はE_Fの単元に対応する。E_Fの単元による座標変換と全体スカラーだけを許す軌道は E_F^×/[k^×(E_F^×)^3]。これは全PGLによるform分類でも、圏同値核の降下障害の分類でもない。幾何学的に分解不能ならE_F=kであり、同じQからのk上の式はスカラー倍まで一意（`gcd:cor:indecomposable-equation`）。

### 残余のadmissibility

`crs:prop:residual-smooth` では、例外部分のadmissibilityだけで残余部分の両側admissibilityを済ませない。残余は仮定によりsmooth、ambientの線束生成部分がproperなのでproperでもある。その包含にPerry Lemma 4.13を適用して左右随伴を得た後、Lemma 4.15(3)でsmoothnessを貼り合わせる。全coherent圏がsmoothであることを先取りしない。

### 有限降下の核・cone

有限表示による降下はToën Théorème 1、perfect核の降下はTV Lemma 2.10、二つのconeによる同値判定と開性はTV Lemma 3.25に先行する一般原理がある。本稿では片側smoothnessから始め、rotationと指定周期の有限図式を付加するため、次のperfect性を直接確認する。一般的な新しい代数化理論とは位置づけない。

`rog:lem:descent` で、C_Dをsmooth proper、Gamma_Dをproperとし、P_DをC_D--Gamma_D同値核の降下とする。C_Dのproper性からP_Dは右Gamma_D-perfect。Q_D=RHom_Gamma(P_D,Gamma_D)は底D上perfectであり、C_DのsmoothnessとToën--Vaquié Lemma 2.8から右C_D-perfectでもある。この順序により単位・余単位の両テンソル積とconeがD-perfectであることを確認する。

体L上で零になるconeの有限個の有限生成cohomologyはD-torsionである。annihilatorの積の反転で一度に消し、非空開の閉点を選ぶ。核・射・有限個の周期図式の降下には同論文Lemma 2.10を使う。任意の高次群作用を有限の周期図式で代用する主張はしていない。

### graded stabilizationと有限rank MF

`tw:lem:stabilization` では、Chen Corollary 2.11により非零Gorenstein-projective B加群MのA射影次元が1となることを使う。有限graded projective表示0→P_0→P_1→M→0から、Omega M=0を用いて他方のfactorization行列を一意に構成する。非次数付き余核定理をそのままdg定理と呼ばず、exact圏・有限totalization・dg商の比較を明記する。

`cft:thm:complete` では、flowのarity 2r+1成分が t^{-r} f_{2r+1} と書けることを `cft:eq:t-weight` に示す。Q=(0,tq_1;q_0,0) の2r+1回の合成では、左下成分にt^r、右上成分にt^{r+1}が現れる。従って像のt冪は0、1に戻り、同じ二つのrank・同じ有限個の内部shiftを持つ通常のMFとなる。Rの正則性を使うのはwindow/Hom側であり、この完備flowの構成自体には有限自由加群の完備性・分離性で足りる。

### 非可換Hesse族の復元jet

`gre:prop:input` の三生成元関係は [y,z]=h x²+(h²/2)(yz+zy) と巡回置換であり、中心変数u,vを加える。一般ファイバーが滑らかな楕円型Sklyaninであることは明示判別式で確認する。各次数は有限生成DVR加群で、一般ファイバーの階数と剰余の次元が等しいためtorsionがなく自由となる。既知の中心式Gと採用したΩの恒等式、および次数四のtorsion-free性が中心性を与える。この全次数証明は有限計算に依存しない。

`gre:prop:jet` ではWeyl同定の積の一次項が(h/2){-,-}_0となる。formalityの逐次持上げを恒等mod h²から始めることでφσ=1+O(h²)に選べ、U_2(f,π_1)には許されるグラフがないためC_pi=1+O(h²)である。従ってΩの中心逆像はW_rec=F+h xyz+O(h²)。xyzはJac(F)_3の非零元なので恒等を剰余とする座標変換・単元倍で消せない。非可換性は次数二の交換子が非零であり三次中心商でも残ることから分かる。

これは形式的potentialのjet計算であり、一般点への有限降下で選んだ方程式のh=0での正則性や同じjetを結論しない。非可換由来の一次積と中心元を実際に使っており、既知の可換勾配空間だけを積分した例とも区別される。

## 完備曲率移送の論理

本文の証明を重複して収録せず、再点検で重要となる依存だけを記す。

1. `cft:lem:model`：曲率導入前のnormalized全Hochschild cochainとpolydifferential cochainを、内部weightを保つbar/Koszul比較でHKR同型に結ぶ。Kontsevichのaffine同変なformalityをweight零へ制限し、各Artin次数で既指定jetを保ってPoisson係数と一入力gaugeを持ち上げる。元の積がbidifferentialであることは仮定しない。
2. `cft:lem:center`：中心逆像C_piは固定次数3の有限自由加群上の1+O(m)行列である。その逆像Wについて中心性と接写像の最低次HKRの単射性から[pi,W]=0を示す。
3. `cft:lem:primitive`：正則勾配Koszulの次数制約からpi=[Xi,W]となる定数trivector Xiが一意に存在する。Jacobiと負の係数次数の不存在から[Xi,pi]=0を得る。Casimir条件だけでは第二の消滅は得られない。
4. `cft:lem:arity`：関数k個とbivectorの出力arityは2−2k、trivector一個を加えると3−2k。関数入力は高々一個で、残りはmの倍数なので、大きい曲率にもかかわらず各Artin次数でTaylor和が有限になる。gamma_sのarityは1と3のみで、単位入力に関してnormalizedである。
5. `cft:lem:flow`：非自律で非可換のcoderivationを順序付き積分する。coalgebra性、逆写像、F b_0=b_1 Fを微分方程式で示す。F_(2r+1),H_(2r+1)∈m^r、偶数arityと零項は零。出力長ellに対し入力長はell+2q以下で、tensor長完備barにも各Artin商で連続に作用する。
6. `cft:thm:complete`：F_(2r+1)の評価はMF行列挿入前のbar写像の評価であり、挿入後のMF関手には偶数入力成分もあり得る。Qがmの倍数でなくても、arity上界により対象と射への挿入公式は各Artin次数で有限。固定bigdegreeの有限自由加群内で極限を取り、逆bar写像から逆関手を得る。t-relative性が内部shiftと指定された(3)=[2]の整合を与える。

一般点へは固定三対象のHom・高次積を先に構成してから局所化する。任意Laurent係数MFへの無限Taylor和の評価は主証明で必要ない。

## 一般点への接続と循環の不存在

windowの生成性は有限長加群 T_j=B(j)_{<1-a} の実際のfiltrationによる。j=a,a+1,a+2の三角的なfiltrationからK(a),K(a+1),K(a+2)を取り出し、三次周期性でK,K(1),K(2)へ移す。特殊ファイバーで生成することだけを一般点へ持ち上げていない。

原点stabilizationのEuler数は chi_r=sum_(s≡−r mod3)(−1)^s binom(N,s) で、sum_r chi_r^2=2·3^(N−1)。自己Euler数chi_0はN=9などで零になるので三成分を用いる。固定三対象の像が一般点で非零であることを示した後、代数閉体上のBFK Theorem 5.15により生成を得る。上界2N(N+1)−1は同定理のd=3への代入である。

幾何学的模型と線束生成残余圏の同値を有限体拡大上へ降ろしてから、残余のsmoothnessを基礎体へ降下する。smooth対角によりpseudo-perfect加群がperfectとなることと、全twistからのHomによる検出を使い、全coherent圏への飽和を証明する。

最後にsmooth proper性を用いて導来自然変換V、Uと積の体拡大との両立を得る。幾何学的模型の存在によりQ=ker(Sym^2 V→U)の可積分行列空間に拡大体上の可逆元がある。線形方程式と無限体性から基礎体にも可逆元があり、G=(1/3)sum x_i A_ia q_aを積分する。これは幾何学的模型の存在を仮定する独立の条件付き定理であり、低積だけで存在を結論していない。

## 一次資料と新規性の位置

| 一次資料 | 本文が依拠する確認箇所 | 本稿での役割 |
| --- | --- | --- |
| [Kontsevich著者最終稿](https://www.ihes.fr/~maxim/TEXTS/DefQuant_final.pdf) | Theorem 4.6, §4.6.2, Theorem 6.3, §§6.2–6.4 | 通常のformality、MC比較、グラフ恒等式。arXiv初版との番号の差を参照版の明記で解消 |
| [Căldăraru--Tu](https://nyjm.albany.edu/j/2013/19-16v.pdf) | §2, Remark 2.8, Theorem 2.12 | twistとgraded MF、無限挿入の有限性の条件 |
| [Carqueville--Kay v4](https://arxiv.org/abs/1104.5438v4) | Proposition 2.3, Remark 2.4, §3.1, Theorem 3.1, Proposition 3.4, 脚注7 | 第二種curved formalityとpotentialの形式変形という直接関係する既知原理 |
| [Etingof--Ginzburg](https://doi.org/10.4171/JEMS/235) | §§3.5–3.6, Theorem 3.6.2 | 非可換楕円特異点のgraded MFとDbCoh(E)の同値という先行例 |
| [Burke--Stevenson v1](https://arxiv.org/abs/1507.00830v1) | Proposition 4.18, Definition 5.1, Lemmas 6.1–6.2, Theorem 6.4と証明 | 導来section、chi、Gorenstein型、i=1−aのwindow |
| [Chen v3](https://arxiv.org/abs/2402.11613v3) | Corollary 2.11, Theorem 7.2, Remark 7.3(2) | 有限A射影次元のGorenstein-projective加群と余核比較 |
| [BFK v3](https://arxiv.org/abs/1012.0864v3) | Theorem 5.15 | 非零対象のd個のshiftによる生成と上界 |
| [Toën--Vaquié v5](https://arxiv.org/abs/math/0503269v5) | Lemmas 2.8, 2.10 | smooth対角とpseudo-perfect性、perfect核・射の有限降下 |
| [Perry v2](https://arxiv.org/abs/1804.00132v2) | Lemmas 4.13, 4.15 | 左右随伴の存在とadmissible分解のsmoothness |
| [Pirozhkov v1](https://arxiv.org/abs/2208.13604v1) | Theorem 1.2 (=5.3)と直後の注意 | rotation付きTorelli。三次の場合は次元n>3。刊行書誌はBull. London Math. Soc. 56 (2024), no.10, 3075–3089, DOI 10.1112/blms.13117 |
| [Smith--Tate](https://sites.math.washington.edu/~smith/Research/tate.pdf) | §1 pp.19–20、p.35 Remark (1) | SklyaninのHilbert級数・domain性と中心三次元。K-Theory 8 (1994), 19–63 |
| [De Laet--Le Bruyn v1](https://arxiv.org/abs/1405.1158v1) | §2 p.3の巡回中心元公式 | 具体例のG。Algebr. Represent. Theory 18 (2015), no.3, 761–776, DOI 10.1007/s10468-014-9515-6 |
| [Lin--Zhang v2](https://arxiv.org/abs/2310.09927v2) | Theorem 3.5, Remark 3.6, §5, Theorem 5.1 | 低rotation積のsector計算と既知のrotation付きTorelli |
| [Toën著者稿](https://www.math.univ-toulouse.fr/~btoen/defdgalg.pdf) | Théorème 1 | smooth proper dg代数と射のfiltered-colimit降下。Bull. London Math. Soc. 40 (2008), 642–650, DOI 10.1112/blms/bdn043 |
| [Tu v2](https://arxiv.org/abs/1009.4151v2) | Theorems 1.1, 1.4, 6.2 | 可換孤立斉次MFのd個のstabilization shiftによる生成。Compos. Math. 150 (2014), 1549–1578 |
| [Lowen--Van den Bergh v2](https://arxiv.org/abs/1505.03698v2) | Theorem 5.4, §4.1 | 形式MCとtorsion Morita変形、通常の一般点同値との区別 |
| [Blanc--Katzarkov--Pandit v1](https://arxiv.org/abs/1705.00655v1) | Theorems 1.1/4.27, 1.2/4.29 | 有界な自己Extを持つcompact generatorの下での非曲率形式模型と生成子。Compos. Math. 154 (2018), 2055–2089 |
| [Ueda--Yoshinaga公刊PDF](https://www.math.sci.hokudai.ac.jp/hmj/page/38-3/pdf/HMJ38_0409-0415.pdf) | Lemma 3, pp.412–414 | 同一Jacobian idealとST型。Hokkaido Math. J. 38 (2009), 409–415 |
| [Wang v2](https://arxiv.org/abs/1402.3810v2) | Theorem 1.1, Corollary 1.3 | 勾配イデアルによる復元のST例外。Manuscripta Math. 146 (2015), 559–574 |
| [Hwang v1](https://arxiv.org/html/2501.08633v1) | Propositions 2.2, 2.6, 3.1, 3.2, Corollary 2.7 | symmetrizer代数、同一勾配空間のfiber、ST分解と冪零元。J. Math. Soc. Japan 78 (2026), 55–62, DOI 10.2969/jmsj/93469346 |


書誌の正本は `references.tex`。LZは Math. Ann. 391 (2025), 163–177、BFKは Invent. Math. 189 (2012), 359–430とし、使用したarXiv版の定理番号も指定する。Kontsevichの定理番号は上記著者最終稿に従う。Crainicのhomological perturbation formula、Dyckerhoffの原点stabilizationのClifford計算は本文の引用と直接計算を併用する。外部文献の全証明を再証明したという監査ではない。

文献上の注意：Ueda--YoshinagaのabstractにはST型の条件にnotが欠けるが、本文Theorem 1とLemma 3を参照する。Wangの[Erratum](https://doi.org/10.1007/s00229-022-01447-2)（Manuscripta Math. 171 (2023), 369–370）はCorollary 6.1の証明中のST locusの閉性を訂正する。本稿が使うTheorem 1.1 / Corollary 1.3は訂正対象ではなく、ST locusが全射影空間で閉であることは使わない。Hwangの公刊書誌は出版社で確認し、命題番号の実読はarXiv v1による。


**既知の形式原理と実関手の構成を区別する。** CK Proposition 3.4は多項式曲率代数の第二種変形複体、Theorem 3.1は固定MFのendomorphism代数を扱う。第二種cochainはarity直和で、各arityは全多重線形Homであるため、非微分的な変形積も対象となる。基点の大きい曲率を微分に含める形式的MC比較と、孤立potentialの変形による記述は既知である。

本稿ではt-relativeな二重次数付き複体へ移る必要があり、勾配Koszul cohomologyは Jac(F)⊗C[t,t^(-1)]、Lie次数1・内部weight0の部分は t Jac(F)_3 となる。normalized単位、一般の完備底、arity直和のm進完備化、全MF対象上の挿入公式と逆関手は、本稿のmodel/arity/flowの補題で別に構成・確認する。各Artin次数の有限arityは有限rank行列への評価に必要だが、一般の非斉次potentialではC[x][[h]]とC[[h]][x]の差が残る。本稿が次数別直和上の通常MFに値を持つことは、固定bigdegreeの有限自由係数空間での極限と二成分行列のt冪計算に依存する。CKだけを引用してこの実関手の結論を省略しない。

Lowen--Van den Bergh Theorem 5.4は先頭曲率の冪零性の下で形式MCとtorsion Morita変形を比較する。Blanc--Katzarkov--Pandit Theorems 1.1/1.2は高次自己Extが消えるcompact generatorを持つ線形圏について一変数形式変形の非曲率模型と両立するcompact generatorを与える。従って、形式変形論一般がtorsion Moritaまでしか与えないと述べるのも不正確である。これらは指定三対象上の有限rank graded MF関手、rotation・周期比較、通常HomのLaurent局所化と可換cubicの同定をそのまま述べるものではない。本稿の固定対象への制限を先に行う構成は、この最後の段階を明示する。

三次の定数trivectorによる一段経路、arity1/3、F_(2r+1)∈m^rの定量的実現は本文に明示する。主題として残るのは、これを代数的中心三次変形の一般点・有限降下・全coherent飽和・基礎体上の方程式へ結びつける結論である。後半の有限降下と抽象飽和は既知の一般原理の応用である。明示的な完備比較・相対windowと包括的な一般点結論を成果の中心とする。同一の一般点定理を述べる一次文献は調査範囲では確認できていないが、この組合せおよび明示的実現の初出は未確定。新規性の評価では「curved formalityが新しい」「一般的にMFをpotentialで記述できることが新しい」という説明を用いない。

Etingof--GinzburgはC上のweighted gradedな有限rank自由MFを既に扱い、Theorem 3.6.2(i)でDbCoh(E)との三角同値を与える。有限rank自体を本稿の新規性としない。同定理は内部shiftと通常の可換三次rotationの指定比較を含むpair同値までは述べない。通常次数三次例はN=3の楕円Sklyanin型である。本稿のN>=5・任意の指定された中心三次変形・一般点のrotation付き残余圏を、同文献がそのまま述べているわけではない。Pirozhkovの定理は三次n>3であり、三次三様体を含めるLZのTheorem 5.1と区別する。LZの一意性とBFKの生成上界は既知結果の利用であり、存在定理の初出を確定する資料でもない。

文献の細部として、Burke--Stevensonの実際のMSRI論文と目次はpp.93–123であり、出版社の章メタデータは末尾空白頁を含む93–124となっている。本文書誌は印刷された論文の範囲に合わせる。De Laet--Le Bruyn arXiv v1の序論Theorem 1には中心式の誤植があるため、正しい式のある§2 p.3を参照し、Smith--Tate p.35の巡回和とも照合する。

## 再発を避けるための反例・障害

- **CasimirとJacobiは別。** F=sum_(i=0)^4 x_i^3/3、Xi=partial_0∧partial_1∧partial_2+partial_0∧partial_3∧partial_4、pi=[Xi,F]では[pi,F]=0だが[Xi,pi]と[pi,pi]は非零である。`verify_complete_curved_transport.py` にnegative controlを保持する。
- **特殊生成性だけの持上げは偽。** P^1上のcone(O(−1) --h s--> O)はh=0でOとO(−1)[1]を含み生成するが、hを反転すると非零section sの零点に支持された対象となり、全導来圏を生成しない。windowの実際のfiltrationと一般点のEuler非消滅が必要である。
- **同じ勾配空間と形式同型は基礎体上の同型を意味しない。** `gcd:ex:forms` のsum x_i^3と(1+h)x_1^3+sum_(i>1)x_i^3はR上smoothで特殊ファイバーが同じ、C[[h]]上同型だがK上では射影非同型。本文にHessianとh+1に沿う付値による証明を収める。核の降下障害の非零例としては使わない。
- **有限可積分性は圏同値を証明しない。** 方程式抽出は幾何学的模型の存在を得た後の段階である。特定のlambda=1の明示方程式を模型と同定するには、実際の非可換低積との追加比較が必要。

## 基礎体降下と非分裂例

K=C(h)、L=C((h))について、z^3=1+hはL-点を持つがK-点を持たない。有限型K空間に形式点があるだけではK有理点は得られない。Brauer群消滅を同値核の降下に使うには、まずその核のGalois不変な同型類と自己同型群を同定する必要がある。非空開の閉点を選ぶ現在の有限降下は、その情報を与えない。有限拡大除去は未解決である。

有限étale代数を分裂代数k^sと混同しないための例として、k=Q(t)上の

`F=x0^3+3t x0 x1^2+x2^3+x3^3+x4^3`

を用いる。t=1で最初の二変数部分は ((x0+x1)^3+(x0-x1)^3)/2 なので一般点はsmooth。二次拡大で五つのcubeに分かれ、E_F=Q(t)[u]/(u^2-t)×Q(t)^3。最初の二変数でuは行列[[0,t],[1,0]]として作用し、u^2=tを満たす。tの付値が奇数なので二次因子はQ(t)上非分裂である。

`verify_generic_cubic_descent.py` は可積分行列の転置空間がこの5次元代数に等しいこと、積の関係、F^a(bx)=F^(ab^3)(x)を厳密に検算する。元からの三例のdim L_Q=5,1,1は、最細幾何学的STブロック数として解釈できる。この計算は既知の可換Fを入力するもので、非可換圏からV,U,積を抽出したものではない。

## 近接する結果との境界

- Efimov--Positselski, [Coherent analogues of matrix factorizations and relative singularity categories](https://msp.org/ant/2015/9-5/ant-v9-n5-p04-s.pdf), Algebra Number Theory 9 (2015), 1159–1292, DOI 10.2140/ant.2015.9.1159, Theorem 2.7と§3.3。coherent MFの比較・局所化と、有限rank locally-free MFの局所化を区別する。§3.3の反例は特異なambient上のもので、本稿の可換Rhat[x]への直接の反例ではない。本稿は固定対象の通常Homの平坦底変更を使う。
- Tu, [Categorical Saito theory, I](https://arxiv.org/abs/1902.04596), Theorems 3.2, 1.6/4.4は与えられた可換Wのcyclic模型・VSHS比較。Segal, [The closed state space of affine Landau--Ginzburg B-models](https://arxiv.org/abs/0904.1339), Theorem 2.14 / Corollary 3.4はHochschild不変量の比較であり、任意の非可換中心商からの圏同値の定理ではない。
- Positselski, [Two kinds of derived categories, Koszul duality, and comodule--contramodule correspondence](https://arxiv.org/abs/0905.2621), §6.4はcoderived/contraderivedの比較。完備化と無限対象を含む圏の種類を区別して使う。
- Lehmann, [Hochschild cohomology parametrizes curved Morita deformations](https://arxiv.org/abs/2406.04945v2), Propositions 2.4/2.5は一次曲率Morita変形とHH^2の全単射、Proposition 3.3は有限Artin底のn-derived categoryの比較である。完備底から通常のLaurent一般点への復元をそのまま与える定理ではない。

## 独立成果との境界

移管した[一次変形稿](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/cubic_first_order_deformations.tex)は本稿の入力でない。再開時に混同しやすい事実だけ保持する。N=5の中心三次対の一次接空間はLambda^3 C^5とJac(F)_3の直和で10+10=20次元。可換Poisson零点で圏論的KSの核を7次元と呼ばず、一次Poisson方向は10次元として扱う。Plücker錐の次元7と頂点の接空間10は異なる。一般非零Poisson点の核7はこれだけから従わない。

Plückerの二次障害、全Artin window、相対étale、明示混合族・高次jet・point schemeの証明・計算は移管先の現行稿に置く。JLLZのHH^2(Ku(cubic threefold))とJac(F)_3の同型を利用する一次変形の議論も移管先が担当する。詳細な所在は `paper_b_scope_and_transfer.md`。Bの監査状態を独立稿の全証明の監査完了と取り違えない。

## 再現と未解決の核心

`verify_complete_curved_transport.py` は5/7変数のSchouten恒等式、定数trivector contraction、negative control、および有限次数の非自律coalgebra flowの逆・coproduct・arity評価を検査する。`verify_three_object_window.py` は有限行列の摂動縮約と三角的filtration、`verify_generic_cubic_descent.py` は既知の可換勾配空間の可積分性と非分裂symmetrizerの例を厳密体Q(t)上で検査する。`verify_recovery_example.py` は具体的な非可換Hesse入力の判別式・中心元係数恒等式をQ[h]上で、三つの中心交換子をh⁴を法として、次数三以下の400組のWeyl積をh²を法として検算し、xyzの非零Jacobian剰余を確認する。いずれもKontsevichグラフ積分や実際の非可換MFの全Hom/高次積の計算機証明ではない。

再現コマンドは研究方針に記載し、最新の終了コード・出力ハッシュ・組版・画面確認の状態は `validation_paper_b.json` に置く。生成PDFと計算出力はbuild/で非追跡。次に必要なのは、一般点結論の初出の確定、具体例のh²補正、および非可換入力からV,U,積の全行列を算出することである。有限拡大の必要性・次数、同値核の具体行列、特殊点を含む代数的模型、全モジュライ上の接着は引き続き独立の未解決課題である。
