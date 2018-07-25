#/bin/bash

# Bagit executable
BAGIT="python3 -m bagit"

# Bagit command
BAGITCMD="${BAGIT} --md5"

if [ -d "$1" ]; then
	bagdir=${1%/}
	for b in $(find ${bagdir} -type d -maxdepth 1 -mindepth 1); do
		${BAGITCMD} ${b};
		zip ${b}.zip ${b}; done
	else echo "Did not specify a target directory."
fi
