import re
from sys import argv

file = argv[1]
prefix = r'''\begin{markdown*}{%
  hybrid,
  definitionLists,
  footnotes,
  inlineFootnotes,
  hashEnumerators,
  fencedCode,
  citations,
  citationNbsps,
  pipeTables,
  tableCaptions,
}
'''
suffix = r'''
\end{markdown*}'''

with open(file, 'r') as f:
    content = f.read()

while r'\markdownInput' in content:
    match = next(re.finditer(r"\\markdownInput\{(.*?)\}", content))
    replace = match.group(0)
    file_md = match.group(1)

    with open(file_md, 'r') as f:
        content = content.replace(replace, prefix + f.read() + suffix)

with open(file, 'w') as f:
    f.write(content)
