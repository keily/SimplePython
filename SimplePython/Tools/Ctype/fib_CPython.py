import time,os,ctypes
pro=ctypes.cdll.LoadLibrary(r'D:\Learning\Python\PythonCallC\Release\PythonCallC.dll')
begin=time.clock()
pro.fib(40)
print 'use time:%s' % (time.clock()-begin)
os.system('pause')