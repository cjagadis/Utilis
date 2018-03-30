import logging as log
import checkimg
import settings
'''Build the command list
   as key value pair. The
   key used is the application
   prefix For example: "appserver" for 
   application server, etc
'''
def buildApplication(appInst,app):
    scriptName = ""
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
        settings.buildScript[appInst["prefix"]] = scriptName

    else:                                           # image is specified
        log.info("buildApplication: Image = " + appInst["image"])
        if (checkimg.checkImages(appInst["image"])):
            log.info("matched the image")
        else:
            log.info("image was not matched")
        imageOption = " -i "     # use existing image
        scriptName = appInst["prefix"] + ".sh " + imageOption \
                      + appInst["image"] + " -s "  \
                      + appInst["subnetwork"]
        settings.buildScript[appInst["prefix"]] = scriptName
    log.info("buildApplication: script called = " + scriptName)

