#coding=UTF-8
'''
Created on 2013-10-6

@author: Administrator
'''
from IStack import IStack
from Node import Node

class LinkStack(IStack):
    __top=None
    __length=0
    def __init__(self):
        pass
    def Push(self,element):
        node=Node(elem=element,node=self.__top)
        self.__top=node
        self.__length+=1
        return True
    def Pop(self):
        if(self.__length==0):raise Exception('栈为空')
        elem=self.__top.Element
        self.__top=self.__top.Next
        self.__length-=1
        return elem
    def Top(self):
        if(self.__length==0):raise Exception('栈为空')
        return self.__top.Element
    def IsEmpty(self):
        if(self.__length==0):return True
        else:return False
    def Length(self):
        return self.__length
    def Display(self):
        data=[]
        cur=self.__top
        while(cur):
            data.append(cur.Element)
            cur=cur.Next
        return data