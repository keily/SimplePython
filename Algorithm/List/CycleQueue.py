#coding=UTF-8
'''
Created on 2013-10-6

@author: Administrator
'''
from IQueue import IQueue
'''
实现IQueue接口，的循环队列
'''
class CycleQueue(IQueue):
    __defalutSize=10#queue‘s default size 
    __size=0
    __rear,__front,__count=0,0,0
    __data=[]
    def __init__(self,size=None):
        if size<>None:
            self.__size=size
        else:
            self.__size=self.__defalutSize            
        for i in range(size):
            self.__data.append(None)
    def Append(self,element):
        if(self.__count>0 and self.__front==self.__rear):
            raise Exception('队列已满')
        self.__data[self.__rear]=element
        self.__rear=(self.__rear+1)%self.__size
        self.__count+=1
    def Delete(self):
        if(self.__count==0):
            raise Exception('队列已空')
        temp=self.__data[self.__front]
        self.__front=(self.__front+1)%self.__size
        self.__count-=1
        return temp
    def Front(self):
        if(self.__count==0):
            raise Exception('队列已空')
        return self.__data[self.__front]
    def IsEmpty(self):
        if(self.__count==0):
            return True
        return False
    def Length(self):
        return self.__count
    def Display(self):
        str1=[]
        if(self.__count>0):
            str1.append(self.__data[self.__front])
            i=(self.__front+1)%self.__size
            while(i<>self.__rear):
                str1.append(self.__data[i])
                i=(i+1)%self.__size
        return str1