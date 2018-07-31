#!/usr/bin/env python3


import os
import subprocess
from glob import iglob


def antiword(path):
    # Try antiword first
    antiwordcall = ['antiword', path]
    a = subprocess.run(antiwordcall, stdout = subprocess.PIPE,
                                     stderr = subprocess.PIPE)

    # Fallback to strings
    stringscall = ['strings', path]

    err = a.stderr.decode('utf-8')
    out = a.stdout.strip().decode('utf-8')

    if err.find('Rich Text') != -1:
        return
    elif err != '':
        b = subprocess.run(stringscall, stdout = subprocess.PIPE,
                                        stderr = subprocess.PIPE)
        err = b.stderr.decode('utf-8') # capturing it even though I'm not handling it after this
        out = b.stdout.strip().decode('utf-8')
    else:
        pass

    newfilename = "{0}/CONVERTED_{1}".format(os.path.dirname(path), 
                                             os.path.basename(path))

    if len(out) > 0:
        if not os.path.exists(newfilename):
            newfile = open(newfilename, 'w')
            newfile.write(out)
            newfile.close()
        else:
            print(newfilename)


def wpd2text(path):
    wpdcall = ['wpd2text', path]
    c = subprocess.run(wpdcall, stdout = subprocess.PIPE,
                                    stderr = subprocess.PIPE)

    # Fallback to antiword
    antiwordcall = ['antiword', path]

    err = c.stderr.decode('utf-8')
    out = c.stdout.strip().decode('utf-8')

    if err !='':
        d = subprocess.run(antiwordcall, stdout = subprocess.PIPE,
                                        stderr = subprocess.PIPE)

        err = d.stderr.decode('utf-8') # capturing it even though I'm not handling it after this
        out = d.stdout.strip().decode('utf-8')

    newfilename = "{0}/CONVERTED_{1}".format(os.path.dirname(path),
                                             os.path.basename(path))

    if len(out) > 0:
        if not os.path.exists(newfilename):
            newfile = open(newfilename, 'w')
            newfile.write(out)
            newfile.close()
        else:
            print(newfilename)





for i in iglob('**/*.doc', recursive=True):
    antiword(i)

for i in iglob('**/*.DOC', recursive=True):
    antiword(i)

for i in iglob('**/*.wpd', recursive=True):
    wpd2text(i)

for i in iglob('**/*.WPD', recursive=True):
    wpd2text(i)


