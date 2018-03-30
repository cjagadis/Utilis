import socket

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
