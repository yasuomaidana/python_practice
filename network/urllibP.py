import urllib.request, urllib.error,urllib.parse
import re
fhand=urllib.request.urlopen("http://data.pr4e.org/page1.htm")
fi=[]
for line in fhand:
    read=line.decode().strip()
    print(read)
    link=re.findall("<a href=\"(.*)\"",read)
    if len(link)>0:
        fi.append(link)
print(fi)
print(fi[0])
print(type(fi[0][0]))