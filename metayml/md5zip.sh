#!/bin/bash

set -o noclobber

CWD=$(pwd);
sdir=$(basename $1);

if [[ -d ${sdir} ]]; then
    # First loop through and do checksum
    for sd in ${sdir}/*; do
        cd ${sd};
        md5sum * > checksum.md5;
        cd ${CWD};
    done

    # Second zip up things
    for sd in ${sdir}/*; do
	cd ${sdir}
        basesd=$(basename ${sd});
        zip ${basesd}.zip -r ${basesd}/*
	cd ${CWD};
    done

    
fi

# TODO: Error message if first param isn't a directory

