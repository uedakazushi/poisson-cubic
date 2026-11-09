# Build from the repository root: latexmk papers/rotation_cubic_reconstruction.tex
# LuaLaTeX by default; PDFs and intermediate files go to ignored build/.
$pdf_mode = 4;
$lualatex = 'lualatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$out_dir = 'build';
$aux_dir = 'build';
$max_repeat = 6;
