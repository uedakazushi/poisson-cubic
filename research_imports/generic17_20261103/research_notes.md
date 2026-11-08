# 研究ノート：generic 17次元族／canonical ambient 復元

**2026-11-03 / v4。現行版のみ。** 詳細な定理・証明は `paper_ja.pdf` の各節を参照。本ノートは未解決の条件、必要な計算資産、先行研究の射程の監査に用いる。

## 主張台帳（簡潔）

| 主張 | 状態 | 根拠 |
|---|---|---|
| 滑らかな平面三次 `f3` に対する3変数Jacobain代数 `S_f3` の3CY性 | 既知の定理 | Mori–Smith, Theorem 4.2(1) |
| 低次cyclic perturbationのPBW・CY性と濾過3以下の中心元の存在 | 既知の定理 | Berger–Taillefer, Etingof–Ginzburg Theorem 3.3.2/Proposition 7.3.1(ii) |
| 2中心一次元を加えた5次元AS正則代数 `B_F` の相対自由性 | 本稿の証明・相対化 | 論文§2、PBWの基底特殊化 |
| 有理係数 witness の `Z(S)_1=Z(S)_2=0`, `dim Z(S)_3=1` | 計算再検証済み | `verify_center_sklyanin.py`。各次数の交換子rank 3,6,9 |
| 線形系の一定rankによる中心三次式 `G_F` の代数的相対構成 | 原稿中に証明あり、一般の証明全体の独立再監査は未了 | 論文§2、一次資料EG |
| 17係数正規形の横断性 | 有理数体上の厳密計算再検証済み | `verify_17_slice.py`，31x31 det = -5538243375000 |
| 一般軌道は24次元、中心三次対の有理商は17次元 | 原稿中に証明あり | 論文§3、Rosenlicht |
| `B_can(A)=B`、三次核 `kG`、偏極付きZ代数からの復元 | 初等的な本文の証明 | 論文§4、Artin–Zhang section algebra |
| Serreから偶数Veronese、中心二次曲線による復元 | 明示した tails有限大域次元などに依存 | 論文§5、Yekutieli–Zhang |
| 無標識導来圏やKuだけからのambient復元 | 未解決 | 本稿は主張しない |

## 具体的な証明上の注意

1. 41次元の係数表示から「本当に17次元非同型」という結論には、一般軌道が24次元であることと、`A`から `(B,[G])` を復元できることの**双方**が必要。18次元のparabolic軌道と31係数の横断性をまず確かめ、中心三次係数の4自由度を加える。量子的な `G` のbinary cubic部分の座標変換補正を、誤って非同変と同一視しない。
2. `G_F` の最高 `x,y,z`-次数記号は三変数代数 `S_f3` の非零中心三次元。`S_f3` の次数1,2の中心が零である開集合上で、相対的中心方程式の9未知数に一意解を得る。EGの点ごとの中心元の存在だけで、全パラメータの多項式解を直ちに主張してはいけない。一定rankと被約な基底を使う。
3. `A=B/(G)` の平坦性から `qgr A` の有限大域次元は自動的に従わない。very-general な正則性、Zariski開な正則性、指定された有理係数の正則性を混同しない。特にRennemo–Segal–Van den Berghの非可換 generic smoothness は有限中心等の仮定を確認して適用すべき。
4. ambient の復元には構造対象 `O` と次数シフト `(1)` を保持した `qgr` の偏極が要る。Serreから `(2)` を得る強化にも、有限大域次元・中心二次の条件・中心環上自由性が必要。構造対象を忘れた導来同値やZhang twistを越えて成立するとは主張しない。
5. 誘導される `qgr A -> qgr B` は Abel圏の完全忠実関手。導来圏の同じ関手が完全忠実とは限らない。

## 一次資料と確認した箇所

- Mori–Smith: https://arxiv.org/abs/1502.07403, §4 Theorem 4.2(1), smooth plane cubic ⇒ 3CY。
- Etingof–Ginzburg: https://arxiv.org/abs/0709.3593, Theorem 3.3.2(i)(ii), §7 Proposition 7.3.1(ii), §9.1 Rains explicit center。
- Berger–Taillefer: https://doi.org/10.4171/JNCG/6, 低次potentialからのPBW変形。
- Chirvasitu–Kanda–Smith: https://arxiv.org/abs/1706.05754, Propositions 2.1/2.3 中心正則拡大とAS正則性。個々の適用条件は引き続き監査。
- Zhou–Shen–Lu: https://arxiv.org/abs/1709.09292, normal extensionの中山自己同型特殊化。
- Artin–Zhang: https://doi.org/10.1006/aima.1994.1087, noncommutative Projとsection algebra。
- Yekutieli–Zhang: https://doi.org/10.1090/S0002-9939-97-03782-9, Serre duality for AS-Gorenstein noncommutative Proj。
- Artin–Tate–Van den Bergh: https://doi.org/10.1007/978-0-8176-4574-8_3, elliptic 3-dimensional regular algebra。
- Artebani–Dolgachev: https://doi.org/10.4171/LEM/55-3-3, Hesse normal form。
- Rennemo–Segal–Van den Bergh: https://doi.org/10.4171/JNCG/334, 非可換Bertini、仮定付き。
- Loray–Pereira–Touzet: https://arxiv.org/abs/1112.3871, Theorems 7.1, 9.1；Mayanskiy https://arxiv.org/abs/1303.5916, cubic Poisson方向。
- Pym: https://arxiv.org/abs/1403.6444, projective space quantum deformations/Poisson components。

**独自の17次元中心三次族と復元結果の初出・新規性は未確認。** 現時点では論文Introductionで既存結果と本稿の追加主張を分け、優先権を断定しない。

## 再開時の優先事項

- `paper_ja.tex` にある引用先の全仮定を再照合する。特に中心元の多項式規格化、Nakayama自己同型特殊化、AS-Gorensteinのsection algebra。
- 一般の17係数族の **tails finite global dimension** がどの非空Zariski開で保証されるか、あるいはvery-generalにしか保証されないかを明確化する。
- generic stabilizer の次数と17係数パラメータの一般ファイバーの実際の有限次数を調べる（17次元性は次数未決でも成立）。