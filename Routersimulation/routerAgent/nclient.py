import socket
import numpy as np
import time

'''Simple Client in python
   python nclient.py
   localhost/port specified 
'''

iteration = 5
fbUrl = "http://facebook.com"
ytUrl = "http://youtube.com"

def getrandomPort():
    rport = np.random.randint(10000)
    return rport

def getrandomStreamKey():
    n = np.random.randint(iteration * 100)
    streamkey = "stream" + (str(n))
    return streamkey


for i in range(iteration):
    host = "localhost"
    port = 500                   # The same port as used by the server

   # Create the data to be sent
    rport = getrandomPort()
    streamkey = getrandomStreamKey()
    msg = "switcher.ip.address |" + streamkey + " |" + str(rport) + "|" \
           + fbUrl + "|" + ytUrl + ";"
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int(port)
    start = time.time()         # Start time
    s.connect((host, port))
    s.sendall(msg.encode('utf8'))
    data = s.recv(1024)
    end = time.time()           # end time
    print("time to connect: " + str(end-start))
    print('Received', repr(data))
print("completed")
