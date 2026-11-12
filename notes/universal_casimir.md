# 一般次元の普遍Jacobian量子化と中心三次元：現行研究ノート

**2026-11-12 / v5。再開時はまず 00_research_plan.md を読む。**
公表用原稿は `papers/paper_a.tex`、中心三次元の詳細証明は
`papers/support/papers/sections/hesse_mixed_universal_center.tex`、
`papers/support/papers/sections/fermat_mixed_universal_center.tex`、
`papers/support/papers/sections/universal_casimir_determinant.tex`。
本ノートは証明全文を重複させず、現行の確実性、計算再現、残る核心を整理する。

## 任意次元への拡張：主定理と再開点

**数学的主張（証明原稿を新規作成・検査）**：
任意の n≥3、N=n+2=3k+m、k≥1、m≥0について、
滑らかな三次超曲面 F=Σ_{s=1}^k f_s(x_s,u) と
各純active制限 g_s=f_s(x_s,0) が滑らかな平面三次であると仮定する。
各Jacobian Poisson bivector q_s=ι_{d f_s}P_s は
Schouten可換であり、π_λ=Σ λ_s q_s|_X は k次元線形族、
一般階数は2#{s:λ_s≠0}。
独立な量子化パラメータ η_1,...,η_k を各ブロックの関係式に置き、
他ブロックのactive生成元を相互可換、中心変数uを共有とする。
一般Hesse公式から中心三次元 Ω_s(η_s) を構成すると
[
  oxed{Omega_{oldsymboleta}=sum_{s=1}^k Omega_{s,eta_s}}
]
が厳密に中心で、Ω_0=F。異なるη_s,η_tを同時に含む補正は不要。
原点を含むZariski開 U⊂A^k_η 上で、各fiberのambientは
Koszul AS-regular（gldim N、AS parameter N、Hilbert (1-z)^(-N)）、
Ωは左右正則、中心商はAS-Gorenstein
（injdim N-1、AS parameter N-3=n-1、
Hilbert (1-z³)/(1-z)^N）。
各内部次数成分はU上局所自由。
**全Poisson線形族の同時量子化**は
(λ,h)↦(hλ_1,...,hλ_k) による逆像の開集合
（λ空間×h=0の全零切断を含む）上で成立する。
固定したFだけでなく、Hesse純三次と全中心混合係数も変数にした
正規形の表示パラメータ空間上にも相対的な多項式中心元を構成する。
これは全非可換cubicモジュライの量子化ではない。

**証明と参照**：論文A
`papers/support/papers/sections/general_dimension_universal_quantization.tex`。
主定理 `thm:pg-all-dimensions`、Poisson互換性
`prop:pg-ad-compatible`、線形族の零切断
`cor:pg-ad-whole-pencil`、係数変動
`prop:pg-ad-relative-chart`、一般次元Hessian和
`cor:pg-ad-hessian`。
証明は三変数中心式のテンソル積、異なるactive微分が他の係数を
微分しないこと、共通C[u]上のPBW自由性、単一activeブロック次数での
最高記号の非零因子性、中央正則列とKoszul/Künneth、有限rankの
平坦性を使用する。完全に新しい一般次元の多変数定理として整理したが、
既知の単一ブロック結果からの形式的な帰結も含むので
独立した数学的新規性・文献網羅調査は未完了。
特に正規形定理 `thm:pg-normal` の証明全体の独立再監査は未完了。

**計算の状態と再現**：
`computations/verify_general_dimension_multiblock.py` を局所実行し、
(k,m)=(1,2),(2,0),(2,2),(3,0),(3,3),(4,0)
すなわち n=3,4,6,7,10 の滑らかな三次式（中心平行移動で
Hesse直和に戻る）に対して、610個のJacobiator、
52個のF-Casimir成分、全ブロック間Hessian交差成分、内在的Hessian縮約を
独立記号 λ_s のまま厳密に確認した。
この有限な実行は任意次元定理の証明ではなく、符号・混合変数の検算。
`computations/build_general_dimension_center.py` を局所実行し、
n=6、k=2、m=2、共有中心u,v、独立η_1,η_2の
明示中心候補のWeyl symbolを構成。
Ω_0=F、異なるηの混合補正がないことを厳密に確認した。
このコードは公式の構成・代入を確認するもので、
自由語の全交換子についての独立再計算ではない。
全次元中心性の証明は論文のテンソル積論法と
三変数の普遍Hesse恒等式に依存する。
GitHubへ保存したコードそのものを接続先で再実行したとは主張しない。

