# 非可換 cubic threefold の generic 17次元モジュライ・Poisson 錐・内在的二次包絡 — 研究ノート

2026-11-03 v3

## 有効な構造と記法

- W=H⁰(P⁴,O(1)), dim W=5; S=Sym W, F∈Sym³W は滑らかな cubic、X=Proj S/(F)。
- パラメータ p∈Λ²W を定数２形式 β と同一視するため、体積形式を選ぶ。Ω=dx₀∧⋯∧dx₄。Π=ι⁻¹_Ω(dF∧β) は二次 bivector、F は Casimir。
- Plücker quadrics q_i は β∧β=ι_vΩ となる v の５成分。β²=0 ⇔ Π の Jacobi 成立。
- R₂=C[p₀₁,...,p₃₄]/(q₀,...,q₄,m³) は Artin 局所環、m=(p)。係数３次以上は零。
- 星積 C₁=Π/2, C₂=ΠΠ/8 + Π∂Π/12。C₂ は入力２個に対称なので星交換子は Π に一致する。F が Casimir より正確に中心。中心イデアルの商 A₂ は degreewise R₂-free。

## 重要な区別

1. **base の２次ジェット**：q_i=0 という p の二次方程式に現れる Poisson 方向。**一つの１パラメータ弧の２次ジェット**：Fermat の G_h=D−h²T/3 のような具体的 h² 係数。前者は後者の集合と同一ではない。
2. **代数的な族**：非被約有限型 Spec R₂ 上の A₂ も厳密な代数族であるが、一般の非零複素パラメータを持たない。Zariski 開の有限量子パラメータ族とは別の実現。
3. **星積 gauge**：A₂ の星積では F は厳密に中心。Fermat の二次関係式を選ぶ gauge では中心元に −h²T/3 の補正が現れる。矛盾しない。２次中心補正は gauge 依存であり、両者の比較を証明なしに同一視しない。
4. **３次元 Poisson と ambient P⁴**：ambient Π は一意に延長するが、非可換 B のどの有限パラメータ境界まで正則化できるかを意味しない。
5. **Grassmannian の cone の頂点**：T=Tot(O_Gr(-1))→Cone Gr は頂点で zero section Gr を収縮する。T 上の族だけから cone への descent は従わない。A₂ は有限２次近傍に限り、頂点を含めて intrinsic に構成できる。

## 証明されている直接恒等式

- α=i_Eβ, dα=2β。β²=i_vΩ のとき α∧dα∧dF = v(F)i_EΩ−3F i_vΩ。
- Fermat の [x,y]=hz², [y,z]=hx², [z,x]=hy², C=y³−z³ に対し [D,x]=h³(Cx+xC), [T,x]=3h(Cx+xC)。従って G_h=D−h²T/3 は中心。
- 一般の C₂ の対称性は添字 k↔ℓ を入れ替えるだけで確かめられる。

## 証拠の水準

- Poisson 錐のスキーム等式、R₂ の星積、中心商の flat：紙面内に証明あり。星積の結合律は Kontsevich の２次公式を使用（今回はランダムな多項式について SymPy のチェックも実施、しかし一般証明は一次文献に依存）。
- Fermat 中心性：紙面の自由代数恒等式で証明。追加で p=1009 において h=0,1,2,5,15 を代入し degree4 のイデアルを線形代数で検証した。これだけでは全パラメータの証明ではない。
- 一般混合族の AS-regular と中心三次：従前の 2026-11-01 v5 研究原稿に詳しい証明があり、一次資料 Mori–Smith, Etingof–Ginzburg に依存。一般の全次数・基底変換・例外集合はこのbundleで独立再監査していない。このノートでは完全な一般族を証明済みとしない。

## 研究上の障害と次の方法

- Jacobi=Plücker だけで任意の有限パラメータの正則な quadratic relation algebra になることは自明でない。無限小の星積法は有限パラメータで一般に多項式で打ち切れない。
- 三次中心元の選択は非零 Poisson 方向では Sym³⟨u,v⟩ の不定性を持つ。異なる chart の規格化・G の差・選択された三次超曲面との対応を計算する。
- より大きい研究課題：モジュライ比 17=10+7 は次元整合を与えるが、中心対の coarse moduli と cubic+Poisson 錐の birational equivalence は未証明。構造対象付き圏、非可換 P⁴ の ambient、Kuznetsov 成分の連携には実際の対応が必要。

## 文献（詳しくは paper_ja.tex）

Loray--Pereira--Touzet (2013; doi:10.1002/mana.201100354), Kontsevich (2003; doi:10.1023/B:MATH.0000027508.00421.BF), Mori--Smith (arXiv:1502.07403; doi:10.1007/s00209-016-1824-5), Etingof--Ginzburg (2010; doi:10.4171/JEMS/235)。この研究原稿の成果の初出・新規性は未監査。

## generic 17次元の有効な正規形

中心一次平面 U=<u,v> を固定。Fの35係数空間は、非可換周囲Q_113の31パラメータと中心三次直線の4パラメータをまとめたチャートである。保U放物型P⊂PGL5の次元は18。標準形は

F = a(x³+y³+z³)+bxyz + ux²+αvy²+β(u+v)z² + M₁(u,v)x+M₂(u,v)y+M₃(u,v)z+g(u,v)

