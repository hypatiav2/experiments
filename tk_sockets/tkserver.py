import random
from tkinter import *
from tkinter import messagebox
import time

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


root = Tk()
root.geometry('600x600')
root.title("Server Chat Application")
root.configure(bg='black')


def send():
    data = entrybox.get()
    w = "Server: " + data
    conn.sendall(w.encode())
    chat = Label(frame1, text=data, fg='blue', anchor='e',bg='black',width=600)
    chat.pack(side=TOP,anchor=E)
    root.update()

def receive():
    while True:
        data = conn.recv(1025).decode()
        chat = Label(frame1, text=data, fg='red', anchor='w',bg='black',width=600)
        chat.pack(side=TOP,anchor=W)
        root.update()



frame1 = Frame(root,height=550,width=600,bg="black")
frame1.pack(fill=Y)

sendbttn = Button(root, text="SEND",command=send,width=500)
sendbttn.pack(side=BOTTOM)
entrybox = Entry(root, width=100)
entrybox.pack(side=BOTTOM)


y = Thread(target=receive)
y.start()

root.mainloop()