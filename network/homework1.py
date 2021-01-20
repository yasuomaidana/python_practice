import urllib.request as request
from bs4 import BeautifulSoup
import ssl

#To ignore SSL
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


def getPage(url):
    page=request.urlopen(url,context=ctx).read()#ugglyfied html
    return BeautifulSoup(page,"html.parser")
def summer(soup):
    rawdat=soup.find_all("span")
    l=[]
    for i in rawdat:
        l.append(int(i.contents[0]))
    s=sum(l)
    print(s)

url1="http://py4e-data.dr-chuck.net/comments_42.html"
url2="http://py4e-data.dr-chuck.net/comments_870200.html"
soup=getPage(url1)
print("Sample data")
summer(soup)
print("Excersice data")
soup=getPage(url2)
summer(soup)