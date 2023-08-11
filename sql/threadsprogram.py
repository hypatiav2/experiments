from threading import Thread
from time import sleep
import random

'''numlist = []
for m in range(5):
    templist = []
    for i in range(100):
        num = random.randint(1,500)
        templist.append(num)
    numlist.append(templist)


def product(row):
    result = 1
    for q in row:
        result = result * q
    print(result)

thread0 = Thread(target=product, args = (numlist[0],))
thread1 = Thread(target=product, args = (numlist[1],))
thread2 = Thread(target=product, args = (numlist[2],))
thread3 = Thread(target=product, args = (numlist[3],))
thread4 = Thread(target=product, args = (numlist[4],))

thread0.start()
thread1.start()
thread2.start()
thread3.start()
thread4.start()

temp1 = open("temp1.txt","a")
temp2 = open("temp2.txt","a")

for i in range(random.randint(1,20)):
    temp1.write("hi\n")

for i in range(random.randint(1,20)):
    temp2.write("hi\n")

temp1.close()
temp2.close()

def counter(file):
    linecount = len(file.readlines())
    print(linecount)


f1 = open("temp1.txt","r")
f2 = open("temp2.txt","r")

t1 = Thread(target=counter, args=(f1,))
t2 = Thread(target=counter, args=(f2,))

t1.start()
t1.join()
t2.start()

f1.close()
f2.close()'''

'''
f1 = open("expressions.txt","a")
f2 = open("answers.txt","a")

signs = ["+","-","/","*"]

for i in range(50):
    op = random.choice(signs)
    if op == "+":
        n1 = random.randint(1,20)
        n2 = random.randint(1,20)
        ans = n1 + n2
        f1.write(str(n1)+"+"+str(n2)+"\n")
        f2.write(str(ans)+"\n")
    if op == "-":
        n1 = random.randint(1,20)
        n2 = random.randint(1,20)
        ans = n1 - n2
        f1.write(str(n1)+"-"+str(n2)+"\n")
        f2.write(str(ans)+"\n")
    if op == "*":
        n1 = random.randint(1,20)
        n2 = random.randint(1,20)
        ans = n1 * n2
        f1.write(str(n1)+"*"+str(n2)+"\n")
        f2.write(str(ans)+"\n")
    if op == "/":
        n1 = random.randint(1,20)
        n2 = random.randint(1,20)
        ans = n1 / n2
        f1.write(str(n1)+"*"+str(n2)+"\n")
        f2.write(str(ans)+"\n")


f1.close()
f2.close()

answerslist = []
problemslist = []
def read_file(file,list1):
    global answerslist, problemslist
    for i in file:
        list1.append(file.readline())

f1 = open("expressions.txt","r")
f2 = open("answers.txt","r")
thread1 = Thread(target=read_file,args=(f1,problemslist))
thread2 = Thread(target=read_file,args=(f2,answerslist))
thread1.start()
thread2.start()

print(problemslist)
print(answerslist)
f1.close()
f2.close()'''

'''def randgen():
    for i in range(100):
        print(random.randint(1,50))

def checker():
    while thread1.is_alive():
        pass
    print("Thread1 is complete")
thread1 = Thread(target=randgen)
thread2 = Thread(target=checker)
thread1.start()
thread2.start()'''
import string
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
def randgen(listname):
    n = random.randint(2,500)
    for i in range(n):
        listname.append(random.choice(string.ascii_letters))
def checker(list1,list2,list3,list4,list5):
    while True:
        if thread1.is_alive != True and len(list1) > 0:
            print("List 1 finished:",list1)
            list1.clear()
        if thread2.is_alive != True and len(list2) > 0:
            print("List 2 finished:",list2)
            list2.clear()
        if thread3.is_alive != True and len(list3) > 0:
            print("List 3 finished:",list3)
            list3.clear()
        if thread4.is_alive != True and len(list4) > 0:
            print("List 4 finished:",list4)
            list4.clear()
        if thread5.is_alive != True and len(list5) > 0:
            print("List 5 finished:",list5)
            list5.clear()
thread1 = Thread(target=randgen, args = (list1,))
thread2 = Thread(target=randgen, args = (list2,))
thread3 = Thread(target=randgen, args = (list3,))
thread4 = Thread(target=randgen, args = (list4,))
thread5 = Thread(target=randgen, args = (list5,))
checkthread = Thread(target=checker,args=(list1,list2,list3,list4,list5))
thread1.start()

thread2.start()

thread3.start()

thread4.start()

thread5.start()


checkthread.start()
