# 研究方針：中心三次変形の量子化と一般点可換復元

2026-11-14 / v86。再開時は本ファイルを最初に読む。GitHub mainが正本。

## 現在の目標と達成基準

論文A `papers/paper_a.tex`（A-v55）は全次元Poisson正規形を中心に、その幾何学的帰結・代数的量子化を扱う。ambient復元と完全交叉の背景は付録に置く。論文B `papers/paper_b.tex`（B-v57）は、次数別有限自由な代数的中心三次変形の一般点可換復元を扱う。公表の達成基準は、主要定理の仮定から結論までの証明が現行原稿内で閉じ、使用する既知定理の適用範囲と新規性が具体的に説明され、全文を再生成できることである。

Bでは n>=3、R=C[h]_(h)、K=C(h) とし、A_R/hA_R が N=n+2 変数多項式環、中心三次元の剰余が滑らかな三次式であることを仮定する。可換方程式はK上、全coherent残余圏のrotation・指定三次周期付き同値はある有限拡大上に構成する。模型の一意性はrotation付きpairを実現する模型の幾何学的射影同型類についてである。K上のformの一意性・同値核のKへの降下・特殊点を含む代数的相対同値は結論に含めない。

## 到達点と証明の所在

AではEuler--Koszul表示、Jacobi条件のHessian線形化、Lie代数補題、全次元正規形、退化軌跡とBondalの次元下界、代数的中心三次元とPBW/AS性、固定・相対Poisson成分、ambient復元の証明を再点検した。本文の証明を追う監査と有限計算は別々に記録している。所在・仮定・一次資料の確認範囲は `notes/poisson_article_submission_audit.md`、実行状態は `validation_paper_a.json` を参照する。

査読の三要求に対する現行構成は、定理ごとの既知入力と追加内容の比較、版・頁を固定したPym比較、および幾何から量子化への依存順である。表現論の入力を集めた独立補題 `lem:pg-basepoint-free-lie` と、一般次数の滑らかな超曲面上の非連結中心に対する `prop:pg-triple-lifting-obstruction` を本文に置く。後者では全連結成分の正次元性が必要であり、連結なら障害消滅、分離型の二曲線では非零となる。

量子化の新規性は点ごとの中心元存在とは区別する。Etingof--Ginzburgの刊行版Theorem 3.3.2(ii), p.1385と§8.3, pp.1410–1411は既知の存在・特殊化を与え、§9, p.1414はRainsの公式を含む。Hesse係数tが可逆なら混合二次項を中心平行移動で既存表示へ移せる。本稿は固定係数環での無極な規格化、指定Casimirへの正則持上げ、特異・零の制限、全ブロック・多パラメータ・同変降下を制御する。旧目標の正規形・Bondal・量子化・成分数は保持され、未解決なのは全モジュライ降下、固定非零変形での同型類像、および刊行版本文・初出の最終照合である。

相対Poisson空間から三次式のパラメータ空間への忘却射は有限型アフィン射であり、閉埋め込みではない。階数層の記述には (F,P)↦(aF,a^{-1}P) の同時スカラー作用と被約構造を明記した。三次三様体の導来復元には左右noetherian性を明示し、偶数Veroneseからの復元に必要な中心二変数上の自由性はambient PBWだけでは従わないと訂正した。最高active記号の正則性が十分条件となる。正規形・Bondal・全Poisson量子化・成分数の主要結論は保持している。

Aの量子化は、全三次式の滑らかさ→active gradientのgcd=1→三次Casimir核の一定次元→普遍交換子小行列式の恒等的消滅→Cramer中心元、という有限代数的構成による。任意の三変数制限をHesse標準形へ帰着する系では滑らかさを仮定するが、全Poisson量子化定理には不要。Kontsevich--Dolgushevの形式理論は背景であって、この存在証明の入力ではない。純中心三次項の配分、相対PBW、中心正則性、AS-Gorenstein商まで本文に証明がある。モジュライ全体へ量子化を降下する同変な構成はまだ得ていない。

固定したactive・中心変数の分解については、全滑らかな三次式の係数空間とh直線の積に、零切断全体を含む一つの開集合を取り、偶な中心元を同時に選べる。`thm:pg-det-global-coefficient-lift` は、割った交換子の定階数核、τ=h²への下降、factorialな係数環のPicard群消滅を用いる。通常の中心はh=0で次数三全体へ増えるため、この核の底変更と混同しない。規格化の変更は Ω'=aΩ+c（aは単元、cは純中心）であり、同じ古典極限でも中心イデアルは変わり得る。具体的Hesse例と同変な中心直線を選ぶ問題は `notes/universal_casimir.md` に整理した。

単一ブロックの同変性は `equivariant_central_lifts.tex` で次の範囲まで解決した。全滑らかなfについてはG_0=(GL3×GLm)×Gmに同変な中心元を、零切断全体を含む不変開上に選べる。g=f(x,0)も滑らかなら、方向微分δ_gの同変左逆から混合二次項の中心B_fを選び、B_f'=(MB_f−C)N^-1によって中心平行移動も含む全ブロック群Gと整合させられる。t=ηhとしてhを固定すると、対応する線形群の商上へ中心商族が降りる。純中心係数の固定と全平行移動の同変性は一般に両立しない。

