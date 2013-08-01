
# coding by python 2.6

#coding=utf-8
import Image
import os

#print list[0]
#exit()
def getlogo(x1,y1):
	im =Image.open("./"+"watermark.jpg")
	z1=int(x1)
	z2=int(y1)
	in2=im.resize((z1,z2))
	#in2.show()
	return in2
	
list=os.listdir("./")
for a in list:
	#print a
	if os.path.isdir(a):
		print  "is path---------"
		continue
	if a.split('.')[1]=='py':       
		print "is py---------"
		continue        
	path="./get/"
	if not os.path.isdir(path):
		os.mkdir(path)
	print ("./"+a)
	if a.split('.')[1]=='jpeg': 
		im=Image.open("./"+a)                
		x=im.size[0]
		y=im.size[1]

		x1=int(x*0.5)
		y1=int(y*0.7)

		logo=getlogo((x-x1),(y-y1))
		box=(x1,y1,x,y)
		im.paste(logo, box)
		im.save(path+a)
	print("==================="+a)
