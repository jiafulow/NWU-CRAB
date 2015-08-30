#!/usr/bin/env python

import os
import re


old_dir = "/eos/uscms/store/user/jiafu/HZG/nuTuples_v9.10_8TeV/MC/TTToHCWB_HToMuMu_M-30_8TeV_pythia8175/"
new_dir = "/tthome/share/noobs/nuTuples_v9.10_8TeV/MC/TT_FCNH_M30/"

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
def check():
    files = os.listdir(old_dir)
    
    if len(files) == 0:
        raise Exception("No file is found.")
    
    print "There are %i files." % (len(files))
    
    files = sorted(files, key=natural_sort_key)
    
    last_file = files[-1]
    last_file_s = split(last_file)
    
    if last_file_s[0] != "nuTuple_" or not last_file_s[1].isdigit():
        raise Exception("File name is not matched.")
    
    print "There should be %i files." % (int(last_file_s[1]))
    
    if not len(files) == int(last_file_s[1]):
        raise Exception("Some files are missing.")
        
    print "All the files are there."
    

def transfer():
    print bcolors.BOLD + "\n>>> Transfer <<<" + bcolors.ENDC
    print 'ssh -Y %s "mkdir -p %s"' % (remote_host, new_dir)
    print 'scp -pr %s %s:%s' % (old_dir, remote_host, new_dir)


# ______________________________________________________________________________
if __name__=="__main__":
    
    print "Transfer from:"
    print old_dir
    print "Transfer to:"
    print new_dir
    
    check()
    
    transfer()
