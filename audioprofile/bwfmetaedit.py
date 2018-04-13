#!/usr/bin/env python3

# Wrap bwfmetaedit

import subprocess
import csv
import sys

# Right now ALL this does is wrap some bwfmetaedit output
# It is meant to be part of a bigger process that actually checks
# embedded metadata against our profile.

# NOTE: Assuming the bwfmetaedit output first line is consistent
# This will also accomodate the event that the output is slightly different at some point since it'll
# be referenced using this variable for the rest of the script.
# NOTE: Run this on one file at a time, so there's only one line of output
bwfheaders = "FileName,Description,Originator,OriginatorReference,OriginationDate,OriginationTime,TimeReference (translated),TimeReference,BextVersion,UMID,LoudnessValue,LoudnessRange,MaxTruePeakLevel,MaxMomentaryLoudness,MaxShortTermLoudness,CodingHistory,IARL,IART,ICMS,ICMT,ICOP,ICRD,IENG,IGNR,IKEY,IMED,INAM,IPRD,ISBJ,ISFT,ISRC,ISRF,ITCH\n"


# TODO Make it modular
# TODO Make sure it does not change the file at all!! Maybe then just run it from the read-only place
bwfcall = subprocess.run(['bwfmetaedit', '-s', '--out-core', 'CULectures_3603226_A3288_A.wav'],
                          stdout=subprocess.PIPE)


bwfout = bwfcall.stdout.decode('utf-8')
bwflines = []

if bwfout.startswith(bwfheaders):
    bwfdata = bwfout[len(bwfheaders):]
    bwflines.append(bwfheaders)
    bwflines.append(bwfdata)
else:
    sys.exit("Unexpected output. Time to panic.")

reader = csv.DictReader(bwflines)
for row in reader:
    print(row)
