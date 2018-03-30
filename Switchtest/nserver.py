import socket

host = 'localhost'      # Symbolic name meaning all available interfaces
port = 500            # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print(host + " , " + str(port))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:

    try:
        data = conn.recv(1024)

        if not data: break

        print("Client Says: "+data)
        conn.sendall("Server Says:hi")

    except socket.error:
        print("Error Occured.")
        break

conn.close()
