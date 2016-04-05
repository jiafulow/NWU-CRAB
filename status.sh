#!/bin/bash

for d in crab_projects/*/
do
    crab status -d $d
done
