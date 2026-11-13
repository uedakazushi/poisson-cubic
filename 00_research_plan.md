# 研究方針：中心三次変形の量子化と一般点可換復元

2026-11-13 / v81。再開時は本ファイルを最初に読む。GitHub mainが正本。

## 現在の目標と達成基準

論文A `papers/paper_a.tex`（A-v51）は一般次元のPoisson幾何・代数的量子化・ambient復元を扱う。論文B `papers/paper_b.tex`（B-v56）は、次数別有限自由な代数的中心三次変形の一般点可換復元を扱う。公表の達成基準は、主要定理の仮定から結論までの証明が現行原稿内で閉じ、使用する既知定理の適用範囲と新規性が具体的に説明され、全文を再生成できることである。

Bでは n>=3、R=C[h]_(h)、K=C(h) とし、A_R/hA_R が N=n+2 変数多項式環、中心三次元の剰余が滑らかな三次式であることを仮定する。可換方程式はK上、全coherent残余圏のrotation・指定三次周期付き同値はある有限拡大上に構成する。模型の一意性はrotation付きpairを実現する模型の幾何学的射影同型類についてである。K上のformの一意性・同値核のKへの降下・特殊点を含む代数的相対同値は結論に含めない。

## 到達点と証明の所在

Bの証明は `papers/generic_recovery/` だけで完結する。`local_model.tex` と `window.tex` が局所proper模型と三対象window、`curved_transport.tex` が実際の完備A_infty比較、`generic_descent.tex` がEuler非消滅・BFK生成・有限降下、`coherent_saturation.tex` が全coherent圏への飽和、`gradient_recovery.tex` と `field_model.tex` が勾配空間の積分と方程式の基礎体降下を与える。

B-v56ではこの証明連鎖を数学的に再点検した。対称積の核という定義、rotation付き一意性の範囲、降下核と随伴coneのperfect性、残余成分のadmissibility、graded stabilizationの構成、曲率移送が有限rank MFを保つ次数を本文に明記した。主定理の入力への追加仮定や、一般点の存在結論の撤回を要する問題は今回の点検では見つかっていない。これはLean等の形式検証・外部査読・包括的新規性確認とは異なる。正確な監査範囲は `notes/paper_b_proof_audit.md`、組版・有限検算の実行状態は `validation_paper_b.json` を参照する。

Carqueville--Kayの曲率付きformalityと、Etingof--Ginzburgの非可換楕円特異点のMF同値を序論で比較する。BFKの生成定理およびLin--Zhangのrotation付きTorelliは既知の入力であり、本研究の新規定理とは扱わない。比較構成・代数的一般点降下を組み合わせた結論の初出はなお未確定である。

独立な点スキーム・Jacobian・一次変形・Artin・étale・相対模型の成果はnc-cubic2へ移管済みである。現在の入口は `notes/paper_b_scope_and_transfer.md`。Bの必要証明を移管先へのリンクだけで代用しない。

## 優先する次の課題

1. 公表前の新規性比較を詰める。まずCarqueville--Kay Theorem 3.1 / Proposition 3.4の第二種Hochschild変形問題と、本稿の実際のgraded MF同値・指定周期・代数的一般点の全coherent残余圏の結論を対照する。主結果の説明はその差分に合わせ、一般的なcurved formalityの初出を主張しない。
2. Bの存在定理を具体的入力で有効化する。非可換入力から V=H^0RHom(Delta,P)、U=H^0RHom(Delta,P^2)、対称積を計算し、Q=ker(Sym^2 V→U)を積分する。既知の可換勾配空間を入力する補助計算と、実際の非可換圏からの抽出を区別する。
3. 有限拡大の必要性・次数と同値核の明示式を検討する。基礎体上で同じ勾配空間を持つ異なるformの例は `gcd:ex:forms`。この例だけを核の降下障害の例とは扱わない。
4. Aは専用監査ノートに従って正規形・PBW/AS・全中心恒等式の検証を継続する。今回のB監査はAの数学的再監査を意味しない。

## 一般原則と保存許可

以下は個別の研究課題と区別した継続原則である。数学的重要性・新規性・理解・応用・正確性・実現可能性を総合し、方針は現在有効な内容へ書き直す。証明済、仮定付き、未完成、予想、有限計算を区別する。誤りがあれば依存先・要約も修正する。必要な証明・例・反例・再現入力を軽量化のために削らず、履歴と重複を整理する。先行研究は一次資料で仮定・適用箇所を確認し、初出未確認は明記する。原稿・ノートは研究の経緯ではなく現在の数学を理解する順に構成する。

本研究はGitHub mainへの節目ごとの保存が継続して許可されており、追加承諾を求めない。保存前に最新mainを確認し、期待する親SHAを指定したfast-forward更新と遠隔ref/blob照合を行う。force push、GitHub Actions、不要なPR、旧版ZIPは作らない。Libraryは実際のGitHub保存失敗時だけの緊急退避とする。外部ファイルの削除はこの整理・保存許可に含めない。

## 再現手順

```sh
python3 scripts/check_layout.py
python3 scripts/verify_bundle.py
python3 scripts/build.py --only paper_b
python3 scripts/verify_bundle.py --only paper_b --require-pdfs
python3 computations/verify_complete_curved_transport.py --output build/verify_complete_curved_transport.json
python3 computations/verify_three_object_window.py --output build/verify_three_object_window.json
python3 computations/verify_generic_cubic_descent.py --output build/verify_generic_cubic_descent.json
```

日本語LuaLaTeX、LuaTeX-ja、latexmk、Pythonと `requirements.txt` の依存を用いる。Aは `python3 scripts/build.py --only paper_a` で組版する。PDF・SyncTeX・中間物・再生成可能な出力はbuild/で非追跡。生成、検証、遠隔保存を別の状態として記録し、有限検算を圏同値の計算機証明とは報告しない。
