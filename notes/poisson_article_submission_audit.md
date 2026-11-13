# 論文Aの公表準備：主張・依存・検証の範囲

**2026-11-14 / A-v54・nc-cubic-v85。** 再開時は `00_research_plan.md` を先に読む。
本文は `papers/paper_a.tex`、専用文献は `papers/support/papers/references_poisson_cubic.tex`。
以下の節ファイルはすべて `papers/support/papers/sections/` にある。
計算・組版・入力ハッシュの実行記録はルートの `validation_paper_a.json` に集約する。

## 現在の公表範囲

中心結果は、滑らかな三次超曲面上の全Poisson構造のJacobianブロック正規形、
全次元でのBondalの下界、全Poisson構造の代数的量子化、Fermatと相対Poissonモジュライの成分数である。
具体的な四次元の帰結として、一般階数四の構造の分離型分類と純楕円退化因子を扱う。
中心元は固定した変数分解の全滑らかな係数空間上で同時選択できる。
単一ブロックではreductive群に関して全係数空間上で同変に選べ、
三変数制限が滑らかな部分では中心平行移動を含む群にも拡張できる。
線形群の商上の中心Gm-gerbeを同定し、gcd(m,3)=1では指標で次数線形化を補正して、
階数二のPoisson対の被約層内の開へ代数族を降ろす。
ambientの二次包絡、偏極付き圏からの復元、三次三様体の条件付き導来復元を同じ原稿に収める。
要約・序論はこの依存順に整理し、Fermatのspace・固定stack・相対stackの三種類の成分数を区別する。
表示式には数値の式番号を付ける。

一般退化イデアル、critical cover、零点完全交叉は本文に必要な証明を保持する。
独立な六・七次元のprimary厚化（長さ8, 64, 49）と数値幾何は
`uedakazushi/nc-cubic2` の `papers/poisson_cubic_six_seven_geometry.tex` が現行入口であり、
Aの一般定理の証明を移管先へのリンクで代用していない。
移管先の独立公表価値とprimary分解の監査は、Aの検証とは別である。

## 主張の確実性と証明の所在

次の証明連鎖を本文と外部入力の適用条件に沿って点検している。
「点検」は独立な数学的読み直しを意味し、Lean等の形式検証や外部査読を意味しない。
既存証明の監査結果を保持し、現改訂では同変中心元・中心商族・商のスカラー作用と
非連結曲線の持上げ障害類を重点的に読み直している。
主定理の記載済み証明、有限計算、初出の確認は区別する。

