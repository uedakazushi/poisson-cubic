# 曲率付き対角：正則な有限積と可換候補

**2026-11-11 / v27。最初に00_research_plan.mdを読む。GitHub mainを正本とする。**

## 現在の結論と証明所在

実際の混合関係式 `[y,z]=h(x²+u y), [z,x]=h(y²+u x), [x,y]=h z²` と指定中心元（λ=1）から、絶対曲率付き対角の閉自己準同型を構成し、全16個の順序付き合成を計算した。人工的な可換候補を積表の入力にはしていない。

現在は Q(h) 上だけでなく **R=Q[h]_(h) 上で、分解・高次ホモトピー・閉行列・積・コホモロジー基底をすべて正則に選べる**。低次数H⁰は自由rank4,6であり、積も含め全Artin切断およびQ[[h]]への底変更と両立する。これは有限曲率付き対角の自己準同型代数についての結果である。actual Nat、指定形式模型Wとの全次数比較、generic Ku同値を証明したことにはならない。

証明全文：`papers/reconstruction/curved_diagonal_recovery.tex`、`regular_diagonal_recovery.tex`（同ディレクトリ）。単独入口は `papers/curved_diagonal_recovery.tex`。既存の全Artin PBWと有界Koszul分解の完全性への依存は本文に明記し、有限Hilbert関数検査で置き換えない。外部査読・形式検証・包括的新規性調査は未実施。

## 候補式と核

四変数の候補は

`G_h=(x³+y³+z³)/3+h²xyz/3+(1+h⁶/54)uxy-h⁴uz²/18-h²u²z/12+(1+29h⁶/648+h¹²/4374)u³`。

独立中心変数vはv³の一変数因子として加える。これはQ(h)上の恒等式から得た多項式であり、特定のhでの補間ではない。

核の基底は

- `q_u=(3+h⁶/54)u²-h²uz/6+xy`
- `q_x=x²+h²yz/3+(1+h⁶/54)uy`
- `q_y=y²+h²xz/3+(1+h⁶/54)ux`
- `q_z=z²-h⁴uz/18-(13h²/12+h⁸/162)u²`。

`G_x=q_x, G_y=q_y, G_z=q_z+h²q_u/3, G_u=(1+h⁶/54)q_u-h⁴q_z/18`。基底変換の行列式は `1+h⁶/27`、従ってR上の単元。例外値h⁶=-27で同じ可逆性を主張しない。G₀+v³は滑らかなF₁である。

## 正則化の方法と検査証明書

有限線形系MX=Bで、特殊化M(0)の独立な列Jとその独立な行Iを選ぶ。M[I,J]の逆だけを使い、残りの未知数を零にする。一般点と特殊点のrankが同じなら正則な解となる。実装はこのrankの一致を推測せず、必ず全行のMX=Bを厳密に検査する。所定の列が右辺を張らなければ停止する。一般の核飽和とこの像への持上げを混同しない。

45個の局所系から正則な高次ホモトピーと四つの閉行列を作った。小複体の隣接項はr=1で(0,10,56)、r=2で(4,35,120)。微分rankは一般点・特殊点とも(0,6)、(4,25)。

C₂⁰の四つの境界と、六つの実際の合成 ux,uy,uz,xy,xz,yz を並べた35×10行列の最初の10行の行列式はh=0で **-3**。したがってこれらは閉元加群のR基底をなし、六合成がH⁰(C₂)のR基底になる。これが全Artin底変更の根拠であり、有限個の切断を試しただけではない。

D=h⁶+162、L=1+h⁶/54として正則な積は

`u²=9h² uz/D−54xy/D`,
`x²=−Luy−h²yz/3`, `y²=−Lux−h²xz/3`,
`z²=(4h¹⁰+675h⁴)uz/(36D)−(2h⁸+351h²)xy/(6D)`。

保存した有限行列の455種類の有理係数の分母の最小公倍数は、Q×を除いて `(h³−1)(h⁶+162)`。これは行列表示の分母であり、圏のsmoothness判別式ではない。

## 有限性・相対模型・再利用する障害

長さNの線形対角Pに対しs_j:P_p→P_(p+2j−1)を構成する。N=5ならs₁,s₂,s₃だけでD²=t(Ω_L−Ω_R)。五変数の小複体r=1,2の隣接次元は(0,15,126)、(5,70,330)。持上げ・合成の係数は内部次数六以下で扱える。これらはcochain次元であってNat次元ではない。

uを底に置く相対対角はg(u)を中心元に加えても変わらず、u³の係数を検出できない。相対式は
`G_rel=(x³+y³+z³)/3+h²xyz/3+lambda(1+h⁶/54)uxy−h⁴lambda uz²/18−h²lambda²u²z/12`。
一般lambda≠0への相対式はuのスケーリングから得るが、絶対式を同じ操作で一般化しない。

Q(h)上の任意のrref基底はh=0で極を持ち得る。多項式Gが得られたことだけで中間模型の正則性を推論しない。現在は単元小行列を用いた別の正則な模型と、同じGへの積分を実際に検証している。

## 次の比較で使える補題と未解決箇所

FとF⁻¹がそれぞれarity≤L_F,L_Gのbar同型、F₀=0なら、arity≤Mのcoderivation Xに対しFXF⁻¹のarityは≤L_G(L_F+M−1)。これにより有限支持Hochschildコチェインのdg Lie同型を得る。証明はregular_diagonal_recovery.texのrd:lem:bounded-conjugation。これは **cup積を保つ比較の証明ではない**。

優先する次の作業は、一入力を標識したbar双加群による比較を作り、有限対角のYoneda積とcompactly supported Hochschild cup積を同定すること。次に内部shift、三次周期性、非恒等sectorを含めて残余圏のNatへ移す。全Artinでの成功からgeneric圏同値・相対対角perfect性を結論しない。SM/ERと指定生成子の有限cone/retractは別経路として維持する。

## 再現手順と一次資料

Python 3、SymPy 1.14で次を実行する。

```sh
python3 computations/verify_regular_diagonal.py --output build/regular_diagonal_certificate.json --full-output build/regular_diagonal_full.json
latexmk papers/curved_diagonal_recovery.tex
```

`regular_diagonal.py` は既存 `absolute_diagonal.py` を継承し、持上げ線形系だけを差し替える。`verify_regular_diagonal.py` は nc 関係式から全計算を再生成する。追跡中の小証明書には積表・rank・小行列・分母・全行列のcanonical JSON SHA256を収録。大きな全行列データは同じコマンドで再生成でき、Gitで重複保守しない。

Guan–Holstein–Lazarev–Rasmussen, arXiv:2312.16645v5 (2026-09-17), Theorems4.7,6.14, Remark6.16（PDF pp.32–33）。Polishchuk–Positselski, arXiv:1010.0982v2, §§3.3,3.5。第二種Hochschildという名称だけで異なるtotalization・双加群導来圏を同一視しない。適用条件を本非可換族について確認したとはしていない。
