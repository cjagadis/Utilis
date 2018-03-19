import os

''' Server names and external ip address
    External IP address is not required 
    Google converts servernames to local ip address
'''

svrNgRtmpi = ["demo3", "104.197.55.47"]    # Nginx RTMP input streams
svrSwitchn = ["demo3", "104.197.55.47"]    # Switching Server
svrRouting = ["demo3", "104.197.55.47"]   # Routing Server
svrApplitn = ["devserver1", "35.193.196.92"]    # Application Server
svrNgRtmpm = ["demo4", "35.188.117.232"]   # Nginx RTMP output streams


# Common glcoud command for remote shell execution
gcshell = "gcloud --quiet compute ssh --ssh-key-file=~/.ssh/compute_engine  --zone us-central1-c"

# Construct the gcloud remote shell authentication
gcsvrNgRtmpi = gcshell + "jagadissh" + "@" + svrNgRtmpi[0] 
gcsvrSwitchn = gcshell + "jagadissh" + "@" + svrSwitchn[0]
gcsvrRouting = gcshell + "jagadissh" + "@" + svrRouting[0] 
gcsvrApplitn = gcshell + "jagadissh" + "@" + svrApplitn[0] 
gcsvrNgRtmpm = gcshell + "jagadissh" + "@" + svrNgRtmpm[0] 

# Specify the order of server names. GCP DNS will convert server namee to local ips
svrOrder = [svrNgRtmpi[0], svrNgRtmpm[0], svrRouting[0], svrSwitchn[0], svrApplitn[0]]

# Specify the commands in each server
svrCommands = {
    svrNgRtmpi[0]: ["sudo /usr/local/nginx/sbin/nginx -s stop && sudo /usr/local/nginx/sbin/nginx"],
    svrNgRtmpm[0]: ["sudo /usr/local/nginx/sbin/nginx -s stop && sudo /usr/local/nginx/sbin/nginx"],
    svrRouting[0]: ["/home/dileepa/c/screen -dmS node node app.js && /home/dileepa/r/screen -dmS node node app.js"],
    svrSwitchn[0]: ["cd /home/dileepa/v4 && ./rtmprs -i rtmp://104.197.55.47:1935/src/Camera1 -i rtmp://104.197.55.47:1935/src/Camera2 -i rtmp://104.197.55.47:1935/src/Camera3 -o rtmp://35.188.117.232:1935/src/all -s cam1 -p 1988 -b 10 -v"],
    svrApplitn[0]: ["cd /opt/Shafeek/Switcher && forever start index.js"]
    }

for svr in svrOrder:
    commands = svrCommands[svr]
    cmnd = ''.join(commands)         # convert coomand in list format to string

    '''Create a gcloud ssh command the example is:
       gcloud --quiet compute ssh --ssh-key-file=~/.ssh/compute_engine  jagadish@demo4 \
                --zone us-central1-c --command 'cd /home && ls -l'
       demo4 is the name of server. Google will conver this to local IP
    '''
    
    gcCommands = gcshell + "jagadish" + "@" + svr + "--command" + cmnd    
    print(gcCommands)
    # os.system(gcCommands)   # call this to execute the commands to start services cleanly

