# 普遍Jacobian量子中心三次元：現行研究ノート

**2026-11-12 / v3。再開時はまず 00_research_plan.md を読む。**
公表用原稿は `papers/paper_a.tex`、中心三次元の詳細証明は
`papers/support/papers/sections/hesse_mixed_universal_center.tex`、
`papers/support/papers/sections/fermat_mixed_universal_center.tex`、
`papers/support/papers/sections/universal_casimir_determinant.tex`。
本ノートは証明全文を重複させず、現行の確実性、計算再現、残る核心を整理する。

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
  次に特異ブロック全体へ閉式を広げる可能性と
  元座標でのGL3同変な式の存在を検討する。
  論文Aの正規形・Bondal主張の全監査とLuaLaTeX全体組版も残る。

GitHub mainが正本。PDFはgit追跡せずlatexmkで生成。
Libraryへの保存はGitHub main反映失敗時に限る。
