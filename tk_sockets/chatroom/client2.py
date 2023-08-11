import socket
from threading import Thread
host = 'localhost'
port = 12345

s = socket.socket()
s.connect((host,port))
print("connected")

import atexit
def handle_exit():
    print("runs after keyboard interrupt")
    s.close()


def send():
    while True:
        data = input()
        w = "Client: "+ data
        s.sendall(w.encode())

def receive():
    while True:
        incoming = s.recv(1025)
        print(incoming.decode())

x = Thread(target=send)
y = Thread(target=receive)

x.start()
y.start()

