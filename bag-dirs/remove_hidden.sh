#!/bin/bash

find . -name ".DS_STORE" -exec rm {} \;
find . -name "._.*" -exec rm {} \;
find . -name "Thumbs.db" -exec rm {} \;
