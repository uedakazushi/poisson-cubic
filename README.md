# nc-cubic — Poisson三次超曲面の量子化と一般点可換復元

**2026-11-13 / v73。** GitHub mainが正本。再開は [研究方針](00_research_plan.md) から。

## 現行の二論文

| 原稿 | 対象 |
|---|---|
| [論文A](papers/paper_a.tex)（A-v51） | 一般次元のPoisson幾何・代数的量子化。移管せず全入力を保持する。 |
| [論文B](papers/paper_b.tex)（B-v55） | 任意のn>=3の中心三次変形の一般点可換復元と必要な証明だけ。 |

Bの証明は [papers/generic_recovery/](papers/generic_recovery/) に集約した。局所模型・三対象window・完備MF比較・一般点生成と有限降下・coherent飽和・低rotation積・方程式の基礎体降下の順である。方程式はC(h)上、同値は有限拡大後という区別を保つ。今回の移管ではA・B本文と共通設定を変更していない。

B-v55は全文27頁を組版・表示確認済み。11TeX入力、102ラベル、94参照、37引用、13文献、未解決・重複・文字欠落・overfullは0。これは全数学的証明の独立監査ではない。記録は [validation_paper_b.json](validation_paper_b.json)、証明の依存は [notes/generic_recovery.md](notes/generic_recovery.md)。

## 独立成果の現在の分担

**点スキーム**はnc-cubic2の [mixed_cubic_point_schemes.tex](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/mixed_cubic_point_schemes.tex) に統合した。必要な中心元の証明、4節、文献、4本の検算、ノートを備え、12頁の組版・表示・参照検査を実施。元の専用17ファイルを除外済み。

**有限Jacobian復元**はnc-cubic2の [cubic_jacobian_recovery.tex](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/cubic_jacobian_recovery.tex) に統合した。有限可積分性判定、一意性、Fermat例、積分不可能な完全交差を証明ごと保持する。6頁、4TeX入力、17ラベル・19参照・7引用・4文献に未解決・重複なし。有理数上の検算と元の証明書の再生成も確認した。元の専用本文・コード・証明書3ファイルを除外し、必要な低次数同定・一意性の証明はBに残す。共有の文献断片は未移管の支持節用に維持する。

**移管全体は未完了。** 一次変形・Plücker障害の節は全文保存済みだが、独立原稿への統合と依存整理が残る。Artin・étale、Sklyanin/多ブロック、対角/bar/Morita、混合jetも現行ソースに保持する。詳細は [notes/paper_b_scope_and_transfer.md](notes/paper_b_scope_and_transfer.md)。旧コミットだけを成果の保存場所にせず、移管先の必要入力・検証・保存を確認してから元を整理する。

## 再現

```sh
latexmk papers/paper_a.tex
latexmk papers/paper_b.tex
python3 scripts/verify_bundle.py --only paper_b
```

LuaLaTeX、LuaTeX-ja、latexmkを使い、PDF・SyncTeX・中間物はbuild/で非追跡。今回A・Bは再組版せず、独立稿の組版と検算を実施した。相対理論の残る検証入口は [reconstruction/README.md](reconstruction/README.md)。

GitHub Actions・force pushなし。Libraryは実際のGitHub保存失敗時のみ緊急退避し、既存Libraryファイルを無断削除しない。
