# 研究方針：論文Aの保持と一般次元の可換復元論文B

**2026-11-13 / v78。再開時は最初に読む。GitHub mainが正本。**

## 現在の目的と達成基準

論文A `papers/paper_a.tex`（A-v51）はnc-cubicに残す。論文B `papers/paper_b.tex`（B-v55）は任意のn>=3に対する代数的中心三次変形の一般点可換復元と必要な証明に集中する。現在のCodex担当は、新しい結果の追加ではなく、分離した既存成果をnc-cubic2の自立した現行原稿へ統合すること。**並行するChat担当**は論文AのPoisson正規形・量子化の独立監査、論文Bの完備MF比較・一般点降下の独立監査と改良、両論文の一次文献・新規性の精査を行う。CodexはA・Bの本文・直接および再帰的入力・共通設定を変更せず、数学的な問題を発見した場合はノートに明記して引き継ぐ。

必要な定理・証明・反例・文献・コードを移管先に揃え、参照・全文組版・必要な検算・main保存を確認する。その後、元側に残る依存を整理して重複を除く。独立稿の整備と、元ソースを安全に削除できることは別の状態として扱う。

## 論文Bの主結果と必要証明

R=C[h]_(h)上の次数別有限自由な中心三次対で、特殊ファイバーが多項式環と滑らかな三次式になるものを入力とする。現行稿はK=C(h)上の滑らかな三次n次元超曲面と、有限拡大後のrotation・指定三次周期性を保つ全coherent残余圏同値を述べる。smooth proper性、有限線束生成、幾何学的一意性、BFK生成上界も保持する。

証明は `papers/generic_recovery/` の現行9ファイルに収録する。`main_result.tex` は主定理と短い証明、`local_model.tex` はnoetherian・Koszul・Gorenstein・線束Hom、`window.tex` は相対stabilizationと三対象、`curved_transport.tex` は完備曲率付き移送と逆、`generic_descent.tex` はEuler非零性・局所化・BFK・有限降下、`coherent_saturation.tex` は全coherentへの拡張、`gradient_recovery.tex` は低rotation積と一意性、`field_model.tex` は基礎体上の方程式、`references.tex` は13文献。

必要な自作証明を移管先への参照だけで代用しない。任意の抽象的nc cubicの表示、特殊点込み相対同値、同値核のKへの降下、全射影化の可換導来同値は結論しない。証明記載、全独立監査、形式検証、外部査読を区別する。

## 論文Aに保持する成果

Aは一般次元のPoisson正規形、退化スキーム、Bondal予想、代数的量子化、固定・相対Poisson moduliを扱う。active偏微分gcd、古典Casimir核、普遍交換子minor、Cramer法による中心元、quadratic envelope・偏極付きambient復元を保持する。Pois(X)、固定商stack、相対stackを区別し、Fermat最大性は未証明。Lie正規形・PBW/AS・普遍中心恒等式などの全独立監査は未完了。研究上の知識は `notes/poisson_article_submission_audit.md`、`notes/universal_casimir.md`、`notes/fermat_relative_poisson_components.md` に保持する。

## 独立成果の現行分担

以下の入口、対応ノート、validationファイルはnc-cubic2の現行mainにある。

- `papers/mixed_cubic_point_schemes.tex`：12頁。混合中心式・PBW、点加群の台と厚化、平坦閉包と判別式。必要4検算を保持し、元の専用17ファイルを整理済み。
- `papers/cubic_jacobian_recovery.tex`：6頁。低積、有限可積分性、一意性、Fermat例、非可積分な完全交差。全14数学的環境を保持し、元の専用3ファイルを整理済み。主定理に必要な低次数同定と一意性はBにも残す。
- `papers/cubic_first_order_deformations.tex`：v2、13頁。直接的な一次MF比較・Plücker障害・categorical KS、双対数window付録、Todd補正付きHKR。直接比較の22ラベルとToddの9数学的環境・8ラベルを保持する。一次消去はN>=5、Plücker・categorical KS・ToddはN=5。専用本文・2コードとTodd本文の計4ファイルを整理済み。既に存在する可換模型の一次係数を消すことと模型の存在を区別する。
- `papers/cubic_artin_windows.tex`：一変数の全有限切断R_N=C[h]/h^(N+1)、d>=5変数での線束残余/MF比較、正則局所模型からの底変更、完備基底で生成性とsmoothnessを失う反例。任意の局所Artin環の定理ではない。比較主部17ラベルと必要証明を保持する。元末尾の `am:cor:formal-residual` の全次数MF存在を仮定した結論は元に残し、`ar:cor:conditional` に弱めて置換しない。独立稿は保存済みだがam:*依存と元重複の整理は未完了。
- **`papers/relative_cubic_realization.tex`：v2、10頁。今回main保存を完了。** 実在するsmooth properな自己同値付き代数的dg族のétale局所実現、任意のn>=3のcubicへの適用、Hochschild sectorとArtin切断の限界。主étale節は元のTeXとバイト一致。有限Artin稿と反例の証明を `papers/artin_windows/artin_smoothness_obstruction.tex` の一ファイルで共用し、二つの外部文脈参照だけを整理した。新しい結果は追加しない。ノートは `notes/relative_cubic_realization.md`、検証は `validation_relative_cubic_realization.json`。保存確認済み内容コミットは `68aa33d243d6541531c2ff2c8b2c1c5f60637215`。

