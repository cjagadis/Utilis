import os

# Server names and external ip address
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


'''
svrNgRtmpi = "demo3"  # Nginx RTMP input streams
svrSwitchn = "demo3"  # Switching Server
svrRouting = "demo3"  # Routing Server
svrApplitn = "devserver1"  # Application Server
svrNgRtmpm = "demo4"  # Nginx RTMP output streams
'''

'''
svrOrder = [svrNgRtmpi, svrNgRtmpm, svrRouting, svrSwitchn, svrApplitn]

svrCommands = {
    svrNgRtmpi: ["sudo /usr/local/nginx/sbin/nginx -s stop","sudo /usr/local/nginx/sbin/nginx"],
    svrNgRtmpm: ["sudo /usr/local/nginx/sbin/nginx -s stop","sudo /usr/local/nginx/sbin/nginx"],
    svrRouting: ["/home/dileepa/c/screen -dmS node node app.js","/home/dileepa/r/screen -dmS node node app.js"],
    svrSwitchn: ["cd /home/dileepa/v4", "./rtmprs -i rtmp://104.197.55.47:1935/src/Camera1 -i rtmp://104.197.55.47:1935/src/Camera2 -i rtmp://104.197.55.47:1935/src/Camera3 -o rtmp://35.188.117.232:1935/src/all -s cam1 -p 1988 -b 10 -v"],
    svrApplitn: ["cd /opt/Shafeek/Switcher", "forever start index.js"]
    }
'''
svrOrder = [svrNgRtmpi[0], svrNgRtmpm[0]]
svrCommands = {
    svrNgRtmpi[0]: ["sudo /usr/local/nginx/sbin/nginx -s stop && sudo /usr/local/nginx/sbin/nginx"],
    svrNgRtmpm[0]: ["sudo /usr/local/nginx/sbin/nginx -s stop && sudo /usr/local/nginx/sbin/nginx"],
    }

for svr in svrOrder:
    print(svr)
    type(svr)
    svrs = ''.join(svr)
    print(svrs)
    commands = svrCommands[svr]
    #gcCommands = gcshell + "jagadish" + "@" + svrs + "--command" + commands
    print(commands)


#retvalue =  os.system("ps aux")
#print(retvalue)
