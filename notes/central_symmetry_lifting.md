# 中心三次変数と全Artin障害の消滅

**2026-11-11 / v32。再開時にはまず `00_research_plan.md`。**
証明全文：`papers/reconstruction/central_symmetry_lifting.tex`。以下は有効な結論、仮定と未解決の比較だけを記録する。

混合量子化では独立中心変数 `v` を三次式 `v^3` として加える。`Γ=μ3^(v)` が `v→ζv`、他の座標と量子パラメータ `h` は固定する。特殊可換五変数三次の `Nat^0(Id,(1))` は `〈x,y,z,u〉⊕〈v〉` で、前半は Γ 不変。一方、`Nat^1(Id,(1))=k²` は二つの非恒等 scalar-μ3 sectorで、normal determinant factorにより Γ 不変部分が0（BFK Theorem 5.39）。各sectorのcharacterの双対規約には依存せず非自明。

**条件付きの新定理。** `R` を任意の局所Artin k代数、ΓはRに自明に作用する。actual Natを計算する `C_{r,R}`（r=1,2）が項別R平坦で鎖レベルのArtin商に整合し、Γ同変で特殊sectorへの作用に整合する、かつ中心vによる積が `C_{1,R}`の互換な閉元を与えるとする。そのとき `H^0(C_{1,R})=R^5, H^0(C_{2,R})=R^{10}` が成り立ち、全Artin底変更と両立する。前者の四つの不変な基底の持上げ障害は `H^1(C_0)^Γ=0` に入るため常に0、vは中心元の自然変換として明示的に持ち上がる。`H^(-1)(C_0)=0` による短完全列と長さ、Nakayamaで自由性が従う。次数2は隣接群消滅による。

これは **正しい導来Nat複体の存在やその鎖レベル底変更を証明していない。** (KF) の全忠実性、相対cofibrant bar模型、導来tensor、同じenhancementでの特殊化が核心であり、実際の(BC)と全次数の形式模型同定、generic圏同値は未完成。

一次障害の任意の `2×5` 行列を逐次計算する方針は、Γ保存の今回の部分族では不要。`v` が分離しない変形族や Γ を破る方向にはこの結果を適用しない。その他のPoisson/量子化・17次元族・相対MF/SM/ER/反例は既存論文に保持する。

検算コード：`python3 computations/verify_central_symmetry.py --output build/central_symmetry_certificate.json`。計算はΓ characterの有限照合と人工的障害モデルだけで、実際の導来Natを計算しない。