| 主張・所在 | 有効な仮定と結論 | 点検した内容 |
| --- | --- | --- |
| `lem:ci-low-twist-vanishing`、`complete_intersections.tex` | 滑らかな完全交叉、n>=2、1<=p<=n-1、t<=pならH⁰(Ω^p(t))=0 | Koszulによる線束消滅、穿孔錐のconormal外積分解、水平形式とCartan公式による独立証明。既知結果である |
| `prop:pg-represent`、`prop:pg-jacobi-extension`、`lem:pg-linearize`、`poisson_geometry.tex` | n>=3、Xが滑らかな三次。Poisson表示、Jacobi条件とHessian線形条件の対応 | Euler/Koszul、divergenceの係数、Hessianとの符号を追跡 |
| `lem:pg-quadratic-lie`、`thm:pg-normal` | 全非零Poisson構造が三変数Jacobianブロックへ分解 | 非退化形式の同時選択、可解根基、最高ウェイト、rank>=2単純因子の排除、混合項の消去 |
| `lem:pg-projective-rank`、`thm:pg-bondal`、`bondal_cubic.tex` | 全2j<nについてdim D_(2j)>=2j+1 | joinの次元、Euler線によるrank低下、ブロック数の端のケース |
| `prop:pg-deg-ideal`、`lem:pg-critical-cover`、`prop:pg-deg-support`、`prop:pg-zero-ci` | 一般退化イデアルは全正規形。critical coverと零点完全交叉には各純active三次の滑らかさが必要 | 正規形に基づく式と仮定の使い分け |
| `prop:pg-split-elliptic`、`cor:pg-cubic-fourfold-elliptic` | 滑らかな三次四様体の一般階数四の構造は全て分離型で純楕円log symplectic | 具体例の滑らかさ、正規なjoin、Pfaffian、被約Poisson零点、modular場、正規形からの分類。Pym v1の非連結持上げ障害も独立に確認 |
| `thm:pg-universal-determinant`、`universal_casimir_determinant.tex` | 全体三次fが滑らかなら、active制限が特異・零でも、原点近傍に代数的中心三次元 | gcd、古典核、普遍行列、局所自由性、稠密Hesse開、Cramer規格化、偶性 |
| `lem:pg-det-divided-kernel`、`prop:pg-det-normalization-transition`、`thm:pg-det-global-coefficient-lift` | 固定変数分解の全係数空間×h内で、全零切断を含む開上の偶な中心元。遷移はΩ'=aΩ+c | 任意底変更、通常の中心との差、偶principal開、忠実平坦下降、UFD/Pic=0、単元補正、Hesseのイデアル不一致、covarianceを独立に再点検 |
| `thm:pg-equivariant-levi-center`、`equivariant_central_lifts.tex` | 全滑らかなfでG_0同変な偶中心元。定義開も不変で全零切断を含む | stable idealへのReynolds平均、twistした古典切断の持上げ、商線束の零点除去 |
| `thm:pg-equivariant-parabolic-center` | g=f(x,0)も滑らかなら、中心平行移動を含む全G同変中心元 | δ_gの同変左逆、B_fの変換則、中心調整した三次式と開集合の引戻し |
| `cor:pg-equivariant-central-quotient` | 線形群の商上の次数別平坦なAS-Gorenstein中心商族 | t=ηhでhを固定、domainと正則性、各次数の局所自由性、スカラーの重み |
| `prop:pg-equivariant-poisson-gerbe`、`cor:pg-equivariant-character-descent` | gcd(m,3)=1なら次数線形化を補正して階数二のPoisson層内の開へ降下。n=3で底は17次元 | GLの付随束表示、方程式スカラー、中心gerbe、mr−3s=1による群の分裂。固定h≠0での像の次元は未主張 |
| `thm:pg-quantization`、`thm:pg-ad-all-poisson` | 全Poisson構造について原点を含むZariski開上のAS-regular ambientと中心正則三次商 | 中心三次配分、PBW、Koszul tensor、中心元の正則性、AS-Gorenstein change of rings |
| `thm:pg-all-dimensions`、`cor:pg-ad-whole-pencil`、`prop:pg-ad-intrinsic-hessian` | 各純active三次が滑らかな場合は独立多変数底と短い多項式中心公式 | 係数環上の自由性、全パラメータでの多項式中心性、交差補正がないこと |
| `thm:pg-fermat-relative-count`、`fermat_relative_poisson_components.tex` | Fermat固定space、固定stack、全cubic相対stackの位相的既約成分 | Hessianによるブロック復元、有限群軌道、被約rank層、同時スカラー作用、閉包の非包含 |
| `ne:main`、`nonelliptic_poisson_components.tex` | 二つの固定された滑らかなcubic fivefoldに2次元の非楕円Poisson成分 | 現行コードによる整数証明書・直接Schouten線形化の検証結果、接空間から成分性への議論 |
| `thm:pg-ambient-recovery-general`、`thm:pg-ambient-recovery-polarized`、`ambient_recovery_general.tex` | 二次包絡と三次核。圏からの復元には本文のnoetherian・AS-Gorenstein条件 | 低次数積、section algebra、飽和のExt消滅 |
| `prop:pg-ambient-even`、`cor:pg-ambient-derived-threefold` | C上、二変数中心、中心上自由性、左右noetherian性、所定のSerre関手を仮定 | conicからの中心復元、局所化と交叉、次数の再設定、必要仮定の明示 |

