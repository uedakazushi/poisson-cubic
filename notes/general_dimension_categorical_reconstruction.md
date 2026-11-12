# 論文B：一般次元のrotation付き可換復元

**2026-11-12 / B-v42。** 再開は `00_research_plan.md`、続いて `notes/paper_b_proof_audit.md`。

主定理は `papers/support/papers/reconstruction/general_dimension_recovery.tex` の `gdr:thm:generic`。新しい `three_object_window.tex` の `tw:thm:window` が、次数別有限自由・滑らかな可換特殊ファイバー・中心三次元という代数的入力から(L)を構成する。一般点AS正則性も独立仮定ではない。

残る比較条件は `tw:def:CF3` の(CF_3)：完備底上のK,K(1),K(2)から可換側E,E(1),E(2)への実際のunital A∞比較。全Hom複体・高次積・内部shift・中心元由来の周期性を含む。全MF比較(CF)は十分条件として保持する。これらの曲率付き関手と逆関手の全独立監査は未完了。

条件の下で、K=C(h)上のsmooth cubic模型、有限拡大上の全coherent残余pair同値、全n>=3での幾何学的一意性、非零対象の三rotation和の生成段数2(n+2)(n+3)-1以下を得る。方程式と同値核の定義体を分ける。全射影化の導来同値、K上の模型の一意性、特殊点込み相対同値、全nc cubicの無条件復元は主張しない。

最短経路は三対象window→CF_3→Euler非零性→BFK→有限降下→coherent飽和→低Nat体拡大→K上の勾配積分。(D)は既知の混合λ=1の明示式を指定する別の入力。多変数正則局所基底の(L)も同じ証明で得るが、CF_3と接着は別課題。

既存の全MF・相対Artin・finite descent・coherent飽和・有限積分・point schemeの有効な証明は主原稿の支持節に保持する。詳細な証明状態・文献位置・反例は監査ノート、実際の計算・組版の状態は `validation_paper_b.json` を参照する。
