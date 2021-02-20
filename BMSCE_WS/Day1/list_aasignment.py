''' Following is the list of you participant names, enter same into a list,
develop a Python program to randomly pick one and print name, shuffle the list
and print the first in the list, at the begining print the length of list '''
import random
nlist = []
f = open("list.txt","r")

fl = f.readlines()
for x in fl:
    nlist.append(x)
f.close()

print(nlist)
print(len(nlist))
x = random.randint(0,len(nlist)-1)
print(x)
print(nlist[x])
random.shuffle(nlist)
print(nlist[0])
