
#coding=utf-8
'''
Created on 2013-9-22

@author: zhangweiae
'''
from QuickSort import *

def intersect(arr_a,arr_b):
    #sort
    len_a,len_b=len(arr_a)-1,len(arr_b)-1    
    res=[]
    count=0
    if(len_a>len_b):count=len_a
    else:count=len_b
    i=0
    m=n=0
    while i<=count:
        if(arr_a[m]>arr_b[n]):
            if(n<len_b):
                n+=1
        elif(arr_a[m]<arr_b[n]):
            if(m<len_a):
                m+=1
        elif(arr_a[m]==arr_b[n]):
            res.append(arr_a[n])
            if (m<len_a):m+=1
            if (n<len_b):n+=1
        i+=1
    return res
        
        