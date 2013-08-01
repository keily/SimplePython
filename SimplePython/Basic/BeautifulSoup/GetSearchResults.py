'''
Created on 2013-7-14

@author: Administrator
'''
import urllib
import re
class SerachResults:
    global path,targetURL
    path=u'd:\\pages\\'
    targetURL='http://www.baidu.com/s?wd='
    
    def __init__(self,key):
        self.key=key
    def getPage(self):
        webStr=urllib.urlopen(targetURL+self.key).read()
        self.setpageToFile(webStr)
    def setpageToFile(self,webStr):
        reSetStr=re.compile("\r ")
        self.key=reSetStr.sub(' ',self.key)
        targetFile=file(path+self.key+'.html','w')
        targetFile.write(webStr)
        targetFile.close()
        print 'done'
    def getResultStr(self,webStr):
        webStrList=webStr.read().split('\n\r')
        line=webStrList.index("<DIV id=Div> </DIV>")
        resultStr=webStrList[line]
        return resultStr
