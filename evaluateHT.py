#!/usr/bin/env python3

import argparse
import requests
import sys
import xml.etree.ElementTree as ET


namespaces = { 'marc' : 'http://www.loc.gov/MARC21/slim' }
baseURL = 'http://newcatalog.library.cornell.edu/catalog'
headers = {'Content-Type': 'application/xml'}


def parsexml(rawxml):
    marcxml = ET.fromstring(rawxml)

    leader = ''
    pagerange = ''

    controlfields = marcxml.findall('marc:controlfield', namespaces)
    datafields = marcxml.findall('marc:datafield', namespaces)

    for cf in controlfields:
        if cf.get('tag') == '008':
            leader = cf.text

    for df in datafields:
        if df.get('tag') == '300':
            for dfc in df.getchildren():
                if dfc.get('code') == 'a':
                    pagerange = dfc.text

    return (leader, pagerange)


def fullview(leader):
    pubyear = leader[7:11]
    pubplace = leader[15:18]
    govdoc = leader[28]

    try:
        pubyear = int(pubyear)
    except:
        pubyear = 9999

    if govdoc == 'f' and pubplace.endswith('u'):
        return True

    if pubyear < 1873:
        return True
    if pubyear >= 1873 and pubyear <= 1922:
        if pubplace.endswith('u'):
            return True
    return False
    
    # 1922 or earlier, and in US, full view
    # 1873 or earlier, full view no matter where
    # us gov doc always full view


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputlist', metavar='[input_list]',
                        help='input list with BIBIDs')
    args = parser.parse_args()

    failures = []
    print(','.join(['bibid', 'isFullView', 'pageRange', 'leader']))

    inputlist = open(args.inputlist).readlines()
    for item in inputlist:
        item = item.strip()
        query = '{0}/{1}.marcxml'.format(baseURL, item)
        resp = requests.get(query, headers=headers)
        if resp.status_code == 200:
            leader, pagerange = parsexml(resp.content.decode('utf-8'))
        else:
            failures.append(item)
            continue
        isfullview = fullview(leader)
        print(','.join([item, str(isfullview), pagerange, leader]))
    sys.stderr.write('\nUNKNOWN BIBS---\n')
    sys.stderr.write('\n'.join(failures))


if __name__ == "__main__":
    main()


