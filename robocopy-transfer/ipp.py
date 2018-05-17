#!/usr/bin/env python

import re
import os
import sys
from collections import defaultdict
from datetime import datetime


# ROBOCOPY stuff
relogstart = re.compile("Started : (.*)")
relogstop = re.compile("Ended : (.*)")

# File statistics stuff
aggregatesize = 0
extensions = defaultdict(lambda: 0)
hf = []
hfmatches = ['Thumbs.db', '.DS_Store']
latest = [0,'']
robocopy = None

# Pilfered from stackoverflow
def formatsize(numbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB'] # Planning.
    i = 0
    while numbytes >= 1024 and i < len(suffixes)-1:
        numbytes /= 1024.0
        i += 1
    f = ('%.2f' % numbytes).rstrip('0').rstrip('.')
    formatted = '{0} {1}'.format(f, suffixes[i])
    return formatted


# Ask about the path
print("The current path is: {0}".format(os.getcwd()))
print("If this is the robocopy directory, type YES to proceed.")
prompt = input()
if prompt != "YES":
    sys.exit("Quitting. Please navigate to the robocopy directory and run the script again.")



# Loop through everything and try to figure out which one is the log
for dirpath, dirnames, filenames in os.walk('.'): # TODO Fix this
    for fn in filenames:
        # This file
        f = os.path.join(dirpath, fn)

        if f.find('robocopy') != -1 and robocopy is None:
            checkrobocopy = input("is this the robocopy log? y/n " + 
            "{0}: ".format(f))

            if checkrobocopy.lower() == 'y':
                robocopy = f

                with open(f, 'rU') as rlog:
                    robocopylog = rlog.readlines()
                    timein = None
                    timeout = None
                    for rcl in robocopylog:
                        if timein is None:
                            rstart = relogstart.search(rcl)
                            if rstart is not None:
                                timein = datetime.strptime(rstart.group(1),
                                         '%A, %B %d, %Y %I:%M:%S %p')
                        if timeout is None:
                            rend = relogstop.search(rcl)
                            if rend is not None:
                                timeout = datetime.strptime(rend.group(1),
                                          '%A, %B %d, %Y %I:%M:%S %p')

        # Only calculate timestamp for nonlog
        else:
            # Earliest mod timestamp
            ts = os.path.getmtime(f)
            if ts > latest[0]:
                latest[0] = ts
                latest[1] = f

        # Extensions and Counts
        ext = os.path.splitext(f)[1]
        if ext == '':
            extensions['NO EXTENSION'] += 1
        else:
            extensions[ext] = extensions[ext] + 1

        # Aggregate size
        aggregatesize = aggregatesize + os.path.getsize(f)

        # Hidden files
        if f in hfmatches:
            hf.append[fn]


# Print everything out really nicely
print("\n")
print("-------------------------------------------------------")
print("File statistics for drive")
print("-------------------------------------------------------")
print("Aggregate size: {0}".format(formatsize(aggregatesize)))
print("\n")
print("Extensions found...")
for k in sorted(extensions, key=str.lower):
    print("{0}: {1}".format(k, extensions[k]))
print("\n")
print("Hidden files found...")
for h in hf:
    print(h)
print("\n")
print("Most recent timestamp...")
print("{0} : {1}".format(datetime.fromtimestamp(latest[0]), latest[1]))
print("\n")
print("Transfer statistics (from log)")
print("Start time: {0}".format(timein.isoformat()))
print("End time: {0}".format(timeout.isoformat()))
elapsed = timeout - timein
print("Transfer time: {0}".format(str(elapsed)))
