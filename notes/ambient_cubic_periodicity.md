# 正則三次超曲面のambient周期性：研究方針とノート

2026-11-12 / v1。本文は `papers/ambient_cubic_periodicity.tex`。このノートはambient周期性に関する小課題の入口であり、プロジェクト全体の研究方針 `00_research_plan.md` を置き換えない。

## 現在の目標と結論

標準多項式型の5次元Koszul AS正則Z代数Bに、次数3の左右正則な正規族 g_i∈B_{i,i+3} があるとき、Bは必ず1周期的である。一般に次元・Gorenstein parameter NのKoszul AS正則Z代数に次数dの正則正規族があれば、最小周期はgcd(N,d)を割る。

証明は原稿の定理1.1・系1.2と第2節。正規性と消去からsigma:B→B(d)、Koszul双対の局所Frobenius対合からrho:B→B(N)を構成する。周期の集合はZの部分群であり、同型の可換性は不要。N=5,d=3ではtheta_ij=rho_{i+1,j+1}^{-1} sigma_{i+3,j+3} sigma_ijが1周期同型である。Veroneseへ移らず元の添字付きB自体を1周期化する。

## 仮定・依存・確認状態

正則正規族の条件はg_i B_{i+d,j+d}=B_ij g_jと左右乗法の単射性である。中心性は仮定しない。AS側は左右AS条件、有限生成射影加群からなる各単純加群の有限最小線型解消、Gorenstein parameter Nを仮定する。単なるquadratic性や低次数Hilbert一致だけからKoszul性を推論しない。

既知入力はBondal–Polishchuk, Homological properties of associative algebras: the method of helices, Russian Acad. Sci. Izv. Math. 42 (1994), 219–260, Proposition 4.1 (pp.234–235), Section 5。
DOI: https://doi.org/10.1070/IM1994v042n02ABEH001536
正規族の定義はChan–Nyman, Noncommutative linear systems and noncommutative elliptic curves, arXiv:2211.12465、著者公開版Definition 8.6 (p.35)。
https://arxiv.org/abs/2211.12465
https://web.maths.unsw.edu.au/~danielch/paper/ncelliptic.pdf

2026-11-12に一次資料の該当箇所を確認し、正規族からの周期同型、Frobenius側の積の保存、添字を合わせた合成を本文で証明した。有限計算・形式検証・外部査読で証明したという意味ではない。既知の一般論からの系として扱い、新規性の最終確認は未了。

LuaLaTeX/latexmkで単独稿を3頁に組版。配布PDFの全頁を表示して確認する。GitにはTeXのみ保存する。

## 低次数で正規性を検出する追加命題

原稿命題3.1：Bが次数一生成、Iが両側イデアル、I_{i,i+3}=kg_i、dim I_{i,i+4}=5、dim B_{i,i+1}=5で、各g_iが左右非零因子なら正規族である。二つの5次元部分空間 B_{i,i+1}g_{i+1} と g_i B_{i+3,i+4} がI_{i,i+4}に入るので一致し、次数一生成から全次数へ延びる。標準cubicのHilbert級数では35−34=1、70−65=5。BがZ-domainなら非零因子性は自動的。この議論はBのAS正則性の代用ではない。

## 残る区別と次の着手

ambientの1周期性は証明済み。一方、今回構成したrhoが三次イデアルIを保つことは未証明として区別する。次はrho(I)=I(5)を調べ、得られればtheta(I)=I(1)と対(B,I)の1周期性へ進む。sigmaはg_iをg_{i+3}へ送ることが消去から既に分かる。

通常のgraded商A=B/(G)への同時降下、Gの中心化、BのCalabi–Yau化はさらに別の主張である。また、任意の抽象的なnc cubic圏が正則正規三次商として表示できることは未証明であり、この結果で置き換えない。nc-cubic2の17次元モジュライ原稿の中心三次対は最初からgradedで、その部分族ではこれらの表示は既知の入力である。一般次元の二次包絡復元は主リポジトリ論文Aに収録した。

一般cubic n-foldでは周期はgcd(n+2,3)を割る。n=2,3では1周期。n=4では1または3が許されるだけで、最小周期3の存在を主張しない。最小周期の区分を既約成分分解と同一視しない。

## 再現

リポジトリrootで `latexmk papers/ambient_cubic_periodicity.tex`。既存 `.latexmkrc` によりLuaLaTeXを使い、PDFは `build/ambient_cubic_periodicity.pdf` に生成される。外部PDF・数値入力・計算証明書は不要。本文の数学的証明が根拠である。

## 常設原則と保存許可

この段落は上の具体的計画と区別した一般原則である。重要性・正確性・新規性・理解・応用・実現可能性を総合して方針を更新し、既知結果、証明済み、仮定付き、未証明、計算的観察を区別する。証明の所在と依存を保ち、誤りがあれば関連する本文・要約・方針を訂正する。公表時は一次資料と先行研究を徹底調査し、新規性未確認を推測で埋めない。

現行の方針・ノート・論文・必要最小限のソースと再現手順を、過去の会話や旧bundleに依存せず再開できる一式として維持する。数学的内容や必要な証明は軽量化のために削除せず、履歴・重複・不要物だけを除く。日本語LuaLaTeXを基本とし、生成・検証・保存の成否を別々に報告する。

ユーザーの常設許可により、研究の節目では承認を求めず保存する。nc-cubicでは最新の個別指定に従いGitHub mainが正本、成功時はLibraryへ二重保存しない。GitHubへの実際の保存失敗時にはLibraryへ緊急保存することが許可されている。既存Libraryファイルの削除は別操作であり明示許可なしに行わない。GitHub Actions、force push、旧版の入れ子ZIP、組版中間物の追跡は行わない。