階数二のPoisson対の被約層内でgが滑らかな開について、この線形群の商は実際のPoissonモジュライ上の中心Gm-gerbeである。gcd(m,3)=1ならmr−3s=1を満たす整数を選び、θ=(det N)^rλ^sで次数dの線形化をθ^-dだけ補正すると、中心スカラーの作用が消えて次数付き代数と中心商がPoissonモジュライへ降りる（`prop:pg-equivariant-poisson-gerbe`、`cor:pg-equivariant-character-descent`）。特に三次三様体ではm=2、θ=(det N)^2λであり、17次元のPoisson対の被約モジュライの稠密開とh直線の積の零切断近傍に量子化族を得る。17は底の次元であり、固定h≠0での非可換代数の同型類の像の次元は未解決である。3|mではこの指標による方法が使えないことだけを示しており、別の降下の不存在は結論しない。

三次四様体の一般階数四の構造は、二つの滑らかな平面三次の分離型F=f+gに限られ、全てpurely elliptic log symplecticとなる。退化因子は正規なjoin、Poisson零点スキームは被約な二本の楕円曲線の非交和である。`prop:pg-split-elliptic` は正規形に依存しない直接証明、`cor:pg-cubic-fourfold-elliptic` は正規形からの分類を与える。Pym arXiv:1507.05668v1のTheorem 1.3・Proposition 5.7とは両立せず、同版Lemma 5.5が非連結曲線で成立しないH¹(I_C)=0を用いることを具体化した。刊行版本文・訂正文との照合は未了で、比較を公開v1に限定する。Definition 4.2はp.17、Theorem 1.3はp.4、Lemma 5.5はpp.28–29、Proposition 5.7はp.30に固定する。

既知部分の帰属も明確にした。Bondal 1993のdivergence-free持上げ、Derdzinski--Gal Theorem Bの半単純Lie代数上の核計算と、本稿のHessian基点自由性からの根基排除を区別する。完全交叉の低twist消滅には `lem:ci-low-twist-vanishing` で穿孔錐とKoszul分解による独立証明を与えた。Brückmann原証明は未取得だが、現行の存在判定の証明依存からは外れている。

Bの証明は `papers/generic_recovery/` だけで完結する。`local_model.tex` と `window.tex` が局所proper模型と三対象window、`curved_transport.tex` が実際の完備A_infty比較、`generic_descent.tex` がEuler非消滅・BFK生成・有限降下、`coherent_saturation.tex` が全coherent圏への飽和、`gradient_recovery.tex` と `field_model.tex` が勾配空間の積分と方程式の基礎体降下を与える。

B-v57ではこの証明連鎖を数学的に再点検した。対称積の核という定義、rotation付き一意性の範囲、降下核と随伴coneのperfect性、残余成分のadmissibility、graded stabilizationの構成、曲率移送が有限rank MFを保つ次数を本文に明記した。主定理の入力への追加仮定や、一般点の存在結論の撤回を要する問題は今回の点検では見つかっていない。これはLean等の形式検証・外部査読・包括的新規性確認とは異なる。正確な監査範囲は `notes/paper_b_proof_audit.md`、組版・有限検算の実行状態は `validation_paper_b.json` を参照する。

先行研究との比較は、CKの第二種変形複体、Lowen--Van den BerghとBlanc--Katzarkov--Panditの形式変形・生成子、Toën/Toën--Vaquiéの有限表示と同値判定、TVのpseudo-perfect性とPerryの貼合せ、Ueda--Yoshinaga/Wang/Hwangの勾配空間まで具体化した。一般的なcurved formality・生成子の存在・有限降下・Jacobian Torelliは既知の原理である。本稿では相対window、単位・二重次数・有限rankを保つ完備MF関手、固定三対象の通常Homの局所化を具体的に証明し、一般点復元へ結びつける。この包括的結論と明示構成の初出は調査範囲で同一の定理を確認できていないが、確定はしていない。

方程式の積分には、Hwangの理論の基本的帰結として有限étaleなsymmetrizer代数E_Fを用いる。可積分行列空間の次元は最細の幾何学的Sebastiani--Thom分解のブロック数に等しく、幾何学的に分解不能なら固定した勾配空間からの方程式は基礎体上でもスカラー倍まで一意である。証明は `ej:lem:symmetrizer-algebra`、`gcd:prop:integrability-symmetrizer`、`gcd:cor:indecomposable-equation`。これは同値核の基礎体降下を意味しない。

独立な点スキーム・Jacobian・一次変形・Artin・étale・相対模型の成果はnc-cubic2へ移管済みである。現在の入口は `notes/paper_b_scope_and_transfer.md`。Bの必要証明を移管先へのリンクだけで代用しない。

## 優先する次の課題

