#/usr/bin/env python3

# Rewriting MD5 script for Python
# Part 1; generating checksums

import glob
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--barcodes_folder', metavar='[barcodes_folder]',
                    required=False, default='.',
                    help='folder with barcodes folders')
args = parser.parse_args()


ignore = ['.DS_Store', 'Thumbs.db']



