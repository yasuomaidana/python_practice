import re
def counter(name):
    filT=open(name,'r')
    c=0
    for i in filT:
        numbs=re.findall('[0-9]+',i)
        for num in numbs:
            c+=int(num)
    print(c)
fiN="test.txt"
counter(fiN)
fiN="excersice.txt"
counter(fiN)