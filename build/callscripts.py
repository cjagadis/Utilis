import settings
import logging as log
import os

def callScripts():
    for b in settings.buildOrder:
        if b in settings.buildScript: # the application needs to be built
            cmd = settings.buildScript[b]
            log.info("callScripts: " +  "building " + cmd)
        # construct the string to call the google cloud shell
 #           gc =  "gcloud --quiet compute ssh --ssh-key-file=~/.ssh/compute_engine jagadish@souvitestingdemo3 --zone us-central1-c --command " + "/home/kaushikaon/" + cmd 
            gc =  "/home/kaushikaon/" + cmd 
            log.info("callScripts:command to be executed by google shell")
            log.info(gc)
            ret = os.system(gc)
            ret = 0
            if (ret == 0):
                print("cmd" + " ran successfully")
            else:
                log.Fatal("Build Failed")
                return False 
    return True


