#coding=UTF-8
import sys
import random
arr_length=11

def maxHeapify(A,i,size_A):
    len_A=size_A
    left=2*i+1
    right=2*i+2
    largest=0
    #比较左叶节点和父节点，获得最大值的索引值
    if(left<len_A and A[left]>A[i]):
        largest=left
    else:largest=i
    #比较右节点和最大索引值
    if(right<len_A and A[right]>A[largest]):
        largest=right
    #上滤-交换数据后递归向上
    if(largest<>i):
        A[largest],A[i]=A[i],A[largest]
        maxHeapify(A,largest,len_A)
def buildMaxHeap(A):
    len_A=len(A)
    for i in range((len_A-1)/2,-1,-1):
        maxHeapify(A,i,len_A)        
def minHeapify(A,i,size_A):
    len_A=size_A
    left=2*i+1
    right=2*i+2
    small=0
    if(left<len_A and A[left]<A[i]):
        small=left
    else:small=i
    if(right<len_A and A[right]<A[small]):
        small=right    
    if(small<>i):
        A[small],A[i]=A[i],A[small]
        minHeapify(A,small,size_A)
def buildMinHeap(A):
    len_A=len(A)
    #i值等于A的长度-1到0
    for i in range((len_A-1)/2,-1,-1):
        minHeapify(A,i,len_A)
'''
倒序排列：需要构造最大堆，然后在尾部向前遍历依次将头(最大)换到尾
'''
def heapSort(A):
    i=len(A)-1
    while(i>=0):
        A[i],A[0]=A[0],A[i]
        maxHeapify(A,0,i)
        i-=1
'''
排列：需要构造最小堆，然后在尾部向前遍历依次将头(最小)换到尾
'''
def heapSortByDesc(A):
    i=len(A)-1
    while(i>=0):
        A[i],A[0]=A[0],A[i]
        minHeapify(A,0,i)
        i-=1
'''
实现最大优先队列的去掉并返回最大键值
'''
def extractMax(A):
    len_A=len(A)-1
    A[0],A[len_A]=A[len_A],A[0]
    maxHeapify(A,0,len_A)
    return A.pop()    
'''
将元素的关键词值增加到key
'''
def increaseKey(A,i,key):
    if(A[i]>key):
        raise "Invaild insert value"
    p=i/2
    while(p>0 and A[p]<A[i]):
        A[p],A[i]=A[i],A[p]
        i=i>>1
        p=p>>1
def insertKey(A,key):
    A.append(key)
    increaseKey(A,len(A)-1,key)
if __name__=='__main__':
    A=[]
    for i in range(arr_length):
        A.append(random.randint(0,100))
    print 'before buildMaxHeap:%s'%(A)
    buildMaxHeap(A)
    print 'after buildMaxHeap:%s'%(A)
    increaseKey(A,10,100)
    print 'after increaseKey:%s'%(A)
    insertKey(A,67)
    print 'after insertKey:%s'%(A)
    print 'before sort:%s'%(A)
    heapSort(A)
    print 'after sort:%s'%(A)
    extractMax(A)
    print 'pop max key:%s'%(A)
    
    A=[]
    for i in range(arr_length):
        A.append(random.randint(0,100))
    print 'before buildMinHeap:%s'%(A)
    buildMinHeap(A)
    print 'after buildMinHeap:%s'%(A)    
    print 'before sort order by desc:%s'%(A)
    heapSortByDesc(A)
    print 'after sort order by desc:%s'%(A)