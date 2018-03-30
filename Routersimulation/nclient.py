import socket
'''Simple Client in python
   python nclient.py
   localhost/port specified 
'''

host = "localhost"
port = 500                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port - int(port)
s.connect((host, port))
msg = "Hello, World"
s.sendall(msg.encode('utf8'))
data = s.recv(1024)
print('Received', repr(data))
