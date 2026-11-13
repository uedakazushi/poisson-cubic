# 一般次元の可換復元：証明の再開案内

2026-11-14 / B-v59。最初に `../00_research_plan.md` を読む。入口は `papers/paper_b.tex`、証明は `papers/generic_recovery/`。監査範囲・文献比較・有効な障害は `paper_b_proof_audit.md`、実行状態は `../validation_paper_b.json` にまとめる。

## 主定理の範囲

n>=3、N=n+2、R=C[h]_(h)。各次数が有限自由の中央代数A_Rについて、特殊ファイバーが多項式環となり、中心三次元Omega_Rの剰余Fが滑らかな射影三次超曲面を定める場合を扱う。可換模型の方程式はK=C(h)上に取れる。rotation・中心元由来の三次周期比較を保つ全coherent残余圏同値は、ある有限拡大上に構成する。

模型の幾何学的射影同型類はrotation付きpairから一意である。K上のformの一意性は従わない（`gcd:ex:forms`）。全coherent導来圏のsmooth proper性と有限線束生成を得るが、非可換射影化全体と可換cubic全体の導来同値を主張しているわけではない。

固定した勾配空間Qの積分については、有限étale symmetrizer代数E_Fが曖昧さを記述する。`gcd:prop:integrability-symmetrizer` によりdim L_Qは最細の幾何学的Sebastiani--Thomブロック数であり、幾何学的に分解不能なら方程式はK上スカラー倍まで一意。これはHwangの理論を基礎体上に書き直した基本的帰結である。

## 証明の依存関係

| 段階 | 現行ソース・主要ラベル | 必要な内容 |
| --- | --- | --- |
| 局所代数 | `local_model.tex`, `lp:thm:main` | 次数別有限性、Koszul分解の持上げ、中心正則性、線束Hom |
| 三対象window | `window.tex`, `tw:thm:window` | 実際のdg section--window、有限長filtration、stabilizationとrotation。`tw:eq:comparison-diagram` と指定周期の二拡張・正方形を参照 |
| 完備MF比較 | `curved_transport.tex`, `cft:thm:complete` | 通常formality、中心逆像、定数trivector、arity 1/3のflowと有限rank上の収束 |
| 一般点 | `generic_descent.tex`, `rog:thm:geometric-generic` | 固定三対象を先に局所化、Eulerベクトルの非零性、BFK、有限降下 |
| 全coherentへの拡張 | `coherent_saturation.tex`, `crs:thm:coherent` | smooth対角、pseudo-perfect加群、全twistによる検出 |
| 方程式の降下 | `gradient_recovery.tex`, `field_model.tex`, `gcd:thm:field-model` | Sym^2 V上の積の核Q、線形可積分性、Euler積分 |

全coherentのsmoothnessを前提に置かず、可換模型の存在から残余のsmoothnessを得て、飽和を適用する。低次数積の可積分性だけで圏同値の存在を結論せず、幾何学的模型の存在を先に確立する。

## 非可換Hesse入力の二次jetと全次数の有理模型

`explicit_example.tex` は [y,z]=h x²+(h²/2)(yz+zy) と巡回置換を持つD_Rへ中心変数u,vを加えた族を扱う。`gre:prop:input` は既知Sklyanin中心元を規格化し、一般・特殊ファイバーのHilbert級数とDVR構造定理から全次数の有限自由性を証明する。

`gre:prop:jet` は生成元を固定するharmonic-angle比較を用い、W_rec=F+h xyz+(h²/3)xyz+O(h³) を導く。F=(x³+y³+z³+u³+v³)/3である。Weyl表示の係数−2/3に、比較作用素ρ₂=(yz∂x²+zx∂y²+xy∂z²)/6によるρ₂F=xyzが加わる。中心接写像の二次項はShoikhetのinner二輪消滅によって零。xyzはJac(F)_3で非零である。

`gre:prop:hesse-normalform` は、Hesse対称群に同変な比較とactive変数の規格化によって W_H=F+λ(h)xyz を与える。底のhと周期tを固定する。`gre:prop:marked-hesse-uniqueness` は恒等を剰余とする線形座標変換・単元倍に関するλの一意性を証明する。

さらに、全次数で

`λ(h)=(h+h²/3+h⁵/12)/(1−h⁴/4)`

が成り立つ。証明の依存は、正規化中心商 D_R/(Ω_D) の相対THCR表示 → 三変数a=0のdg Orlov・MF比較 → 完備MF同値とPerf曲線の分数体への底変更 → 有理点を持つ楕円曲線の導来同値からの同型 → j不変量の形式分枝の一意性、である。特殊ファイバーがP²となる元の点スキームと、一般点の点曲線の平坦閉包E_Rを区別する。商にはG=−9hΩ_DではなくΩ_Dを使う。

従ってK上の可換三次三様体は

`(4−h⁴)(x³+y³+z³+u³+v³)+(12h+4h²+h⁵)xyz=0`

と明示できる。元の五変数の完備MF比較から、この固定K模型へのrotation・指定周期付き同値を `rog:lem:descent` により有限拡大へ降ろす。楕円曲線の同型だけから五変数のperiod比較を結論するのではない。

`verify_recovery_example.py` は必要な中心式・有限jet・Weierstrass変換・c₄、Δ、j・有理係数・五変数式の恒等式を厳密検算する。全次数の自由性、THCR、Orlov同値、全次数のλの同定は本文の証明による。

## 次の計算への入口

明示方程式が得られたため、次は実際の非可換入力でrotation核Pと対角Deltaの有限表示を作り、V、U、積を取り出す。三対象stabilizationの有限Homへ戻り、shiftを表す双加群と導来自然変換の複体を具体化する。Qの基底q_aに対し、行列Aの線形条件

`sum_a A_ia partial_j q_a = sum_a A_ja partial_i q_a`

を解き、可逆解から `G=(1/3)sum_(i,a) x_i A_ia q_a` を作る。既存の `verify_generic_cubic_descent.py` は既知の可換勾配空間からこの線形代数を検算するコードであり、非可換のV,U,積を算出するコードではない。今回の楕円比較による方程式同定とも方法が異なる。

同コードは3例の積分に加え、F=x0³+3t x0 x1²+x2³+x3³+x4³の非分裂代数 E_F=Q(t)[u]/(u²−t)×Q(t)³ とF^a(bx)=F^(ab³)(x)を検算する。本文の証明は計算結果に依存しない。同値核の具体行列、必要な有限拡大の次数、Kへの核の降下は未解決である。

## 担当境界

三次三様体の接空間20→10、Plücker障害、相対Artin/étale理論、多ブロック・明示混合族の一般論・point schemeは独立成果であり、主定理の入力に用いない。現行の所在は `paper_b_scope_and_transfer.md`。必要証明は本稿内に置き、独立成果の全文を再導入しない。
