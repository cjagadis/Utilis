import requests
import json
import socket

'''Simulating routing agent
   The router agent (routeragent.py) has received the forwarded request
   The HTTP/LB is simulated by librouter.py using
   Sanic acting as Asynchronous HTTP Server
   The routeragent.py then sends a request to routerswitchagent.py.
   The routerswitchagent.py is listening on switcher servers
'''
host='localhost'
port=500


'''Simple Client in python
   python nclient.py
   localhost/port specified 
'''
def nclientFunc(host, port, msg):
    port = int(port)        # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(msg.encode('utf8'))
    data = s.recv(1024)
    print('Received', repr(data))
    return

# GET
url3 = 'http://104.198.252.0:8000/'
r = requests.get(url3).json()
print(r)

# GET
url3 = 'http://104.198.252.0:8000/rtmp'
r = requests.get(url3)
data = r.json()
print(data)

if '200' in str(r): 
    msg = "rtmp request"
    nclientFunc(host,port,msg)
    print("success")

