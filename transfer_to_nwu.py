#!/usr/bin/env python

import os
import re


#old_dir = "/eos/uscms/store/user/jiafu/HZG/nuTuples_v9.10_8TeV/MC/TTToHCWB_HToMuMu_M-30_8TeV_pythia8175/"
#new_dir = "/tthome/share/noobs/nuTuples_v9.10_8TeV/MC/TT_FCNH_M30/"

old_dir = "/uscms_data/d2/jiafu/HZG/CMSSW_6_1_1/src/HZG_Analyzer/HiggsZGAnalyzer/skims/nuTuples_v9.10_8TeV/MC/"
new_dir = "/tthome/jiafulow/HZG/CMSSW_6_1_1/src/HZG_Analyzer/HiggsZGAnalyzer/skims/nuTuples_v9.10_8TeV/MC/"

remote_host = "jiafulow@ttgrid01.ci.northwestern.edu"


# ______________________________________________________________________________
def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    """
    from http://stackoverflow.com/questions/4836710/does-python-have-a-built-in-function-for-string-natural-sort
    """
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)]

def split(s, _nsre=re.compile('([0-9]+)')):
    return re.split(_nsre, s)

class bcolors:
    """
    from http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ______________________________________________________________________________
datasets = []

def check():
    global datasets
    datasets = os.listdir(old_dir)
    datasets = filter(lambda x: os.path.isdir(os.path.join(old_dir, x)), datasets)

    if len(datasets) == 0:
        raise Exception("No dataset is found.")

    print "There are %i datasets." % (len(datasets))

    datasets = sorted(datasets, key=natural_sort_key)

    print "-" * 20
    for dataset in datasets:
        print dataset
    

def transfer(rsync=True):
    print bcolors.BOLD + "\n>>> Transfer <<<" + bcolors.ENDC
    if not rsync:
        print 'ssh -Y %s "mkdir -p %s"' % (remote_host, new_dir)
        print 'scp -pr %s %s:%s' % (old_dir, remote_host, new_dir)
    else:
        print 'rsync -avz %s %s:%s' % (old_dir, remote_host, new_dir)


# ______________________________________________________________________________
if __name__=="__main__":
    
    print "Transfer from:"
    print old_dir
    print "Transfer to:"
    print new_dir
    
    check()
    
    transfer()
