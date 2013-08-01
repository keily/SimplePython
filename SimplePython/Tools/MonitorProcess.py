#coding=gbk
import threading
import time
import os
import subprocess


def getProcessCount(proName):
    p=os.popen('tasklist /FI "IMAGENAME eq %s"'%proName)
    return p.read().count(proName)

def monitorPro(msg):
    print 'Monitor...',msg
    if getProcessCount('chrome.exe')==0:
        print subprocess.Popen([r'cmd.exe'])
    startTimer()
    
def startTimer():
    t=threading.Timer(120, monitorPro,('is running...'))
    t.start()

if __name__=="__main__":
    startTimer()
    while True:
        time.sleep(1)
