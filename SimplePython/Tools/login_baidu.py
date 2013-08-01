import urllib,urllib2,httplib,cookielib,json
import os
def auto_login(url,name,pwd):
	url='http://passport.baidu.com/?login'
	cookie=cookielib.CookieJar()
	cj=urllib2.HTTPCookieProcessor(cookie)
	pastdata=urllib.urlencode({'username':name,'password':pwd})
	request=urllib2.Request(url,pastdata)
	opener=urllib2.build_opener(cj)
	f=opener.open(request)
	print f
	hhtml=opener.open(url)
	return hhtml

name='rollngzhang'
psw='123'
h=auto_login('http://hi.baidu.com/rollngzhang',name,psw)
h.read()

os.system('pause')