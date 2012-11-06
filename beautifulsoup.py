# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
url="http://ftp.xdlinux.info/books/book.html"
content_stream = urllib2.urlopen(url)
soup=BeautifulSoup(content_stream)
length=len(soup('a'))
for i in range(0,length):
    url=soup('a')[i]['href']
    url=url.encode('utf-8')
    try:
        content_stream = urllib2.urlopen(url)
        url=soup('a')[i]['href']
        title=url.split('/')[-1]
#    title=title.encode('utf-8')
        f  =  open(title,"wb")
        f.write(str(content_stream.read()))
        f.close()
    except:
        pass


#f  =  open("linuxbook.html","wb")
#f.write(str(soup))
#f.close()
#print soup.prettify()
