# 研究ノート：可換復元の現在有効な知識と障害

**2026年11月10日・v17。GitHub mainだけを正本とする。** 詳細な局所模型・具体式は `reconstruction/research_notes.md`、証明全文は `reconstruction/tex/rotation_saturation_reduction.tex` とそのinputに置く。

## 1. 復元の論理と現在の核心

所定の正則局所底上の次数別自由な中心三次量子化から、properな線束生成残余dg代数Γ_Rと、逆 `(-1)R_O` を持つ標準rotationが得られる。残余対角条件(SM)があれば全coherent残余圏との一致と有限型smooth proper pairへのspreadが従う。

étale局所実現(ER)は、実在するsmooth proper pairを入力とする定理として独立の証明を得た。従って量子化入力がある成分では、generic可換復元の未解決条件はSMである。非楕円二成分の量子化は既存の具体的構成を使えるが、全Poisson成分について量子化を一括して構成したわけではない。

## 2. ERの実際の証明に必要な点

sourceの滑らかな幾何的変形族とtargetの実在するsmooth proper dg族を取る。同値双加群Pの小拡大障害はExt²(P,P)=HH²(source)に入る。両側に自己同値のliftがあり、還元上のintertwinerがあるため、障害の自然性からその類はrotation不変である。ここでintertwiner自体のliftはまだ仮定しない。

幾何的KSが不変HH²に全射なので、sourceのliftを修正して障害を消す。Pのperfect liftはunit/counitのconeにNakayamaを適用して同値となる。intertwinerの持上げ障害はHH¹であり、cubicでは零。最後にactual perfect対象と射のmoduliを使い、同値・同型が開条件であること、負HH消滅によるArtin性、無限小smoothness、pointed étale sectionを確認する。

この方法は抽象的なHochschild変形のactual性、HH³=0、formalityを使わない。自己同値一つのpairだけを扱い、選択した三次周期性のcoherenceは結論しない。親 `rotation_models.tex` の形式変形比較全体を再監査したことでもない。

一次資料と参照箇所は `reconstruction/tex/etale_references.tex`。Toën–Vaquié, arXiv:math/0503269v5, Theorem 3.6/Corollaries 3.15,3.17,3.19、Lowen, arXiv:0707.2602v1, Theorem 4.8を使う。Lin–Zhang, arXiv:2611.05915v1, §2.1/Theorem 2.2/Proposition 2.4は幾何的な両側projectorを仮定するため非幾何的targetへ直接引用しない。同じ障害消去原理との関係を本文に明記した。

## 3. cubicのHochschild入力と具体的slice

N=n+2≥5に対し、HH<0=0、HH0=C、HH1=0。HH2はJ(F)_3、ただしn=4では二つの追加方向を持つ。BFKのsector公式で非恒等sectorは3|Nかつcohomological degree N/3に各一次元となる。四次元の追加二方向はrotation固有値ζ,ζ²を持ち、不変部分は常にJ(F)_3で、次元はbinom(N,3)。幾何的KSとの同定にはn≥4でHuybrechts–RennemoのLemma 2.19と§3.3、n=3でJLLZ Theorem 4.4(2)を用いる。単なる次元一致だけでKS同型を結論しない。

節点・尖点の滑らかなcubic fivefold
F=f+ux²+a³+b³+c³+u(a²+b²+c²)+u³、f_C=xz²+y³、f_N=xyz+y³+z³
について、84個の三次単項式と49個の z_j partial_i F からなる整数行列を構成した。コード `reconstruction/computations/verify_etale_inputs.py` は階数49、表示された35単項式の商基底、射影の二恒等式を厳密検算する。採用49行の小行列式は尖点で2^15·3^26、節点で−2^6·3^25。SymPyの有理演算と独立な整数Bareiss消去で照合した。

これによりF+Σt_m mという具体的35係数source族が得られる。量子パラメータ(r,s)からt_mへの閉公式は未計算であり、SMを検算したわけではない。証明書には単項式の順序、全基底、採用行を収録する。

## 4. 各成分を扱う支配的chart

`tex/papers/all_poisson_components.tex` のスカラーchart定理は、非零被約既約アフィン錐Zを滑らかな S=T×A¹_h で支配する。h≠0では稠密開への同型、h=0では零点へ縮約する。Tは射影化の滑らかな稠密アフィン開で、スカラー代表を一座標で規格化する。

generic復元のために特異な頂点への量子化の降下を先に解く必要はない。幾何学的一般点のブロック正規形を有限分離拡大へ移し、分母と判別式を除いて有限étale被覆上で固定する。これは正規形の存在を入力とする帰結である。一つのPoisson方向だけの形式弧では成分のgenericを扱えず、係数方向Tを保つ必要がある。

