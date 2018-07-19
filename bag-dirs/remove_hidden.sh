#!/bin/bash

# TODO: Find replace first dir

find $1 -name ".DS_Store" -exec rm {} \;
find $1 -name "._.*" -exec rm {} \;
find $1 -name "Thumbs.db" -exec rm {} \;
