import random
from tkinter import *
from tkinter import messagebox
import time

import socket
from threading import Thread
host = 'localhost'
port = 12345


root = Tk()
root.title("Client Chat Application")
root.geometry('600x600')
root.configure(bg='black')

s = socket.socket()
s.connect((host,port))
print("connected")


def send():
    data = entrybox.get()
    w = "Client: "+ data
    s.sendall(w.encode())
    chat = Label(frame1, text=data, fg='blue', anchor='e',bg='black',width=600)
    chat.pack(side=TOP)
    root.update()

def receive():
    while True:
        incoming = s.recv(1025).decode()
        chat = Label(frame1, text=incoming, fg='red', anchor='w',bg='black',width=600)
        chat.pack(side=TOP,anchor=W)
        root.update()

frame1 = Frame(root,height=500,width=600,bg="black")
frame1.pack()


sendbttn = Button(root, text="SEND",command=send,width=500)
sendbttn.pack(side=BOTTOM)
entrybox = Entry(root, width=100)
entrybox.pack(side=BOTTOM)


y = Thread(target=receive)
y.start()


root.mainloop()