全モジュライ上の同変量子化、粗モジュライの構成、Poissonスキームの全被約構造、
全閉パラメータでのqgr滑らかさ、特殊点を含む相対残余圏同値はここでの定理ではない。
B-v57の一変数一般点での全coherent残余圏復元（同値は有限拡大後）とは区別する。

## 誤りを避けるための構造上の要点

### 相対Poisson空間

`poisson_moduli_stacks.tex` の相対Poisson空間は、
$\mathcal E=\Lambda^3V\otimes\mathcal O_{U_N}(-1)$ の全空間に閉埋め込みされる。
底 $U_N$ への忘却射自体は有限型アフィン射であり、一般には閉埋め込みではない。
固定F上にはPoisson構造を動かす非自明なファイバーがある。

相対Koszul複体は、被約底上で各次数のコホモロジー次元が一定であることから局所分裂し、任意底変更と両立する。
普遍三次式をアフィン錐で扱うときは $(F,P)\mapsto(aF,a^{-1}P)$ で割る必要がある。
被約rank層は $GL_N\times^{\operatorname{Stab}(P_k)}\mathcal F_{N,k}^{sm}$ から得られ、
射影化のための $\mathbb G_m$ が次元を1下げる。スタビライザーの次元は $8k+3km+m^2$。
この規約を落とすと相対次元と成分数の議論が不正確になる。
詳細は `notes/fermat_relative_poisson_components.md`。

### 中心二変数とambient復元

$S=\mathbf C[u,v]$、$D=S^{(2)}=\mathbf C[a,b,c]/(ac-b^2)$ とする。
$D_1$ のconicのgraded自己同型は $GL_2/\{\pm1\}$ から来る。
偶数Veroneseを元の次数の2倍に戻してからSとtensorし、uとvの局所化を取る。
$S[u^{-1}]=D[(u^2)^{-1}]\oplus uD[(u^2)^{-1}]$ と奇数部分の記述、
S自由基底に関する交叉から元の代数を回復する。
このため商代数自身のS自由性が必要である。

**ambientのPBW性だけでは商のS自由性は従わない。** 例えば $B/(u^3)$ はS-torsionを持つ。
active filtrationに関して中心三次元Gの最高記号 $g_3$ が正則で、
$\operatorname{gr}B=S_{f_3}\otimes S$ なら
$\operatorname{gr}(B/(G))=(S_{f_3}/(g_3))\otimes S$ となり、斉次基底の持上げでS自由性を得る。
これは `eq:pg-ambient-quotient-symbol` の十分条件である。
導来復元の系にはBの左右noetherian性を明示し、AのAS-Gorenstein injective dimension 4からsection algebraを回復する。

### 正規形とBondalの下界

$K(P)$ の基点自由性からVとsupport Wの両方に非退化なBを取るには、二つの非空開集合の交叉を使う。
可解根基の作用が既約加群上スカラーとなるだけでは零とはいえず、$W=[W,W]$ によるtrace零性を併用する。
最高根が単純根ではないことは、隣接単純根のroot stringを使って正当化する。

半単純性を得た後の二次形式の核はDerdzinski--Gal Theorem Bの直接の帰結でもある。
本稿の追加の還元は、Hessianの基点自由性から可解根基を排除する段階である。
Cartan三形式によるブロックの復元も同論文Lemma 7.1(a)で述べられるが、
公開PDFの補助主張(e)の最小像の説明にはsl₂⊕sl₂の混合rank 1+2による反例がある。
これはLemma 7.1(a)の結論への反例ではなく、本稿は`ne:blocks`の独立証明を用いる。
詳細と一次資料の所在は `notes/bondal_cubic.md` に整理する。

