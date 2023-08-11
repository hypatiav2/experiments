import sqlite3
conn = sqlite3.connect("newdata.db")
c = conn.cursor()

from tkinter import *
from tkinter import messagebox
import time
root = Tk()

'''c.execute("CREATE TABLE newschools (column1 INTEGER,column2 TEXT)")
c.execute("INSERT INTO newschools (column1, column2) VALUES (?,?);", (50,"hello world"))
c.execute("INSERT INTO random3 (column1, column2) VALUES (45,'hello world')")
sql = "INSERT INTO random4 (column1, column2) VALUES (?,?)"
c.execute(sql, (45,"hello world"))
c.execute("SELECT * FROM newtable;")'''


'''print("LOGIN MENU:")
print("1. LOGIN \n 2. SIGN UP")
choice = input("Enter your choice (1/2):")'''


username = StringVar()
password = StringVar()
confirmpass = StringVar()
regstatus = StringVar()

def signup():
    home.pack_forget()
    signpage.pack()
    username.set("")
    password.set("")
    confirmpass.set("")
    userlbl = Label(signpage,text="Username:")
    userlbl.grid(column=0,row=0)
    input1 = Entry(signpage, textvariable=username)
    input1.grid(column=1, row=0)
    psswdlbl = Label(signpage,text="Password:")
    psswdlbl.grid(column=0,row=1)
    input2 = Entry(signpage, textvariable=password, show="*")
    input2.grid(column=1, row=1)
    confirmlbl = Label(signpage,text="Cofirm password:")
    confirmlbl.grid(column=0,row=2)
    input3 = Entry(signpage, textvariable=confirmpass, show="*")
    input3.grid(column=1, row=2)

    submitbttn = Button(signpage, text="Submit", fg="blue",command=register)
    submitbttn.grid(column=0,row=3)

    status = Label(signpage,textvariable=regstatus)
    status.grid(column=1,row=3)
    backbttn = Button(signpage,text="Back",command=back)
    backbttn.grid(column=2,row=3)

def login():
    home.pack_forget()
    loginpage.pack()
    username.set("")
    password.set("")
    userlbl = Label(loginpage,text="Username:")
    userlbl.grid(column=0,row=0)
    input1 = Entry(loginpage, textvariable=username)
    input1.grid(column=1, row=0)
    psswdlbl = Label(loginpage,text="Password:")
    psswdlbl.grid(column=0,row=1)
    input2 = Entry(loginpage, textvariable=password, show="*")
    input2.grid(column=1, row=1)
    submitbttn = Button(loginpage, text="Submit", fg="blue",command=submit)
    submitbttn.grid(column=1,row=2)
    backbttn = Button(loginpage,text="Back",command=back)
    backbttn.grid(column=0,row=3)
def submit():
    user = username.get()
    password2 = password.get()
    c.execute("select username from logins where password=(?);",(password2,))
    var1 = c.fetchall()
    print(var1)
    if len(var1) !=0:
        if var1[0][0] == user:
            messagebox.showinfo("Welcome!","Welcome "+user)
    else:
        messagebox.showerror("Sorry","Wrong username/passcode")
        login()

def register():
    user = username.get()
    password2 = password.get()
    confirmation = confirmpass.get()
    print(password2,confirmation)
    if confirmation == password2:
        c.execute("CREATE TABLE IF NOT EXISTS logins (name TEXT, username TEXT, password TEXT)")
        c.execute("INSERT INTO logins (username, password) VALUES (?,?);",(user, password2))
        c.execute("select * from logins")
        logins = c.fetchall()
        print(logins)
        regstatus.set("SIGN UP SUCCESSFUL")
    else:
        regstatus.set("SIGN UP FAILED")

def back():
    loginpage.pack_forget()
    signpage.pack_forget()
    home.pack()

home = Frame(root)
loginpage = Frame(root)
signpage = Frame(root)

home.pack()
loginbttn = Button(home,text="Login",fg="red",command=login)
loginbttn.pack()

signupbttn = Button(home,text="Sign Up",fg="blue",command=signup)
signupbttn.pack()


root.mainloop()
'''conn.commit()
c.close()
conn.close()'''