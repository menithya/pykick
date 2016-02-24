import urllib
from BeautifulSoup import *

url = raw_input("enter url..")
count=raw_input("enter count...")
count = int(count)
position=raw_input("enter postion...")
position=int(position)

for k in range(0,count+1):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    if k < count:
        print "retrived url",url
    else:
        print "last url",url
        break
    tags = soup('a')

    pos=0
    for tag in tags:
        if pos == position-1:
            url = str(tag.get('href',None))
            break
        pos +=1
