#!/usr/bin/env python3

import csv
import argparse
from string import Template

# Input:
# Output:
# Rule:

# TODO: This is not properly generalized!!

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', metavar='[input_file]', type=argparse.FileType('rt'),
                        help='name of file with input data')
    parser.add_argument('-a', '--archivescoll', action='store_true',
                        help='Use RMC template (archival collection)', default=False)
    args = parser.parse_args()

    # Load the template file as a string
    if args.archivescoll is True:
        tmpl = open('PREINGEST_TEMPLATE_RMC.md', 'r').read()
    else:
        tmpl = open('PREINGEST_TEMPLATE.md', 'r').read()
    tmpl = Template(tmpl)

    infile = csv.DictReader(args.infile, delimiter='\t')
    for row in infile:
        outputfile = 'PreIngest_Report_{0}.md'.format(row['CULAR_TITLE'])
        # TODO: Do not clobber old files!
        with open(outputfile, 'w') as mdtmp:
            for key in row:
                if key.endswith('LIST'):
                    row[key] = row[key].replace('|', '\n        * ')
            mdtmp.write(tmpl.safe_substitute(row))

if __name__ == "__main__":
    main()
