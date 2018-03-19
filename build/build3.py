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

#testCmd=""

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
     # Call the build script with all the options
    if appInst["image"] == "":
        imageOption = "-n"   # build a new image
        if appInst["branch"] == "":
            branch = "main"
            log.info("buildApplication: branch = " + branch)
        else: 
            branch = appInst["branch"]
        scriptName = appInst["prefix"] + ".sh " + imageOption + " -b " \
                        + appInst["branch"] + " -t " + appInst["tag"] + " -s " \
                        + appInst["subnetwork"]
    else:
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
    for b in buildOrder:
        log.info("before build application: " + b)
        if b in buildKV:       # check if the application needs to be built
            log.info("matched the application: " +b)
            i = buildKV[b]     # get the index of instance
            buildApplication(otterInst[i],b)
else:            # global status is not active
    log.info("global active flag is not set")
    buildKV = {}    # server key value pair
    i = 0           # value of the server  - order which they appear in jsone
    for inst in otterInst:
        if inst["status"] == "active":  # only build apps with active stats
            buildKV[inst["prefix"]] = i
            i = i+1
    log.info("build list from JSON as Key-Value pair as below with global active not set")
    log.info(buildKV)
    for b in buildOrder:
        log.info("before build application: " + b)
        if b in buildKV:       # check if the application needs to be built
            log.info("matched the application: " +b)
            i = buildKV[b]     # get the index of instance
            buildApplication(otterInst[i],b)

for inst in otterInst:
    lenI = len(inst)
    log.debug("instance length = " + str(lenI))
    log.debug(inst)
    
    instanceName = inst["name"]
    if instanceName == "appserver":
        log.info("appserver build requested")
    elif instanceName == "routerserver":
        log.info("router server build requested")
    elif instanceName == "switcherserver":
        log.info("switcher build requested")
    elif instanceName == "rtmpserver":
        log.info("rtmp server build requested")

        # Check if the local server build is active
        if not appServerBuild:
            if inst["status"] == "active":
                appServerBuild = True
                log.info("appserver build is requested")

        # Check if we need to build
        if appServerBuild == True:
            appServerImage = inst["prefix"]+"-V"+inst["tag"] + inst["build"]
            log.info("appserver Image = " + str(appServerImage))

        # Call the build script with all the options
        if inst["image"] == "":
            imageOption = "-n"   # build a new image
            if inst["branch"] == "":
                branch = "main"
            else: 
                branch = inst["branch"]
                scriptName = inst["prefix"] + ".sh" + " " + imageOption + " -b " \
                        + inst["branch"] + " -t " + inst["tag"] + " -s " \
                        + inst["subnetwork"]
        else:
            imageOption = " -i "     # use existing image
            scriptName = inst["prefix"] + ".sh" + " " + imageOption \
                        + inst["image"] + " -t " + inst["tag"] + " -s " \
                        + inst["subnetwork"]
        log.info("script called = " + scriptName)


    elif instanceName == "switcher":
        log.info("switcher server build reauested")

    checkImages("test")
