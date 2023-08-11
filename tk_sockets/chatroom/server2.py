import socket
from threading import Thread

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

def send():
    while True:
        data = input()
        w = "Server: " + data
        conn.sendall(w.encode())

def receive():
    while True:
        incoming = conn.recv(102)
        print(incoming.decode())

x = Thread(target=send)
y = Thread(target=receive)

x.start()
y.start()


s.close()