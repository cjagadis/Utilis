import socket
import select
import sys

'''RouterSwitchAgent sits on all the switcher
   server listeing on a particular port. They
   handle requests from routeragents to allocate
   switcher resources
'''

host = 'localhost'      # Symbolic name meaning all available interfaces
port = 500            # Arbitrary non-privileged port
msg  = 'Server Says:hi'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print(host + " , " + str(port))
s.listen(1)
while True:
    conn, addr = s.accept()
    print('Connected by', addr)

    try:
        data = conn.recv(1024)

        if not data: 
            continue
        sys.stdout.write(data.decode('utf8'))
        conn.sendall(msg.encode('utf8'))

    except socket.error:
        print("Error Occured.")
        break

#conn.close()
