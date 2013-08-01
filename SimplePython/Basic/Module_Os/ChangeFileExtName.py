#!/usr/bin/python

'''
        File      : changefileextname.py
        Author    : keily
        E-Mail    : rollngzhang@gmail.com
'''
import sys,os,random

#filedic = {'xml': 'html', 'txt': 'rtf'}
filedic = {'avi': 'bin','wmv':'wbin','mp4':'mbin','mkv':'kbin'}
def convertext(_path):
	global filedic
	for root,dirs,fileNames in os.walk(_path):
		for f in fileNames:
			fname=os.path.join(root,f)
			try:
				ext=f[f.rindex('.')+1:]
				if(filedic.has_key(ext)):
					_name=f[:f.rindex('.')]+'.'+filedic[ext]
					nname=os.path.join(root,_name)
					if(os.path.exists(nname)):
						x=int(random.uniform(1, 100))
						_name=f[:f.rindex('.')]+str(x)+'.'+filedic[ext]
						nname=os.path.join(root,_name)
					print fname,nname
					os.rename(fname,nname)
					print 'old name:',fname,'  new name:',nname
				else:
					print 'old name:',fname,'  no change'
			except:
				print 'error occur!'
if __name__ == '__main__':
	curPath=raw_input("Press Enter to continue:")
	while((os.path.exists(curPath))==False):
		curPath=raw_input("Press try again:")
	convertext(curPath)
	raw_input("Press Enter to continue")
		
