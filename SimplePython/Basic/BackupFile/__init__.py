#backup source files to a zip file
#code utf-8
import os
import time

#if your os is windows 
source=[r'd:\tmp']

#The backup must be stored in a main backup directory
target_dir=r'd:\backup'

#The name of the zip archive is the current date and time
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
if not os.path.exists(today):
    os.mkdir(today)
    print 'successfully create directory ',today

target=today + os.sep + now  +'.zip'
print(target)

#We use the zip command (in Windows/Unix/Linux) to put the files in a zip archive
zip_command="zip -qr %s %s" % (target,' '.join(source))
print(zip_command)
#run the backup script
if os.system(zip_command)==0:
    print 'succeddfull backup to',target
else:
    print 'backup failed'
