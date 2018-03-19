'''
    Testin the Socket protocol
'''
import socket
# import pdb

# pdb.set_trace()

host = 'localhost'
port = 2000
buf = 1024

data = ['List', 'Status']

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
client.connect((host, port))
client.setblocking(0)      #non-blocking socket
#recvs = client.recv(buf)
#print("buf len recv: " + str(len(recvs)))
#print("Server Output: " + recvs.decode('utf8'))


for l in data:
    datas = l+"\n"
    print("sending: " + datas)
    client.send(datas.encode('utf8'))
    while 1:
        print("while")
        recvs = client.recv(1024)
        print("buf len recv: " + str(len(recvs)))
        print("Server Output: " + recvs.decode('utf8'))
        if not recvs:
            break

client.close()

