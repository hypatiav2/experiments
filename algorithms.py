'''numlist = [4,9,21,6,8]
num = 21
for i in numlist:
    if i == num:
        print(numlist.index(num))
        break
    elif numlist.index(i) == len(numlist)-1:
        print("sorry not found")'''


'''def fibonacci(n):
    if n<=1:
        return n
    else: 
        return(fibonacci(n-1)+fibonacci(n-2))


num = int(input("How many numbers?"))
for i in range(num):
    print(fibonacci(i))
x = 0
def findsum(n):
    global x
    if n == 0:
        return x
    else:
        x = x + n%10 + findsum(n//10)
        return x
num = int(input("Enter a number:"))
print(findsum(num))

x = ""
def reverse(s):
    global x
    if len(s) == 0:
        return x
    else:
        x =  x + reverse(s[1:]) + s[0]
        return x

inputstring = input("Enter string")
print(reverse(inputstring))'''

'''def pascal(layer):
    if len(layer) > 10:
        return
    print(*layer)
    temp = []
    temp.append(1)
    for m in range(len(layer)-1):
        temp.append(layer[m]+layer[m+1])
    temp.append(1)
    pascal(temp)


print(1) # First line can be printed as it is
pascal([1,1])'''

import random
'''list1 = random.sample(range(1,100),20)
print(list1)
list1.sort()
print(list1)
x = int(input("Find number index"))
min = 0
max = len(list1)-1
found = False
while found == False:
    mid = int((min + max) /2)
    if x > list1[mid]:
        min = mid + 1 
    elif x < list1[mid]:
        max = mid - 1
    elif x == list1[mid]:
        found = True
        print(mid)
        break
    if min == max:
        print("Item not found")
        break'''

'''def binsearch(list1, x, min, max):
    if min > max:
        return "Item not found"
    else:
        mid = (min + max) // 2
        if x==list1[mid]:
            return "found at index "+str(mid)
        elif x > list1[mid]:
            return binsearch(list1,x,mid+1,max)
        elif x<list1[mid]:
            return binsearch(list1, x, min, mid-1)

print(binsearch(list1,x,0, len(list1)-1))'''

import random
'''unsorted = random.sample(range(1,100),6)
print(unsorted)

while True:
    sorts = False
    for i in range(len(unsorted)):
        if i+1 != len(unsorted) and unsorted[i] > unsorted[i+1]:
            unsorted[i],unsorted[i+1] = unsorted[i+1],unsorted[i]
            sorts = True
        print(unsorted)
    if sorts == False:
        print(unsorted)
        break'''

list1 = random.sample(range(1,30),5)

min = 0

while min+1 < len(list1):
    a = list1.index(min(list1))
    w
    

