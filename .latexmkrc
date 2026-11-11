# Build from the repository root: latexmk papers/paper_c.tex
# LuaLaTeX by default; PDFs and intermediate files go to ignored build/.
$pdf_mode = 4;
$lualatex = 'lualatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$out_dir = 'build';
$aux_dir = 'build';
$max_repeat = 6;

# Main manuscripts: papers/paper_a.tex, papers/paper_b.tex, papers/paper_c.tex.
# Shared sources remain under papers/support/papers/.
