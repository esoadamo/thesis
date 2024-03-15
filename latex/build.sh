#!/bin/bash
set -xEeuo pipefail

cd "$(dirname "$(realpath "$0")")"

find compile -type f -exec rm {} \;

find . -type f -maxdepth 1 -exec cp {} compile/{} \;
cp -r ../assets/* compile/
cp -r ../*.md compile/

cp fi-pdflatex.tex main.tex

cd compile
for f_md in *.md; do
    sed -e 's/\[\[/[/g' -e 's/]]/]/g' -i "$f_md"
    sed -Ee 's|\[@([^]]*)]| \\cite[]{\1}|g' -i "$f_md"
done
pdflatex --shell-escape main.tex
biber main
pdflatex --shell-escape main.tex
cd ..

cp compile/main.pdf dist/thesis.pdf

set +u
if [ "$1" == "--open" ]; then
    xdg-open dist/thesis.pdf
fi
