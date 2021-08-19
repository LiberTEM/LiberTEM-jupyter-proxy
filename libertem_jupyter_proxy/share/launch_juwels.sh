#!/bin/bash

# you might need to modify your environment
# before you can start 'libertem-server'
# Do it here.

module purge > /dev/null
module use $OTHERSTAGES > /dev/null
module load Stages/2020 > /dev/null
module load GCCcore/.10.3.0 > /dev/null
module load libertem/0.7.1-Python-3.8.5 > /dev/null

libertem-server "$@"
