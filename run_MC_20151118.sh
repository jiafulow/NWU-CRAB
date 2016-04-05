#!/bin/bash

cfg=makingBacon_MC_25ns_MINIAOD_20151118.py

# DAS query:
#   dataset=/*/*RunIISpring15MiniAODv2*/MINIAODSIM

# Z+jets
./run.sh DYJetsToLL_M-50                /DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM  $cfg

# ttbar
./run.sh TTJets_amcatnlo                /TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v3/MINIAODSIM           $cfg
