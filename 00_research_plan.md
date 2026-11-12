# 研究方針：論文Aの保持と一般次元の可換復元論文B

**2026-11-13 / v75。最初に読む。GitHub mainが正本。**

## 現在の目的と編集方針

論文Aはnc-cubicに残す。論文Bは任意のn>=3の代数的中心三次変形の一般点可換復元と、その証明に必要な結果に集中させる。新結果の追加ではなく、完全な証明を備えた現行原稿への整理と独立成果の移管を優先する。

現行入口は `papers/paper_a.tex`（A-v51）と `papers/paper_b.tex`（B-v55）。A・Bの本文・入力ソース・共通設定は変更しない。移管先はuedakazushi/nc-cubic2。点スキーム、有限Jacobian復元、一次変形・Plücker障害とそのTodd補正による別証明を独立稿に統合した。全移管は未完了で、残る数学的内容は現行ソースに保持する。

## 論文Bの主結果と証明

R=C[h]_(h)上の次数別有限自由な中心三次対で、特殊ファイバーが多項式環と滑らかな三次式となるものを入力とする。原稿はK=C(h)上の滑らかな三次n次元超曲面と、有限拡大後のrotation・指定三次周期性を保つ全coherent残余圏同値を与える。smooth proper性・有限線束生成、模型の幾何学的一意性、BFK生成上界も保持する。

必要証明は `papers/generic_recovery/` に集約する。`main_result.tex` は主定理と短い証明、`local_model.tex` はnoetherian・Koszul・Gorenstein・線束Hom、`window.tex` は相対stabilizationと三対象、`curved_transport.tex` は完備曲率付き移送と逆、`generic_descent.tex` はEuler非零性・局所化・BFK・有限降下、`coherent_saturation.tex` は全coherentへの拡張、`gradient_recovery.tex` は低rotation積と一意性、`field_model.tex` は基礎体上の方程式、`references.tex` は13文献を収める。

必要な自作証明をnc-cubic2への参照だけで代用しない。任意の抽象的nc cubicの表示、特殊点込み相対同値、同値核のKへの降下、全射影化の可換導来同値は結論しない。証明記載、独立監査、形式検証、外部査読を区別する。

## 論文Aに保持する成果

Aは一般次元のPoisson正規形、退化スキーム、Bondal予想、代数的量子化、固定・相対Poisson moduliを扱う。active偏微分gcd、古典Casimir核、普遍交換子minor、Cramer法による中心元、quadratic envelope・偏極付きambient復元を保持する。Pois(X)、固定商stack、相対stackを区別し、Fermat最大性は未証明。Lie正規形・PBW/AS・普遍中心恒等式等の全独立監査は未完了。知識は `notes/poisson_article_submission_audit.md`、`notes/universal_casimir.md`、`notes/fermat_relative_poisson_components.md` に保持し、今回変更しない。

## 独立成果の現在の所在

**点スキーム**はnc-cubic2の `papers/mixed_cubic_point_schemes.tex`（12頁）。中心式・PBWと4節、文献、4検算コードを統合し、元の専用17ファイルを除外済み。現行ノートは `notes/mixed_cubic_point_schemes.md`。

**有限Jacobian復元**は `papers/cubic_jacobian_recovery.tex`（6頁）。全14数学的環境を保持し、低積・可積分性・一意性・Fermat例・非可積分な完全交差と有理数上の検算を収録。元の専用3ファイルを除外済み。Bの必要証明は `gradient_recovery.tex` に残す。現行ノートは `notes/cubic_jacobian_recovery.md`。

**一次変形・Plücker障害とTodd補正付きHKR**は `papers/cubic_first_order_deformations.tex`（v2、13頁）。元の直接的な一次MF比較とPlücker障害の22ラベル・全数学的環境を保持し、必要な双対数windowを付録に収める。一次消去はN>=5、Plücker二次障害・categorical KSはN=5。Todd補正による別証明は三次三様体の基礎dg圏の一次類を扱い、可換復元の存在やrotation付き全データの自明化を示すものではない。既に存在する可換模型の一次係数に関する系では、純Poisson KSと残余制限の両立を明示的に仮定する。

