#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

ARGS="$*"

python $SCRIPTPATH/env_scanner.py $ARGS

