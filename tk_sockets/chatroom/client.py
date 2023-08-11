import socket
host = 'localhost'
port = 12345

s = socket.socket()
s.connect((host,port))
print("connected")

import atexit
def handle_exit():
    print("runs after keyboard interrupt")
    s.close()


while True:
    data = s.recv(1024)
    print(data.decode())
    if data.decode() == 'stop':
        atexit.register(handle_exit)
    data = input("Client:")
    s.sendall(data.encode())