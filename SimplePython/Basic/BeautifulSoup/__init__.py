import os,sys
import BeautifulSoup
import urllib
import fnmatch

f=open('d:\\down.txt','w')
url='http://www.bt5156.com/html/tv/oumeitv/20130401/41951.html'
html=urllib.urlopen(url).read()
soup=BeautifulSoup.BeautifulSoup(html)

for link in soup.findAll('a'):
    content=link.get('href')
    if type(content)==type(None):
        pass
    elif fnmatch.fnmatch(content, "*.mp4") or fnmatch.fnmatch(content, "*.rmvb"):
        print content
        f.write(str(content))
        f.write('\n')
    else:
        pass
    
    