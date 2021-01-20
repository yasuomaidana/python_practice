import urllib.request as request
from bs4 import BeautifulSoup
import ssl

#To ignore SSL
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
#Raw page
def printL(lis,row=5):
    c=0
    for i in lis:
        
        print(i)
        if c>row:
            break
        c+=1

page=request.urlopen("https://www.crummy.com/software/BeautifulSoup/",context=ctx).read()#ugglyfied html
soup = BeautifulSoup(page,"html.parser")
pretty=soup.prettify() #pretty
c=0
#Show by lines
#for i in pretty.splitlines():
#    c+=1
#    print(i)
#    if c==3:
#        break
print('Single form')
aL=soup.a
print(aL)
print('List form')
aL=soup('a') #equivalent soup.find_all('a')
printL(aL)
print("Get an atribute of an element")
print(aL[0])
print(aL[0].get("href"))

##Get elemens insde enclosed by an object
print("Elements inside")
head=soup.head
print(head)
#Get elements as list
print("As list")
headL=head.contents
print(type(headL))
print("As list (body)")
body=soup.body
bodyL=body.contents
print(type(bodyL))
print(bodyL[1])
#as childrens
bodyC=body.children
print("#########################")
print(type(bodyC))
printL(bodyC,2)