#!/usr/bin/env python3

import csv
import argparse
from string import Template

# Input:
# Output:
# Rule:


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', metavar='[input_file]', type=argparse.FileType('rtU'),
                        help='name of file with input data')
    args = parser.parse_args()

    # Load the template file as a string
    rmctmpl = open('PREINGEST_TEMPLATE.md', 'rU').read()
    rmctmpl = Template(rmctmpl)

    infile = csv.DictReader(args.infile, delimiter='\t')
    for row in infile:
        outputfile = 'PreIngest_Report_RMC_{0}.md'.format(row['CULAR_TITLE'])
        # TODO: Do not clobber old files!
        with open(outputfile, 'w') as mdtmp:
            for key in row:
                if key.endswith('LIST'):
                    row[key] = row[key].replace('|', '\n        * ')
            mdtmp.write(rmctmpl.safe_substitute(row))

if __name__ == "__main__":
    main()
