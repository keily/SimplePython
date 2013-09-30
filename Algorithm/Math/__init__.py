#coding=UTF-8
import random

if __name__=="__main__":
    from kMath import sqrt
    print '10’s sqrt is %s'% sqrt(10)
    
    from kMath import binMax_Min
    A=[]
    for i in range(10):
        A.append(random.randint(0,100))
    _min,_max = binMax_Min(A,0,len(A)-1)
    print 'array:%s min value:%s,max value:%s'%(A,_min,_max)
    
    A=[3,4,7,8,13,20]
    from kMath import findSumNums,findSumNums2
    print findSumNums2(A,15)
    
    B=[5,7,8,7,7,3,7]
    from kMath import findMoreHalf
    print findMoreHalf(B)