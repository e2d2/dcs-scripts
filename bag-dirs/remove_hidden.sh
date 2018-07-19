#!/bin/bash

find $1 -name ".DS_STORE" -exec rm {} \;
find $1 -name "._.*" -exec rm {} \;
find $1 -name "Thumbs.db" -exec rm {} \;
