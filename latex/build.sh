#!/bin/bash
set -xEeuo pipefail

cd "$(dirname "$(realpath "$0")")"

find compile -type f -exec rm {} \;

if [ ! -d compile/fithesis ]; then
    mkdir -p compile/fithesis
fi

find . -type f -exec cp {} compile/{} \;
cp -r ../assets/* compile/
cp -r ../*.md compile/
cp ../citations/database.biblatext compile/

cp fi-pdflatex.tex compile/main.tex

cd compile
for f_md in *.md; do
    sed -e 's/\[\[/[/g' -e 's/]]/]/g' -i "$f_md"
    sed -Ee 's|\[@([^]]*)]| @\1|g' -i "$f_md"
done
python3 insert_md.py main.tex

latexmk
cd ..

cp compile/main.pdf dist/thesis.pdf

set +u
if [ "$1" == "--open" ]; then
    xdg-open dist/thesis.pdf
fi