rank 2rの二重ベクトルを一次元Lで割ったときのrankは、
$L\subset\operatorname{im}b$ なら2r-2、それ以外なら2rである。
この線形代数補題を明示して、join上でEuler線が像に入ることとBondalのrank評価を結ぶ。
本文の一般証明と一具体例の外積計算は別である。詳細は `notes/bondal_cubic.md`。

### 分離型三次四様体と非連結曲線の持上げ

F=f(x)+g(y)ではD=V(f,g)が正規な(3,3)完全交叉で、
特異集合は互いに素な楕円曲線E_f、E_gとなる。
E_f近傍でπ=A∂w∧E_v+q_g、(1/2)π²=3Agν⁻¹、
modular場はE_f上で−3A∂w≠0である。
Poisson零点スキームは被約だが、Dの特異スキームは各曲線の横断方向に長さ8を持つ。
Pym arXiv:1507.05668v1 Definition 4.2の全条件を満たす。

同版Theorem 1.3のcubic非存在、Proposition 5.7の非正規性とは両立しない。
Lemma 5.5の証明が使うH¹(I_C)=0はC=E_f⊔E_gでは誤りで、H¹(I_C)=H¹(I_C²)=Cとなる。
g|_Xのambient liftはλf+(1+λ)gで、E_fでの三重消滅はλ=0、E_gではλ=−1を要求する。
IをP⁵内、JをX内のCのイデアルとすると、
0→I²→I³(3)→i_*J³(3)→0の境界類δ(g|_X)は非零で、H¹(I²)を生成する。
比較対象はこのv1に限定する。刊行版の書誌とOxford accepted manuscript登録は確認したが、
刊行本文・accepted本文は取得できず、訂正状況の確定も未了である。
独立な反例証明と一般階数四の分類は本文に保持し、未取得資料の内容を推測しない。

## 代数的中心元の証明の依存

1. `lem:pg-det-gradient-coprime`：全体fの滑らかさから $\gcd(f_x,f_y,f_z)=1$。
   共通因子と中心偏微分を同時に消す非零点がKrullの高さ定理から生じれば、全勾配の零点となって矛盾する。
2. `lem:pg-det-classical-kernel`：三次古典Casimirは $\mathbf C f+\mathbf C[u]_3$。
   分数体上の比例係数はgcd=1により多項式で、斉次次数から定数となる。
3. `lem:pg-det-universal-rank`：有限表示の次数別行列は被約な係数底上で一定階数を持ち、局所自由な商を与える。
   各固定fのh曲線上で、滑らかなactive制限に対するHesse中心公式から小行列式の消滅を得る。
   その後fを動かして普遍恒等式とする。Hesse座標の代数的な同時選択は仮定しない。
4. `thm:pg-universal-determinant`：古典rankの非零小行列を局所化し、Cramer法で $\Omega_0=f$ を規格化する。
   語の反転と $h\mapsto-h$ により係数は $h^2$ の有理関数となり、分母は原点で消えない。
5. `thm:pg-det-global-coefficient-lift`：固定した全係数空間の零切断全体を含む偶principal開へ縮める。
   割った交換子行列をτ=h²へ降ろし、factorial係数環のPic=0と特殊化の単元補正で全係数に正則な中心元を得る。
   規格化変更のaffine遷移は同じ中心イデアルを保証しない。実例と同変降下の条件は `notes/universal_casimir.md`。
6. `thm:pg-equivariant-levi-center`、`thm:pg-equivariant-parabolic-center`：
   affine底上でReynolds平均を定義開・中心元・方向微分の左逆へ適用する。
   滑らかなgでは混合二次項からB_fを作り、B_f'=(MB_f−C)N^-1を用いて全G同変に戻す。
   純中心係数の固定は全平行移動との同変性に一般には両立しないため、この規格化を外す。
