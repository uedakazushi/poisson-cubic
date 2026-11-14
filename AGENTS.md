# Codex実行指示 — nc-cubic

2026-11-14 / v93。最初に `00_research_plan.md` と `notes/paper_b_scope_and_transfer.md` を読む。GitHub mainが正本。

## 公表向け監査と担当境界

論文AはA-v60。添付の独立査読報告（対象f4c8fb131f346099ed2fb8af29429574861b505e）に基づき、既知結果との差分、Pymとの比較範囲、証明の順序と記号を整理した。中心成果は全次元正規形であり、Lie代数の根基排除を `lem:pg-basepoint-free-lie` として独立させた。EG Theorem 3.3.2(ii)の一ブロック中心元存在、Proposition 8.1.1(i)の所定古典剰余を持つ形式中心元（相対係数・還元群への対応を含む）、§9のRains公式は既知である。Proposition 8.1.1(i)に孤立特異点仮定はない。Hesse混合項はt可逆なら平行移動でその表示へ移る。本稿の追加を指定Casimirへの規格化、係数環上の正則な選択、全ブロック・独立パラメータ・同変降下として記述する。

本文順は、正規形と幾何→固定・相対モジュライ→一ブロックのPBW・中心元→全ブロック→同変化・降下→例。`quantization_foundations.tex`、`algebraic_quantization.tex`、`special_poisson_blocks.tex` が旧一体節の現行支持ファイルである。ambientはA、中心商はBに統一し、ambient復元と完全交叉背景は付録に置く。既存の主定理・必要証明・仮定は保持する。

非連結中心Cに沿う任意のr>=2重消失の持上げは `prop:pg-triple-lifting-obstruction` で独立に証明し、全連結成分正次元・滑らかという条件の下でH¹(I_C^{r−1})=C^{π₀(C)}/Cを得る。持上げ次数は超曲面の定義式の次数dに固定する。分離型では障害δ(g|X)=[(0,1)]が非零。Pymとの比較は確認したarXiv v1の番号・頁に固定し、刊行版本文・関連訂正文は未照合である。未取得資料の内容や包括的な初出を推測しない。

三次四様体ではrank4 Poissonの存在、(3,3)分離型、ambient P⁵のHessian rank<=3軌跡が平面を含む条件が同値である。後二者の同値はBricalli–Favale–Pirola (2025), Theorem 3.4を引用し、Poissonとの同値は本稿の正規形に依存する。Hessianの可約性だけでrank4を結論しない。`ex:pg-reducible-hessian-no-rank-four` と `verify_hessian_split_obstruction.py` が具体的障害を与える。

現行の仮定・証明所在・文献比較は `notes/poisson_article_submission_audit.md`、実行確認は `validation_paper_a.json` に集約する。相対忘却射のアフィン性、被約rank層、中心核と通常の中心の違い、Ω'=aΩ+cによるイデアルの不一致、複数ブロックの一般の同変構成と中心商の比較の未解決性を保持する。17は構成した底の次元であり、固定h≠0の非可換同型類の像の次元ではない。Bの一般点復元と全閉パラメータでの相対同値を混同しない。

論文BはB-v59。添付の独立査読報告に基づき、完備曲率移送を序論の独立した中心定理として述べ、window・dg商・余核・totalization・mutationを一つの比較図式へ集約した。指定三次周期は二拡張のYoneda類からrotation正方形まで追跡する。arity評価はMF行列を挿入する前のbar写像に対するものであり、挿入後のMF関手の偶数Taylor成分の消滅と混同しない。

Pirozhkov Theorem 1.2の三次の場合はn>3と明記し、Lin--Zhangの低積・Torelliとの関係を整理した。EGは既に有限rank graded MFを扱い、CKは第二種変形複体を比較する。本稿の追加は一般入力・完備実関手・指定周期・一般点降下・全coherentへの接続である。一般的なformality、BFKの上界、Jacobian Torelliを新しい結果に数えない。包括的な初出は未確定である。

