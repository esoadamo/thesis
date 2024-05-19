import re
from sys import argv
from pathlib import Path

MD_PREFIX = r'''\begin{markdown*}{%
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
MD_SUFFIX = r'''
\end{markdown*}'''

TABLE_STYLE=r'row{odd} = {bg=gray!5},row{1} = {font=\bfseries\centering, bg=gray!10},rowhead = 1,hlines,vlines,'


def process_acronyms(content, file_md_acronyms: Path):
  with file_md_acronyms.open('r') as f:
    lines = f.read().split('\n')

  acronyms = {}
  
  for line in lines:
    try:
      _, key, value, _ = line.split('|', 4)
    except ValueError:
      continue
    key = key.strip()
    value = value.strip()

    if key == "Acronym" or set(key) == {"-"}:
      continue

    acronyms[key] = value

  for key in acronyms:
    content = re.sub(f"([^\w]){key}([^\w])", "\\1\\\\gls{%s}\\2" % key, content)

  acronyms_commands = ""
  for key, value in acronyms.items():
    acronyms_commands += "\\newacronym{%s}{%s}{%s}\n" % (key, key, value)
  acronyms_commands += "\\makenoidxglossaries\n"
  
  content = content.replace("%% [META] ACRONYMS GO HERE %%", acronyms_commands)

  return content


def main():
  file = argv[1]

  with open(file, 'r') as f:
      content = f.read()

  while r'\markdownInput' in content:
      match = next(re.finditer(r"\\markdownInput\{(.*?)\}", content))
      replace = match.group(0)
      file_md = Path(Path(match.group(1)).name)
      markdown = MD_PREFIX + process_obsidian_md(file_md, file_md.parent) + MD_SUFFIX
      content = content.replace(replace, markdown)

  content = process_acronyms(content, Path("Acronyms.md"))

  with open(file, 'w') as f:
      f.write(content)

def process_obsidian_md(file_md, root):
  with file_md.open('r') as f:
    content = f.read()

  # User correct citation syntax
  content = re.sub(r"\[\[@([^]]*?)]]", r"[@\1]", content)
  content = re.sub(r"\s\[@", r"~[@", content)

  # Include other .md files
  while True:
    try:
      match = next(re.finditer(r"!?\[\[([^@][^]]*?)]]", content))
    except StopIteration:
      break
    replace = match.group(0)
    file_link_name = caption = match.group(1)

    if '|' in file_link_name:
      file_link_name, caption = file_link_name.split('|')

    if '.' in file_link_name:
      content = content.replace(replace, '```latex\n\\begin{figure}[H]\n\\caption{' + caption + '}\n\\label{fig:' + file_link_name + '}\n\\centering\n\\includegraphics[width=\\textwidth,height=0.4\\textheight,keepaspectratio]{' + file_link_name + '}\n\\end{figure}\n```')

    else:
      file_md_insert = Path(file_link_name + '.md')
      content = content.replace(replace, process_obsidian_md(file_md_insert, root))

  # Parse raw latex blocks
  while True:
    try:
      match = next(re.finditer(r"```latex(\n(?:.|\n)*?\n)```", content))
    except StopIteration:
      break
    replace = match.group(0)
    latex = match.group(1)

    # apply table style
    latex = re.sub(r'(colspec\s*=.*?,)', r"\1 %STYLE_TABLE%", latex)
    latex = latex.replace("%STYLE_TABLE%", TABLE_STYLE)


    content = content.replace(replace, MD_SUFFIX + latex + MD_PREFIX)

  # Parse inline latex commands
  while True:
    try:
      match = next(re.finditer(r"`TEX:(.*?)`", content))
    except StopIteration:
      break
    replace = match.group(0)
    latex = match.group(1)
    content = content.replace(replace, latex)

  # Replace single-character words with an unbreakable spaces
  content = re.sub(r"(\s+\w) (\w)", r"\1~\2", content)

  return content


if __name__ == "__main__":
  main()
