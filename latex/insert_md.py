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
      file_md = Path(match.group(1))
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

  # Include other .md files
  while True:
    try:
      match = next(re.finditer(r"\[\[([^@][^]]*?)]]", content))
    except StopIteration:
      break
    replace = match.group(0)
    file_md_insert = Path(match.group(1) + '.md')
    content = content.replace(replace, process_obsidian_md(file_md_insert, root))

  # Parse raw latex blocks
  while True:
    try:
      match = next(re.finditer(r"```latex(\n(?:.|\n)*?\n)```", content))
    except StopIteration:
      break
    replace = match.group(0)
    latex = match.group(1)
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



  return content


if __name__ == "__main__":
  main()
