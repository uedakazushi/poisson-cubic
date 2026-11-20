# Build from the repository root: latexmk papers/poisson-cubic.tex
# LuaLaTeX by default; PDFs and intermediate files go to ignored build/.
$pdf_mode = 4;
$lualatex = 'env TEXINPUTS=./papers/support//: lualatex -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$out_dir = 'build';
$aux_dir = 'build';
$max_repeat = 6;

@default_files = ('papers/poisson-cubic.tex');
# Main manuscript: papers/poisson-cubic.tex.
# TEXINPUTS permits the retained A source tree to compile from the repository root.
# Shared sources remain under papers/support/papers/.
