import json
import argparse
import logging as log
import os
import subprocess
import time
import settings
import buildimg
import buildapp
import callscripts
import updatejson

if __name__ ==  '__main__':
    print("calling init")
    settings.init()
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
    log.info("main:in the build.py file")

    log.debug('main:argument file = '+ args.file)

    # read the build json file - build.json

    with open(args.file, 'r') as buildFile:
        buildDict = json.load(buildFile)
        log.debug("main:json file")
        log.debug(buildDict)

    # JSON Variables extracted from JSON build file
    otterName   = buildDict["g-name"]
    otterVers   = buildDict["g-version"]
    otterEnv    = buildDict["g-env"]
    otterStatus = buildDict["g-status"]
    otterDate   = buildDict["g-date"]
    otterInst   = buildDict["instances"]

    # Build Google Image List and set it to global variable images
    buildimg.buildImageList()


    '''If the global status is active, all the
        applications in Json file is build even if they
        have inddividual status as inactive. The global
        active status overrides the individual application
        status. 
    '''
    if otterStatus == "active":
        otterBuildAll = True
        log.info("main:global build status is active")
        log.info("main:all server builds are requested")

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
            log.info("main:build list from JSON as Key-Value pair as below")
        log.info(buildKV)
    else:            # global status is not active
        log.info("main:global build status is not active")
        log.info("main:check for individual app build status for active")
        buildKV = {}    # server key value pair
        i = 0           # value of the server  - order which they appear in jsone
        for inst in otterInst:
            if inst["status"] == "active":  # only build apps with active stats
                buildKV[inst["prefix"]] = i
                i = i+1
        log.info("main:build list from JSON as Key-Value pair as below with global active not set")
        log.info(buildKV)

    ''' The KV pair of servers that need to built
        is captured. We now have to match the order
        in which the servers have to be built and
        the creates the script and build. The global
        buildScript has all the scripts that will be called
    '''

    for b in settings.buildOrder:
        log.info("main:before build application: " + b)
        if b in buildKV:       # check if the application needs to be built
            log.info("main:matched the application: " +b)
            i = buildKV[b]     # get the index of instance
            buildapp.buildApplication(otterInst[i],b)

    log.info(settings.buildScript)


    val = callscripts.callScripts()
    if val == True:
        log.info("Build was successful")
        updatejson.updateJsonTimeBuild(args.file, buildDict)       # update JSON build number and time