この別証明は既存の9個の数学的環境・8ラベルを保持して移管し、Jacobian商環をJac(F)に統一、JLLZ著者版の図式の参照番号をTheorem 3.10へ訂正した。移管先の保存確認済み内容コミットは `c98c57a511ad550954ae47ba776e57dff89f08bd`。現行ノートは `notes/cubic_first_order_deformations.md`、検証は `validation_cubic_first_order.json`。元の直接比較本文・2コードに続き、Todd別証明の本文も除外する。共有文献断片は未移管支持節の文献入力のため保持する。一般Artin原稿全体の移管ではなく、`artin_residual_mf_comparison.tex` は保持する。

相対理論、Sklyanin/多ブロック、対角/bar/Morita、混合族の二次jet等はなお残る。`mixed_test_family.tex` とそのコードも保持する。全所在と旧ノートのパスの解釈は `notes/paper_b_scope_and_transfer.md` にまとめる。会話や旧コミットだけを再開の前提にしない。

## 次の作業と達成基準

次は一般Artin・étale相対理論を、双対数の付録では扱わない底変更・形式復元・実現の成果も含めて自立させる。その後Sklyanin/多ブロック、対角/bar/Morita、混合jetを、移管先で同時に進む原稿との重複も照合して整理する。各単位で本文・必要補題・文献・計算を揃え、組版・参照・必要検算・移管先main保存を確認してから元を整理する。Aが読むファイルは移管・削除しない。

短くしたBの全証明の通読と一次資料の仮定照合は別の課題。組版成功を数学的正しさと混同せず、必要証明の省略や未確認文献の引用済み扱いによって短くしない。

## 再現と実施範囲

B-v55は既存.latexmkrcで全文27頁を生成し、11TeX入力・102ラベル・94参照・37引用・13文献を検査済み。全頁表示確認、未解決・重複・overfull・文字欠落0。今回本文は変更せず再組版しない。状態は `validation_paper_b.json`、依存は `notes/generic_recovery.md`。

一次変形統合稿は移管先で `latexmk -g -r .latexmkrc papers/cubic_first_order_deformations.tex` と `python scripts/check_cubic_first_order.py` を実行した。6TeX入力・36ラベル・32参照・20引用・9文献、未解決・重複・overfull・文字欠落0、全13頁表示確認。既存2コードの8挿入恒等式、Jacobian次数3 rank25/36、JacobiとPlücker span rank5等は既実行の結果として保持し、この更新ではコードを変更・再実行していない。Toddの証明はコホモロジーの議論で、新しい有限計算を証明の代用にしない。

Aの再組版、全既存計算、全数学的証明の独立監査は今回行っていない。PDF・中間物はbuild/で非追跡。

## 研究一般の原則と保存許可

以下は研究固有の計画とは別の常設原則。

1. 重要性・新規性・理解・応用・正確性・実現可能性を総合して価値を最大化し、方針変更は現時点の理由と解決・未解決の境界として整理する。履歴を蓄積しない。
2. 証明済み、追加仮定付き、未完成、予想、計算的観察を区別し、仮定・依存・証明所在と記載・監査・検算を明記する。誤りなら依存する本文・要約・方針も訂正する。
3. 公表稿は一次資料を確認し、既知結果との関係を示す。文献・新規性を推測で補わず、外部PDFを大量収録しない。
4. 有効な成果と十分な証明を日本語LuaLaTeXで現在の論理順に保持し、軽量化のために数学的内容を削らない。
5. ノートは現在有効な着想・計算・反例・障害・文献比較をまとめ、会話・日誌・重複証明を蓄積しない。
6. 現行方針・ノート・論文・必要資産だけから再開できるようにし、旧ZIPや過去会話を前提にしない。
7. 履歴・重複・cacheを除き、検証可能性を固定容量のために削らない。必要な証明書・入力・再現手順を保持する。
8. 保存許可により区切りで承諾を求めずGitHub mainへfast-forward保存し遠隔ref/blobを確認する。Actions・force pushは禁止。Libraryは実際のpush失敗時のみ緊急退避し、既存Libraryを無断削除しない。生成・検算・組版・保存を分けて報告する。
