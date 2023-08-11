import socket
s = socket.socket()
host = ''
port = 12345
s.bind((host,port))
s.listen(5)
print("listening")
conn, addr = s.accept()
print("got a connection from", addr)

import atexit
def handle_exit():
    print("runs after keyboard interrupt")
    s.close()
atexit.register(handle_exit)

while True:
    data = input("Server:")
    conn.sendall(data.encode())
    data = conn.recv(1024)
    print(addr, ";" , data.decode())
    if data.decode() == 'stop':
        atexit.register(handle_exit)