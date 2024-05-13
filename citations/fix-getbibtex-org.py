#!/usr/bin/env python3

# This script fixes formatting from https://www.getbibtex.com/

import re
from os import rename

def parse_bib_file(filepath):
    entries = []
    current_entry = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip() == '' and current_entry:
                entries.append(current_entry)
                current_entry = []
            if line.strip():
                current_entry.append(line)
        if current_entry:
            entries.append(current_entry)
    return entries

def process_entries(entries):
    updated_entries = []
    for entry in entries:
        if entry[0].strip().startswith("@misc{"):
            new_entry = []
            for line in entry:
                # Change type from misc to online
                if line.strip().startswith("@misc{"):
                    line = line.replace("@misc", "@online")
                
                # Handle howpublished to url
                if line.strip().startswith("howpublished"):
                    url = re.findall(r'{\\url{(.*?)}}', line)[0]
                    line = f"\turl = {{{url}}},\n"
                
                # Handle note to urldate
                if line.strip().startswith("note"):
                    date = re.findall(r'\[(.*?)\]', line)[0]
                    formatted_date = '-'.join(reversed(date.split('-')))
                    line = f"\turldate = {{{formatted_date}}},\n"
                
                # Process title simplification
                if line.strip().startswith("title"):
                    try:
                        title = re.search(r'{(.+)}', line).group(1)
                    except AttributeError:
                        continue
                    title = title.split(' --- ')[0]
                    line = f"\ttitle = {{{title}}},\n"

                new_entry.append(line)
            updated_entries.append(new_entry)
        else:
            updated_entries.append(entry)
    return updated_entries

def write_bib_file(filepath, entries):
    with open(filepath, 'w', encoding='utf-8') as file:
        for entry in entries:
            for line in entry:
                file.write(line)
            file.write("\n")

def main():
    filepath = 'database.biblatext'
    entries = parse_bib_file(filepath)
    updated_entries = process_entries(entries)
    output_filepath = filepath + '.new'
    write_bib_file(output_filepath, updated_entries)
    rename(output_filepath, filepath)
    print("Fixed")

if __name__ == "__main__":
    main()

