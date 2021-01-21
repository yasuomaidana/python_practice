import urllib.request as request
import ssl
import re
import xml.etree.ElementTree as ET
#To ignore SSL
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


def getPage(url):
    page=request.urlopen(url,context=ctx).read()#ugglyfied html
    return page
def excer(url):
    tree=ET.fromstring(getPage(url))
    comments = tree.find("comments")
    val=0
    for comment in comments:
        val+= int(comment.find("count").text)
    return val

url1="http://py4e-data.dr-chuck.net/comments_42.xml"
url2="http://py4e-data.dr-chuck.net/comments_870202.xml"
print("Test sum:",excer(url1))
print("Excersice sum:",excer(url2))