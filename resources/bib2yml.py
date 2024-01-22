import bibtexparser
import yaml
import sys

# mamba install -c conda-forge bibtexparser pyyaml
# Convert a bibtex file to a yaml file
# Usage: python3 bib2yml.py publist.bib publist.yml

def fix_author(author):
    # split author string into list of authors (separated by ' and ')
    a = author.split(' and ')
    # create list of dictionaries with first and last name
    b = []
    for i in a:
        c = {}
        c['last_name'] = i.split(', ')[0]
        c['first_name'] = i.split(', ')[1]
        b.append(c)
    # create list of first initials
    d = []
    for j in b:
        d.append(j['first_name'].split(' '))
    e = []
    for k in d:
        f = []
        for i in k:
            f.append(i[0])
        e.append(''.join(f))
    # create list of first initials and last name
    g = []
    for j in range(len(a)):
        g.append(f'{e[j]} {b[j]['last_name']}')
    # return string of authors initials and last name
    return ', '.join(g)

def convert_bibtex_to_yaml(bibtex_file, yaml_file):
    with open(bibtex_file, 'r') as file:
        bibtex_str = file.read()

    bib_database = bibtexparser.loads(bibtex_str)
    entries = bib_database.entries
    for i in entries:
        i['author'] = fix_author(i['author'])
        i['year'] = int(i['year'])
        i['title'] = i['title'].replace('{', '').replace('}', '')
        # i['journal'] = i['journal'].replace('{', '').replace('}', '').replace('\&', '&').replace('\textit', '').replace('\textbar', '|')
        if 'abstract' in i.keys():
            i.pop('abstract')
        if 'note' in i.keys():
            i.pop('note')
        if 'file' in i.keys():
            i.pop('file')

    with open(yaml_file, 'w') as file:
        yaml.dump(entries, file)

# Usage example
if len(sys.argv) != 3:
    print("Usage: python3 bibtex_to_yaml.py input.bib output.yaml")
else:
    convert_bibtex_to_yaml(sys.argv[1], sys.argv[2])
