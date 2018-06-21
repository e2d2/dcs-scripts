#!/bin/bash

for i in PreIngest*.md; do
    docname=$(basename -s '.md' ${i}).docx
    pandoc -f markdown -t docx ${i} -o ${docname}
    done