`explicit_example.tex` のHesse--Sklyanin族はAの一般量子化定理に依存しない。既知Sklyanin理論とDVRの構造定理で全次数の自由性を示す。生成元を固定するharmonic-angle比較の二次jetは W_rec=F+h xyz+(h²/3)xyz+O(h³) であり、全次数のHesse係数は λ=(h+h²/3+h⁵/12)/(1−h⁴/4)。K上の模型は (4−h⁴)(x³+y³+z³+u³+v³)+(12h+4h²+h⁵)xyz=0 と確定した。相対THCR、a=0のdg Orlov比較、properなPerf模型の底変更と楕円曲線の同定が証明を支える。三変数ではOを例外対象と扱わず、N>=5の正のaのwindow定理をそのまま流用しない。生の点スキーム方程式の共通因子h、G=−9hΩの規格化、Weyl gaugeと中心写像の同時変更を保持する。同値核の行列・拡大次数・直接抽出した低rotation積の全行列は未計算。

主定理の存在結論と仮定は保持する。方程式のK降下、核の有限拡大K'上の存在、幾何学的一意性、K-form、線束部分と全coherent圏、通常の局所化とtorsion Moritaの区別は `gdr:subsec:scope` に集約した。固定勾配空間の積分は有限étale代数E_Fで記述し、E_F=kなら方程式は基礎体上でスカラー倍まで一意。ただし同値核のKへの降下は未解決。現在の確認範囲と再現は `notes/paper_b_proof_audit.md` と `validation_paper_b.json` を参照する。

### 完了した移管

論文Bから独立した現行成果の移管は完了。nc-cubic2の `papers/relative_reconstruction_models.tex` と既存五稿、専用ノート・validation・manifestが正本。完了した専用ソースを再導入しない。移管先の既存研究や別担当の更新を上書きしない。

Chat側の担当はAのPoisson正規形・量子化、Bの完備MF比較・一般点降下、一次文献・新規性の独立監査と改良。Codexの新しい主担当は **nc-cubic2の統合稿の公表向け再構成と、移管で文脈調整された9数学的環境・共有証明の重点監査** である。Codexは本リポジトリのA/B・再帰入力を編集せず、必要な数学的指摘は根拠と参照を付して伝える。ファイル移管のやり直しをしない。移管完了と全数学的監査の完了を混同しない。

### 同変中心元の現在の範囲

階数二の全supportでの共変中心元は `intrinsic_rank_two_center.tex` に証明した。古典核 OF⊕Sym³Q* のH¹消滅、h冪厚化の逐次持上げ、Stiefel開の正則関数のSL3不変式環への延長、有限核の完備化の完全性を用いる。Khat/h³Khat=K/h³Kによって指定普遍Hessian二次jetを代数的に持ち上げ、全GL_N×Gmの平均化を行う。形式級数全体の代数性を主張するものではない。gcd(N,3)=1なら全被約rank2 Poisson層×h直線の零切断近傍へ実際の代数族が降り、N=5では全非零Poisson対を扱う。三次Veronese A_(3d)⊗λ^d は全Nで降下する。Pic(S_N)=0と重みの像gcd(N,3)Zからgerbeの位数はgcd(N,3)であり、3|Nでは重み±1の可逆層による次数一の補正は不可能。N>=6では零制限標準中心直線への全support一致も二次jetの相対H¹障害で不可能である。zero Poisson、全h、一意性、商の抽象非同型やqgr非同値は結論しない。全係数・η,hを使っても補空間の正則同変選択は不可能で、自由なU商も非アフィンである。次は複数ブロックの整合と、三次偏極の族に対する別ambient・Morita/qgr比較を調べる。CMRの節点中心公式は既知の入力として明記し、独立検算 `verify_cmr_nodal_center.py` は一般係数での中心性・規格化・安定化群共変性を扱う。

以下は保持している各層の明示的構成であり、全supportの存在証明とは区別する。

