import urllib.request as request
from bs4 import BeautifulSoup
import ssl
import re
#To ignore SSL
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


def getPage(url):
    page=request.urlopen(url,context=ctx).read()#ugglyfied html
    return BeautifulSoup(page,"html.parser")
def getNLink(url,N):
    soup=getPage(url)
    rawdat=soup.find_all("a")
    c=0
    for i in rawdat:
        if c==N-1:
            return i.get("href")
        c+=1
def getName(url):
    l=re.findall("by_(.+).html",url)
    return l[0]
def finder(url,pos,times):
    print("Initial url",url)
    print("")
    for _ in range(times):
        url=getNLink(url,pos)
        print("Next url",url)
    print("")
    print("Final name",getName(url))

url1="http://py4e-data.dr-chuck.net/known_by_Fikret.html"
finder(url1,3,4)
url1="http://py4e-data.dr-chuck.net/known_by_Peaches.html"
finder(url1,18,7)