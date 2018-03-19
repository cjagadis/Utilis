import json
import argparse
import logging as log
import subprocess
import time

# Instance KV Variables
instanceInfo = {}

# Build Variables
otterBuildAll = False
appServerBuild = False
routerServerBuild = False
rtmpServerBuild = False
switchServerBuild = False

'''build Order - the order which the build serveres needs to build
   It is impoortan to have prefix name in JSON which is used below
   It is not required to have all applications to be built. The order
   however will be followed for configurationn are dependent on the
   order of the build.
'''
buildOrder = ["rtmpserver", "switcherserver", "routerserver", "appserver"]


''' Get the list of images
    form Google Cloud and match the
    img. If the image exist
    return true
'''
def checkImages(img):
    imageListCmd = "gcloud image list"
    testCmd = "ls -l"
    process = subprocess.Popen(testCmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--debug',
    help="print debugging statements",
    action="store_const", dest="loglevel", const=log.DEBUG,
    default=log.WARNING,
)
parser.add_argument('-v', '--verbose',
    help="verbose",
    action="store_const", dest="loglevel", const=log.INFO,
)
parser.add_argument("-f", "--file", type=str, required=True)
args = parser.parse_args()

# set up logging
log.basicConfig(level=args.loglevel, format='%(asctime)s - %(levelname)s - %(message)s')
log.info("in the build.py file")

log.debug('argument file = '+ args.file)

with open(args.file, 'r') as buildFile:
    buildDict = json.load(buildFile)

for b in buildDict:
    print(b)

# JSON Variables
otterName   = buildDict["name"]
otterVers   = buildDict["version"]
otterEnv    = buildDict["env"]
otterStatus = buildDict["status"]
otterDate   = buildDict["date"]
otterInst   = buildDict["instances"]

def buildApplication(appInst,app):
    log.info("buildApplication: building the " + app)
    log.info("buildingapplication: appInstance ")
    log.info(appInst)
    
    if appInst["image"] == "":                      # if the image is not set
        imageOption = "-n"                          # build a new image
        if appInst["branch"] == "":
            branch = "main"
            log.info("buildApplication: branch = " + branch)
        else: 
            branch = appInst["branch"]
        scriptName = appInst["prefix"] + ".sh " + imageOption + " -b " \
                        + branch + " -t " + appInst["tag"] + " -s " \
                        + appInst["subnetwork"]
    else:                                           # image is specified
        log.info("buildApplication: Image = " + appInst["image"])

        imageOption = " -i "     # use existing image
        scriptName = appInst["prefix"] + ".sh " + imageOption \
                      + appInst["image"] + " -s "  \
                      + appInst["subnetwork"]
    log.info("buildApplication: script called = " + scriptName)

'''If the globa status is active, all the
   applications in Json file is build even if they
   have inddividual status as inactive. The global
   active status overrides the individual application
   status. 
'''
if otterStatus == "active":
    otterBuildAll = True
    log.info("global build status is active")
    log.info("all server builds are requested")

    # check instances to built and should be in order
    # format is: {"appserver':1, "switcherserver:"2, etc}
    # they can be in any order, but we hve to force the build order as
    # rtmp - switcher - router - appserver
    # And this is specified in the buildOrder global

    buildKV = {}    # server key value pair
    i = 0           # value of the server  - order which they appear in jsone
    for inst in otterInst:
        buildKV[inst["prefix"]] = i
        i = i+1
    log.info("build list from JSON as Key-Value pair as below")
    log.info(buildKV)
else:            # global status is not active
    log.info("global build status is not active")
    log.info("check for individual app build status for active")
    buildKV = {}    # server key value pair
    i = 0           # value of the server  - order which they appear in jsone
    for inst in otterInst:
        if inst["status"] == "active":  # only build apps with active stats
            buildKV[inst["prefix"]] = i
            i = i+1
    log.info("build list from JSON as Key-Value pair as below with global active not set")
    log.info(buildKV)

''' The KV pair of servers that need to built
    is captured. We now have to match the order
    in which the servers have to be built and
    the creates the script and build
'''

for b in buildOrder:
    log.info("before build application: " + b)
    if b in buildKV:       # check if the application needs to be built
        log.info("matched the application: " +b)
        i = buildKV[b]     # get the index of instance
        buildApplication(otterInst[i],b)
