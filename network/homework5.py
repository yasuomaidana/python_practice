import urllib.request as request
import urllib.parse as parse
import ssl
import re
import json
#To ignore SSL
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


def getPage(location=None):
    url="http://py4e-data.dr-chuck.net/json?"
    params={"key":42}
    params["address"]=location
    url = url + parse.urlencode(params)
    page=request.urlopen(url,context=ctx).read()
    return page
def excer(location):
    data=json.loads((getPage(location)))
    return data["results"][0]["place_id"]
ir="South Federal University"
print(ir+" id:",excer(ir))
ir="Saint Petersburg State University of Aerospace Instrumentation"
print(ir+" id:",excer(ir))