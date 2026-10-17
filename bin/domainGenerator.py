#!/bin/sh
export PYTHONPATH="$PWD":$PYTHONPATH
exec python3 "upstream/tools/xmlGenerator/domainGenerator.py" "$@"
