# nc-cubic — 一般次元のrotation付き可換復元

**2026-11-10 v15。GitHub `main` が唯一の正本。** まず [研究方針](00_research_plan.md)、次に [研究ノート](research_notes.md) を読む。旧ZIP/ChatGPT Library/会話履歴は不要。

## 最優先：可換復元定理
任意のn≥3、各Poisson既約成分の一般点において、量子化の残余dg圏を滑らかな可換cubicのrotation付きKuznetsov成分として実現する。現在の核心は残余対角の相対smoothness (SM) と局所実現原理 (ER)。**無条件の一般可換復元はまだ未証明**である。

## 現行論文と証明全文

| 主論文 | TeX入口 |
|---|---|
| A：Poisson構造と量子化 | [tex/poisson_cubic_quantization.tex](tex/poisson_cubic_quantization.tex) |
| B：一般17次元族とambient復元 | [tex/generic17_ambient_recovery.tex](tex/generic17_ambient_recovery.tex) |
| C：rotation付き可換復元 | [tex/rotation_cubic_reconstruction.tex](tex/rotation_cubic_reconstruction.tex) |

論文Cの最新の局所rotation逆関手・(SM)還元の**独立組版用証明全文**は [reconstruction/tex/rotation_saturation_reduction.tex](reconstruction/tex/rotation_saturation_reduction.tex) に保持し、[reconstruction/README.md](reconstruction/README.md) に再現方法を記す。これは現行の論文C部分研究であり、過去版のアーカイブでも第四論文でもない。親論文A/B/Cと独立境界研究の既存成果・証明は削除していない。

局所proper残余圏でのrotationの逆 `(-1)R_O`、(SM)下でのfull coherent比較・有限型spreadは原稿に論証があるが、外部査読・形式検証は未実施。(SM)、(ER)、一般成分の量子化入力は未完成である。

## GitHubだけから再現
必要：Python 3、SymPy、LuaLaTeX、LuaTeX-ja/ltjsarticle、標準LaTeX数学パッケージ。

```sh
python3 reconstruction/computations/verify_nonelliptic_inputs.py --output /tmp/nc-cubic-input-checks.json
python3 reconstruction/scripts/build.py
python3 reconstruction/scripts/verify.py
```

最新の論文C局所原稿のPDFは `reconstruction/pdf/rotation_saturation_reduction.pdf` に生成される（git追跡しない）。三論文全体は `python3 scripts/build.py` で組版する。**この更新では親三論文の完全再ビルドは未実施**。実行済み検証と数学的検証を分けて記録する。

## GitHub正本の永続指示
詳しくは [AGENTS.md](AGENTS.md)。研究の区切りで証明全文・方針・ノート・必要な検証資産を `main` にfast-forward pushし、remoteのref/ファイルを再読して確認する。**ChatGPT Library保存は実際のGitHub push失敗時にだけ許される緊急避難**であり、通常時には保存しない。