## 5. 中心元の有限jet代数化

有限行列M(h)の形式核ベクトルは、係数整域の縮小とq(h)の反転（q(0)可逆）によって、任意の指定有限jetを保つ代数的核ベクトルに置換できる。一定rankは仮定しない。K[h]_(h)→K[[h]]の忠実平坦性を有限余核へ用いる。

次数3,4の自由PBW模型があれば、中心三次元は z↦h^−1[z,x_i] の有限行列で扱える。未知数binom(N+2,3)、方程式N binom(N+3,4)。形式中心の存在は入力であり、指定無限級数全体の一致を主張しない。これは全次数PBW性・AS性・残余対角の代数化を証明しない。

## 6. 非楕円成分とsmoothnessへの障害

固定した滑らかなcubic fivefold上に、一般点で節点型または尖点型の純三次ブロックを持つ二次元Poisson既約成分がある。`tex/papers/nonelliptic_poisson_components.tex` のne:mainに証明、全Jacobi接行列35列の階数33、整数小行列式（節点2^24·3^12、尖点−2^33·3^12）の証明書を保持する。support内の縮約二形式の平方零スキームからブロックの内在性を示す。

従って楕円Sklyaninだけでは全成分を覆えない。一般化Jacobianは節点でG_m、尖点でG_aであり、楕円Picardへの有理写像障害をそのまま適用しない。これは可換復元の反例ではない。

SMに必要なのは、特殊ファイバーの有限対角ではなく、実際の底上のP∈Perf(Γ_R^e)と射P→Γ_Rである。Γ_RがproperならPのconeも底上perfectで、一ファイバーで擬同型なら局所Nakayamaを使える。各Artin切断のsmoothnessやHom階数だけでこの持上げを置換しない。

中心変数uの通常微分は量子代数の導分にならない。ambientの対角を中心商で両側テンソルしたものは残余対角ではない。Serre自己同値の存在もsmoothnessを含意しない（対称Frobenius代数C[epsilon]/epsilon²）。詳細な障害と具体式は `reconstruction/research_notes.md`。

## 7. 他の有効な成果と依存範囲

論文Aは一般次元のPoisson正規形・退化・量子化、Bは中心三次対の41次元incidence、17係数族、構造対象と次数シフト付きambient二次包絡復元、Cはrotation付き可換復元と障害を扱う。BではambientをB、商をAと書き、CではambientをA、商をBと書く。

Bの分離型は余次元15、法線は中心変数一次6方向と二次9方向。元の可換cubicのJacobian変形への17次元接写像の核は平面移動6とPoissonスカラー1。これは量子化後の可換模型への写像ではない。固定cubic・固定平面のG_mから滑らかな楕円Picardへの有理写像は定数だが、分岐対応や動くcubicは排除しない。

混合15方向の中心式と一次持上げの一意性は独立節に保持する。有限体特殊化の成功を普遍中心性の証明としない。`fermat_center_certificate.json` の15項整数恒等式は混合なし三変数Fermat中心式の証明書である。

Cの一楕円ブロックの良い複素ファイバーでの比較、有限位数条件付き多ブロック比較、形式復元の既存証明は保持する。一般混合項の全点復元、二つ以上の無限位数ブロックの全生成、元の底への一意降下は未解決。Brill–Noether、Pfaffian、Reye、特異圏の境界研究の唯一の証明を削除しない。PDF-only資産の全面的TeX再構成と全過去計算の再監査は未了。

## 8. 再現と次の着手

`reconstruction/README.md` の二つの計算、build、verifyを実行する。参照とハッシュは全TeX inputを含む。計算的確認と圏論的証明は別である。最優先の次作業は非楕円二成分の有限残余対角証明書の構成。研究の量化は一般次元・各成分を保ちつつ、具体的量子化のある成分から実証する。

GitHubへ全文と再現資産を保存し遠隔確認する。Libraryはpushが実際に失敗した場合だけの緊急退避とする。

## Hochschildの第三次数障害（現行の確定した整理）

滑らかなN変数三次F（n=N−2≥3）に対するBFK Theorem 5.39の恒等sectorは偶数次 q=2r にJ(F)_{3r}を与え、μ₃の非自明二sectorは3|Nなら次数q=N/3に各一次元を与える。二sectorのrotation固有値はζ,ζ²。したがってHH³はN=9の場合だけC²で、全N≥5でHH³のrotation不変部分は零。具体的検証は`reconstruction/tex/hochschild_obstructions.tex` と同じディレクトリの整数証明書を参照。形式変形の一次障害の消滅と有限型でのSMを混同しない。