1. Aの公表上の中心を全次元正規形・Bondal・全Poisson代数的量子化・相対成分数に置き、三次四様体の純楕円分類を具体的帰結として示す。Pym論文の刊行版または著者のaccepted manuscriptを通常の公開経路で入手し、v1との該当箇所・訂正状況を最優先で照合する。Oxfordの登録メタデータは確認できたが本文は取得できていない。独立な反例証明は現行本文にある。Bondal・Derdzinski--Gal・LPT/Mayanskiy・Gualtieri--Pym等との比較を踏まえ、包括的な正規形・成分定理の初出も引き続き調べる。
2. 特異な三変数制限での全G同変性と、複数ブロックの配分・相対規格化の整合性を調べる。全fでのG_0平均、滑らかなgでの全G同変性、gcd(m,3)=1での階数二モジュライへの降下は解決済みである。まずgが節点・尖点・零となる場合に、f全体の混合係数も使って中心直線の分裂を選べるかを調べる。δ_gだけの正則な左逆は全非cone三次の開には延長できないので、同じ手法の形式的延長に頼らない。複数ブロックについては、中心核の射影束と古典直線に沿うdilatation、中心元の正則性、表示群に関する降下を `notes/universal_casimir.md` §3に整理した。次に分解・純中心配分を変えた間の整合を調べる。3|mでの別の降下法、固定h≠0での像の次元、全閉パラメータのqgr滑らかさ、特殊点を含む相対残余圏同値は、それぞれ別に定式化する。
3. Bの存在定理を一つの具体的な非可換入力で有効化する。rotation核Pと対角Deltaの有限表示から V=H^0RHom(Delta,P)、U=H^0RHom(Delta,P^2)、積を算出し、Q=ker(Sym^2 V→U)を積分する。まず既存のstabilization模型の有限Homへ戻り、構造写像のどの係数までがV,Uに必要かを特定する。可換勾配空間を入力する補助計算を、非可換圏からの抽出の代用にしない。
4. 公表上の貢献を、完備比較と相対windowの具体的構成、および包括的な一般点復元に絞る。既知の一般原理と本稿の適用条件の対照は監査ノートにある。新たな引用が必要になれば一次資料で範囲を確かめ、同一の定理の初出が判明すれば序論・方針を修正する。
5. 同値核のGalois降下を調べる。E_F=kという方程式の一意性と、rotation付き同値核の降下を分け、まずその自己同値群・自己同型群を同定する。`gcd:ex:forms` は特殊ファイバーも完備化も一致するがK上非同型の例である。TsenによるBrauer群消滅や形式点の存在だけでK'=Kを結論しない。

## 一般原則と保存許可

以下は個別の研究課題と区別した継続原則である。数学的重要性・新規性・理解・応用・正確性・実現可能性を総合し、方針は現在有効な内容へ書き直す。証明済、仮定付き、未完成、予想、有限計算を区別する。誤りがあれば依存先・要約も修正する。必要な証明・例・反例・再現入力を軽量化のために削らず、履歴と重複を整理する。先行研究は一次資料で仮定・適用箇所を確認し、初出未確認は明記する。原稿・ノートは研究の経緯ではなく現在の数学を理解する順に構成する。

本研究はGitHub mainへの節目ごとの保存が継続して許可されており、追加承諾を求めない。保存前に最新mainを確認し、期待する親SHAを指定したfast-forward更新と遠隔ref/blob照合を行う。force push、GitHub Actions、不要なPR、旧版ZIPは作らない。GitHub mainを正本とし、節目ごとの保存に追加承諾は不要とする。現在の利用者指示に従い、研究の区切りでは現行の方針・ノート・原稿・必要な再現資産だけからなる軽量bundleも、承諾を求めずLibraryへ保存する。生成PDF・中間物はGitで追跡しない。Library上の既存ファイルの削除はこの許可に含めない。

## 再現手順

```sh
python3 scripts/check_layout.py
python3 scripts/verify_bundle.py
python3 scripts/build.py --only paper_a
python3 scripts/verify_bundle.py --only paper_a --require-pdfs
python3 computations/verify_equivariant_centering.py
python3 computations/verify_split_cubic_fourfold.py
python3 computations/verify_hesse_translation.py
python3 scripts/build.py --only paper_b
python3 scripts/verify_bundle.py --only paper_b --require-pdfs
python3 computations/verify_complete_curved_transport.py --output build/verify_complete_curved_transport.json
python3 computations/verify_three_object_window.py --output build/verify_three_object_window.json
python3 computations/verify_generic_cubic_descent.py --output build/verify_generic_cubic_descent.json
```

日本語LuaLaTeX、LuaTeX-ja、latexmk、Pythonと `requirements.txt` の依存を用いる。Aの厳密計算は `validation_paper_a.json` のコマンドで再現する。大きな記号行列を扱うスクリプトは一つずつ実行する。PDF・SyncTeX・中間物・再生成可能な出力はbuild/で非追跡。生成、検証、遠隔保存を別の状態として記録し、有限検算を一般定理や圏同値の計算機証明とは報告しない。今回のA改訂ではB-v57と共通preambleを変更していない。
