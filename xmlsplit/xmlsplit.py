#!/usr/bin/env python3

# https://stackoverflow.com/questions/36155049/splitting-xml-file-into-multiple-at-given-tags
# Plus some optional input/wrappering

import argparse
import sys
import os
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('inputxml', metavar='[XML to split]',
                     help='XML file you need to split')
parser.add_argument('outputdir', metavar='[Output directory]',
                    help='Output directory for split MARCXML')
args = parser.parse_args()

outputdir = args.outputdir

try:
    os.mkdir(outputdir)
except FileExistsError:
    sys.exit('Output directory already exists. Quitting!')


# Right now this doesn't check if the file exists before
# trying to read it...
with open(args.inputxml) as xmlfile:
    xmltosplit = ET.iterparse(xmlfile, events=('end', ))
    for event, elem in xmltosplit:
        ldr = None
        ctrlfld = None
        bibid = None
        datafld = None
        barcode = None
        record = None

        if elem.tag == 'record':
            ldr = elem.find('leader').text[6:8]
            ctrlfld = elem.findall('controlfield')
            for cf in ctrlfld:
                if cf.attrib['tag'] == '001':
                    bibid = cf.text
            datafld = elem.findall('datafield')
            for df in datafld:
                if df.attrib['tag'] == '955':
                    for dfc in df.getchildren():
                        if dfc.attrib['code'] == 'b':
                            barcode = dfc.text

            newrec = ET.Element('collection')
            newrec.insert(0, elem)
            record = ET.ElementTree(newrec)

            outputxmlname = '{0}_{1}_{2}.xml'.format(bibid, barcode, ldr)
            outputdest = os.path.join(outputdir, outputxmlname)

            record.write(outputdest, xml_declaration=True, encoding='utf-8',
                         method='xml')


# BIBID - BARCODE - LEADER 06-07 - DOT - XML