Aの同変性では、全滑らかなfでG_0=(GL3×GLm)×Gmに関する平均化を完了し、滑らかなg=f(x,0)では混合二次項の中心調整により全ブロック群Gへ拡張した。g=0では既知のPBW対称化の随伴同変性によりΩ=sym(f)が全tにわたり全G共変で、純中心係数の固定とも両立する。零制限の滑らかな層はm>=3でのみ非空であり、P(W_P)⊂Xの条件に対応する。gcd(m,3)=1ならθ=(det N)^rλ^s、mr−3s=1によって次数線形化を補正し、滑らかなgの層では零切断近傍へ、零制限の層では全h直線の積へ中心商族を降ろせる。三次三様体m=2では底が17次元となるが、固定h≠0の非可換代数の同型類の像の次元を結論しない。節点・尖点の各軌道でも安定化群同変なδ_gの左逆を移送して全G同変性を得た。一意な特異点直線ℓ_gは引戻しdatumで重み−1なので、A_d⊗ℓ_g^dにより全mで実際のPoisson層へ降下する。各層はrank2内の余次元1,2、n=3で16,15次元である。全hではなく零h切断近傍の結論であり、零制限標準中心直線への全層での一致はN>=6で不可能であり、節点・尖点公式との比較は別に残る。不可約全域の単一のδ_g依存左逆は余次元2の延長障害で存在せず、接線＋conicの一軌道にも非分裂がある。複数ブロックの分解・配分の一般の整合、既存中心商の抽象的比較、三次偏極からの別ambient表示は残る。零制限以外で全平行移動との同変性を課すときに純中心係数固定を無条件に再導入しない。補正前の中心Gm-gerbeと、補正後のPoissonモジュライ上の族を区別する。詳細は `papers/support/papers/sections/equivariant_central_lifts.tex` と `notes/universal_casimir.md`。

## 厳格な保護

- 移管整理では `papers/paper_a.tex`（A-v60）、`papers/paper_b.tex`（B-v59）、両者の再帰的な全入力、`papers/generic_recovery/`、`papers/support/papers/common.tex`、共通設定を保護する。ユーザーが依頼した公表向け監査によるA/Bの修正はこの移管保護とは区別する。本A-v60改訂ではB-v59の全入力・専用検証記録と共通preambleを保持する。必要証明を移管先へのリンクだけで代用しない。
- パスだけで移管可否を決めず、input/include・論理参照・引用・ノート・コードの実依存を確認する。共有する文献・証明書・検算を消さない。
- 数学的問題は具体的な仮定・反例・依存先とともに監査ノートへ記し、主定理を迂回して強化・弱化しない。
- 全次数MF存在と条件付き移送、全coherentと線束生成圏、有限Artinと一般Artin、形式と代数的同値、相対smooth properの仮定を区別する。

## 検証と保存

変更前・push前に最新mainを取得する。通常のfast-forward pushと遠隔ref/blob確認を行い、force push・Actions・不要なPR・旧版ZIP・バックアップ複製を作らない。生成PDF・中間物はbuild/で非追跡。GitHub mainを正本とし、節目ごとの保存に追加承諾は不要とする。現在の利用者指示に従い、研究の区切りでは現行の方針・ノート・原稿・必要な再現資産だけからなる軽量bundleも、承諾を求めずLibraryへ保存する。生成PDF・中間物はGitで追跡しない。Library上の既存ファイルの削除はこの許可に含めない。

重要な証明・例・反例・書誌・再現入力を落とさず、移管先へ統合して参照・必要な全文組版・厳密計算・保存を確認してから元の真の重複を除く。旧ZIP・旧PDF・旧コミットを現行証明の代用にしない。有限体での零を特性零の恒等式の証明と混同しない。証明記載・有限検算・独立監査・形式検証・新規性を区別する。

日本語LuaLaTeXと現行.latexmkrcを使い、研究方針・現在有効なノート・必要最小限のvalidationを更新する。数学的重要性・正確性・理解・応用・実現可能性を重視し、歴史ログや重複した論文を増やさない。
