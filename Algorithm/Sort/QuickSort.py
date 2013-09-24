#coding=utf-8
'''
Created on 2013-9-22
@author: zhangweiae
'''
def quicksort(arr,left,right):
    key=arr[right]
    i,j=left,right
    if i==j:return
    while (i<j):
        while(j>i and arr[i]<=key):i+=1
        while(j>i and arr[j]>=key):j-=1
        arr[i],arr[j]=arr[j],arr[i]
    arr[j],arr[right]=arr[right],arr[j]    
    if(left<i):
        quicksort(arr,left,i-1)
    quicksort(arr,j,right)
    
def partion(arr,left,right):
    key=arr[right]
    i,j=left,right
    while i<j:
        while(j>i and arr[i]<=key):i+=1
        while(j>i and arr[j]>=key):j-=1
        arr[i],arr[j]=arr[j],arr[i]
    arr[j],arr[right]=arr[right],arr[j] 
    return j
       
def quicksort2(arr,left,right):
    if(left<right):
        m=partion(arr,left,right)
        quicksort2(arr,left,m-1)
        quicksort2(arr,m+1,right)
    