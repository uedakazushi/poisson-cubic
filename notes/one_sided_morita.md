# 片側compact核とgeneric復元への最短の残条件

**2026-11-11 / v34。最初に00_research_plan.mdを読む。GitHub mainが正本。**
証明全文：`papers/reconstruction/one_sided_morita_algebraization.tex`。単独入口：`papers/one_sided_morita_algebraization.tex`。

## 現在使える判定

可換Kuのsmooth proper生成代数C、nc残余のproper生成代数Gammaを使う。周囲の次数付き代数A、中心商Bとは別の記号。関手は **可換からncへ** 取る。

右Gamma-perfectな(C,Gamma)-双加群Pが特殊点でMorita同値を与えるなら、局所底上で同値となる。逆はQ=RHom_Gamma(P,Gamma)。CのsmoothnessによりQは右C-perfectで、単位・余単位のconeは底上perfect。特殊点で零なのでperfect Nakayamaが働く。Gammaのsmoothnessは結果であり事前仮定ではない。開基底では指定点の近傍で成立する。

rotationを保つために必要なのは一つの射 L_C tensor_C P -> P tensor_Gamma L_Gamma と、その特殊点での可逆性。逆射はperfect coneの判定から従う。HH^0(C/R)=Rを追加仮定すれば、三次周期性の差はscalar uであり、c^3 u=1のetale根で補正できる。任意の高次群作用のcoherence全部をこのscalar補正だけで済ませたとはしない。

## 形式から代数へ

RがNoether局所G-ringで、通常の導来双加群圏に完備底のP_hatが存在し、右Gamma_hat-perfectで、剰余同値とrotation射を持つとする。CのsmoothnessからP_hatは包絡代数上compact。PopescuでR_hatをsmooth有限表示R代数のfiltered colimitとし、perfect加群と射の有限表示性で一つの段階へ降ろす。その段階の指定有限jetを保つetale切断を取ると代数的P'を得る。特殊点の同値判定により近傍でMorita同値となる。

任意の指定有限jetは保てるが、元の形式分枝を全次数で再現するとは限らない。既約有限型C基底では、etale近傍の一般点から幾何学的一般点の同値が従う。

## この族で未証明の入力

既存全Artin同値の逆像として、可換側の一つの生成子Hを追跡する。必要なのはP_mの整合系だけでなく、**通常の導来圏の一つのP_hatとしての実現、左C_hat作用・rotationのcoherence、右Gamma_hat-perfect性**である。

有限rankの自由MF、底上perfectなHom、各Artin切断でのperfect性だけでは不足。Gamma=k[e]/e^2のkは底上perfectでもGamma-perfectでなく、Torが全次数に残る。旧生成子持上げの反例は保持し、ここで撤回しない。

次は逆functorのHへの作用を、Gamma_hatの有限個のshiftのconeとretractで表示する。一様な有限filtrationを示せば、逆核・単位・余単位・代数化は新定理へ任せられる。双方向を同時に未知量として解く必要はなくなった。一般KFには戻らない。

## 検証と先行研究

Toën–Vaquié *Moduli of objects in dg-categories*, Lemmas2.8,2.10（printed pp.404–407）、Stacks07GC,07M7,068Uを一次資料で確認した。一般原理の新規性は主張せず、具体的nc核は未構成。

`verify_one_sided_morita.py` は通常のねじった2×2行列代数で206個の多項式恒等式、balanced relation階数、周期補正mod h^8、compact性の反例を検算する。nc cubicのP_hatを計算したコードではない。
