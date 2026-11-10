# 相対Artin基底のsectorと(BC)の現在有効な判断

**2026-11-11 / v30。再開時は00_research_plan.mdを先に読む。** 証明全文は `papers/reconstruction/relative_artin_sector.tex`。検算と本質的な障害だけを本ノートに整理する。

## 証明済みの可換側

`R_m=C[h]/(h^(m+1))`上で、斉次三次形式`W_m`の特殊ファイバーが滑らかな五変数cubicなら、勾配Koszulの正のホモロジーは零で、`Jac(W_m)`は次数別R_m自由、Hilbert級数`(1+t)^5`。次数1,2は自由rank5,10。証明：`0→K(∂F)→K(∂W_m)→K(∂W_(m-1))→0`の長完全列とNakayama・長さ比較。五変数の非恒等µ3-sectorはnormal rank5の奇数cohomological parityで、H0には寄与しない。

## 対角unitとK-flat障害

**相対対角のunit（v30、証明あり）。** 任意の可換基底環の斉次三次式に対する差分商stabilized diagonalの畳込みは、有限自由graded MFへ自然な強ホモトピー同値を与える。Koszul収縮h0と摂動pについて(h0p)^(n+1)=0なので、逆とホモトピーは有限和であり、全Artin底変更・内部shift・mu3スカラー作用と両立する。原稿：`papers/reconstruction/diagonal_kernel_identity.tex`、計算：`computations/verify_diagonal_identity.py`（厳密恒等式606件）。**(KF)の全忠実性は未完成。** k[epsilon]/epsilon²上の両側無限自由周期複体は非輪状でもK-flatでない。相対cofibrant/h-projectiveな二側bar模型とBFK体上比較への同一enhancementでの特殊化を次に検証する。

## 乗法的比較に残る(KF)

項別R_m平坦な複体の射が特殊化後擬同型なら、元も擬同型である（coneの有限hフィルトレーション）。体上でMorita生成元となる特殊生成子をR_mに持ち上げる議論にも、両側bar評価が項別平坦で特殊化に可換という入力を使う。

**未解決(KF)：** 相対stabilized diagonalのkernel作用を、指定された有限rank graded MFと同じenhancementの二側bar複体上で構成し、その特殊化が体上Ballard–Favero–Katzarkovのkernel比較の擬同型に一致すること。符号・内部shift・µ3-equivariance・convolutionとの両立を検証する。これが確認できればnilpotent比較から(BC)を導けるが、現時点で実際のcategorical Nat/rotation積を無条件に同定したわけではない。

## 反例・検算・次の課題

特殊ファイバーのコホモロジー次元だけでは底変更を保証しない。`R_1=k[h]/h²`上の`[R_1 --h--> R_1]`のH0特殊化は零写像である。

`F=(x³+y³+z³)/3+u³+v³+uxy`と、計算済み候補の`h=1/2`について、厳密GroebnerによるHilbert関数はともに`(1,5,10,10,5,1)`、長さ32。これは相対Koszulの一般証明やカテゴリ比較の検証ではない。

`python3 computations/verify_artin_sectors.py --output build/artin_sector_certificate.json`、`python3 scripts/verify_artin_sector_assets.py`、`latexmk papers/relative_artin_sector.tex`。新規性網羅的調査・外部査読は未実施。

次は、特に`G_m=stab(k),(1),(2)`上のkernel convolutionを鎖レベルで書き、体上のkernel mapとの同一性を有限自由行列で確認する。MFの全perfect生成性やgeneric同値の証明は別に必要。