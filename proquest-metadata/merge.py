#!/usr/bin/env python

# Load files
contentsPDF = open('contentsPDF.txt', 'rU').readlines()
contentsXML = open('contentsXML.txt', 'rU').readlines()
keylist = open('keylist.txt', 'rU').readlines()

PDFdict = {}
for c in contentsPDF:
    c = c.strip('\n')
    p = c.split('_')[-1].strip('.pdf')
    PDFdict[p] = c

XMLdict = {}
for c in contentsXML:
    c = c.strip('\n')
    p = c.split('|')[-1].strip('.xml')
    XMLdict[p] = c

for k in keylist:
    k = k.strip('\n')
    print(('|').join([k, XMLdict[k], PDFdict[k]]))