étale稿は相対smooth proper性を仮定し、次数別flatnessだけからこれを導くものではない。自己同値一つとintertwinerを指定し、rho^3≃[2]という選択や群作用coherenceは別のデータとする。一般点のBと入力の水準を混同しない。

**今回は元側の数学的ソースを削除していない。** `rotation_saturation_reduction.tex` などがer:*、その他の未移管節がam/ho/asを参照する。独立稿の自足性だけでこれらの依存を解消したとは扱わない。全所在と必要な依存整理は `notes/paper_b_scope_and_transfer.md` を参照する。広い形式復元、Sklyanin/多ブロック、対角/bar/Morita、混合jetの移管は未完了。

## 次の具体的作業

**Codexの責務は移管（以下）、Chatの責務はA・Bの数学的監査・証明改良・先行研究調査。** Codexは両repoの最新mainを確認し、移管先の既存成果との統合、必要な検証、移管先main保存、元側の参照閉包とA・B保護の確認、元側mainでの重複削除という順序を守る。具体的な実行・削除ゲートは `AGENTS.md` に定める。

次は元の `relative_formal_models.tex` と `relative_etale_models.tex` の形式持上げ・同値スタック・smoothnessの入力を、保存済みのArtin稿とétale稿へ接続する。元のArtin末尾の形式復元系を必要な全次数存在証明とともに統合し、mixed/formal等のam参照、rotation_saturation_reductionのer参照を整理してから元重複を除く。現在の独立稿の仮定を弱めず、必要証明を未公表外部リンクだけで済ませない。

続いてSklyanin/多ブロック、対角/bar/Morita、混合jetを、移管先の同時作業との重複を照合して統合する。Aが読むファイルは移管・削除しない。Bの全証明の通読と一次文献の仮定照合は別の課題として保持する。

## 再現と今回の実施範囲

B-v55は既存の全文27頁の組版・表示確認、11TeX入力・102ラベル・94参照・37引用・13文献、未解決・重複・文字欠落・overfull0という記録を保持する。今回その本文は変更せず再組版しない。状態は `validation_paper_b.json`、依存は `notes/generic_recovery.md`。

étale稿は現行ソースで `python3 scripts/check_relative_cubic_realization.py --calculations --build` を実行。6TeX入力・29ラベル・24参照・16引用・9文献、10頁、未解決・重複・文字欠落・overfull0、全頁表示確認済み。N=5,...,60の整数次数検算を再実行し、元の証明書blob8e7a35337e43b45fc26b04c11414554732213ea4と完全一致した。引用したBFK公式そのものや圏論的議論の形式検証ではない。

有限Artin稿の過去の13頁組版とQQ[h]上の64結合律・16Leibniz則・8単位条件、d²、一般/特殊cohomologyと6有限切断のrank検算は記録として保持する。ただし共用反例の二つの参照を整理した後のArtin稿全文は今回再組版していない。その未実施と、現行共有ファイルを使ったétale稿の組版成功を移管先のvalidationで区別した。

Aの再組版、全既存検算、全数学的証明の独立監査は今回行っていない。PDF・中間物・容易に再生成できる出力はbuild/で非追跡。

## 研究一般の原則と保存許可

以下は研究固有の計画と区別する常設原則である。

1. 重要性・新規性・理解・応用・正確性・実現可能性を総合して価値を最大化する。変更は現時点の理由と解決・未解決の境界として整理し、履歴を蓄積しない。
2. 証明済み、仮定付き、未完成、予想、計算的観察を区別する。仮定・依存・証明所在と記載・監査・検算の差を明示し、誤りなら依存する本文・要約・方針も訂正する。
3. 一次資料を確認し既知結果との関係を示す。文献や新規性を推測で補わず、外部PDFを大量収録しない。
4. 有効な成果と十分な証明を日本語LuaLaTeXで現在の論理順に保持し、軽量化のために数学的内容を削らない。
5. ノートは現在有効な着想・計算・反例・障害・文献比較をまとめ、会話・日誌・重複証明を蓄積しない。
6. 現行方針・ノート・論文・必要資産だけから再開できる一式を保ち、旧ZIPや過去会話を前提にしない。
7. 履歴・重複・cacheを除き、固定容量のために検証可能性を削らない。不可欠な入力・証明書・再現手順を保持する。
8. 保存許可に従い区切りで承諾を求めずmainへfast-forward保存し遠隔ref/blobを確認する。Actions・force pushは禁止。Libraryは実際のpush失敗時のみ緊急退避し、既存Libraryを無断削除しない。生成・検算・組版・保存を分けて報告する。
