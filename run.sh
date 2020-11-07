#!/bin/bash
BASE_DIR="$(cd "$(dirname "$0" )" && pwd )"
VENV_DIR=$BASE_DIR/venv
SRC_DIR=$BASE_DIR/src

source $VENV_DIR/bin/activate
python3 $SRC_DIR/main.py
