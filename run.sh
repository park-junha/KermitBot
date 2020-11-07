#!/bin/bash
BASE_DIR="$(cd "$(dirname "$0" )" && pwd )"
VENV_DIR=$BASE_DIR/venv
SRC_DIR=$BASE_DIR/src

# TODO (park-junha): extend this script to check if venv is valid, if
# app runs correctly, etc

source $VENV_DIR/bin/activate
python3 $SRC_DIR/main.py
