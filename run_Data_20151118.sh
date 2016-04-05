#!/bin/bash

cfg=makingBacon_Data_25ns_MINIAOD_20151118.py

# DAS query:
#   dataset=/*/Run2015D-PromptReco-v4/MINIAOD
#   dataset=/*/Run2015*05Oct2015*/MINIAOD

# DoubleMuon
./run.sh DoubleMuon_Run2015D-05Oct2015-v1   /DoubleMuon/Run2015D-05Oct2015-v1/MINIAOD                                                                           $cfg
./run.sh DoubleMuon_Run2015D-PromptReco-v4  /DoubleMuon/Run2015D-PromptReco-v4/MINIAOD                                                                          $cfg

# DoubleEG
./run.sh DoubleEG_Run2015D-05Oct2015-v1     /DoubleEG/Run2015D-05Oct2015-v1/MINIAOD                                                                             $cfg
./run.sh DoubleEG_Run2015D-PromptReco-v4    /DoubleEG/Run2015D-PromptReco-v4/MINIAOD                                                                            $cfg
