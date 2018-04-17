import socket

host = 'localhost'      # Symbolic name meaning all available interfaces
port = 500            # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print(host + " , " + str(port))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Connected by', addr)

    try:
        data = conn.recv(1024)

        if not data: continue

        print(data)
        msg = "Server Says hi"
        conn.sendall(msg.encode('utf8'))

    except socket.error:
        print("Error Occured.")
        break