で、(a,b,α,β)４個、三つの二元二次式９個、二元三次式４個、合計17個。f3 smooth, b≠0, 三つのL_iの零点が互いに異なることは稠密開条件。Hesse変換は有限多価、相対スカラーによるL1の規格化は非零条件で可能。代数的な量子中心元Gの有理選択は従前の原稿 G §§8–13 の相対線形方程式に依存する。

厳密な接行列計算：19個のGL3×GL2×Hom(C²,C³)パラメータに対し、Lie作用 δF=(tr A)F−(Ax+Cs)·∂xF−(Bs)·∂sF、中心に全体スカラー1次元の核。付属 `verify_17_slice.py` は具体的有理係数の F0 でorbit rank=18、sliceとの結合rank=35をQ上で得る。従って全35係数空間への作用写像は支配的、17次元正規形から一般同型類への写像は generically finite（degree 1とは限らない）。この階数計算は有理数体上の厳密計算として再実行可能であり、論文にも記載している。

`technical_core_ja.pdf` 定理32.1・補題32.2 の一般 stabilizer 有限と、命題29.2 の二次/三次関係からの復元を合わせて使う。独立の幾何学的正規化により一般性を確認したが、Gにおける相対中心公式の全証明の今回再監査はまだ行っていない。非可換 cubic を偏極付き次数付き代数として考える場合と、構造対象を忘れた導来圏で考える場合を混同しない。

Gの定理28.2によるgeneric tails gldim=3には滑らかな量子的楕円境界・良い中心chartと係数の代数的独立性が必要。generic 17係数を関数体上で扱う段階で条件を満たすか、量子的楕円判別式の非零性を明示的に点検する。全閉点についてのZariski開性は別問題であり、この研究では未証明と明記する。

### 広い研究の再開に必要な未解決の本体

非可換17次元の存在/非同型性は達成済み。一般の17次元族から可換側のデータ (Y,Λ,ξ) を関手的・大域的に回復すること、Ku(A) と Ku(Y) の実際の対応、構造対象を忘れた同値とfinite identificationsが残る。二次Poisson錐の頂点への降下は研究上有用だが、generic点を扱うための前提ではない。

## 内在的 quadratic envelope と Serre の偶数 Veronese（現行の研究内容）

- **偏極付き入力**：C=qgr A, O=πA, T=(1) とし E_i=T^{-i}O, Z_{ij}=Hom_C(E_j,E_i) (i≤j) と定めると、section algebra の復元の下で Z_{ij}≃A_{j−i}。次数１から生成し二次合成の核だけを課すと Q(A)=T(A₁)/(ker(A₁⊗A₁→A₂))。A=B/(G), deg G=3, B quadratic なら Q(A)=B, ker(B₃→A₃)=CG。これは既存の数学的帰結であり、一般のZ-algebraの二次包絡がAS-regularになることを意味しない。
- **generic 次数２の中心**：B=相対 Jacobian 型、S_h=B/(u,v) の Z(S_h)_1=Z(S_h)_2=0、f₃=F|_{u=v=0} smooth、h≠0 とする。PBW濾過で Z(B)₂=Sym²⟨u,v⟩。q∈Z(A)₂ の持上げ Q∈B₂ は [Q,x_i]=c_iG (i=x,y,z)。Jacobi により G∑c_i F_{x_jx_i}=0。G 正則、mod (u,v) で Hess(f₃)c=0。すると ∂(∑c_i∂_i f₃)=0、斉次二次なので ∑c_i∂_i f₃=0。c≠0 なら f₃ は錐になり smoothness に矛盾。従って c=0、Z(A)₂=Sym²⟨u,v⟩。本文 `paper_ja.tex` の補題に完全な証明。
- **Serre からの構造対象付き復元**：tails gldim<∞ を仮定すると Serre=(-2)[3]。よって (D^b(qgr A),O) から偶数環 R=A^(2) が canonical。中心次数１は D₁=Sym²⟨u,v⟩、その生成環 D=k[u²,uv,v²] は conic ac=b²。二重被覆 S=k[u,v] と R の中心局所化を組み合わせ、A= A[u^-1]∩A[v^-1]（S-自由性）によって odd part を回復。従前の技術原稿§33.1の補題を一般混合族に適用できる。二通りの持上げの差は奇数次数の符号。O を忘れた導来圏や Ku(A) からの復元は未証明。
- **generic仮定の分離**：B ５次元 AS正則、G 中心正則、A が S 上自由であることは相対 PBW に基づく。Z(S_h)≤2=0 は smooth elliptic Sklyanin shift τ²≠id で成立。tails 正則性にはそれとは別の仮定と原稿G §§28,31の議論が必要。generic の関数体で成立する主張と全閉点で成立するZariski開性を混同しない。
- **不可避の marking**：O と T があればZ-algebraは関手的だが、O を忘れれば自然に始点を選べない。Serre は index 2 なので偶数 shift は決まるが、奇数 shift は標識・二重被覆の選択を要する。一般の Z-algebra に一周期性はない。今回の17次元族は既に１周期化可能な B から来る。

## 内在的AS-regular判定として残ること

一般の nc cubic の (C,O,T) から得た Q(A) に対し、単に dim A₁=5, dim A₂=15 ではAS-regularは従わない。Q(A) の五段 Koszul 複体が正確、二次双対が次元ベクトル (1,5,10,10,5,1) の Frobenius 代数、GK成長とnoether性を持つことをチェックする必要がある。中央三次商であることは、ker(Q(A)₃→A₃) が１次元で代表Gがcentral regular、かつ全次数のkernelが(G)という追加検証を要する。二次関係の存在だけから第３次以後の構造は決まらない。