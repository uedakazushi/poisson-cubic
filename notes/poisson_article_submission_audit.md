# 論文Aの投稿準備：現行の監査と再開点

**2026-11-12 / A-v38。** 最初に 00_research_plan.md を読む。
論文本文は papers/paper_a.tex、専用文献は papers/support/papers/references_poisson_cubic.tex。
本ノートは現在有効な知識・依存・課題を整理し、証明全文を重複させない。

## 主張の確実性と所在

1. Poisson正規形（thm:pg-normal、papers/support/papers/sections/poisson_geometry.tex）：全非零構造の三変数Jacobianブロック分解。n>=3、X smooth。証明は記載済みだが、核心のLie代数補題 lem:pg-quadratic-lie を含め、今回の全面的独立監査は未完了。
2. Bondal予想（thm:pg-bondal、papers/support/papers/sections/bondal_cubic.tex）：全 2j<n について dim D_{2j}>=2j+1。j<k で j+1 個のブロック上の平面曲線joinを構成し、Euler線の射影化でrankが2低下する。正規形定理に依存。scheme-theoretic primary分解を与える主張ではない。高次元での新規性調査は未完。
3. 退化スキーム（prop:pg-deg-ideal）：任意の正規形に適用できる。critical cover と零点の完全交叉（lem:pg-critical-cover、prop:pg-zero-ci）には各 f_s(x_s,0) が滑らかな平面三次という追加仮定が必要。
4. 量子化（thm:pg-quantization）：個々のPoisson構造に対する原点を含む一変数Zariski開上のAS-regular ambientと中心正則三次商。相対PBW、相対/絶対Calabi–Yau、形式的中心元と次数3の代数化が主要依存。全係数上の一様相対量子化やqgrのsmoothnessは未証明。
5. 非楕円Poisson成分（ne:main）：固定した二つの滑らかなcubic fivefoldのPoisson schemeで2次元成分を示す。35列の線形化Jacobi行列がrank33という整数証明書に依存する。今回全行列を再実行したわけではない。全cubicを動かすrelative成分性を主張しない。
6. Hesse中心元（thm:explicit-hesse-center）：既知Sklyanin公式のPoissonパラメータへの翻訳。基本中心公式の新規性は主張しない。

## 三次中心元：検証した新しい有効結果

- **反自己同型による偶数次正規化**（補題 lem:pg-center-parity、本文 papers/support/papers/sections/poisson_geometry.tex）：Jacobian量子化の関係式は、語の反転と h→-h による反自己同型で符号が逆転する。中心元をこの反自己同型で平均し、Weyl対称化で表せば、任意の既存の中心三次元を法hでの剰余を変えずにhの偶数次係数だけの形へ規格化できる。これは**中心元の存在を仮定した結論**であり、その存在自体には lem:pg-formal-center が必要。
- **普遍Hessian二次補正**（命題 prop:pg-universal-casimir-jet）：active三変数に関して次数3以下の任意の f （係数は任意の可換中心環）について、
  \[
  \Theta_f=\operatorname{sym}\left(f-\frac{h^2}{12}\det\operatorname{Hess}_{x,y,z}f\right)
  \]
  はJacobain交換子の代数で3生成元と **mod h^4** で可換。証明は20個の独立係数 a_{ijk}（i+j+k≤3）の多項式を自由語の隣接転置規則で有界h次数に還元し、全係数がQ[a]で恒等的に零となる厳密記号計算に基づく。計算では20係数を特殊化していない。反自己同型とh-torsion-free PBW性から、**mod h^5** の中心性が従う。これは実際の厳密な有限証明書を持つ低次結果であり、全次数の中心元をこの式で与えるとは主張しない。
- **二次係数の必要条件**：偶数次正規化した形式的中心元 sym(f+h² f₂+...) については f₂ + (det Hess f)/12 が古典Jacobian括弧のCasimirである。したがって二次補正は、Casimirの不定性を除いてHessian式により決定する。所定の二次係数が全高次で実現されるという主張とは区別する。
- **検証コード**：computations/verify_cubic_casimir_jet.py（SymPy）。別個の実行環境で同じ20係数普遍式の3生成元に対する零恒等式を確認し、さらにHesse明示中心公式のh²係数と一致することを検算した。GitHubに登録したスクリプトそのもののクローン環境での再実行は未確認。
- **先行研究**：Berger–Taillefer, *PBW deformations of Calabi–Yau algebras*, J. Noncommut. Geom. 1 (2007), p.242 Theorem 1.1(i), p.246以降 Theorem 3.1、Theorem 3.6を原PDFで確認。正規ポテンシャルに低次ポテンシャルを加えるPBW変形と3-CYを与え、AのPBW性の**各u特殊化**には適用できる。全係数環上の自由性は別途確認する必要がある。
- Etingof–Ginzburg, *Noncommutative del Pezzo surfaces and Calabi-Yau algebras*, arXiv:0709.3593v4、PDF pp.29–30, Proposition 8.1.1(i)とその証明を原PDFページ画像で確認。同命題の証明自身が R=C[u] 上の相対微分・formality・CYから中心元を作り、中心元の存在に **isolated singularity仮定を課さない**。複数中心変数のR=C[u_1,...,u_m]への適用は原文にそのまま書かれた定理ではないため、論文Aの相対完備双加群論証がなお重要。

**相対/絶対Kontsevichの接続で検証した点：** 論文Aの lem:pg-formal-center の証明に、相対C[u]-線型多微分作用素が絶対多微分作用素へ埋め込まれ、Gerstenhaber括弧・Hochschild微分を保つことを明記した。相対Poisson tensor Π に ∂u 成分がないため、Kontsevichグラフ公式は絶対空間上でもu微分を使わず、相対星積が絶対Πの星積と一致する。よってDolgushevのTheorem 3を適用する絶対classの代表はΠである。またunimodularityで得たρの次数零成分はh進単元であり、C*重みから標準体積形式そのものが不変であることを詳述した。これは原稿内の論理接続を明確化した段階で、必要な完備CY双加群分解とrelative formality準同型の全ての関数解析・代数幾何条件を独立に再証明したという意味ではない。

**投稿のための残課題：** universal finite h-jetの計算証明書は論文中の還元規則を読めば再実行できるが、査読で計算なしの短い恒等式証明が必要と判断される場合は導出を補う。主定理 thm:pg-quantization 全次数の中心元については、絶対CY双加群分解・相対Kontsevich対応・Dolgushevの全適用条件の逐語監査が未完成。低次の証明を中心元の存在証明と混同しない。

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

2026-11-12の静的検査では、論文A入力閉包の20 bibliography keys、49 citation uses、119 labelsに、未解決引用・重複bibitem・未解決ref・重複labelがなかった。
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

1. prop:pg-represent、lem:pg-linearize、lem:pg-quadratic-lie の証明の独立再検証。Etingofの主要一次資料は確認済みなので、Jacobi線形化・Bertini・Lie構成の接続を重点監査する。
2. lem:pg-formal-center と prop:pg-PBW の相対formality、完備双加群分解、絶対CY、代数化の妥当性を徹底検査する。中心元の偶性と普遍Hessian二次補正は検証済みだが、全次数の存在証明の代わりにはならない。
3. 論文A全体のlatexmk組版・視覚確認、整数証明書の再実行、網羅的文献比較。主張の仮定と証明の所在を確認して投稿判定する。
4. 数学的まとまりを保ちつつ非楕円量子化をAに収めるか独立論文へ分けるか再評価する。価値ある証明を削除しない。

GitHub mainを正本とし、Libraryは実際のGitHub反映失敗時に限り緊急退避。