**適用範囲**：
各kの固定した正規形表示の中で、滑らかなFと全g_s滑らかは
非空Zariski開条件。F=Σ_{s,i}x_{si}³+Σ_alpha u_alpha³が例。
よって一般次元・各許容Poisson一般rank2kの非空な表示開部分を扱う。
高次元Poisson成分全体または全Poissonモジュライの相対量子化は
無条件に主張しない。g_sが特異な場合の問題は
現在の最優先から外し、既存の有効結果を保持する。

**次の研究目標**：
(A) 各kでの正規形表示空間からPoisson pair moduliへの写像と
この多変数量子化の降下・同型による同定を調べる
（Hesse正規化の非一意性・中心三次式の規格化の差に注意）。
(B) 全nでのAS-regular ambientと中心商の
相対noetherian性/滑らかさの必要条件を調べる。ただし
qgrのsmoothnessを現定理の帰結とはしない。
(C) 論文AのPoisson正規形とBondal主張の独立監査、
普遍Hesse計算証明書の査読しやすい短縮、
一次文献の網羅比較とLuaLaTeX全体組版を行う。
特異制限の短い公式の追求は当面の優先課題ではない。

## 内在的な任意次元Hessian補正

**証明を追加（論文A prop:pg-ad-intrinsic-hessian）：**
任意次元 N のV、定数三重ベクトルP∈Λ³V、斉次三次式Fについて
\[
 \mathscr H(P,F)=\frac16\sum_{i,j,k,a,b,c}
 P^{ijk}P^{abc}\,F_{ia}F_{jb}F_{kc}\in\operatorname{Sym}^3V^*
\]
を定義する。これは座標不変なHessianと三重ベクトルの縮約であり、
正規形 P=Σ_sλ_sP_s、F=Σ_s f_s(x_s,u) では
\[
 \mathscr H(P,F)=\sum_s\lambda_s^2
 \det\operatorname{Hess}_{x_s}(f_s)
\]
となる。交叉項は異なるactiveブロック間のHessianが零なので消える。
smooth ternary g_s の範囲では、純中心三次の調整を行って
\[
 \widetilde\Omega_{P,h}
 =\operatorname{sym}\left(
 F-\frac{h^2}{12}\mathscr H(P,F)+h^4K_{P,F}\right)
\]
という**全次数で厳密な中心元**を取れる。
二次補正はブロック座標に依存せず、
四次補正Kは選択したHesse座標におけるΣ_sλ_s⁴Ψ_{t_s}(f_s)
の変換で明示可能。四次項まで座標に依存しない唯一の式が
得られたという主張ではない。
この定理は一般次元の主結果であり、特殊な一変数例の
計算的観察とは区別する。

**検算**：
`computations/verify_general_dimension_multiblock.py` に
六指数のHessian縮約とブロックHessian行列式の和との
厳密な照合を追加した。
(k,m)=(1,2),(2,0),(2,2),(3,0),(3,3),(4,0)
の6例について、独立パラメータλ_sと共有中心を保持したまま
同一式をSymPyで再計算し全件PASS。
これは任意次元の証明を数値試験で置き換えたものではない。
一般証明は論文Aのテンソル恒等式と全Hesse中心公式にある。

## 1. 解決した核心：全Hesse型・全中心混合の短い普遍多項式

