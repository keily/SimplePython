#coding=gbk
import thread
import time
'''
warp thread class
'''
class timer(threading.Thread):
    def __init__(self,num,interval):
        threading.Thread.__init__(self)
        self.thread_num=num
        self.interval=interval
        self.thread_stop=False
    def run(self):
        print 'Thread Object(%d),Time:%s'%(self.thread_num,time.ctime())
        time.sleep(self.interval)
    def stop(self):
        self.thread_stop=True
        
def timefun(threadid,interval):
    count=0
    while count<10:
	    print 'current thread:%d count:%d'%(threadid,count)
	    time.sleep(interval)
	    count+=1
    print 'exitt thread %s'% time.ctime()
    thread.exit_thread()

def test():
    thread.start_new_thread(timefun,(1,1))
    thread.start_new_thread(timefun,(2,1))

if __name__=="__main__":
    #via method call
    #test()
    thread1=timer(1,1)
    thread2=timer(2,1)
    thread1.run()
    thread2.run()
    time.sleep(10)
    thread1.stop()
    thread2.stop()
