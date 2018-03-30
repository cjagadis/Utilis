import settings
import logging as log

def callScripts():
    for b in settings.buildOrder:
        if b in settings.buildScript: # the application needs to be built
            cmd = settings.buildScript[b]
            log.info("callScripts: " +  "building " + cmd)
        # construct the string to call the google cloud shell
            gc =  "gcloud --quiet compute ssh --ssh-key-file=~/.ssh/compute_engine jagadish@demo4 --zone us-central1-c --command " + cmd
            log.info("callScripts:command to be executed by google shell")
            log.info(gc)
            # ret = os.system(gc)
            ret = 0
            if (ret == 0):
                print("cmd" + " ran successfully")
            else:
                log.Fatal("Build Failed")
                return False 
    return True