**証明済み（記号計算証明書付き）**：標数0可換次数付き中心係数環 R で
A,B,C∈R_1、D,E,H∈R_2、G∈R_3、t∈C任意について
F=g_t+Axy+Byz+Czx+Dx+Ey+Hz+G、
g_t=(x³+y³+z³)/3+txyz とおく。
Jacobian交換子 [x,y]=h sym(F_z) 等の量子代数では、
以下の略記（Tは6語の平均）で厳密な中心元が得られる：
\[
S=x³+y³+z³,\quad T=\operatorname{sym}(xyz),\quad
Q=A\operatorname{sym}(xy)+B\operatorname{sym}(yz)+C\operatorname{sym}(zx),
\quad Z_2=Az²+Bx²+Cy²,
\]
\[
 L=Dx+Ey+Hz,\quad R_2=B²x+C²y+A²z,\quad R_{11}=ACx+ABy+BCz.
\]
q=h²に対し
\[
\begin{aligned}
 U&=1+qt²/2+q²t/6-q²t^4/48,&
 W&=(4-qt²)(12t+q(t³-8))/48,\\
 c&=(4-qt²)(12+qt²)/48,&
 d&=q(12t+q(2-t³))/36,\\
 e&=1+q²t(8-t³)/144,&
 f&=q(4-qt²)/24,\\
 g&=-q(12t+q(t³+4))/72.
\end{aligned}
\]
\[
 \boxed{\Omega=US/3+WT+cQ+dZ_2+eL+fR_2+gR_{11}+G.}
\]
Omega_0=F、原点h=0を含む適切な開集合で **全次数で厳密に中心**。
**形式的中心存在補題 lem:pg-formal-center に依存しない。**
定理ラベル thm:pg-universal-hesse-mixed。

### 証明・検算の正確な意味

独立中心係数A,B,C,D,E,H（重み1,1,1,2,2,2）とh,tを
**不定元のまま保持**する自由語の全次数4のベクトル空間は339次元。
全二次関係式の左右からの次数2倍数162個の張る空間は、
Q(h,t)上でrank 144。各 [Omega,x], [Omega,y], [Omega,z] はその空間へ属する。
h=0では可換多項式環の同次数部分が195次元なので同じrank144。
したがってh=0直線を含む近傍で次数4商は局所自由・h-flatとなり、
分数体上の恒等式が原点を含む開上へ降下する。
**今回独立Python実行で Q(h,t) 上のrank144と3交換子剰余0を確認。**
保存コード `computations/verify_universal_hesse_mixed_center.py` は
全自由語と行を再生成する（必要ライブラリ SymPy）。
保存後のGitHub実行環境でコードそのものを走らせたわけではない。
有限有理標本から得た候補係数の補間は探索方法であり、
**最終証明は全不定元を持つ普遍恒等式の検証**である。
また独立したSymPy計算でHessianによるコンパクト式の差が恒等的に0と確認済み。

## 2. コンパクトなHessian公式

Fのactive Hessianの行列式をH_Fとすると、
\[
 \Omega=\operatorname{sym}\bigl(F-qH_F/12+qABC/6+q²\Psi_t(F)\bigr)
\]
と等価である。ただし
\[
\begin{aligned}
 \Psi_t(F)={}&t(8-t³)g_t/48-t^4Q/48
 +(2-t³)Z_2/36\\
 &+t(8-t³)L/144-t²R_2/24
 -(t³+4)R_{11}/72.
\end{aligned}
\]
これは前回の一般的二次ジェット
sym(F-h²det Hess(F)/12) が mod h⁵ 中心となることを含み、
**h⁴補正までで中心性が全次数で成立する**という強い結果。
純中心補正qABC/6は規格化の自由度である。
論文A cor:pg-hesse-hessian-form を参照。

## 3. 任意の混合項・任意の滑らかな三変数三次式

Fに対角二次混合
\(\ell_x x²+\ell_y y²+\ell_z z²\) があっても
\(X=x+\ell_x,Y=y+\ell_y,Z=z+\ell_z\) の中心平行移動で消去できる。
このとき
\[
 A'=A-t\ell_z,\quad B'=B-t\ell_x,\quad C'=C-t\ell_y,
\]
\[
\begin{aligned}
 D'&=D-\ell_x²-A\ell_y-C\ell_z+t\ell_y\ell_z,\\
 E'&=E-\ell_y²-A\ell_x-B\ell_z+t\ell_x\ell_z,\\
 H'&=H-\ell_z²-B\ell_y-C\ell_x+t\ell_x\ell_y
\end{aligned}
\]
とし、純中心三次G'も論文A式 (HT) で変換する。
これで **中心変数の任意の個数・全混合次数**を扱える。
論文A cor:pg-universal-hesse-all-mixed。

