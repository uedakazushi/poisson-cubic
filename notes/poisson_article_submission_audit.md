# 論文Aの投稿準備：現行の監査と再開点

**2026-11-12 / A-v44。** 最初に 00_research_plan.md を読む。
論文本文は papers/paper_a.tex、専用文献は papers/support/papers/references_poisson_cubic.tex。
本ノートは現在有効な知識・依存・課題を整理し、証明全文を重複させない。

## 主張の確実性と所在

1. Poisson正規形（thm:pg-normal、papers/support/papers/sections/poisson_geometry.tex）：全非零構造の三変数Jacobianブロック分解。n>=3、X smooth。証明は記載済みだが、核心のLie代数補題 lem:pg-quadratic-lie を含め、今回の全面的独立監査は未完了。
2. Bondal予想（thm:pg-bondal、papers/support/papers/sections/bondal_cubic.tex）：全 2j<n について dim D_{2j}>=2j+1。j<k で j+1 個のブロック上の平面曲線joinを構成し、Euler線の射影化でrankが2低下する。正規形定理に依存。scheme-theoretic primary分解を与える主張ではない。高次元での新規性調査は未完。
3. 退化スキーム（prop:pg-deg-ideal）：任意の正規形に適用できる。critical cover と零点の完全交叉（lem:pg-critical-cover、prop:pg-zero-ci）には各 f_s(x_s,0) が滑らかな平面三次という追加仮定が必要。
4. 量子化（thm:pg-quantization）：個々のPoisson構造に対する原点を含む一変数Zariski開上のAS-regular ambientと中心正則三次商。相対PBW、相対/絶対Calabi–Yau、形式的中心元と次数3の代数化が主要依存。全係数上の一様相対量子化やqgrのsmoothnessは未証明。
5. 非楕円Poisson成分（ne:main）：固定した二つの滑らかなcubic fivefoldのPoisson schemeで2次元成分を示す。35列の線形化Jacobi行列がrank33という整数証明書に依存する。今回全行列を再実行したわけではない。全cubicを動かすrelative成分性を主張しない。
6. Hesse中心元（thm:explicit-hesse-center）：既知Sklyanin公式のPoissonパラメータへの翻訳。基本中心公式の新規性は主張しない。

## 正則三次超曲面のambientの周期性（論文Aに統合）

- **証明済み（仮定付き）**：標準型 (1,5,10,10,5,1) の5次元Koszul AS正則Z代数が、次数3の左右正則な正規族を持つとき、ambientは1周期的。より一般に次元・AS parameter N の対象に次数dの正則正規族があれば、最小周期は gcd(N,d) を割る。**本文の証明**：`papers/support/papers/sections/ambient_periodicity.tex`（定理 `thm:pg-ambient-gcd`、系 `cor:pg-cubic-ambient-periodic`、正規性判定命題 `prop:pg-cubic-normal-criterion`）。主論文入力は `papers/paper_a.tex`。正規族の消去が d 周期、局所Frobenius/Koszul双対性が N 周期を与える。N=5,d=3 なら 2×3−5=1。
- **論文Aとの接続**：定理 `thm:pg-quantization` の量子化は最初からgraded ambientと中心三次元を構成するため、その族の1周期性は自明。新しい帰結は、最初からgradedと仮定せず正則正規三次超曲面を持つZ代数ambientへ拡張する点。非1周期的な一般AS正則Z代数と矛盾しない。
- **未証明**：この構成による任意の1周期同型が三次商イデアルを保つこと、商の同時1周期化、中心化・CY化、任意の抽象的nc cubicの超曲面表示の存在は主張しない。既知の一般論からの系で、結論自体の新規性は未確認。
- **文献**：Bondal--Polishchuk, *Homological properties of associative algebras: the method of helices*, Russian Acad. Sci. Izv. Math. 42 (1994), 219--260, Proposition 4.1 と §5, DOI 10.1070/IM1994v042n02ABEH001536。Chan--Nyman, *Noncommutative linear systems and noncommutative elliptic curves*, arXiv:2211.12465, Definition 8.6。引用キーは `PBondalPolishchukHelices`、`PChanNymanNormalFamily`。
- **検証状態**：数学的証明を論文Aに書き、今回一次資料の文献情報と定義を照合。本文の全独立監査、形式検証、外部査読、論文A全体の組版とは区別する。既存の論文A公表準備優先順位は維持。

## 普遍的・厳密な代数的中心三次公式（主結果）

現在有効な主張・公式・再現手順は `notes/universal_casimir.md` に整理した。
公表用証明は`papers/support/papers/sections/hesse_mixed_universal_center.tex`、
`fermat_mixed_universal_center.tex`、`universal_casimir_determinant.tex`。

