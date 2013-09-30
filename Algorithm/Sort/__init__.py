#coding=UTF-8

import time
import sys
import random
from QuickSort import *
import IntersectOfArrays

arr_length=10
def qsort():
    arr=[]
    for i in range(arr_length):
        arr.append(random.randint(0,100))
    print 'before sort:',arr
    quicksort(arr,0,arr_length-1)
    print 'after sort:',arr
def intersect():
    arr_a=[]
    arr_b=[]
    for i in range(20):
        arr_a.append(random.randint(0,100))
    for i in range(15):
        arr_b.append(random.randint(0,100))
    
    quicksort(arr_a,0,len(arr_a)-1)
    quicksort(arr_b,0,len(arr_b)-1)
    res = IntersectOfArrays.intersect(arr_a,arr_b)
    print arr_a,arr_b
    print res
    
if __name__=='__main__':
    #qsort()
    #intersect()
    A=[random.randint(0,10) for x in range(10)]
    from CountingSort import *
    B=[0 for x in range(len(A))]#构建新的数组
    countingSort(A,B,11)
    print A
    print B
    