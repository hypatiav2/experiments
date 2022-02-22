#####################################################################################
#								Tkinter Match Game
#							Author: Meryl Mathew 
#							Description: Game
#							Last modified: 2/15/22
#####################################################################################
import random
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
root = Tk()
root.title("Memory Tile Game")

list1 = []
for i in range(2):
    for m in range(1,9):
        list1.append(m)

question = ImageTk.PhotoImage(Image.open("question.png").resize((170,170)))

bulbasaur = ImageTk.PhotoImage(Image.open("img1.png").resize((170,170)))
bulbasaur2 = ImageTk.PhotoImage(Image.open("img1.png").resize((170,170)))
charizard = ImageTk.PhotoImage(Image.open("img2.png").resize((170,170)))
charizard2 = ImageTk.PhotoImage(Image.open("img2.png").resize((170,170)))
greninja = ImageTk.PhotoImage(Image.open("img3.png").resize((170,170)))
greninja2 = ImageTk.PhotoImage(Image.open("img3.png").resize((170,170)))
eevee = ImageTk.PhotoImage(Image.open("img4.png").resize((170,170)))
eevee2 = ImageTk.PhotoImage(Image.open("img4.png").resize((170,170)))
sylveon = ImageTk.PhotoImage(Image.open("img5.png").resize((170,170)))
sylveon2 =ImageTk.PhotoImage(Image.open("img5.png").resize((170,170)))
dragonair = ImageTk.PhotoImage(Image.open("img6.png").resize((170,170)))
dragonair2 =ImageTk.PhotoImage(Image.open("img6.png").resize((170,170)))
squirtle = ImageTk.PhotoImage(Image.open("img7.png").resize((170,170)))
squirtle2 = ImageTk.PhotoImage(Image.open("img7.png").resize((170,170)))
vaporeon =ImageTk.PhotoImage(Image.open("img8.png").resize((170,170)))
vaporeon2 = ImageTk.PhotoImage(Image.open("img8.png").resize((170,170)))

list2 = [(bulbasaur,1),(bulbasaur2,1),(charizard,2),(charizard2,2),(greninja,3),(greninja2,3),(eevee,4),(eevee2,4),(sylveon,5),(sylveon2,5),(dragonair,6),(dragonair2,6),(squirtle,7),(squirtle2,7),(vaporeon,8),(vaporeon2,8)]
random.shuffle(list2)
clickedlist =[]
count = 0

quitbttn = Button(root, text="Quit Game",command=root.destroy)
quitbttn.grid(row=0,column=0)


class Tile:
    def __init__(self,row, column, image,number):
        self.row = row
        self.column = column
        self.image = image
        self.number = number
        self.buttonstate = NORMAL
        self.isclicked = 0
        self.questionmark = Button(root)

    def showquestion(self):
        self.questionmark = Button(root,image=question,state=self.buttonstate,command=self.buttonclick,bg='white')
        self.questionmark.grid(row=self.row,column=self.column)
    def showimage(self):
        self.questionmark["image"] = self.image
    def buttonclick(self):
        global count
        self.showimage()
        if self not in clickedlist and self.buttonstate == NORMAL:
            clickedlist.append(self)
            if len(clickedlist) == 2:
                if clickedlist[0].number == clickedlist[1].number:
                    clickedlist[0].buttonstate = DISABLED
                    clickedlist[1].buttonstate = DISABLED
                    count+=1
                    clickedlist.clear()
                    if count == 8: 
                        messagebox.showinfo("You Won!", "You matched all the tiles in " + timetaken.get()+ " seconds.")
                else:
                    root.update()
                    time.sleep(0.3)
                    clickedlist[0].questionmark["image"] = question
                    clickedlist[1].questionmark["image"] = question
                    clickedlist.clear()
                

x = 0
for m in range(4):
    for s in range(4):
        newtile = Tile(m+1,s,list2[x][0],list2[x][1])
        x+=1
        newtile.showquestion()
start = time.time()
timetaken = StringVar()
timetaken.set(0)
timelbl = Label(root, textvariable=timetaken)
timelbl.grid(row=0,column=2)
while True:
    timetaken.set("Time taken:" + str(int(time.time()-start)))
    root.update()