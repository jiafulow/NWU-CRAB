#!/bin/bash

label=$1
dataset=$2
config=$3
projdir=crab_${label}

mkdir -p crab_projects crab_projects_old
rm -rf crab_projects_old/${projdir}
[ -d crab_projects/${projdir} ] && mv crab_projects/${projdir} crab_projects_old
sed "s@XX-LABEL-XX@$label@g" crab_template.py | sed "s@XX-DATASET-XX@$dataset@g" | sed "s@XX-CONFIG-XX@$config@g"   > crab.py
crab submit -c crab.py
#crab submit -c crab.py --dryrun
cp crab.py crab_projects/${projdir}/
