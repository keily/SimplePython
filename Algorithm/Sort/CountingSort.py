#coding=UTF-8
'''
Created on 2013-9-27

@author: zhangweiae
'''

'''
计数据排序，数组中满足(A[n]<k,0<=n<A.length)，将A排序到B中
'''
def countingSort(A,B,k):
    #初始化计数器
    countArr=[]
    for x in range(k):
        countArr.append(0)
    #对A累积统计，将A的值作为计数器计算器的下标
    for x in range(len(A)):#这里为了方便，还是使用常规的索引遍历
        countArr[A[x]]+=1
    #累加计数器转换为可现实A存储下标
    for x in range(1,len(countArr),1):
        countArr[x]+=countArr[x-1]
    #倒序循环A.length，将计数结果复制给新的数组
    for x in range(len(A)-1,-1,-1):
        B[countArr[A[x]]-1]=A[x]
        countArr[A[x]]-=1
    