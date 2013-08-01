#coding=gbk
import os
def percent_wrapped(fun):
    def wrapped(*args,**kw):
	    return str(fun(*args,**kw)*100)+'%'
    return wrapped

@percent_wrapped
def computeaverage(a,num):
    if type(a) is list and num in a:
	    import math
	    result= num/math.fsum(a)
	    return result
    return 0

arr=[x for x in range(5)]
print computeaverage(arr,2)
os.system('pause')