7. `lem:pg-central-splitting-smooth`：純中心三次を各ブロックへ配分する。
   $u=0$ は全体Xの滑らかさ、$u\ne0$ は基点自由な線形系のBertiniを用いる。
   射影線形系のうち元のブロックの係数が非零のchartで係数を1に規格化し、必要なアフィン配分空間に戻る。
8. `thm:pg-quantization`、`thm:pg-ad-all-poisson`：各中心元の和、共有中心上のPBW/Koszul性、
   一つのactive blockのfiltrationによる正則性から、全Poisson構造と固定正規形のpencilを量子化する。
   非可換domainのtensor積が常にdomainである、という一般には誤る命題は使わない。

短い有限多項式中心公式には滑らかなactive制限が必要だが、Cramer構成は特異・零の制限を含む。
普遍Hesse証明書は独立混合係数を保持した有理関数体上の恒等式であり、数値特殊化による推測ではない。
内在的な二次補正は $H(P,F)=\frac16\sum P^{ijk}P^{abc}F_{ia}F_{jb}F_{kc}$、
正規形では $\sum_s\lambda_s^2\det\operatorname{Hess}_{x_s}(f_s)$。
四次補正を一つの座標不変式と断定しない。
詳しい公式、例、Dolgushevによる代替形式ルートの制約は `notes/universal_casimir.md` を参照する。

## 一次文献と本稿の位置づけ

| 文献 | 確認した所在・適用範囲 | 本稿との関係 |
| --- | --- | --- |
| Bondal, MPIM 93-67 (1993) | §4、印刷pp.11–12の無番号Lemma/Theorem | 射影Poissonの一意な斉次divergence-free持上げは既知。本稿はcubic上のJacobiatorの延長へ適用 |
| Derdzinski–Gal, DOI 10.1007/s12188-013-0085-z、arXiv:1304.2801 | 著者PDF (1.4) p.2、Theorem B p.3・§5、Lemma 7.1(a) p.10 | 式の符号・係数まで同じ核計算。半単純性への還元は別。ブロック復元は本稿の独立証明を使用 |
| Pym, DOI 10.1112/S0010437X16008174、arXiv:1507.05668v1 | 確認したv1 Definition 4.2、Theorem 1.3、Lemma 5.5、Prop.5.7 | 分離型例との不整合と非連結曲線の持上げ障害。刊行版本文・訂正状況は未確認 |
| Loray--Pereira--Touzet, arXiv:1112.3871v3 | Theorems 7.1, 9.1 | 三次三様体の分類は既知。本稿は高次元の複数Jacobianブロックを扱う |
| Mayanskiy, arXiv:1303.5916 | Theorem 1 | GrassmannスキームのJacobi方程式による記述とPoisson cohomology |
| Gualtieri--Pym, DOI 10.1112/plms/pds090 | Theorem 7.13 | Fano四次元のBondal予想は既知 |
| Druel--Pereira--Pym--Touzet, arXiv:2606.03424v1 | Theorem 1.2、Corollary 1.3、著者PDF | 奇数次元のsubmaximal退化軌跡とFano五次元。本稿はcubicというクラスで全次元・全rank |
| Darío Martín Aza, arXiv:2604.07217v1 | Theorem 1.3, p.2、証明p.10 | 隣接退化軌跡の真包含の下での選言。全Bondal予想の証明とは扱わない |
| Etingof, MIT 2024 lecture notes | Prop.16.9 p.88、Def.21.13/Lem.21.14 p.114、Thm.25.17 p.137、§32.2 p.173 | 可解根基、最高ウェイト、最高根の既知入力 |
| Mori--Smith, Math. Z. 287 (2017), 215--241, DOI 10.1007/s00209-016-1824-5 | 本文確認はarXiv:1502.07403v2。Thm.1.4、Cor.2.7/2.9、Thm.4.2(1)、Lemma 7.1/Thm.7.2 pp.23--24 | standard性、AS-regular/3-CY、滑らかな平面三次で全パラメータの判定、point curve |
| Berger--Taillefer, JNCG 1 (2007), 241--270, DOI 10.4171/JNCG/6 | 刊行PDFのThm.1.1(i) p.242、Thm.3.1 p.246、Thm.3.6 p.251 | 低次数potentialからのPBW変形。(ii)の逆向き分類の追加条件は使わない |
| Le Bruyn--Smith--Van den Bergh, Math. Z. 222 (1996), 171--212 | 著者PDF、Thm.2.6/Cor.2.7、Thm.3.1.3 | 中心正則拡大。Fermatブロックのパラメータ代入を本文で明示 |
| Smith--Tate; De Laet--Le Bruyn | 後者arXiv:1405.1158v1 §2 p.3 | 純Sklyanin中心公式は既知。本稿の追加は混合係数、普遍恒等式、Cramer構成。表示の誤植注意は中心ノートに記載 |
| Etingof--Ginzburg, arXiv:0709.3593v4 | Prop.8.1.1(i)、§8.3 | potentialのrankと特殊化の既知手法。本稿の規格化された有限Cramer構成と比較 |
| Derksen, Advances in Mathematics 141 (1999), 366–384 | 著者公開PDF §2, p.369 | Reynolds射影とstable部分加群を保つ性質は既知。本稿は不変開・中心lift・方向微分の分裂へ適用 |
| Dolgushev, Selecta Math. 14 (2009), 199--228, DOI 10.1007/s00029-008-0062-z | 本文確認はarXiv:math/0612288v3 Prop.1 p.9、Thm.3 pp.15--16 | 条件は全形式Poisson classのunimodularity。本稿の代数化の証明には用いない |
| Fu--Hwang, arXiv:1608.00846v2 | Lemma 4.1 p.13：完全交叉Zで1<=r<=dim Z-1、p<=rならH^0(Ω_Z^r(p))=0 | Brückmann型消滅の明示的定理文と適用条件を確認 |
| SGA 2 XII Cor.3.7、Stacks Tags 06FI/0BCH、Artin--Zhang | Picard群、商stack、UFDのPic=0、section algebra | モジュライ・係数空間上の中心元・偏極付き復元の既知の一般原理 |

