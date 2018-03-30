import settings
import json
import logging as log

'''The Josn file will have updated
   time and build numbe
   Inpute: file - Json file to be updated
           buildDict - input Jsone file in dictrionary
'''
def updateJsonTimeBuild(file, buildDict):
    otterInst  =  buildDict["instances"]
    log.info("updateJsonTimeBuild:")
    for inst in otterInst:
        if inst["prefix"] in settings.buildScript:       # the server that was built
            log.info("updateJsonTimeuild:json for server updated")
            log.debug(inst)
            buildNumber = int(inst["build"])    # convert string to integer
            buildNumber = buildNumber + 1
            inst["build"] = str(buildNumber)    # build number in incremented
            log.info("updateJsonTime:New build number = " + inst["build"])
    log.info("updateJsonTime:updating Json file")
    with open(file, 'w') as outfile:  
        json.dump(buildDict,indent=4,  outfile)           # buildDict has the entire Json File


