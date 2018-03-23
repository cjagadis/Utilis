'''
    Example to show that  system
    command can be called 
    in pyton.
'''

import os
#ret = os.system("ps aux")
#print(ret)


ret1 = os.system("gcloud --quiet compute ssh --ssh-key-file=~/.ssh/compute_engine  jagadish@demo4 --zone us-central1-c --command 'cd /home && ls -l'")
print(ret1)
