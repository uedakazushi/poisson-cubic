# 曲率付き対角：正則な有限積と可換候補

**2026-11-11 / v28。最初に00_research_plan.mdを読む。GitHub mainが正本。** 乗法的bar比較と次の(BC)課題は `notes/bar_comparison.md`。

## 現在の結論と証明所在

混合関係式 `[y,z]=h(x^2+uy), [z,x]=h(y^2+ux), [x,y]=hz^2` と指定中心元（lambda=1）から、絶対曲率付き対角の閉自己準同型を構成し、全16順序付き合成を計算した。人工可換候補を積表の入力にしない。

R=Q[h]_(h)上で分解・高次ホモトピー・閉行列・積・基底をすべて正則に選べる。H^0は自由rank4,6で、積を含め全Artin切断・Q[[h]]への底変更と両立する。これは有限対角の結果である。新しい同次分裂bar比較により有限支持cup積へ同定できるが、actual Natへのcharacteristic写像が同型となる標的条件(BC)は未確認。指定Wとの全次数比較・generic Ku同値も未証明。

証明は `papers/reconstruction/curved_diagonal_recovery.tex`, `regular_diagonal_recovery.tex`, `multiplicative_bar_comparison.tex`。有限行列計算は全次数PBW/Koszul完全性の代用ではない。外部査読・形式証明・包括的新規性調査は未完了。

## 候補式と核

`G_h=(x^3+y^3+z^3)/3+h^2xyz/3+(1+h^6/54)uxy-h^4uz^2/18-h^2u^2z/12+(1+29h^6/648+h^12/4374)u^3`。

独立中心変数vはv^3の一変数因子として加える。Q(h)の恒等式から得た多項式で、特定hでの補間ではない。核は

- `q_u=(3+h^6/54)u^2-h^2uz/6+xy`
- `q_x=x^2+h^2yz/3+(1+h^6/54)uy`
- `q_y=y^2+h^2xz/3+(1+h^6/54)ux`
- `q_z=z^2-h^4uz/18-(13h^2/12+h^8/162)u^2`。

`G_x=q_x, G_y=q_y, G_z=q_z+h^2q_u/3, G_u=(1+h^6/54)q_u-h^4q_z/18`。基底変換の行列式1+h^6/27はRの単元だが、h^6=-27で同じ可逆性を主張しない。G_0+v^3は滑らかなF_1。

## 正則化と局所自由性

有限線形系MX=BでM(0)の独立列J、その独立行Iを選び、M[I,J]の逆だけで持ち上げ、残りの未知数は零にする。一般・特殊rankが同じなら正則解となる。実装はrank一致を推測せず全行の等式を厳密検査し、列が右辺を張らなければ停止する。一般の核飽和と像への持上げを区別する。

45個の局所系から高次ホモトピーと四閉行列を構成。小複体の隣接項はr=1で(0,10,56)、r=2で(4,35,120)、微分rankは一般・特殊とも(0,6)、(4,25)。C_2^0の四境界と六つの実際の合成ux,uy,uz,xy,xz,yzを並べた35x10行列の先頭10行の行列式はh=0で-3。これが閉元のR基底とH^0の自由性、全Artin底変更の根拠であり、有限個の切断テストではない。

D=h^6+162、L=1+h^6/54として
`u^2=9h^2 uz/D-54xy/D`、
`x^2=-Luy-h^2yz/3`、`y^2=-Lux-h^2xz/3`、
`z^2=(4h^10+675h^4)uz/(36D)-(2h^8+351h^2)xy/(6D)`。

有限行列455種類の係数分母lcmはQ^*を除き `(h^3-1)(h^6+162)`。これは選んだ表示の分母であって圏のsmoothness判別式ではない。

## 有限性・相対模型・障害

長さNの線形対角でs_j:P_p->P_(p+2j-1)。N=5ならs_1,s_2,s_3だけでD^2=t(Omega_L-Omega_R)。五変数の小複体r=1,2の隣接次元は(0,15,126)、(5,70,330)。持上げ・合成は内部次数六以下の係数で扱える。これらはcochain次元でありNat次元ではない。

uを底とする相対対角はg(u)を加えても不変で、u^3係数を検出できない。相対式は
`G_rel=(x^3+y^3+z^3)/3+h^2xyz/3+lambda(1+h^6/54)uxy-h^4lambda uz^2/18-h^2lambda^2u^2z/12`。
一般lambda!=0への相対式はuのスケーリングで得るが、絶対式を同じ操作で一般化しない。

Q(h)の任意のrref基底はh=0で極を持つ。最終Gが多項式でも中間模型の正則性は従わない。正則な別模型を作り同じGへの積分を確認済み。

## 積の比較の現在地

F,F^-1のarity上界L_F,L_Gから、arity<=Mのcoderivationの共役はarity<=L_G(L_F+M-1)。これは有限支持dg Lie同型であり、それだけではcup保存を意味しない。

新しい `multiplicative_bar_comparison.tex` ではcap作用と明示的ホモトピーを使って、同次分裂比較の下でYoneda積=cup積を証明した。MFの実際の導来自然変換へはbrace挿入による乗法的写像を構成済み。同型性には標的側の(BC)が残る。次は可換形式模型の相対kernel/sectorにより(BC)を検査する。sourceのrankや体上の公式からH^0底変更を推論しない。全Artin成功からgeneric圏同値・SMを結論せず、SM/ERと指定生成子の有限cone/retractも保持する。

候補Gについてはq=h^6の代数正規形のL_1=127/5184、C_1=1613/1679616を得た。これは元の形式Wの係数への無条件な同定ではない。詳細は新ノートと本文。

## 再現・一次資料

```sh
python3 computations/verify_regular_diagonal.py --output build/regular_diagonal_certificate.json --full-output build/regular_diagonal_full.json
latexmk papers/curved_diagonal_recovery.tex
python3 computations/verify_bar_comparison.py --output build/bar_comparison_certificate.json
latexmk papers/multiplicative_bar_comparison.tex
```

regular_diagonal.pyはabsolute_diagonal.pyの線形持上げを差し替え、verify_regular_diagonal.pyは非可換関係から全行列を再生成する。小証明書は積表・rank・小行列・分母・全行列canonical JSON SHA256を保持。再生成できる全行列は重複保守しない。

GHLR arXiv:2312.16645v5 (2026-09-17), Theorems4.7,6.14/Remark6.16（PDF pp.32--33）、Polishchuk--Positselski arXiv:1010.0982v2 §§3.3,3.5の異なるtotalizationと導来圏を区別する。今回のcap/HPL/braceの一次資料と適用範囲は `notes/bar_comparison.md`、`multiplicative_bar_references.tex` に記録する。
