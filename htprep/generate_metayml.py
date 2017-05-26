#!/usr/bin/env python3

import yaml
import csv
import os
import glob
import argparse
import sys

# TODO Put into main
parser = argparse.ArgumentParser()
parser.add_argument('file_template', metavar='[yml_template]',
                    help='template for meta.yml')
parser.add_argument('file_pagedata', metavar='[csv_file]',
                    help='csv file with pagedata')
parser.add_argument('-b', '--barcodes-folder', metavar='[barcodes_folder]',
                    required=False, default='.',
                    help='folder with barcodes folders')
args = parser.parse_args()

if not os.path.isfile(args.file_template):
    sys.exit("Template not a file") # TODO better note
if not os.path.isfile(args.file_pagedata):
    sys.exit("CSV is not a file") # TODO better note

file_template = args.file_template
file_pagedata = args.file_pagedata

# Does the barcode folder as supplied exist?
barcode = os.path.join(args.barcodes-folder, os.path.splitext(file_pagedata)[0])

if not os.path.exists(barcode):
    sys.exit("Barcode folder doesn't exist")
# TODO: Should there be a check for existing meta.yml?

# Open up all of the files
template = yaml.safe_load(open(file_template, 'rU', encoding='utf-8-sig'))
pagedata = csv.DictReader(open(file_pagedata, 'rU', encoding='utf-8-sig'))

# Valid pagedata column headings
validcols = ['image number', 'orderlabel', 'label']

# Verify column headings in pagedata
for f in pagedata.fieldnames:
    if f not in validcols:
        sys.exit("Invalid column heading in metadata spreadsheet: '{0}'".format(f))
            
# Set up pagedata
template['pagedata'] = {}

# Valid label values
validlabels = ['BACK_COVER', 'BLANK', 'CHAPTER_PAGE', 'CHAPTER_START', 'COPYRIGHT', 'FIRST_CONTENT_CHAPTER_START',
               'FOLDOUT', 'FRONT_COVER', 'IMAGE_ON_PAGE', 'INDEX', 'MULTIWORK_BOUNDARY', 'PREFACE', 'REFERENCES',
               'TABLE_OF_CONTENTS', 'TITLE', 'TITLE_PARTS']

# Load in pagedata from csv
for row in pagedata:
    # Check for valid labels
    if row['label'] not in validlabels:
        sys.exit("Invalid label in metadata spreadsheet: '{0}'".format(row['label']))

    # TODO make the double quoting happen

    template['pagedata'][row['image number']] = {}
    if row['orderlabel'] != '':
        template['pagedata'][row['image number']]['orderlabel'] = row['orderlabel']
    if row['label'] != '':
        template['pagedata'][row['image number']]['label'] = row['label']

# Set up meta.yml in destination
metayml_output = os.path.join(barcode, 'meta.yml')

with open(metayml_output, 'w') as meta:
    meta.write(yaml.dump(template))

