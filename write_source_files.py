#!/usr/bin/env python

import os
import re


#ui_working_dir = "MC0"
ui_working_dir = "MC1"
#ui_working_dir = "FCNH_ntuple"
user_remote_dir = "/eos/uscms/store/user/jiafulow/HZG/nuTuples_v9.10_8TeV/MC/"

#ui_working_dir = "/uscms_data/d2/bpollack/ntuplesGitNew/CMSSW_5_3_14/src/NWU/ntupleProducer/test/MC/"
#user_remote_dir = "/eos/uscms/store/user/lpchzg/nuTuples_v9.10_8TeV/MC/"


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

warning = bcolors.WARNING + "WARNING" + bcolors.ENDC + ": "

# ______________________________________________________________________________
datasets = []

def check():
    global datasets
    datasets = os.listdir(ui_working_dir)
    datasets = filter(lambda x: os.path.isdir(os.path.join(ui_working_dir, x)), datasets)
    
    if len(datasets) == 0:
        raise Exception("No dataset is found.")
    
    print "There are %i datasets." % (len(datasets))
    
    datasets = sorted(datasets, key=natural_sort_key)
    
    # Find number of jobs submitted
    mydict1 = {}
    for dataset in datasets:
        crab_log = "{0}/{1}/log/crab.log".format(ui_working_dir, dataset)
        
        njobs = 0
        with open(crab_log) as f:
            for line in f.readlines():
                m = re.search("Total of ([0-9]+) jobs created.", line)
                if m:
                    njobs = int(m.group(1))
                    break
        if njobs == 0:
            raise Exception("You haven't submitted no job for %s" % dataset)
        
        mydict1[dataset] = njobs
    
    # Find number of output files
    mydict2 = {}
    for dataset in datasets:
        if not (os.path.exists(user_remote_dir) and
                os.path.exists(os.path.join(user_remote_dir, dataset)) and
                os.path.isdir(os.path.join(user_remote_dir, dataset))):
            #raise Exception("You haven't made the remote directory for %s" % dataset)
            print(warning + "You haven't made the remote directory for %s" % dataset)
            continue
        
        files = os.listdir(os.path.join(user_remote_dir, dataset))
        nfiles = len(files)
        
        mydict2[dataset] = nfiles
        
        if nfiles == 0:
            #raise Exception("You haven't got no output file for %s" % dataset)
            print (warning + "You haven't got no output file for %s" % dataset)
            continue
        
        mylist = []
        nduplicates = 0
        for f in files:
            ff = split(f)
            if ff[0] != "nuTuple_" or not ff[1].isdigit():
                raise Exception("File name is unexpected: %s" % f)
            
            ff[1] = int(ff[1])
            if ff[1] not in mylist:
                mylist.append(ff[1])
            else:
                nduplicates += 1
                print(warning + "Found duplicate in %s: %i" % (dataset, ff[1]))
    
    # Report
    print bcolors.BOLD + "\n>>> Report <<<" + bcolors.ENDC
    for dataset in datasets:
        percent = "%6.2f%%" % (100.*mydict2.get(dataset, 0)/mydict1[dataset])
        if percent == "100.00%":
            percent = bcolors.OKGREEN + percent + bcolors.ENDC
        print "{0:20s}:  {1:6d} / {2:6d}    [{3}]".format(dataset, mydict2.get(dataset, 0), mydict1[dataset], percent)

def write(xrd=True):
    srcdir = "sourceFiles/"
    ext = ".txt"
    if not os.path.exists(srcdir):
        os.mkdir(srcdir)

    print bcolors.BOLD + "\n>>> Write <<<" + bcolors.ENDC
    for dataset in datasets:
        if xrd:
            print "ls -v {0}/*.root | sed -e 's@^/eos/uscms@root://cmsxrootd-site.fnal.gov/@' > {1}".format(os.path.join(user_remote_dir, dataset), os.path.join(srcdir, dataset+ext))
        else:
            print "ls -v {0}/*.root > {1}".format(os.path.join(user_remote_dir, dataset), os.path.join(srcdir, dataset+ext))


# ______________________________________________________________________________
if __name__=="__main__":
    
    print "Working area:"
    print ui_working_dir
    print "Store area:"
    print user_remote_dir
    
    check()
    
    write()
