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

import random
import pygame    ###draw a checker board   CORRECT
from pygame.locals import *
pygame.init()
m=700
n=700
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("My game")
a=(255,0,0)
b=(0,0,255)
white=(255,255,255)
black=(0,0,0)
x=0
y=0


def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))



def check():
    for i in d:
        if d[1]==d[2]==d[3]!="":
            screen.fill(black)
            show_text("Winner is",100, 200,(255,255,255),100)
            show_text(d[1],150, 300,(255,255,255),100)
            break
        elif d[4]==d[5]==d[6]!="":
            screen.fill(black)
            show_text("Winner is",150, 200,(255,255,255),100)
            show_text(d[4],150, 300,(255,255,255),100)

           #print('Winner is',d[4])
            break
        elif d[7]==d[8]==d[9]!="":
            screen.fill(black)
            show_text("Winner is",150, 200,(255,255,255),100)
            show_text(d[7],150, 300,(255,255,255),100)

            #print('Winner is',d[7])
            break
        elif d[1]==d[4]==d[7]!="":
            screen.fill(black)
            show_text("Winner is",150, 200,(255,255,255),100)
            show_text(d[1],150, 300,(255,255,255),100)

            #print('Winner is',d[1])
            break
        elif d[2]==d[5]==d[8]!="":
            screen.fill(black)
            show_text("Winner is",150, 200,(255,255,255),100)
            show_text(d[5],150, 300,(255,255,255),100)
            #print('Winner is',d[2])
            break
        elif d[3]==d[6]==d[9]!="":
            screen.fill(black)
            show_text("Winner is",150, 200,(255,255,255),100)
            show_text(d[9],150, 300,(255,255,255),100)
            #print('Winner is',d[3])
            break
        elif d[1]==d[5]==d[9]!="":
            screen.fill(black)
            show_text("Winner is",150, 200,(255,255,255),100)
            show_text(d[1],150, 300,(255,255,255),100)
            #print('Winner is',d[1])
            break
        elif d[3]==d[5]==d[7]!="":
            screen.fill(black)
            show_text("Winner is",150, 200,(255,255,255),100)
            show_text(d[5],150, 300,(255,255,255),100)
            #print('Winner is',d[3])
            break
        else:
            return False
 



d={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
turn=1
for y in range(0,600,200):
    for x in range(0,600,200):
        pygame.draw.rect(screen,a,(x,y,200,200))
        x=x+200
        a,b=b,a
    pygame.display.update()
    

while True:
    data = conn.recv(1024)
    print(addr, ";" , data.decode())

    
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            if event.button==1 and turn%2==0:
                m=event.pos[0]
                n=event.pos[1]
                print(m,n)
                data = (m,n)
                conn.sendall(data.encode())
                



        
        if event.type==QUIT:
            pygame.quit()
            exit()
        if 0< m <200 and 0< n < 200 and d[1]=="":
            if turn%2==1:
                pygame.draw.line(screen,white,(0,0),(200,200))
                pygame.draw.line(screen,white,(200,0),(0,200))
                d[1]='x'
            else:
                pygame.draw.circle(screen,white,(100,100),50,10)
                d[1]='o'
            turn=turn+1
            
        if 200< m <400 and 0< n < 200 and d[2]=="":
            if turn%2==1:
                pygame.draw.line(screen,white,(200,0),(400,200))
                pygame.draw.line(screen,white,(400,0),(200,200))
                d[2]='x'
            else:
                pygame.draw.circle(screen,white,(300,100),50,10)
                d[2]='o'
            turn=turn+1
            
        if 400< m <600 and 0< n < 200 and d[3]=="":
            if turn%2==1:
                pygame.draw.line(screen,white,(400,0),(600,200))
                pygame.draw.line(screen,white,(600,0),(400,200))
                d[3]='x'
            else:
                pygame.draw.circle(screen,white,(500,100),50,10)
                d[3]='o'
            turn=turn+1
            
        if 0< m <200 and 200< n < 400 and d[4]=="":
            if turn%2==1:
                pygame.draw.line(screen,white,(0,200),(200,400))
                pygame.draw.line(screen,white,(200,200),(0,400))
                d[4]='x'
            else:
                pygame.draw.circle(screen,white,(100,300),50,10)
                d[4]='o'
            turn=turn+1
            
        if 200< m <400 and 200< n < 400 and d[5]=="":
            if turn%2==1:
                pygame.draw.line(screen,white,(200,200),(400,400))
                pygame.draw.line(screen,white,(400,200),(200,400))
                d[5]='x'
            else:
                pygame.draw.circle(screen,white,(300,300),50,10)
                d[5]='o'
            turn=turn+1
        if 400< m <600 and 200< n < 400 and d[6]=="":
            if turn%2==1:
                pygame.draw.line(screen,white,(400,200),(600,400))
                pygame.draw.line(screen,white,(600,200),(400,400))
                d[6]='x'
            else:
                pygame.draw.circle(screen,white,(500,300),50,10)
                d[6]='o'
            turn=turn+1

        if 0< m <200 and 400< n < 600 and d[7]=="":
            if turn%2==1:
                pygame.draw.line(screen,white,(0,400),(200,600))
                pygame.draw.line(screen,white,(200,400),(0,600))
                d[7]='x'
            else:
                pygame.draw.circle(screen,white,(100,500),50,10)
                d[7]='o'
            turn=turn+1
        if 200< m <400 and 400< n < 600 and d[8]=="":
            if turn%2==1:
                pygame.draw.line(screen,white,(200,400),(400,600))
                pygame.draw.line(screen,white,(400,400),(200,600))
                d[8]='x'
            else:
                pygame.draw.circle(screen,white,(300,500),50,10)
                d[8]='o'
            turn=turn+1
        if 400< m <600 and 400< n < 600 and d[9]=="":
            if turn%2==1:
                pygame.draw.line(screen,white,(400,400),(600,600))
                pygame.draw.line(screen,white,(600,400),(400,600))
                d[9]='x'
            else:
                pygame.draw.circle(screen,white,(500,500),50,10)
                d[9]='o'
            turn=turn+1
        
        c=check()
        #if c!=False:
            #break
        for i in d:
            if d[i]=="":
                isempty=True
                break
            else:
                isempty=False
        if isempty==False:
            screen.fill(black)
            show_text("Its a tie!!",120, 300,(255,255,255),100)
            #print("It is a tiee!!!")
        
    pygame.display.update()
 

