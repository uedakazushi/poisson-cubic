# Build from the repository root: latexmk papers/paper_b.tex
# LuaLaTeX by default; PDFs and intermediate files go to ignored build/.
$pdf_mode = 4;
$lualatex = 'env TEXINPUTS=./papers/support//: lualatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$out_dir = 'build';
$aux_dir = 'build';
$max_repeat = 6;

# Main manuscripts: papers/paper_a.tex and papers/paper_b.tex.
# TEXINPUTS also permits auxiliary standalone manuscripts in papers/support/papers/ to compile from the repository root.
# Shared sources remain under papers/support/papers/.
