#/usr/bin/env python3

# Rewriting MD5 script for Python

import glob
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--barcodes-folder', metavar='[barcodes_folder]',
                    required=False, default='.',
                    help='folder with barcodes folders')
args = parser.parse_args()

