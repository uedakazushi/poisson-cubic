# 研究方針：三次超曲面のPoisson幾何

2026-11-25 / v101。再開時は本ファイルを最初に読む。GitHub mainが正本。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。

## 現在の目標と三論文の分担

主公表原稿は `papers/poisson-cubic.tex`（A-v66、日本語LuaLaTeX）。arXiv公開・論文誌投稿を予定し、標準的背景を持つ隣接分野の研究者を読者とする。全次元Poisson正規形を中心に、退化軌跡・Bondal下界・固定および相対Poissonモジュライを扱う。達成基準は、主要定理の仮定から結論までの証明が現行原稿内で閉じ、既知の入力と貢献が具体的に説明され、本文を再生成できることである。作業報告と検証履歴は本文に含めず、研究ノートと検証記録に置く。数学的な仮定・必要な留保・計算証明の再現情報は本文に保持する。

量子化の構成と非可換幾何の比較では対象範囲・仮定が異なるため、公表単位を次の三つに分ける。有効な結果を削らず、各証明と再現資産の正本を一か所に置く。

| 論文 | 正本と役割 |
| --- | --- |
| Poisson幾何 | 本repo `papers/poisson-cubic.tex`。正規形、退化、Bondal、Poisson層・成分、四様体、完全交叉の古典的背景。 |
| 代数的量子化 | [cubic-quantization/papers/cubic-quantization.tex](https://github.com/uedakazushi/cubic-quantization/blob/main/papers/cubic-quantization.tex)。PBW・AS正則性、指定Casimirの代数的中心持上げ、全ブロック・独立パラメータ、同変化・gerbe・Veronese降下、二次包絡によるambient復元。 |
| 非可換幾何とモジュライ | [nc-cubic/papers/nc-cubic.tex](https://github.com/uedakazushi/nc-cubic/blob/main/papers/nc-cubic.tex)。一般中心三次変形の完備MF移送・一般点の可換復元、良い一ブロック型のO-markedモジュライ、残余射・Ku比較と降下障害。 |

論理的な入力は古典的正規形から量子化へ、量子化から非可換比較へ進む。Poisson論文の証明を量子化論文や非可換比較へ依存させない。量子化の多ブロック・全次元の一般性を、非可換モジュライの良い一ブロックという仮定へ狭めない。一般点の比較を全閉パラメータでの同値と読み替えない。

## 主要到達点・仮定・証明の所在

基礎体はC、X=V(F)⊂P(V)は滑らかな三次超曲面、N=dim V=n+2≥5とする。非零Poisson構造はN=3k+m、V=⊕W_s⊕U、dim W_s=3という分解を持つ複数Jacobianブロック正規形に入る。`poisson_geometry.tex` のEuler–Koszul表示、Jacobi恒等式の錐への持上げ、Hessian線形化、`lem:pg-basepoint-free-lie` から `thm:pg-normal` を証明する。非退化形式は三重ベクトルの支持W上で選び、Wに完全かつ中心なしのLie代数を構成する。根基の可換イデアル内のsl₂加群と最高根のベクトルを4変数の恒等式へ代入し、基点自由性から根基と階数2以上の単純因子を排除する。BondalのEuler–divergenceの方法とLie代数の既知定理を用いるが、Derdzinski–Gal Theorem Bの核計算は比較結果として位置づけ、必要な結論は本文で直接証明する。

改稿は `nc-cubic-lean` のcommit `9736787f3a95f52bc3d233ab768a6ab6396d0c24` を参照した通常の数学的証明である。各Leanソースとの対応と対象範囲は `notes/lean_proof_sources.txt` に記す。今回Leanの再ビルド・公理依存監査およびTeX本文の形式検証は行っていない。一般階数・退化スキーム・Bondal下界・固定および相対モジュライは、参照版の幾何学的主定理の形式化された結論には含まれず、本文の証明と文献に依拠する。

`bondal_cubic.tex` は退化軌跡のjoinによる記述と全階数のBondal次元下界を扱う。Fermat型のPoisson零点の非被約構造・横断長さ8^k、零三変数制限が起こる幾何学的条件は `special_poisson_blocks.tex` に保持する。これらは量子中心元の存在とは独立の古典的結論である。

固定三次上のPoissonスキーム、群作用の商、全三次を動かす相対空間を区別する。`poisson_moduli_stacks.tex`、`fermat_relative_poisson_components.tex`、`nonelliptic_poisson_components.tex` がその正本である。相対忘却射は有限型アフィン射であり閉埋め込みではない。階数層は被約構造と(F,P)↦(aF,a⁻¹P)の同時スカラー作用を明示する。Fermatの固定スキームの分割と相対成分数⌊N/3⌋を混同せず、被約階数層の記述から全スキームの被約性を結論しない。

三次四様体の階数四Poisson構造は、二つの滑らかな平面三次の(3,3)分離型F=f+gに限られ、purely elliptic log symplecticとなる。退化因子は正規なjoin、零点スキームは二本の楕円曲線の被約な非交和である。`prop:pg-split-elliptic` は正規形に依存しない直接証明、`cor:pg-cubic-fourfold-elliptic` は分類からの帰結である。Bricalli–Favale–Pirola, Forum Math. Sigma 13 (2025), e80, Theorem 3.4, pp.10–12, DOI 10.1017/fms.2025.36の既知判定により、(3,3)型は周囲P⁵のHessian階数≤3軌跡が平面を含む条件と同値。平面はX内とは限らず、Hessianの可約性だけでは不十分である。`ex:pg-reducible-hessian-no-rank-four` と `computations/verify_hessian_split_obstruction.py` はその障害を与える。

滑らかな超曲面上の非連結中心に対する持上げ障害を `prop:pg-triple-lifting-obstruction` に保持する。全連結成分が正次元・滑らかという条件で、任意の消失次数r≥2についてH¹(I_C^(r−1))=C^(π₀(C))/Cを用いる。持上げる式の次数は超曲面の定義式の次数dに固定する。連結なら障害消滅と一意性、分離型二曲線ではδ(g|X)=[(0,1)]≠0。任意のtwistに同じ群を使う主張ではない。

Pymとの比較は確認済みarXiv:1507.05668v1のDefinition4.2 (p.17)、Theorem1.3 (p.4)、Lemma5.5 (pp.28–29)、Proposition5.7 (p.30)に限定する。同版の非存在記述と上の直接構成は両立せず、非連結曲線について用いられたH¹(I_C)=0が障害となる。刊行版本文・訂正文との照合は未了であり、それらの内容を推測しない。

完全交叉の背景は `complete_intersections.tex` に置く。低twist消滅 `lem:ci-low-twist-vanishing` は穿孔錐とKoszul分解から独立に証明しており、未取得のBrückmann原証明には依存しない。三次元以上の存在判定と既知の二次・二次二本の例を保持する。

以上は原稿に証明がある結果である。既存の読解点検・厳密計算と、今回の改稿ソースの統合・参照確認・組版を区別し、実施した検査の範囲は `validation_paper_a.json` に記す。仮定・文献の確認範囲は `notes/poisson_article_submission_audit.md`、研究上の知識の入口は `notes/research_notes.md`。包括的な新規性・外部査読は未確定である。

## 未解決の核心と次の着手

序論の文献比較では、次元3以上の完全交叉4型、Cerveau–Lins NetoのAnnals論文、訂正済みLPT v3のFano三様体分類、任意次元の対角型・大域分解・log symplectic変形理論を整理した。全次元の先行結果が扱う仮定と、本稿の全ての滑らかな三次・全階数の正規形を区別する。「最初」はこの限定の下での著者の主張であり、包括的な先取権確認は継続する。`poisson-p4` の固定版commit `f118dfbfc5bb9b7a394d1985b4800b6228eebaf6` が主張する147被約既約成分は、人間による検証未了の公開分類案として引用する。一次資料と適用範囲は公表監査ノートに集約する。

1. 公表に先立ち、Pym刊行版またはaccepted manuscriptと訂正を通常の公開経路で入手し、v1との該当箇所を精密に照合する。独立した反例証明は現行原稿にある。未取得資料について結論を先取りしない。
2. Bondal、Derdzinski–Gal、LPT/Mayanskiy、Gualtieri–Pym等との仮定・範囲を比較し、全次元正規形と相対成分定理の初出を引き続き調査する。証明監査は `prop:pg-jacobi-extension`、支持上のLie代数構成、`lem:pg-basepoint-free-lie` とHessian線形化から再開する。Leanの実行・公理依存確認を行う場合は、参照commitを固定して本文の検査とは別に記録する。
3. 固定Poissonスキームの非被約構造と相対の被約階数層を分けて整理し、既存のFermat計算・非楕円ブロック例を一般の局所構造と比較する。詳細な証明・有限証明書は本文と計算資産へ置く。

量子化側の未解決問題（m>0かつk≥2の同変中心元、全hへの延長、中心商の抽象同型・Morita/qgr比較、固定h≠0の同型類像）は [cubic-quantizationの研究方針](https://github.com/uedakazushi/cubic-quantization/blob/main/00_research_plan.md) と [量子化ノート](https://github.com/uedakazushi/cubic-quantization/blob/main/notes/cubic_quantization.md)を正本とする。点ごとの量子化と、全層の同変降下や全パラメータのqgr滑らかさは別の主張である。

## 一般原則と保存許可

以下は上の研究固有の計画と区別した継続原則である。

- 数学的重要性、新規性、理解、応用、正確性、実現可能性を総合し、目標と方針を柔軟に更新する。重要な変更では現在の理由、元の目標の解決部分・残存部分を記し、時系列の変更履歴を蓄積しない。
- 証明済み、追加仮定付き、証明未完成、予想、計算的観察を区別し、仮定・依存結果・証明所在・未解決箇所を記す。既知結果と本研究の成果を分け、新規性未確認を明示する。原稿内の証明、読解点検、計算、形式証明器の実行を区別する。誤りは依存する本文・要約・方針・hubにも反映し、有用な反例はノートへ残す。
- 公表稿の重要な文献は一次資料で確認し、Introductionで仮定・範囲・貢献を具体的に比較する。未確認の内容・書誌は推測せず、必要な参照箇所・識別子・リンクを保存する。外部PDFや検索結果を大量収録しない。
- 方針・ノート・論文と最小限の再現ソース・入力・証明書で自己完結した現行研究一式を作る。論文にある証明全文をノートへ重複せず、着想・反例・障害・再取得困難な情報を整理する。既存の有効な成果と必要な証明を軽量化のために削らない。旧版ZIP・旧稿・履歴・ログ・キャッシュを蓄積せず、過去の会話や旧bundleを再開の前提にしない。
- 主原稿は本文を持つ `papers/poisson-cubic.tex`、日本語LuaLaTeX、著者欄は空欄。新規原稿・設定にはresearch-hubの `papers/paper-template.tex`、`papers/README.md`、`.latexmkrc`、`.vscode/`を参照し、有効な設定を保つ。改名・移動時はinput、文献、root指定、README、方針、ビルドとSyncTeXを揃える。
- GitHub管理前は区切りごとにPDF入りの現行bundleをLibraryへ承諾なく保存する。指定repoへ移行し反映確認後はmainを正本とする。本研究はGitHub段階であり、通常コミットとmainへのfast-forward保存は追加承諾不要。15〜30分を目安に保存し、他の作業者の変更を保持する。force push、Actionsの追加・起動、不要なPRを行わない。Libraryへの定常的な二重保存やZIP作成は不要で、push不能時の緊急保存または明示指示時に限る。既存Libraryファイルを明示指示なしで削除しない。
- 主要文書に日付・版を付け、必要な組版・計算・参照切れを確認する。PDF・中間生成物はGitで追跡しない。生成、証明点検、計算、組版、GitHub反映、Library保存、hub更新は別々に実際の確認状態を報告する。
- 研究の区切りには本repoの原稿・ノート・方針・READMEを先に保存し、最新research-hubを読んで該当項目の到達点・確実性・未解決点・次の一手・依存・正本・資料確認日を更新する。他研究と並行変更を保ち通常コミットでmainに反映する。詳細todo・証明・履歴を重複せず、実質的変化なしの日付のみの更新は行わない。保存とhub更新の成否を別々に確認する。

## 再現手順と検証状態

- `python3 scripts/verify_bundle.py` と `python3 scripts/verify_article_a_numbering.py` で主原稿の入力・ラベル・引用を確認する。Git追跡対象は `python3 scripts/check_layout.py`。
- repoルートで `latexmk papers/poisson-cubic.tex` または `python3 scripts/build.py --only poisson-cubic`。入力は `papers/support/papers/` 以下をルート基準で解決し、PDF・SyncTeXは `build/`。LuaLaTeX・LuaTeX-ja・latexmkが必要。
- 有限計算は `requirements.txt` の依存を用い、`validation_paper_a.json` の対象と実行範囲を参照する。計算資産を移した事実だけを再実行とみなさない。
- 外部論文は閲覧可能なGitHub上の現在の主原稿と定理ラベルで参照し、組版は他repoのaux/PDF取得を要求しない。保存には認証済みGitHub接続を用いる。
