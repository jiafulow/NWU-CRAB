#!/bin/bash

label=$1
dataset=$2
config=$3

rm -rf crab_projects/crab_${label}
/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select mkdir /store/group/cmst3/group/monojet/production/05/${label}
sed "s@XX-LABEL-XX@$label@g" crab_template.py | sed "s@XX-DATASET-XX@$dataset@g" | sed "s@XX-CONFIG-XX@$config@g"   > crab.py
crab submit -c crab.py
mv crab.py old/crab_${label}.py
