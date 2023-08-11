import random
import time

import socket
from threading import Thread



allconnections = {}

def send(msg):
    for m in allconnections:
        allconnections[m].sendall(msg.encode())


def receive(conn,username):
    while True:
        try:
            message = conn.recv(1025).decode()
            print(message)
            send("<"+username+">: " + message)
        except:
            send("<"+username+"> "+ "has left the chat.")
            del allconnections[username]
            return

def manage():
    while True:
        s = socket.socket()
        host = ''
        port = 12345
        s.bind((host,port))
        s.listen(5)
        print("listening")
        conn, addr = s.accept()
        print(conn)
        print("got a connection from", addr)
        newuser = conn.recv(1025).decode()
        allconnections[newuser] = conn
        print(newuser)
        tempthread = Thread(target=receive, args=(conn,newuser))
        tempthread.start()
        send(newuser+" has joined the chat")


x = Thread(target=manage)
#y = Thread(target=receive)
x.start()
#y.start()