さらに任意の滑らかな平面三次
g=F(x,y,z,0) は、あるM∈GL3(C)、λ≠0、
t³≠-1によりg(x)=λg_t(Mx) と書ける
（Artebani–Dolgachev, *The Hesse pencil of plane cubic curves*,
Enseign. Math. 55 (2009), Lemma 1, DOI 10.4171/LEM/55-3-3）。
\(F'(X,u)=λ^{-1}F(M^{-1}X,u)\)、\(h'=λ\det(M)h\)とすれば
\[
 \boxed{\Omega_{F,h}(x,u)=λ\Omega_{F',h'}(Mx,u)}
\]
が明示的な厳密中心元。これにより **任意の滑らかな三変数制限**
に形式中心存在補題なしで中心元を構成できる
（cor:pg-smooth-ternary-explicit）。
滑らかな全ブロックの量子化では、PBW正則性と既存の
中心正則性の証明を組み合わせ、
形式的なKontsevich–Dolgushev中心元議論を使わず
AS-regular ambient / AS-Gorenstein商を構成できる
（cor:pg-smooth-block-algebraic-quant）。

Hesse標準形とMの選択は一般にはFの係数の単一有理関数として
正準的には定まらない。これは**座標選択後の普遍多項式公式**であり、
元の座標で単一のGL3同変な低次数不変式を与えたとは言わない。

## 4. 同時に無条件になったCramer決定式

滑らかなgで古典次数3 Casimirは厳密に C F ⊕ C[u]_3
（論文A lem:pg-det-classical-kernel、形式中心に依存しない）。
Hesse明示中心元の存在から量子次数3の中心が
最低その次元あると分かり、r×r小行列の逆から
**元の座標で**普遍Cramer式を導ける
（thm:pg-universal-determinant）。
以前必要とされた形式的中心元の存在という仮定は**不要**になった。
中心変数m=0ではr=9、m=2ではr=30。
Fermat基準点の小行列式はm=0で-72、
m=2で4608（`computations/verify_universal_casimir_minor.py` により
有理数計算で確認済み）。
これは決定式表示であり短い座標不変式ではない。

## 5. 先行成果との関係・今後の核心

- Fermat型の短い式は論文C関連の
  `papers/support/papers/sections/mixed_center_picard.tex` に既に存在した。
  全係数不定元による厳密中心性を証明したのは
  `papers/support/papers/sections/fermat_mixed_universal_center.tex`；
  現在は一般Hesse型の定理のt=0特殊化となる。
- 混合を除くHesse型Sklyanin中心元は既知の結果に依存し、
  `papers/support/papers/sections/explicit_hesse_center.tex` に
  Poisson規約の式がある。新しい定理は**全中心混合項**への拡張と
  独立な普遍恒等式による検証に価値がある。完全な先行研究調査・
  数学的新規性の確定は未実施。
- **未解決：** 節点型・尖点型・零の三変数制限など
  全ての特異gを単一の短い普遍式で覆うこと。
  既存の二つの特異ブロックの閉式は
  `papers/support/papers/sections/nonelliptic_quantization.tex`。
  全Poisson構造の代数的量子化 thm:pg-quantization の
  **特異ブロック部分**には、なお形式的中心元存在
  lem:pg-formal-center とその相対formality/絶対CYの
  独立監査が必要。
- **次の優先：** Hesse中心公式の普遍証明書を独立再実行し、
  投稿用に短い手計算恒等式証明を整理する。
  次に一般次元の正規形表示上の相対構成とそのモジュライへの降下を優先し、
  特異制限の短い式は保留する。
  論文Aの正規形・Bondal主張の全監査とLuaLaTeX全体組版も残る。

GitHub mainが正本。PDFはgit追跡せずlatexmkで生成。
Libraryへの保存はGitHub main反映失敗時に限る。
