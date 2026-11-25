# Poisson論文：主張・依存・一次資料の確認範囲

2026-11-25 / v5（A-v66、repo v101）。最初に `00_research_plan.md` を読む。
この文書は現行原稿の仮定・証明所在・一次資料の確認範囲を整理する。
証明の構成と引用箇所は現行ソースに合わせている。既存の内部点検は過去の確認範囲であり、今回の通読と編集は全証明の再査読・形式検証を意味しない。
新規性・外部査読の確定と、証明記載・内部点検・有限計算・組版は別の状態である。

本文は `papers/poisson-cubic.tex`、文献は `papers/support/papers/references_poisson_cubic.tex`。
節ファイルは `papers/support/papers/sections/` に置く。
量子化の主原稿は [cubic-quantization](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex)、
関連する確認記録は [量子化監査](https://github.com/uedakazushi/nc-cubic/blob/main/notes/quantization_audit.md)を参照する。可換復元は `nc-cubic` の `papers/nc-cubic.tex` が正本である。

## 公表範囲

arXiv公開・論文誌投稿を予定し、標準的背景を持つ隣接分野の研究者が通読できる原稿とする。本文では数学的な仮定、論証、引用結果との関係を展開し、文献取得・作業管理・検査履歴は本ノートと検証記録に置く。未検証の公開草稿の位置づけは引用箇所に残し、計算による証明では入力、係数環、方法、出力・証明書、再現先を省かない。

中心結果は全次元のJacobianブロック正規形、Bondal下界、退化軌跡、固定・相対Poisson成分と三次四様体の分離型判定である。
Hessianの可約性だけでは不十分な滑らかな例、非連結中心に沿う同次数持上げ障害を保持する。
量子化・非可換ambient復元の結論を本稿の定理番号へ混在させない。

独立な六・七次元のprimary厚化（長さ8, 64, 49）と数値幾何は
`uedakazushi/nc-cubic2` の `papers/poisson_cubic_six_seven_geometry.tex` が現行入口であり、
Aの一般定理の証明を移管先へのリンクで代用していない。
移管先の独立公表価値とprimary分解の監査は、Aの検証とは別である。


## 主張と証明の所在

| 主張・所在 | 有効な仮定と結論 | 証明の構成・保持する確認範囲 |
| --- | --- | --- |
| `lem:ci-low-twist-vanishing`、`complete_intersections.tex` | 滑らかな完全交叉、n>=2、1<=p<=n-1、t<=pならH⁰(Ω^p(t))=0 | Koszulによる線束消滅、穿孔錐のconormal外積分解、水平形式とCartan公式による独立証明。既知結果である |
| `prop:pg-represent`、`prop:pg-jacobi-extension`、`lem:pg-linearize`、`poisson_geometry.tex` | n>=3、Xが滑らかな三次。Poisson表示、Jacobi条件とHessian線形条件の対応 | 現行本文はEuler列による接性の補正、gradientのKoszul複体、E∧J=FQからNJ=3Jへの持上げ、係数次数1のsyzygy消滅によるHessian線形化を展開 |
| `lem:pg-nondegenerate-pencil`、`lem:pg-basepoint-free-lie`、`lem:pg-quadratic-lie`、`thm:pg-normal` | 全非零Poisson構造が三変数Jacobianブロックへ分解 | 現行本文は支持W上の非退化形式、完全かつ中心なしのLie代数、可換イデアル内のsl₂加群と最高根による共通零点、Cartan3形式の分解、混合項の消去を使用 |
| `lem:pg-projective-rank`、`thm:pg-bondal`、`bondal_cubic.tex` | 全2j<nについてdim D_(2j)>=2j+1 | joinの次元、Euler線によるrank低下、ブロック数の端のケース |
| `prop:pg-deg-ideal`、`lem:pg-critical-cover`、`prop:pg-deg-support`、`prop:pg-zero-ci` | 一般退化イデアルは全正規形。critical coverと零点完全交叉には各純active三次の滑らかさが必要 | 正規形に基づく式と仮定の使い分け |
| `prop:pg-split-elliptic`、`cor:pg-cubic-fourfold-elliptic` | 滑らかな三次四様体の一般階数四の構造は全て(3,3)分離型で純楕円log symplectic。その存在はambient Hessian階数≤3軌跡が平面を含むことと同値 | join・Pfaffian・被約Poisson零点・modular場の既存直接証明を保持。BFP Theorem 3.4のn=5,k=2の照合を保持。Pym v1 Definition 4.2との適合を再読 |
| `ex:pg-reducible-hessian-no-rank-four` | F=x₀³+x₁³+Σzᵢ³−(Σzᵢ)³は滑らかでHessian可約だが(3,3)型に分解しない | 符号による滑らかさ、全点での定数symmetrizer E_F=diag(a,b,cI₄)、座標共役、階数三冪等元の不存在を独立に読解。QQ線形代数の検算は別記 |
| `prop:pg-triple-lifting-obstruction`、`cor:pg-split-lifting-obstruction`、`poisson_geometry.tex` | 滑らかな次数d超曲面内の滑らかな非空C、全連結成分が正次元。任意r>=2についてH¹(I_C^{r−1})=C^{π₀(C)}/C、次数d・r重消失の障害δ_r | ideal sheafの冪、正則局所方程式、余法束の全対称冪の切断消滅、全厚みの成分定数。連結時は存在・一意性。r=3の分離型でδ(g_X)≠0。全射性と任意twistへの拡張は未主張 |
| `thm:pg-fermat-relative-count`、`fermat_relative_poisson_components.tex` | Fermat固定space、固定stack、全cubic相対stackの位相的既約成分 | Hessianによるブロック復元、有限群軌道、被約rank層、同時スカラー作用、閉包の非包含 |
| `ne:main`、`nonelliptic_poisson_components.tex` | 二つの固定された滑らかなcubic fivefoldに2次元の非楕円Poisson成分 | 現行コードによる整数証明書・直接Schouten線形化の検証結果、接空間から成分性への議論 |

粗モジュライの構成とPoissonスキームの非被約構造の完全な決定は本稿の結論ではない。

## 査読を踏まえた論証と説明の補足

A-v66は、commit `1437cab69fff5e9dd095241c45d67c5d1c634e1a`（A-v65）を対象とした2026-11-25の査読レポートに基づく改稿である。初読・論証の追跡・構成と組版を独立したAI読者に分担した読解であり、人間による外部査読や形式検証ではない。主要な分類結果は保持し、以下の適用範囲と中間論証を本文に統合する。

- `prop:pg-leaf-closure` は周囲の射影空間と超曲面上の葉をともに扱う。超曲面上では `Σd_s=0` を保った支配射を定め、滑らかな始域への一般的滑らかさを用いる。特に `k=1` では `d_1=0` である。
- `cor:pg-generic` の階数2の射影パラメータ空間は被約構造でGrassmannianと同一視する。Jacobiスキーム全体の非被約構造をこの集合論的分類から結論しない。
- 正規形のunorderedな3次元部分空間は内在的だが、補空間・基底・純中心項の配分は選択に依存する。許される3次式は異なる内在的ブロック間の混合Hessianの消滅で定まるので、余次元計算に補空間のパラメータを加えない。
- 相対成分の議論では、滑らかさを課す前の全3次式を扱う段階でHessian条件の逆向きを直接証明する。混合成分を除いた各寄与は3次元空間上の交代4形式である。
- 第5節末のFermat三様体の例で、第一積分、滑らかな一般葉の閉包、零点の楕円曲線と長さ24の残余スキームを具体化する。Fermat四様体の成分数11と自己同型商の成分数2も定理の直後に説明する。

Pymとの不整合と非連結中心の障害は序論から読める形にし、書誌ではarXiv v1と刊行版を分ける。本文の記号、成分数表、付録の式・命題番号と改ページを整える。改稿後の別の初読者が指摘した、付録の形式次数と点の記号の重複も解消した。計算コード・保存済み証明書は変更していない。日付入りPDFの生成スクリプトは、任意metadataの新規作成後にも表紙を再組版するようにした。

## 構造上の要点

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

`lem:pg-intrinsic-block-cover` は既存のunordered block復元を有限étale被覆に整理する。
ブロック被覆O^blkの次数はk、順序付けtorsorの次数はk!であり、補空間や中心配分を選ぶ被覆ではない。
全階数層のgerbe位数はFermat点での交換子から求める。
3|Nなら全座標を三つ組に分け、各組の巡回SとT=diag(1,ζ,ζ²)は(F,P_k)を固定する。
[S,T]=ζ⁻¹I_Nなので、同変可逆層の重みは三の倍数である。
λ⁻¹の重み三とgcd(N,3)=1での重み一指標を合わせると位数gcd(N,3)を得る。
全層を含む結論であり、Fermat点を除いた稠密開や一般Brauer類の位数へ読み替えない。

### 正規形とBondalの下界

`prop:pg-represent` はEuler列から得る接性の補正 $q=B-E\wedge A/3$ とgradientのKoszul複体により、定数3重ベクトルPの存在・一意性を示す。
`prop:pg-jacobi-extension` では $J=[q,q]/2$ に対し、局所座標でのJacobi恒等式を $E\wedge J=FQ$ へ移す。
$\iota_{dF}J=0$、$\delta J=0$ と定数係数syzygyの消滅から $\delta Q=0$ を得て、Euler–divergence恒等式により $NJ=3J$、従ってN>=5でJ=0となる。

$K(P)$ を三重ベクトルの支持Wへ制限した線形系は基点を持たない。`lem:pg-nondegenerate-pencil` をこの制限系に適用してW上の非退化形式Bを選び、そのBでPの添字を下げてLie代数を構成する。周囲V上でも同時に非退化となる形式を選ぶ必要はない。
括弧の値がWを張ることとBの不変性から、$W=[W,W]$ と $Z(W)=0$ を得る。
可解根基内の極小可換イデアルIに対しては、根基のスカラー作用とtrace零性を併用して根基の作用を零にする。
半単純商の根sl₂部分代数がIに非自明に作用することと有限次元sl₂表現の完全可約性から、正の最高ウェイトを持つベクトルを取る。
本文の `eq:pg-radical-witness` を4変数の恒等式に代入すると全Hに共通する零点が生じ、根基を排除できる。
階数2以上の単純因子も、最高根を二つの正根の和に表した交換子を同じ恒等式へ代入して排除する。最高根が単純根ではないことは、隣接単純根のroot stringを使って正当化する。

半単純Lie代数上の二次形式の核はDerdzinski--Gal Theorem Bでも記述される。
現行本文は必要な半単純性と単純因子の3次元性を基点自由性から直接導き、この核計算を証明の必須入力とはしない。
Cartan三形式によるブロックの復元も同論文Lemma 7.1(a)で述べられるが、
公開PDFの補助主張(e)の最小像の説明にはsl₂⊕sl₂の混合rank 1+2による反例がある。
これはLemma 7.1(a)の結論への反例ではなく、本稿は`ne:blocks`の独立証明を用いる。
詳細と一次資料の所在は `notes/bondal_cubic.md` に整理する。

証明構成の参照版は `uedakazushi/nc-cubic-lean` のcommit `9736787f3a95f52bc3d233ab768a6ab6396d0c24` である。
各Leanファイル・定理との対応は `notes/lean_proof_sources.txt` に記す。
今回Leanの再ビルド・公理依存監査は行っておらず、TeX本文の形式検証を主張しない。
参照版の幾何学的主定理は非零Poisson構造のブロック正規形と逆構成を扱い、一般階数・退化スキーム・Bondal下界・固定および相対モジュライはその形式化された結論に含まれない。

rank 2rの二重ベクトルを一次元Lで割ったときのrankは、
$L\subset\operatorname{im}b$ なら2r-2、それ以外なら2rである。
この線形代数補題を明示して、join上でEuler線が像に入ることとBondalのrank評価を結ぶ。
本文の一般証明と一具体例の外積計算は別である。詳細は `notes/bondal_cubic.md`。

### 分離型三次四様体、Hessian判定と持上げ

Bricalli–Favale–Pirolaの刊行Theorem 3.4は、滑らかなcubicの(k+1,n−k)分離型と、ambient Hessian階数≤k+1軌跡内のP^kの存在を同値にする。n=5,k=2を本稿の正規形に合わせるとrank4 Poissonの存在を方程式Fだけから判定できる。平面はX内ではなくambient P⁵内にある。Theorem AのHessian可約性・非正規性の条件は全サイズの分離を含むため、(3,3)条件とは区別する。

反例 `ex:pg-reducible-hessian-no-rank-four` の定数symmetrizerはdiag(a,b,cI₄)である。その冪等元の階数は0,1,2,4,5,6だけなので、座標に依存しない(3,3)分解の障害になる。E_Fの条件はHessianの全係数に対する恒等式であり、一点の行列に関する自己共役性ではない。既知Hessian判定そのものの新規性は主張しない。

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
2026-11-25の追加確認では、Cambridgeの正式PDFリンクはabstractページへ転送され、[McGill著者サイトの論文一覧](https://www.math.mcgill.ca/bpym/papers-bib.html)もDOIとarXivへのリンクのみであった。Oxfordの受理原稿登録は引き続きメタデータの確認にとどまる。今回の追加照合によって刊行版本文を確認済みとは扱わない。

一般次数の持上げ命題では、全連結成分が正次元なら
周囲をP^Mとし、余法束→Ω¹_P|C→O_C(-1)^{M+1}の部分束埋込みの対称冪から、全j>=1でH⁰(I^j/I^{j+1})=0となる。
全ての厚みの大域関数は成分定数だけなので、任意r>=2でH¹(I^{r−1})=C^{π₀(C)}/Cである。
0→I^{r−1}→I^r(d)→i_*J^r(d)→0によりr重消失の持上げ障害を得る。
ここでd=deg Xに固定することが重要であり、次数eなら障害群はH¹(I^{r−1}(e−d))となる。
正次元という仮定は不可欠な証明入力であり、点を含む中心へ無条件に拡張しない。
独立命題は文献比較から切り離され、連結時の存在・一意性も明示する。

確認した版の番号・頁は、Theorem 1.3 p.4、Definition 4.2 p.17、
Lemma 5.5 pp.28–29、Proposition 5.7 p.30である。
刊行版・Oxford受理原稿の本文は未取得であり、登録メタデータの確認を本文照合の代わりにしない。
訂正文の不存在も結論しない。
公開v1: https://arxiv.org/pdf/1507.05668v1
刊行書誌: https://doi.org/10.1112/S0010437X16008174
受理原稿登録: https://ora.ox.ac.uk/objects/uuid:a457621f-f733-41b0-99c7-fa475b8e807e



## 一次文献と位置づけ

序論の完全交叉の4型は、複素数体上の通常の射影空間内の滑らかな完全交叉で、次元n>=3、一次方程式を除いた多重次数d_i>=2という範囲で述べる。
s=Σ(d_i−1)に対しΛ²T_X≅Ω_X^(n−2)(n+1−s)であり、s>=3ならFu--Hwang Lemma 4.1の低twist消滅が適用できる。
残る射影空間・2次超曲面・3次超曲面・(2,2)完全交叉での存在は本文 `thm:ci-poisson-existence` にある。曲面ではK3完全交叉も現れるため、n>=3を外さない。

「最初の例」は、射影完全交叉の一つの型に属する全ての滑らかなメンバーの全ての非零Poisson構造を、全次元n>=3・全一般階数にわたり同じ正規形で記述する、という限定付きの位置づけである。
現行序論は「著者の知る限り」と留保する。任意次元の特定成分・特定退化条件の分類や一般構造定理には先行研究があり、包括的な優先権の確定ではない。
序論の定理文・適用範囲・書誌についてはA-v64で照合した。A-v65では本文と書誌の表現・配置を整え、原稿全体に対して独立したAI読者による通読を行った。これらは既存の全証明の再査読、Lean検証、Poisson P4原稿の証明検証とは区別する。

| 文献 | 原稿の引用箇所・既存の確認範囲 | 本稿との関係 |
| --- | --- | --- |
| Bondal, MPIM 93-67 (1993) | §4、印刷pp.11–12の無番号Lemma/Theorem | 射影Poissonの斉次divergence-free持上げは既知。本稿はEuler–divergence恒等式を明示し、cubic上で消えるJacobiatorを錐上へ持ち上げる |
| Derdzinski–Gal, DOI 10.1007/s12188-013-0085-z、arXiv:1304.2801 | 著者PDF (1.4) p.2、Theorem B p.3・§5、Lemma 7.1(a) p.10 | 同じ4変数の恒等式の核計算との比較。現行本文は半単純性・3次元性・ブロック復元に独立の証明を用いる |
| Bricalli–Favale–Pirola, Forum Math. Sigma 13 (2025), e80, DOI 10.1017/fms.2025.36、arXiv:2406.12024 | 刊行Theorem A p.2、Theorem B p.3、Theorem 3.4 p.10・証明pp.11–12 | Hessian階数軌跡による分離型判定は既知。本稿はn=5,k=2をrank4 Poisson存在に結び付ける |
| Pym, DOI 10.1112/S0010437X16008174、arXiv:1507.05668v1 | 確認したv1 Definition 4.2、Theorem 1.3、Lemma 5.5、Prop.5.7 | 分離型例との不整合と非連結曲線の持上げ障害。刊行版本文・訂正状況は未確認 |
| Cerveau--Lins Neto, Ann. of Math. (2) 143 (1996), 577--612, DOI 10.2307/2118537 | Annals公式の原論文要旨と書誌、LPT §6 Theorem 6.1での定理再掲を確認 | P^n、n>=3の次数2・余次元1の葉層構造の6成分。高次元の全Poisson構造の分類ではない。P³ではΛ²T≅Ω¹(4)を用い、因子零点を含む適用はLPT §9と合わせる |
| Loray--Pereira--Touzet, Math. Nachr. 286 (2013), 921--940, DOI 10.1002/mana.201100354、arXiv:1112.3871v3 | 訂正済みv3のTheorems 7.1, 9.1とTable 1 | Picard数1の滑らかなFano三様体。非零構造をスカラー倍で割った空間ではP³は6成分、Q³は3成分。三次三様体のpencilによる分類は既知。旧版の9・4という数を使用しない |
| Mayanskiy, J. Algebra 424 (2015), 21--45, DOI 10.1016/j.jalgebra.2014.08.049、arXiv:1303.5916 | Theorem 1（原稿p.2）と帰属の説明（p.3） | 三次三様体のPlücker埋め込みGr(2,5)をJacobi方程式から記述し、Poisson cohomologyを計算。分類自体はLPTに帰属する |
| Druel, Bull. Soc. Math. France 127 (1999), 229--253, DOI 10.24033/bsmf.2347 | 刊行原典Introductionの主定理、p.230 | 滑らかな射影三様体の非零quasi-regular Poisson構造（有限点を除きrank 2）を分類し、至る所rank 2となることを示す。任意の特異Poisson構造の分類ではない |
| Lima--Pereira, Bull. Lond. Math. Soc. 46 (2014), 1203--1217, DOI 10.1112/blms/bdu074、arXiv:1312.3596v2 | Theorems 1--2 | 全n>=3でP^nの対角構造の閉包は1既約成分。偶数次元>=4、Pic(X)=ZのFano、generically symplectic、被約SNC退化因子という仮定ではXが射影空間で構造が対角型となる |
| Druel--Pereira--Pym--Touzet, Geom. Topol. 26 (2022), 2831--2853, DOI 10.2140/gt.2022.26.2831 | 刊行原典Theorem 1.1、p.2832 | compact Kähler Poisson多様体が有限基本群のcompact symplectic leaf Lを持つなら、有限étale Poisson被覆L̃×Y→Xが存在する。任意次元の構造定理であり、固定Fano上の全Poisson構造の分類ではない |
| Corrêa--Muniz, arXiv:2207.12880v5（2026-01-19） | Theorem Aと直後の範囲説明、Corollary C、§5 | 次数2の葉層構造とrank 2 Poisson幾何。既約成分の精密記述には一般元の非代数的可積分性・接層の安定性等の限定があり、代数的場合の成分所属には未解決部分が残る。P⁴のCorollary Cも一般元・因子零点なしを仮定し、非分解型ではnormal crossing typeを扱う。全rank・全次元のPoisson分類とはしない |
| Matviichuk--Pym--Schedler, arXiv:2010.08692v2（2021-07-15） | Theorems 1.2--1.4、§5.3 | SNC退化因子を持つlog symplectic構造の近傍の変形理論。Theorem 1.4の40成分はP⁴のSNC log symplectic軌跡と交わる成分であり、全成分の総数ではない |
| uedakazushi/poisson-p4、2026-11-09版v73、commit `f118dfbfc5bb9b7a394d1985b4800b6228eebaf6` | `papers/poisson_p4_classification_ja.tex` の固定公開版（2026-11-25参照）。本文の引用キー `PoissonP4Draft` に固定URLを記載 | 非零Poisson構造をスカラー倍で射影化した空間の被約既約成分が147=141（一般rank 4）+6（一般rank 2）という分類案。PGL₅で割る前の成分数。人間による証明検証は未完了であり、本稿の既知定理として使用しない |
| Gualtieri--Pym, DOI 10.1112/plms/pds090 | Theorem 7.13 | Fano四次元のBondal予想は既知 |
| Druel--Pereira--Pym--Touzet, arXiv:2606.03424v1 | Theorem 1.2、Corollary 1.3、著者PDF | 奇数次元のsubmaximal退化軌跡とFano五次元。本稿はcubicというクラスで全次元・全rank |
| Darío Martín Aza, arXiv:2604.07217v1 | Theorem 1.3, p.2、証明p.10 | 隣接退化軌跡の真包含の下での選言。全Bondal予想の証明とは扱わない |
| Etingof, MIT 2024 lecture notes | 現行本文の引用：Thm.11.16 p.66、Prop.16.9 p.88、Lem.19.16 p.104、Cor.19.18/Thm.19.19 pp.105–106、Def.21.13 p.114、§32.2 | 有限次元sl₂表現の分解、既約表現上の根基のスカラー作用、根sl₂部分代数・根空間の交換子、最高根の既知入力 |
| Fu--Hwang, Asian J. Math. 22 (2018), 333--354, DOI 10.4310/AJM.2018.v22.n2.a10、arXiv:1608.00846v2 | Lemma 4.1 p.13：滑らかな完全交叉Zで1<=r<=dim Z-1、p<=rならH^0(Ω_Z^r(p))=0 | Brückmann型消滅の明示的定理文と適用条件を確認。序論ではr=n−2、p=n+1−sに適用し、n>=3・s>=3で大域双ベクトルの非存在を導く |

本文で引用する文献のURL・DOIと引用キーは専用参考文献にある。上表は背景比較の記録も含み、今回新たに全ての原典を確認した記録ではない。
Brückmannの1976年論文はMath. Nachr.71,203--210、DOI 10.1002/mana.19760710116で書誌を確認した。
1977年続編はFu--Hwangの書誌でMath. Nachr.77,307--318。
**原証明（1976年Satz 3、1977年Satz 6）は未取得であり、読了と報告しない。**
必要な低twist範囲には本文`lem:ci-low-twist-vanishing`で独立証明を与えたので、
現行の完全交叉の存在判定は未取得の原証明に依存しない。
高次元の正規形・Bondalのjoin証明・相対成分数と同一の先行定理は既存の調査範囲では確認できていないが、包括的な初出は未確定である。
Pym刊行版本文・関連訂正文の照合を優先し、arXiv v1で特定した不整合を刊行版の主張へ無条件に移さない。

## 有限計算と再現

以下は保存済みの検算の内容であり、今回の実行と以前の記録は `validation_paper_a.json` で区別し、概要は `validation.json` を参照する。

| スクリプト（computations/） | 保持する検算の範囲 |
| --- | --- |
| `verify_hessian_split_obstruction.py` | 既存の結果。単一の具体例でHessian行列・行列式を照合。QQ上90方程式・36未知数のrank33、核dim3、冪等元の可能rank0,1,2,4,5,6。滑らかさ・一般分解判定・Poisson分類の証明ではない |
| `verify_split_cubic_fourfold.py` | 既存の結果。分離型Fermat例のambient 20 Jacobi成分とCasimir、射影10括弧・10 Jacobi・接性、暗黙消去後の4 Jacobi、Pfaffian、modular場の二通りの計算がPASS |
| `verify_poisson_article_A.py` | 既存の結果。滑らかな一具体例、56 Jacobi成分と56 Euler外積成分が厳密に零 |
| `verify_nonelliptic_components.py --direct` | 既存の結果。nodal/cuspidal両例でHessian線形化と直接Schouten線形化のrank 33。保存した整数小行列証明書を照合 |
| `verify_poisson_stack_component_counts.py` | 既存の結果。n=3,...,10の三種類の成分数、全8行一致 |

非楕円例の33次小行列式は nodal: $8916100448256=2^{24}3^{12}$、
cuspidal: $-4565043429507072=-2^{33}3^{12}$。
その非零性と既知の2次元pencilにより接空間次元2を得る。
元のPoissonスキームは有限型Cスキームなので、正則局所環から該当点での滑らかさを結論できる。

A-v65の編集時に `python3 computations/verify_nonelliptic_components.py` を再実行し、続く同版の査読では `--direct` を付けて直接Schouten線形化も照合した。両例の階数33と保存済み証明書との一致を確認した。A-v66ではコード・証明書を変更せず、この計算を再実行していない。本文には整数行列の係数規約、行選択の方法、固定版の公開計算資料へのリンクと実行コマンドを記す。


非楕円例の量子関係行列の行列式は、独立した量子化資産 `nc-cubic/computations/quantization/verify_nonelliptic_point_curves.py` と対応JSONへ分離した。
Poisson成分用の整数小行列・Jacobi・滑らかさの証明書は本repoに残す。

```sh
python3 scripts/check_layout.py
python3 scripts/verify_article_a_numbering.py
python3 scripts/verify_bundle.py --run-computations
latexmk papers/poisson-cubic.tex
python3 computations/verify_nonelliptic_components.py --direct
```

有限例の検算は全次元正規形・成分定理の一般証明を代替しない。出力PDFをGitで追跡せず、実行結果と組版確認の範囲を分けて記す。
