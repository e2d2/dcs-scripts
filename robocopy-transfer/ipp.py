#!/usr/bin/env python3

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
oldest = [315537897600, '']
robocopy = None
thisscript = os.path.abspath(os.path.basename(__file__))
thispath = os.getcwd()

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
print("The current path is: {0}".format(thispath))
print("If this is the robocopy directory, type YES to proceed.")
prompt = input()
if prompt != "YES":
    sys.exit("Quitting. Please navigate to the robocopy directory and run the script again.")



# Loop through everything and try to figure out which one is the log
for dirpath, dirnames, filenames in os.walk(thispath): # TODO Fix this
    for fn in filenames:
        # This file
        f = os.path.join(dirpath, fn)

        if os.path.basename(f).find('robocopy') != -1 and robocopy is None:
            checkrobocopy = input("is this the robocopy log? y/n \n" + 
            "{0}\n".format(f))

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

        # Also ignore self
        elif f == thisscript:
            continue

        # Only calculate timestamp for nonlog
        else:
            # Latest mod timestamp
            ts = os.path.getmtime(f)
            print("are we here")
            print(ts, oldest[0])
            if ts > latest[0]:
                latest[0] = ts
                latest[1] = f
            if ts < oldest[0]:
                oldest[0] = ts
                oldest[1] = f

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
print("File statistics for most recent deposit")
print("-------------------------------------------------------")
print("Aggregate size: {0}".format(formatsize(aggregatesize)))
print("\n")
print("Extensions found: Number of files found")
for k in sorted(extensions, key=str.lower):
    print("{0}: {1}".format(k, extensions[k]))
print("\n")
print("Hidden files found: (None found if none listed)")
for h in hf:
    print(h)
print("\n")

# Hedge the time calculations (in case there's something weird about the folder)
if latest != [0,'']:
    print("Most recent timestamp...")
    print("{0} : {1}".format(datetime.fromtimestamp(latest[0]), latest[1]))
    print("\n")

if oldest != [315537897600, ''] and oldest[1] != latest[1]:
    print("Oldest timestamp...")
    print("{0} : {1}".format(datetime.fromtimestamp(oldest[0]), oldest[1]))
    print("\n")

if robocopy is not None:
    print("Transfer statistics (from original robocopy log)")
    print("Start time: {0}".format(timein.isoformat()))
    print("End time: {0}".format(timeout.isoformat()))
    elapsed = timeout - timein
    print("Transfer time: {0}".format(str(elapsed)))
