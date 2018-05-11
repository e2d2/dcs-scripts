#!/bin/bash

set -o noclobber

sdir=$(basename $1);
if [[ -d ${sdir} ]]; then
    # First loop through and do checksum
    for sd in ${sdir}/*; do
        cd ${sd};
        md5sum * > checksum.md5;
        cd -;
    done

    # Second zip up things
    for sd in ${sdir}/*; do
        basesd=$(basename ${sd});
        zip ${basesd}.zip ${sdir}/${basesd}/*
    done

    
fi

# TODO: Error message if first param isn't a directory
