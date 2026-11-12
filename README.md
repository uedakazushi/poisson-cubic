# nc-cubic — Poisson三次超曲面の量子化と一般点可換復元

**2026-11-13 / v74。** GitHub mainが正本。再開は [研究方針](00_research_plan.md) から。

## 現行の二論文

| 原稿 | 内容 |
|---|---|
| [論文A](papers/paper_a.tex)（A-v51） | 一般次元のPoisson幾何・代数的量子化。本文と入力ソースを保持。 |
| [論文B](papers/paper_b.tex)（B-v55） | 任意のn>=3の代数的中心三次変形の一般点可換復元と必要な証明。 |

Bの必要証明は [papers/generic_recovery/](papers/generic_recovery/) に集約した。局所模型、三対象window、完備MF比較、一般点生成と有限降下、coherent飽和、低rotation積と勾配空間、基礎体上の方程式という順序である。模型の方程式をC(h)上に取れることと同値が有限拡大後に存在することを区別する。今回A・Bの本文と設定は変更していない。

B-v55は27頁の全文組版・表示確認済み。11TeX入力、102ラベル、94参照、37引用、13文献、未解決・重複・文字欠落・overfullなし。全数学的証明の独立監査ではない。状態は [validation_paper_b.json](validation_paper_b.json)、依存は [notes/generic_recovery.md](notes/generic_recovery.md)。

## 独立成果の現行所在

以下の三単位をnc-cubic2の独立原稿へ統合し、必要な参照・組版・有限計算・保存を確認した。

- [点スキームとPoisson零点](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/mixed_cubic_point_schemes.tex)：12頁。混合中心式の証明と4節、4検算コード。元の専用17ファイルを整理済み。
- [有限Jacobian復元](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/cubic_jacobian_recovery.tex)：6頁。低積・有限可積分性・一意性・反例。元の専用3ファイルを整理済み。主定理に必要な部分はBに保持。
- [中心三次対の一次変形とPlücker障害](https://github.com/uedakazushi/nc-cubic2/blob/main/papers/cubic_first_order_deformations.tex)：10頁。全既存結果と必要な双対数windowの証明、元と一致する2検算コード。一次消去は一般のN>=5、Plücker障害とcategorical接空間はN=5。専用本文・2コードを移管先の保存確認後に整理する。

各原稿と同名の `notes/` ノートを研究再開の入口とし、 `validation_*.json` で検証範囲を確認する。全文の独立監査・新規性確定・圏同値の計算機形式検証まで済んだとはしない。

**移管全体は未完了。** 一般Artin・étale理論、Sklyanin/多ブロック、対角/bar/Moritaの別構成、混合族のjet・同変復元等は現行支持ソースに残す。必要な一部分の抽出を広い成果全体の移管完了と混同しない。[現在の所在と残件](notes/paper_b_scope_and_transfer.md)を参照。

## 再現と保存

```sh
latexmk papers/paper_a.tex
latexmk papers/paper_b.tex
python3 scripts/verify_bundle.py --only paper_b
```

LuaLaTeX、LuaTeX-ja、latexmkを用いる。.latexmkrcは変更しない。今回A・Bの再組版や全既存計算の再実行はしていない。PDF・SyncTeX・中間物はbuild/で非追跡。GitHub Actions・force pushは使用せず、Libraryは実際のGitHub保存失敗時のみ緊急退避する。
