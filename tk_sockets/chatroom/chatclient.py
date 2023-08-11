import random
from tkinter import *
from tkinter import messagebox
import time

import socket
from threading import Thread
s = socket.socket()

root = Tk()
root.title("Client Chat Application")
root.geometry('600x600')
root.configure(bg='black')



def send():
    data = entrybox.get()
    s.sendall(data.encode())
    entrybox.delete(0,END)


def receive():
    global frame1
    while True:
        incoming = s.recv(1025).decode()
        print(incoming)
        chat = Label(frame1, text=incoming, fg='white', anchor='w',bg='black')
        chat.pack(side=TOP,anchor=W,fill=X)
        root.update()

def show_chat():
    global frame1
    host = 'localhost'
    port = 12345

    s.connect((host,port))
    print("connected")

    user = username.get()
    loginframe.pack_forget()
    frame1.pack(fill=BOTH,side=TOP)
    frame2.pack(side=BOTTOM)
    root.title(user)
    root.update()
    s.sendall(user.encode())

    y = Thread(target=receive)
    y.start()

    


frame1 = Frame(root,height=500,width=600,bg="black")
frame2 = Frame(root,height=500,width=600,bg="black")
loginframe =  Frame(root,height=500,width=600,bg="black")
loginframe.pack()


sendbttn = Button(frame2, text="SEND",width=500,command=send)
sendbttn.pack(side=BOTTOM)
entrybox = Entry(frame2, width=100)
entrybox.pack(side=BOTTOM)




username = Entry(loginframe)
username.pack()
joinbttn = Button(loginframe, text="Join chat",command=show_chat)
joinbttn.pack()


root.mainloop()