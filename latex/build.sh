#!/bin/bash
set -xEeuo pipefail

cd "$(dirname "$(realpath "$0")")"

if [ ! -d compile ]; then
    mkdir compile
fi
find compile -type f -exec rm {} \;

cp  -r fithesis compile/
find . -type f -exec cp {} compile/{} \;
cp -r ../assets/* compile/
cp -r ../*.md compile/
cp -r ../chapters/*.md compile/
cp ../citations/database.biblatext compile/


cd compile
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
