#!/bin/bash
set -xEeuo pipefail

cd "$(dirname "$(realpath "$0")")"

if [ ! -d compile/fithesis ]; then
    mkdir -p compile/fithesis
fi
find compile -type f -exec rm {} \;

find . -type f -exec cp {} compile/{} \;
cp -r ../assets/* compile/
cp -r ../*.md compile/
cp ../citations/database.biblatext compile/


cd compile
for f_md in *.md; do
    sed -e 's/\[\[/[/g' -e 's/]]/]/g' -i "$f_md"
    sed -Ee 's|\[@([^]]*)]| @\1|g' -i "$f_md"
done
python3 insert_md.py main.tex

latexmk
ls
cd ..

if [ ! -d dist ]; then
    mkdir dist
fi

cp compile/main.pdf dist/thesis.pdf

set +u
if [ "$1" == "--open" ]; then
    xdg-open dist/thesis.pdf
fi
