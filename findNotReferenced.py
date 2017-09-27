'''
Ioannis Papavasileiou

This script will take a bibliography file, bibliography.bib and a source tex file, paper.tex 
and it will create a new bibliography file, notReferenced.bib, with every entry in bibliography.bib
that has not been referenced in the tex source, paper.tex

Usage: python findNotReferenced <bibliography.bib> <paper.tex> <notReferenced.bib>')
'''

import sys
from bibtexparser import load
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase


if len(sys.argv)<4:
    print('Usage: python findNotReferenced <bibliography.bib> <paper.tex> <notReferenced.bib>')
    sys.exit(1)

bibFileName = sys.argv[1]
texFileName = sys.argv[2]
outFileName = sys.argv[3]
with open(bibFileName) as bibtex:
    bibDB = load(bibtex)

with open(texFileName) as texFile:
    text = ''.join(texFile.readlines())

toInclude = [entry for entry in bibDB.entries if entry['ID'] not in text]
bibDB.entries = toInclude
print('found %d bibliography entries not cited in %s'%(len(toInclude),texFileName))

writer = BibTexWriter()
with open(outFileName, 'w') as bibfile:
    bibfile.write(writer.write(bibDB))
print('wrote %d bibliography entries in %s\n'%(len(toInclude),outFileName))
