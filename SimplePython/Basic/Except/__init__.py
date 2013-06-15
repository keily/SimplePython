
import time
import sys

t_len=3

class InputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self,obj,length):
        Exception.__init__(self)
        self.obj=obj
        self.length=length
        
        if(len(obj)>length):
            print('Exception: %s more than %d chars' % (obj,length))
try:
    s=raw_input('enter ...')
    if len(s)>t_len:
        raise InputException(s,t_len)
except EOFError:
    print('\nWhy did you do an EOF on me?')
    sys.exit()
except InputException,o:
    print('you raise a custom defined InputException,object:%s, the length of input chars :%s' % (o.obj,o.length))
except:
    print('\nSome error/exception occurred.') 

finally:
    s=s[:t_len]
    #this thread will be suspend 2 second.
    time.sleep(2)
    print('finally,input is cutted :%s' % s)
