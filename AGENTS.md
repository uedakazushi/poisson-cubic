# AGENTS.md — nc-cubicの研究継続指示

**2026-11-11 / v27。GitHub mainを正本とする。** 最初に00_research_plan.md、次にnotes/curved_diagonal.md、notes/finite_algebraic_recovery.mdを読む。一般背景はnotes/research_notes.mdとreconstruction/README.md、証明は現行論文A/B/C。旧ZIPや会話を必要としない構成にする。

## 最優先の研究

代数的中心三次対から **実際の低rotation積** を有限代数的に構成し、核の局所飽和とEuler積分により可換三次式を直接抽出する。formalityの特定の無限級数の収束・代数性を先に要求しない。形式MF復元は完成底比較に使う。SM/ERはgeneric圏同値の別経路として保持する。

## 現在の確定範囲

- λ=1の混合非可換入力の曲率付き絶対対角について、すべての高次ホモトピー・閉自己準同型をQ[h]_(h)上で正則に選べる。一般のrref基底をそのまま特殊化しない。
- `computations/regular_diagonal.py` は既存の `absolute_diagonal.py` を継承し、h=0で可逆な小行列による線形持上げを使う。全行の等式を検査する。一般rankが特殊rankと同じだと無検査に推測しない。
- `verify_regular_diagonal.py` は全16合成、H⁰rank4,6、境界と六つの積の小行列式−3、勾配空間との一致を検証する。候補Gは最後の積分検査にのみ使う。
- 有限対角の積は全Artin切断と完備化に両立する。生成元u,x,y,zを用いた核の積分式Gは `curved_diagonal_recovery.tex` と同じ。v³を独立因子として加える。
- 保存行列の係数分母のlcmは(h³−1)(h⁶+162)。これはsmoothness判別式ではない。
- 有限arityのbar同型による共役は有限支持Hochschild cochainsのdg Lie同型を与える。arity上界L_G(L_F+M−1)。これだけでcup積保存を結論しない。

証明全文は `papers/reconstruction/regular_diagonal_recovery.tex`。次元・rankの有限検算はKoszul分解の全次数完全性やPBW性の代用ではない。

## 次の着手

1. 一入力を標識したbar双加群の比較を構成し、有限対角のYoneda積とcompactly supported Hochschild cup積を同定する。内部shiftと周期変数を保持する。
2. 実際の残余dg圏の導来自然変換へ比較する。包絡代数上の第二種理論とtwisted bimodule categoryの理論を区別し、GHLR Theorem6.14/Remark6.16、Polishchuk–Positselski §§3.3,3.5の条件を個別に確認する。
3. 指定生成子の像、generic生成性、有限cone/retractと同値双加群を調べる。全Artinのsmoothness/生成性だけではgenericへ進めない。
4. 一般λの絶対式やh⁶,h⁸係数は比較の検査に必要な範囲で扱う。相対対角はg(u)を検出できず、中心u³係数を相対式から補作しない。

**未証明：** finite diagonal=actual Nat、指定形式Wとの全次数積比較、generic rotation付き圏同値、一般混合残余SM。今回の正則化はこれらを解決したという主張ではない。

## 保持すべき数学

論文Aの一般Poisson正規形と固定方向の代数的量子化、論文Bの17次元族・ambient復元・余次元15・核7、論文Cの形式MF/Artin相対window、二次星積、同変正規形、有限代数的積分、SM/ER、非楕円成分、A∞arity、反例を削除しない。本文に証明があること、今回の点検、計算検証、外部査読・形式証明を区別する。既知結果を新規成果としない。新規性の網羅的調査は未完了。

## 再現と検査

```sh
python3 computations/verify_regular_diagonal.py --output build/regular_diagonal_certificate.json --full-output build/regular_diagonal_full.json
python3 computations/verify_finite_recovery.py --output build/finite_recovery_certificate.json
latexmk papers/curved_diagonal_recovery.tex
python3 scripts/verify_regular_assets.py
```

追跡証明書とJSONの内容を比較する。全行列データのSHA256はcanonical sorted compact UTF-8 JSONについての値。容易に再生成できる全行列を重複して追跡しない。今回の単独原稿は10頁で組版・全頁表示確認済み。A/B/C全体の現行再組版と全旧計算の再実行は未実施。validation.jsonに状態を分離する。

## 保存規則

研究の区切りに承認を求めず、方針・ノート・論文の証明全文・コード・必要な証明書・再現手順をmainへ反映する。新inputとbibliographyも統合する。要約だけのpushを全文保存と呼ばない。remote headを先に確認し、既存変更を保持して通常のfast-forwardのみ。force push・無断PR・GitHub Actionsは禁止。反映後にrefと主要blob SHAを照合する。

GitHub反映が成功した場合はLibraryへ二重保存しない。実際に失敗した場合のみ緊急退避し、未同期を明示する。Libraryの既存ファイルを無断削除しない。

日本語LuaLaTeXを既定にし、latexmkでbuild/へ出力する。PDF・旧ZIP・ログ・cache・旧稿・バックアップをGit追跡しない。数学的内容と再現性を固定容量のため削らない。独立境界研究と原PDFはnc-cubic2、Reye研究はreyeに保全されている。