文献URL・DOIと現在の引用キーは専用参考文献にある。
Brückmannの1976年論文はMath. Nachr.71,203--210、DOI 10.1002/mana.19760710116で書誌を確認した。
1977年続編はFu--Hwangの書誌でMath. Nachr.77,307--318。
**原証明（1976年Satz 3、1977年Satz 6）は未取得であり、読了と報告しない。**
必要な低twist範囲には本文`lem:ci-low-twist-vanishing`で独立証明を与えたので、
現行の完全交叉の存在判定は未取得の原証明に依存しない。
高次元の正規形・Bondalのjoin証明・相対成分数・量子化の包括的結論と同一の先行定理は調査範囲で確認できていないが、初出は未確定である。
刊行書誌を確認したことと、その刊行版の定理番号・証明全文を再照合したことも区別する。

## 実行済みの厳密計算と限界

以下は現行スクリプトの作業環境での実行状態であり、GitHub Actionsによる実行ではない。
本改訂では中心調整の変換則を、25個の独立混合係数と二組の有理座標変換で厳密に検算した。
分離型四様体の計算はA-v53、他の七本はA-v52での実行結果を保持する。
それら八本のスクリプト・必要な証明書のハッシュ一致を確認し、本改訂での再実行とは区別する。
スクリプトハッシュと最終状態は `validation_paper_a.json`。

