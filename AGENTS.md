# AGENTS.md — nc-cubic研究継続

**2026-11-11 / v31。GitHub mainを唯一の正本とする。** 00_research_plan.md、notes/bar_comparison.md、notes/curved_diagonal.md、notes/finite_algebraic_recovery.mdの順に読む。一般背景はnotes/research_notes.md、reconstruction/README.md、証明は現行論文A/B/C。旧ZIPや会話を再開条件にしない。

## v31：導来Natの隣接障害と生成性の訂正

体上の五変数三次のNat（cohomological次数−1,0,1）の階数は内部shift r=1で(0,5,2)、r=2で(0,10,0)。真の標的導来bar cochainが項別flatかつ剰余に厳密整合すれば、r=2はH0が全Artin自由rank10。r=1の一次障害はk^5→k^2の2×5行列であり高次も別検証。非可換Nat計算は未実施。**重要な訂正：** 特殊Morita生成子とHom項別自由性だけでArtin生成性を推論するv29の補題は偽。二周期複体による反例をartin_rotation_obstructions.texに記載。導来二側bar評価の正しいcofibrant模型・特殊化を独立の入力とする。KF/BCとgeneric同値は未証明。

## 最優先

代数的中心三次対から実際の低rotation積を有限代数的に構成し、核の局所飽和とEuler積分で可換式を直接抽出する。特定のformality級数の収束・代数性を先に要求しない。形式MF復元は完成底比較に使い、SM/ERはgeneric圏同値の別経路として保持する。

## 現在使えること

- lambda=1の曲率付き絶対対角はQ[h]_(h)で正則。regular_diagonal.pyはabsolute_diagonal.pyを継承し、単元小行列で持上げ、全行を検査する。一般rref基底を無条件に特殊化しない。
- verify_regular_diagonal.pyは全16合成、H^0 rank4,6、境界と六積の小行列式-3、勾配空間を検査する。有限対角の積は全Artin底変更と完備化に両立。候補Gは最後の比較にのみ使う。分母lcm(h^3-1)(h^6+162)は圏のsmoothness判別式ではない。
- multiplicative_bar_comparison.texは同次分裂bar比較を入力に、有限対角Yoneda積=有限支持Hochschild cup積を証明する。Q(a)=epsilon_P a Pi、Jの乗法性の差は-d(Pi R_phi H R_psi I)。有限arity dg Lie共役だけでcup保存を結論しない。
- 有限支持brace挿入はMFの内部shift付き導来自然変換への乗法的Thetaを与える。r=1,2に必要なarityは<=2,4。**写像の構成と同型性を区別する。**
- 計算済みlambda=1候補は四本の代数方程式、初期Jacobian9で正規化でき、L=1+127q/5184+O(q^2)、C=13/36+1613q/1679616+O(q^2)、q=h^6。これを未確認の形式Wの係数と同定しない。

## v29：相対Artin sector（証明と未解決の区別）

可換形式五変数cubicの勾配Koszulは任意のArtin切断で正のホモロジー零、Jac(W_m)は次数別自由で一次・二次rank5,10。μ3非恒等sectorは奇数parity。項別平坦な複体の擬同型は特殊化で検出できる。以上の証明は`papers/reconstruction/relative_artin_sector.tex`に保持する。

**(KF)を未確認の核心条件として維持する。** 相対stabilized diagonalのkernel畳込みを指定graded MFの同一enhancementで構成し、特殊化が体上BFK kernel比較と一致することを符号・内部shift込みで示す。これは実際のNatとrotation積の無条件同定ではない。検算は`computations/verify_artin_sectors.py`と証明書（Jacobianの有限計算のみ）。研究ノートは`notes/relative_artin_sector.md`。

## 相対対角のunitと残るderived bar

**相対対角のunit（v31、証明あり）。** 任意の可換基底環の斉次三次式に対する差分商stabilized diagonalの畳込みは、有限自由graded MFへ自然な強ホモトピー同値を与える。Koszul収縮h0と摂動pについて(h0p)^(n+1)=0なので、逆とホモトピーは有限和であり、全Artin底変更・内部shift・mu3スカラー作用と両立する。原稿：`papers/reconstruction/diagonal_kernel_identity.tex`、計算：`computations/verify_diagonal_identity.py`（厳密恒等式606件）。**(KF)の全忠実性は未完成。** k[epsilon]/epsilon²上の両側無限自由周期複体は非輪状でもK-flatでない。相対cofibrant/h-projectiveな二側bar模型とBFK体上比較への同一enhancementでの特殊化を次に検証する。

## 次の着手と禁止する飛躍

第一優先は標的の(BC)：全Artin底で実際のNat(Id,(1)),Nat(Id,(2))が自由rank5,10、自然なH^0剰余同型を持ちThetaと両立すること。形式MF同値で可換形式cubicへ移し、相対対角kernel/sectorを構成する。gradient Koszulの相対完全性と非恒等sectorの次数を確認する。体上の次元公式、導来Hom底変更、sourceの局所自由性だけで(BC)を証明済みにしない。

(BC)なら特殊fiberのJacobian同定と単元行列式でTheta_1,Theta_2は同型になる。この条件付き判定と既存Artin残余比較を合成できるが、**本族の(BC)、指定形式Wとの全次数比較、generic rotation圏同値、一般混合SMは未証明**。GHLRの包絡代数とtwisted bimoduleの二つの第二種理論の仮定も混同しない。

genericでは指定生成子の像、有限cone/retract、代数的同値双加群が必要。全Artinのsmoothness/生成性だけでgenericへ進めない。一般lambda、lambda^3=-12の高次項は比較に役立つ範囲で扱う。相対対角はg(u)を検出できないためu^3係数を補作しない。

## 保持・検証

AのPoisson正規形/固定方向量子化、Bの17次元族・ambient復元・余次元15・核7、Cの形式MF/Artin window、二次星積、同変正規形、有限代数的積分、SM/ER、非楕円成分、A∞arity、反例を削除しない。証明記載・今回の点検・有限計算・外部査読/形式証明を区別する。既知cap/HPL/brace原理を新規成果と呼ばない。包括的新規性調査は未完了。

```sh
python3 computations/verify_bar_comparison.py --output build/bar_comparison_certificate.json
python3 computations/verify_finite_recovery.py --output build/finite_recovery_certificate.json
latexmk papers/multiplicative_bar_comparison.tex
python3 scripts/verify_bar_assets.py
```

新しい計算は有限テスト代数・ホモトピー符号・候補の代数正規化の検証であり、categorical Natやv27全行列を検証しない。既存verify_regular_diagonal.pyとverify_regular_assets.pyを保持する。全行列はcanonical JSON SHA256と生成コードで再現し、不要な重複出力をGitへ追加しない。A/B/C現行全体の組版は今回未実施。詳細はvalidation.json。

## 保存

区切りごとに承認を求めず、方針・ノート・論文の証明全文・コード・証明書・再現手順をmainへ反映する。新input/bibliographyも統合し、要約だけのpushを全文保存と呼ばない。remote headと既存変更を保持したfast-forwardのみ。force push・無断PR・GitHub Actions禁止。反映後refと主要blob SHAを照合する。

成功時はLibraryへ二重保存せず、実際のGitHub失敗時のみ緊急退避する。未同期を明記しLibrary既存ファイルは無断削除しない。日本語LuaLaTeX、latexmkでbuild/出力、PDF・旧ZIP・ログ・cache・バックアップはGit追跡しない。数学と再現性を固定容量制限のため削らない。独立境界研究/原PDFはnc-cubic2、Reyeはreyeに保全。
