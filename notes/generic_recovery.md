# 一般次元の可換復元：現行論文Bの証明と検証

**2026-11-12 / B-v55。** 最初に `00_research_plan.md` を読む。現行入口は `papers/paper_b.tex`。証明は `papers/generic_recovery/` に置く。

## 主張の範囲

n>=3、N=n+2。次数別有限自由なR=C[h]_(h)上の中央代数A_Rが特殊化で多項式環になり、中心三次元Ω_Rの剰余が滑らかな三次式となる場合を扱う。方程式はK=C(h)上、rotation・指定周期付きの残余圏同値は有限拡大上に構成する。全coherent導来圏のsmooth proper性と有限線束生成、模型の幾何学的一意性、BFKの生成段数上界を保持する。

## 必要な依存だけを残した証明

`local_model.tex` でnoetherian性と有限Koszul持上げ、相対Gorenstein型、線束Homとproper模型を用意する。`window.tex` は完備Homの有限縮約と実際のdg section--window、有限長filtrationによる三対象生成、rotationを比較する。特殊ファイバーの生成性だけを一般点へ持ち上げる証明ではない。

`curved_transport.tex` は通常のgraded formalityを曲率を入れる前に用い、中心元の有限行列逆像、勾配Koszul、arity1/3のflow、逆写像と固定内部次数での収束を示す。対応する三対象のHomを構成してからLaurent体へ局所化し、任意のLaurent係数MFへ無限Taylor和を直接評価しない。

`generic_descent.tex` は残余体stabilizationの三成分Eulerベクトルを計算する。自己EulerだけではNによって零になり得るので使わない。非零性の後に代数閉包上でBFKを適用し、三次係数とperfect同値核・rotation比較を有限生成K代数へ降ろして閉点を選ぶ。

`coherent_saturation.tex` はsmooth対角によるpseudo-perfect加群のperfect性と評価射を用いる。有限線束からのHomの有限性と全twistによる検出により、線束生成部分を全coherent圏に同定する。全coherent圏のsmoothnessを最初から仮定しない。

`gradient_recovery.tex` と `field_model.tex` は、幾何学的な可換模型の存在を先に得た後、次数1/2の導来自然変換の積から勾配空間Qを復元する。可積分行列の線形空間が拡大体上で可逆元を持つことから、無限体K上でも可逆元を選び、G=(1/3)Σx_iA_iaq_aを作る。smoothな三次式の同じ勾配空間に対する射影的一意性の証明も本文に残す。積分条件だけで圏同値を証明しているのではない。

## 除外したものと保持する数学

三次三様体固有の接空間20→10、Plücker二次障害、独立の相対Artin/étale復元、Sklyanin/多ブロック模型、明示混合族・二次jet、point scheme、積分不可能例と有限検査器は主定理の証明に不要なのでBから外した。主証明が使う補題は、その証明だけを抽出して本文内に保持する。

独立成果の移管は未完了であり、証明を削除したわけではない。現在の保存先と残件は `paper_b_scope_and_transfer.md` を参照。旧 `paper_b_proof_audit.md` には独立成果の詳細・障害・計算情報が残るので、現行移管先ノートへの統合が終わるまで削除しない。Bの現在の再開入口は本ノートである。

## 検証と未実施事項

既存 `.latexmkrc` と同一内容で `latexmk -g -r .latexmkrc papers/paper_b.tex` を実行。全文27頁、11TeXファイル、102ラベル・94参照・37引用・13文献項目、未解決と重複0。全27頁の画像を点検し、切れ・重なりを認めなかった。共通preambleとAは変更していない。

この組版と参照照合は、新しい数学的証明の独立監査ではない。全既存検算、Aの全文再組版、移管側の全引用解決・独立原稿の組版は未実施。包括的新規性調査・外部査読・形式検証も未完。文献の書誌・適用箇所は現行 `papers/generic_recovery/references.tex` および各証明に保持する。
