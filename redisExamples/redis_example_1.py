import redis
import time
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import mysql.connector
from mysql.connector import errorcode


# globals
# connect with Staging
rp = redis.StrictRedis(host='35.193.241.194', port=6379,
    password='7913511eca0b03a225a5d9cc60ce65800f3c37b059116898b189acbcd54cdcb6')

rr = redis.Redis(host='35.193.241.194', port=6379,
    password='7913511eca0b03a225a5d9cc60ce65800f3c37b059116898b189acbcd54cdcb6')

# connect with Perf
rs = redis.StrictRedis(host='35.232.62.92', port=6379,
    password='a304a11072df60bca0a14666528e79636336b0692fd8ecd98c33e79b99ccb2c0')

# Output files
fswitch = "switcher.csv"
frtmp  = "rtmp.csv"

#DB_NAME = 'employees'

TABLES = {}
TABLES['staging3-rtmp_queueu'] = (
    "CREATE TABLE `staging3-rtmp_queue` ("
    "  `time` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")





def redisKey(ky):
    if rp.exists(ky):
        return(rp.llen(ky))
    else:
        print(ky + "does not exist")
        return(0)

def redisCard(ky):
    if rp.exists(ky):
        return(rp.scard(ky))
    else:
        print(ky + "does not exist")
        return(0)

'''Capture all the Init Data before a run of router
   1. Length of Session
   2. Lenght of RTMP Queue and Switcher Queue
'''
def initData(debug=False):
    with open("config.json", "r") as json_file:
        configJson = json.load(json_file)

    if debug:
        print(configJson)
    

    # capture relevant Json config
    rtmp_queue_limit = configJson["rtmp_queue_limit"]
    switcher_queue_limit = configJson["switcher_queue_limit"]

    # Capture data from Redis 
    cs = redisCard("switcher_ips")
    cr = redisCard("rtmp_ips")
    crl = rp.smembers("rtmp_ips")
    print(type(crl))
    print(crl)
    for x in crl:
        print(type(x))
        y = x.rpartition(b',')
        print(type(y))
        print(str(y[0].decode('utf-8')))
        print(str(y[1].decode('utf-8')))
        print(str(y[2].decode('utf-8')))
        print(x)
    #crl = rp.type("rtmp_ips")
    la = redisKey("app_sessions")
    lr = redisKey("rtmp_queue")
    ls = redisKey("switcher_queue")
    if debug:
        print("Switcher IPS " + str(cs))
        print("RTMP IPS len " + str(cr))
        print("RTMP IPS " + str(crl))
        print("RTMP Queue Limit " + str(rtmp_queue_limit))
        print("Switcher Queue Limit " + str(switcher_queue_limit))
        print("App Sessions " + str(la))
        print("Current RTMP Queue " + str(lr))
        print("Current Switcher Queue " + str(ls))

# Connect to MySql DB
def connectMySQL():
    try:
        cnx = mysql.connector.connect(user='apidevuser', password='DevApp@9967',
                              host='35.192.65.205',
                              database='otter')    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

'''Capture RTMP and Switcher Queue length in Redis and write
        it out to a file.
        Parameters:
        rtime: length of time to collect statistics of RTMP and Switcher Queue, 
              default is 1 minute. The time is in minutes
        Sample: Sample the queues in milliseconds, default is 500 milliseconds.
               Sample time is in milliseconds
        debug: dump debug info
'''
# Capture RTMP and Switcher Queue with sampling rate
def dataRSQueue(rtime=1,sample=500,debug=True):
    i = 0
    j = 0
    # time in minutes convert to secondes
    t = 1 * 60 * 1000.0
    sample = 500 
    fs = open(fswitch, "w")
    fr = open(frtmp, "w")
    while i < t:
        fs.write(str(j) + "  ")
        fr.write(str(j) + "  ")
        fr.write(str(redisKey("switcher_queue")))
        fs.write(str(redisKey("rtmp_queue")))
        fr.write("\n")
        fs.write("\n")
        #wait for seconds
        time.sleep(0.5)
        i = i + sample
        j = j + 1

# List Current Clients
def currentClients(debug=False):
    print("Client list")
    print(len(rp.client_list()))
    i = 0
    if debug:
        for s in rp.client_list():
            i = i + 1
            print("client-" + str(i) + " " + str(s))

# Plot RTMP/Switcher Queues - Resources remaining
def plotQ():
    x1, y1 = np.loadtxt(fswitch, unpack=True, delimiter = '  ')
    x2, y2 = np.loadtxt(frtmp, unpack=True, delimiter = '  ')
    plt.plot(x1, y1, 'r--', x2, y2, 'bs')
    plt.show()

initData(debug=True)
connectMySQL()
#dataRSQueue(1,500,True)
#currentClients()
#plotQ()

'''
# Check Contact
if rp.exists(b'contacts'):
    #s = rp.get("contacts")
    print('Contacts')
    print(rp.llen(b'contacts'))
else:
    print("contacts does not exist")

# Check RTMP Queue
if rp.exists("rtmp_queue"):
    #s = rp.get("rtmp_queue")
    print('Rtmp Queue')
    print(rp.llen('rtmp_queue'))
else:
    print("rtmp queue does not exist")

# check switcher queue
if rp.exists('switcher_queue'):
    #s = rp.get("switcher_queue")
    print('Switcher Queue')
    print(rp.llen('switcher_queue'))
else:
    print("switcher queue does not exist")

print(rp.keys(pattern="*contacts*"))



# List configuration
print("-------------------------------------------------")
print("Configuration")
print(rp.config_get())

# Number of Keys in database
# keys should be deleted if not in use
print("-------------------------------------------------")
print("Keys in Database")
print(rp.dbsize())

# iterate through all keys
print(rp.keys())
print(rp.keys(pattern="*queue"))
for key in rp.scan_iter():
    # delete the key
    print(key)
'''




#"redis_host":"35.193.241.194",
# "redis_port":"6379",
# "vm_api_url": "http://35.232.60.100:1936", 
# "redis_password":"7913511eca0b03a225a5d9cc60ce65800f3c37b059116898b189acbcd54cdcb6"
#SWITCHER_REDIS_HOST='35.232.62.92'
#SWITCHER_REDIS_PORT='6379'
#SWITCHER_REDIS_PASSWORD='a304a11072df60bca0a14666528e79636336b0692fd8ecd98c33e79b99ccb2c0'