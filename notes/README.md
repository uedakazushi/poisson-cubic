# 研究ノート

研究方針はルートの `00_research_plan.md` にあり、本フォルダーには現時点で有効な知識・未解決課題・計算・障害を置く。

- `notes/research_notes.md`：一般次元・各Poisson成分の研究ノート
- `notes/reconstruction.md`：可換復元の相対理論
- `notes/research_notes.tex`：既存の詳細な数学研究ノート
- `notes/reconstruction_notes.tex`：一楕円ブロックと相対化の技術ノート
- `notes/rotation_saturation_reduction_v14.md`：既存のrotation・saturation補足ノート

- `notes/sm_bar_and_spreading.tex`：SMの有限bar対角判定・generic spreading。PDF-only原本第18--21節を証明付きで再構成した独立ノート

TeXノートもルートから `latexmk notes/research_notes.tex` と `latexmk notes/reconstruction_notes.tex` で組版する。生成PDFは `build/` に置き、Git追跡しない。

ソース未確認のノート原本PDFは `notes/pdf-only/` に二本保存する。これらのみ例外的なGit追跡対象である。

`latexmk notes/sm_bar_and_spreading.tex` で現行SMの有限判定ノートを再生成する。
