import json
import argparse
import logging as log
import subprocess

# Instance KV Variables
instanceInfo = {}

# Build Variables
otterBuildAll = False
appServerBuild = False
routerServerBuild = False
rtmpServerBuild = False
switchServerBuild = False

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
log.basicConfig(level=args.loglevel)

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

# Check to see if we need to build all specified apps
if otterStatus == "active":
    otterBuildAll = True
    appServerBuild = True
    routerServerBuild = True
    rtmpServerBuild = True
    switchServerBuild = True
    log.info("all server builds are requested")

def buildScriptCmd(inst):

# Iterate through all instances and check the
# applicatons that needs to be built
# and specify the options

for inst in otterInst:
    lenI = len(inst)
    log.debug("instance length = " + str(lenI))
    log.debug(inst)
    
    instanceName = inst["name"]
    if (instanceName == "appserver"):
        log.info("appserver build requested")

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
