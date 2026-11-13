# 一般次元の可換復元：証明の再開案内

2026-11-13 / B-v57。最初に `../00_research_plan.md` を読む。入口は `papers/paper_b.tex`、証明は `papers/generic_recovery/`。監査範囲・文献比較・有効な障害は `paper_b_proof_audit.md`、実行状態は `../validation_paper_b.json` にまとめる。

## 主定理の範囲

n>=3、N=n+2、R=C[h]_(h)。各次数が有限自由の中央代数A_Rについて、特殊ファイバーが多項式環となり、中心三次元Omega_Rの剰余Fが滑らかな射影三次超曲面を定める場合を扱う。可換模型の方程式はK=C(h)上に取れる。rotation・中心元由来の三次周期比較を保つ全coherent残余圏同値は、ある有限拡大上に構成する。

模型の幾何学的射影同型類はrotation付きpairから一意である。K上のformの一意性は従わない（`gcd:ex:forms`）。全coherent導来圏のsmooth proper性と有限線束生成を得るが、非可換射影化全体と可換cubic全体の導来同値を主張しているわけではない。

固定した勾配空間Qの積分については、有限étale symmetrizer代数E_Fが曖昧さを記述する。`gcd:prop:integrability-symmetrizer` によりdim L_Qは最細の幾何学的Sebastiani--Thomブロック数であり、幾何学的に分解不能なら方程式はK上スカラー倍まで一意。これはHwangの理論を基礎体上に書き直した基本的帰結である。

## 証明の依存関係

| 段階 | 現行ソース・主要ラベル | 必要な内容 |
| --- | --- | --- |
| 局所代数 | `local_model.tex`, `lp:thm:main` | 次数別有限性、Koszul分解の持上げ、中心正則性、線束Hom |
| 三対象window | `window.tex`, `tw:thm:window` | 実際のdg section--window、有限長filtration、stabilizationとrotation |
| 完備MF比較 | `curved_transport.tex`, `cft:thm:complete` | 通常formality、中心逆像、定数trivector、arity 1/3のflowと有限rank上の収束 |
| 一般点 | `generic_descent.tex`, `rog:thm:geometric-generic` | 固定三対象を先に局所化、Eulerベクトルの非零性、BFK、有限降下 |
| 全coherentへの拡張 | `coherent_saturation.tex`, `crs:thm:coherent` | smooth対角、pseudo-perfect加群、全twistによる検出 |
| 方程式の降下 | `gradient_recovery.tex`, `field_model.tex`, `gcd:thm:field-model` | Sym^2 V上の積の核Q、線形可積分性、Euler積分 |

全coherentのsmoothnessを前提に置かず、可換模型の存在から残余のsmoothnessを得て、飽和を適用する。低次数積の可積分性だけで圏同値の存在を結論せず、幾何学的模型の存在を先に確立する。

## 次の計算への入口

実際の非可換入力でrotation核Pと対角Deltaの有限表示を作り、V、U、積を取り出す。Qの基底q_aに対し、行列Aの線形条件

`sum_a A_ia partial_j q_a = sum_a A_ja partial_i q_a`

を解き、可逆解から `G=(1/3)sum_(i,a) x_i A_ia q_a` を作る。既存の `verify_generic_cubic_descent.py` は既知の可換勾配空間からこの線形代数を検算するコードであり、非可換のV,U,積を算出するコードではない。

同コードは3例の積分に加え、F=x0^3+3t x0 x1^2+x2^3+x3^3+x4^3の非分裂代数 E_F=Q(t)[u]/(u^2-t)×Q(t)^3 とF^a(bx)=F^(ab^3)(x)を検算する。本文の証明は計算結果に依存しない。

## 担当境界

三次三様体の接空間20→10、Plücker障害、相対Artin/étale理論、Sklyanin・多ブロック・明示混合族・point schemeは独立成果であり、主定理の入力に用いない。現行の所在は `paper_b_scope_and_transfer.md`。必要証明は本稿内に置き、独立成果の全文を再導入しない。
