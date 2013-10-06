#coding=UTF-8
'''
Created on 2013-9-26

@author: zhangweiae
'''
#@sqrt精度
EPSION=0.000001
'''
求平方根，精度为0.01
'''
def sqrt(num):
    low=EPSION
    high=EPSION
    mid=0.0
    _sqrt=0.0
    #如果数是小于1的正数
    if(num<1.0):
        high+=1.0
    else:high=num+1.0
    #如果原数据不等（在精度范围内），循环求的
    while (_sqrt-num)>EPSION or (_sqrt-num)<-EPSION:
        mid=(low+high)/2.0
        _sqrt=mid*mid
        if(_sqrt>num):high=mid
        else:low=mid
    return mid

'''
二分法求最大值
'''
def binaryMax(A,left,right):
    mid=(left+right)/2
    max1,max2=A[left],A[right]
    if(mid>left):
        max1=binaryMax(A,left,mid)
    if((mid+1)<right):
        max2=binaryMax(A,mid+1,right)
    if(max1>max2):return max1
    else:return max2
'''
二分法求极值，返回一个tuple（min，max）
'''
def binMax_Min(A,left,right):
    mid=(left+right)/2
    #初始化当前极值
    min1,max1=A[left],A[right]
    min2,max2=min1,max1
    #二分递归返回极值
    if(mid>left):        
        min1,max1=binMax_Min(A,left,mid)
    if((mid+1)<right):
        min2,max2=binMax_Min(A,mid+1,right)
    #将极小值存于min1中
    if(min1>min2):min1=min2
    #将极大值存于max1中
    if(max1<max2):max1=max2
    #比较极小值和极大值，返回结果
    if(min1<max1):
        return min1,max1
    else:
        return max1,min1
'''
二分查找，返回key的索引值，未找到返回-1
'''
def binarySearch(A,left,right,key):
    while(left<=right):
        mid=(left+right)/2
        if(A[mid]>key):
            right=mid-1
        elif(A[mid]<key):
            left=mid+1
        else:return mid
    return -1
'''
找出数组A中和为sum的2个数（只找出第一队）
'''
def findSumNums(A,sum):
    len_A=len(A)
    for i in range(len_A):
        temp=binarySearch(A,0,len_A-1,sum-A[i])
        if(temp<>-1 and temp<>i):
            return A[i],A[temp]
    return None
'''
找出数组A中和为sum的2个数（只找出第一队）
'''
def findSumNums2(A,sum):
    len_A=len(A)
    B=[]
    for x in range(len_A):
        B.append(sum-A[x])
    j=len_A-1
    i=0
    print B
    while(i<j):
        print A[i],B[j]
        if(B[i]>A[j]):
            i+=1
        elif(B[i]<A[j]):
            j-=1
        else:
            return A[i],A[j]        
    return None
'''
给定数组中有元素N超过一半，找出他
'''
def findMoreHalf(A):
    count=0#计数器,相异递减，相同递增
    num=None#存放返回的元素
    for i in A:
        if(count==0):
            num=i
            count+=1
        else:
            if(i==num):
                count+=1
            else:
                count-=1
    return num