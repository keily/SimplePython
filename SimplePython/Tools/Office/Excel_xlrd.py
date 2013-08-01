import sys
import urllib2
import xlrd

reload(sys)
sys.setdefaultencoding( "utf-8" )

fname=r"d:\result.xlsx"
bk=xlrd.open_workbook(fname)
sh1=bk.sheet_by_index(0)

txtf=open('d:\\1.txt','w')


try:
        for i in range(0,sh1.nrows):
                #if i>5:break
                str1=''
                for r in sh1.row(i):                        
                        str1=str1+','+str(r.value)
                txtf.writelines(str1)
                txtf.writelines('\n')
except:
        print 'exception:'
finally:
        txtf.close()
        print 'over!'

a=urllib2.urlopen('http://static.oschina.net/uploads/user/468/936282_50.jpg')
f=open('d:\\','wb')
f=open('d:\\1.jpg','wb')
f.write(a.read())
f.close()
