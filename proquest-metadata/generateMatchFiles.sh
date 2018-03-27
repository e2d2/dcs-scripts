#!/bin/bash

# Each nested for loop generates a manifest of contents of zip files
# in the proquest dataset. Run each separately, in the PDF and ZIP
# directories.

# After script is run, tidy up pathnames for contentsXML.txt and
# contentsPDF.txt so that the relative path for each zip file is
# represented correctly.


for i in $(ls *.zip); do 
    for j in $(zipinfo -1 ${i}); do
        echo "${i}|${j}";
    done;
done > ../contentsXML.txt


for i in $(find . -name "*.zip"); do
    for j in $(zipinfo -1 ${i}); do
        echo "${i}|${j}";
    done;
done > ../contentsPDF.txt