- **一般Hesse型の全混合（無条件・厳密）：**
  任意のtと独立な中心係数A,B,C,D,E,Hに対し
  f=(x³+y³+z³)/3+txyz+Axy+Byz+Czx+Dx+Ey+Hz+G の
  Jacobian量子化は、h²の高々二次の短い係数多項式で表せる
  厳密な中心三次元を持つ（thm:pg-universal-hesse-mixed）。
  Q(h,t)上で自由語339列、全関係倍数162行の階数144、三交換子剰余0を
  独立変数のまま厳密に計算確認。h=0で階数144なので原点を含む開集合上でも成立する。
  これは値の補間で得た候補ではなく、**普遍恒等式の全係数計算証明**による主張。
  再現コード：`computations/verify_universal_hesse_mixed_center.py`。
- **Hessianによる簡潔な式：**
  `cor:pg-hesse-hessian-form` に
  sym(F-h² det Hess_x F/12 +h² ABC/6+h⁴ Ψ_t(F))
  を示し、具体的な Ψ_t を本文に明示した。
  h²のHessian補正は既存の普遍二次ジェットと整合し、
  **h⁴補正込みで全次数で中心**となる。
- **任意のsmooth ternary g（無条件・明示）：**
  対角二次混合は中心平行移動で消去でき、平面三次曲線の
  Hesse標準形（Artebani–Dolgachev Lemma 1）とGL3のJacobian括弧の
  変換則から、全ての滑らかなg=f(x,y,z,0)へ有限公式を適用できる。
  `cor:pg-smooth-ternary-explicit`、`cor:pg-smooth-block-algebraic-quant`。
  この滑らかな部分では形式的中心元存在を入力とせず代数的量子化できる。
- **Cramer決定式も無条件化：**
  古典次数三Casimir核=CF+C[u]_3 の補題と、上の明示代数中心元から
  `thm:pg-universal-determinant` を無条件に証明。
  中心変数m=2で30×30、Fermat基準点det4608等の古典検算は従来どおり。
- **残るギャップ：**
  三変数制限が節点・尖点・零など一般に特異の場合の短い包括公式は未解決。
  それらを含む定理`thm:pg-quantization`の形式中心存在補題
  `lem:pg-formal-center`の相対formalityと完備絶対CYの独立監査は
  引き続き必要。Hesse座標の選択なしの単一GL3同変低次数式も未構成。
  今回の式の先行研究上の完全な新規性は未確認。

## 全般的Hessianジェット・形式存在補題の残る役割

- **反自己同型による偶数次正規化**（lem:pg-center-parity）：語の反転とh→-hで中心元を平均すると、Weyl表示はhの偶数次だけを含む。これは形式的中心元を仮定したときの正規化だが、smooth ternary gでは一般Hesse明示式が独立に存在を保証する。
- **任意の三変数以下三次式の二次ジェット**（prop:pg-universal-casimir-jet）：20独立係数の有界非可換語の厳密恒等式によりsym(f-h² det Hess_x f/12)はmod h⁵で中心。これ自体は特異ブロックを含む全次数中心公式ではない。再現コードは computations/verify_cubic_casimir_jet.py。
- **特異ブロックの形式的中心元**（lem:pg-formal-center）：既存原稿はrelative PBWと完成絶対Calabi–Yau分解からDolgushevを適用し、中心元を構成する。Etingof–Ginzburg Prop.8.1.1(i)、Mori–Smith Thm.1.4, Cor.2.9、Berger–Taillefer Thm.1.1(i)、Dolgushev Thm.3/Prop.1の原資料を以前点検済みだが、相対形式変形・完備双加群の全仮定を通した完全独立監査は未完成。
- **一般Hesseの新公式との関係**：thm:pg-universal-hesse-mixed は形式存在補題に依存せず、Hessianの二次補正にh⁴の明示項を加えた厳密中心元を与える。したがってsmooth gの形式存在補題の独立監査は量子化の主結果の証明に不要となった。ただし一般特異gの全量子化定理ではその入力を引き続き必要とする。

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

1. `computations/verify_universal_hesse_mixed_center.py` の独立再実行と、339×162普遍恒等式の短い証明書・手計算式への整理。今回ローカルで等価なQ(h,t)計算を実行してrank144・三交換子余り0を確認したが、保存したスクリプトそのものの実行は未実施。
2. 特異三変数制限について、既存の節点型・尖点型の公式を体系化し、一般特異gへの拡張を検討。相対formality・absolute CYによる形式的中心元存在補題も必要な範囲で監査する。
3. `prop:pg-represent`、`lem:pg-linearize`、`lem:pg-quadratic-lie`、`thm:pg-bondal`の独立再検証と先行研究の一次資料比較。
4. 論文A全体のLuaLaTeX組版・PDF目視、整数行列証明書、引用・ラベル整合性の再検査を経て投稿可否を判定する。投稿可能とはまだ断定しない。

GitHub mainが正本。Libraryは実際のpush失敗時だけ緊急退避。
