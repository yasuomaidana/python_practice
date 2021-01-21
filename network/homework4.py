import urllib.request as request
import ssl
import re
import json
#To ignore SSL
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


def getPage(url):
    page=request.urlopen(url,context=ctx).read()
    return page
def excer(url):
    data=json.loads((getPage(url)))
    c=0
    for comment in data["comments"]:
        c+=int(comment["count"])
    return c
url1="http://py4e-data.dr-chuck.net/comments_42.json"
url2="http://py4e-data.dr-chuck.net/comments_870203.json"

print("Test sum:",excer(url1))
print("Excersice sum:",excer(url2))