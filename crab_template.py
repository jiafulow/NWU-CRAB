from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'XX-LABEL-XX'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'XX-CONFIG-XX'
config.JobType.outputFiles = ['Output.root']

config.Data.inputDataset = 'XX-DATASET-XX'
config.Data.inputDBS = 'global'
#config.Data.splitting = 'FileBased'
#config.Data.unitsPerJob = 1
config.Data.splitting = 'EventAwareLumiBased'
#config.Data.unitsPerJob = 10000
config.Data.unitsPerJob = 30000
config.Data.outLFNDirBase = '/store/group/lpchzg/makingBacon/01/XX-LABEL-XX/'
config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3'

config.Site.storageSite = 'T3_US_FNALLPC'


test_run = False
if test_run:
    config.Data.splitting = 'EventAwareLumiBased'
    config.Data.unitsPerJob = 200
    config.Data.totalUnits = 1