| スクリプト（computations/） | 結果と範囲 |
| --- | --- |
| `verify_equivariant_centering.py` | 25混合係数を記号のまま保持。二組の座標変換で左逆、B_fの変換、中心調整した三次式、三つのJacobian括弧がPASS。Reynolds存在や全群定理の計算機証明ではない |
| `verify_split_cubic_fourfold.py` | 分離型Fermat例のambient 20 Jacobi成分とCasimir、射影10括弧・10 Jacobi・接性、暗黙消去後の4 Jacobi、Pfaffian、modular場の二通りの計算がPASS |
| `verify_poisson_article_A.py` | 滑らかな一具体例、56 Jacobi成分と56 Euler外積成分が厳密に零 |
| `verify_nonelliptic_components.py --direct` | nodal/cuspidal両例でHessian線形化と直接Schouten線形化のrank 33。保存した整数小行列証明書を照合 |
| `verify_poisson_stack_component_counts.py` | n=3,...,10の三種類の成分数、全8行一致 |
| `verify_universal_hesse_mixed_center.py` | 339基底語、162関係倍数、rank 144。Q(h,t)上で独立な6混合係数を保持し、3交換子が恒等的に零 |
| `verify_cubic_casimir_jet.py` | 20自由係数。x,y,z各交換子の125個の語・次数係数が零。有限jetの検算であり、任意次数の中心性を単独で証明しない |
| `verify_singular_cubic_classical_kernel.py` | active制限0の滑らかな例で378×56行列のrank 45、核次元11 |
| `verify_nonelliptic_quantization.py` | 二つのmonic Diamond系と重なり、六普遍中心交換子、h=0極限、potential syzygy、分母範囲、二つのnegative control、17項Fermat恒等式がPASS。保存JSON全体と厳密一致 |

非楕円例の33次小行列式は nodal: $8916100448256=2^{24}3^{12}$、
cuspidal: $-4565043429507072=-2^{33}3^{12}$。
その非零性と既知の2次元pencilにより接空間次元2を得る。
元のPoissonスキームは有限型Cスキームなので、正則局所環から該当点での滑らかさを結論できる。

独立多ブロックの補助例・Hesse平行移動・別のminor等のコードも保持しているが、
上表にない計算を今回再実行済みとは扱わない。
有限例のJacobi/rank検算は全次元正規形や成分定理の一般証明の代わりではない。
普遍係数での恒等式検証と有限例への特殊化を区別する。

## 再現と残る課題

```sh
python3 scripts/check_layout.py
python3 scripts/build.py --only paper_a
python3 scripts/verify_bundle.py --only paper_a --require-pdfs
python3 computations/verify_equivariant_centering.py
python3 computations/verify_split_cubic_fourfold.py
python3 computations/verify_poisson_article_A.py
python3 computations/verify_nonelliptic_components.py --direct
python3 computations/verify_poisson_stack_component_counts.py
python3 computations/verify_universal_hesse_mixed_center.py
python3 computations/verify_cubic_casimir_jet.py
python3 computations/verify_singular_cubic_classical_kernel.py
python3 computations/verify_nonelliptic_quantization.py
```

大きな記号行列のスクリプトは一つずつ実行する。
組版の成功、PDF表示の確認、数学的証明の監査、遠隔保存は別々に記録する。

優先課題は、Pym刊行本文・訂正状況の照合、包括的な結果の初出照合、
特異な三変数制限での全G同変選択、および複数ブロックの配分・相対規格化の整合性である。
smooth gでの中心調整とG_0平均は本文で解決した範囲として扱う。
gcd(m,3)=1では指標補正により中心スカラーを除いたPoissonモジュライへの
次数付き代数の下降まで得た。3|mの場合と、全モジュライでのカテゴリーの降下は区別する。
Brückmann原証明の入手は帰属の補充として残るが、本文の消滅証明の未解決箇所ではない。
相対残余圏と全閉パラメータの滑らかさは独立の研究課題として扱い、原稿Aの確立した結果の仮定へ曖昧に混ぜない。
公表価値は主要結果の正確さと既知結果との差から判断し、形式検証・外部査読・初出確定が済んだとは断定しない。

GitHub mainが正本。節目の保存に追加承諾は不要。LibraryはGitHub保存が実際に失敗した時だけ緊急退避に用いる。
