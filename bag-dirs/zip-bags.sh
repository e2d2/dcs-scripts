#!/bin/bash

CWD=$(pwd)

if [ -d "$1" ]; then
	bagdir=${1%/}
	for b in $(find ${bagdir} -type d -maxdepth 1 -mindepth 1); do
		cd ${bagdir};
		zipname=$(basename ${b});
		zip ${zipname}.zip -r ${zipname};
		cd ${CWD};
	done
	else echo "Did not specify a target directory."
fi
	
