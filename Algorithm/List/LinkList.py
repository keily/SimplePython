#coding=UTF-8
'''
Created on 2013-10-6

@author: Administrator
'''
from IList import IList
from Node import Node
'''
单链表
'''
class SingleLinkList(IList):    
    def __init__(self):
        self.__current=None
        self.__end=None
        self.__head=None
        self.__size=0
    '''
    location index node
    '''
    def __locationNode(self,index):
        if(index==None):
            self.__current=self.__end
            return
        self.__current=self.__head        
        while(self.__current and index>0):
            self.__current=self.__current.Next
            index-=1
    def Insert(self,index=None,element=None):
        self.__locationNode(index)
        node=Node(element)
        #list have no node
        if(self.__size==0):
            self.__current=self.__end=self.__head=node
        else:            
            #new node's next node is current's next
            node.Next=self.__current.Next
            #new node's previous node is current node
            self.__current.Next=node
            #insert at end of list,End need move on
            if(self.__current==self.__end):
                self.__end=self.__end.Next
        #increases size
        self.__size+=1        
    def Update(self,index,element):
        self.__locationNode(index)
        self.__current.Element=element
    def Delete(self,element):
        if(self.IsEmpty()):
            return True
        #only one node
        if(self.__head==self.__end and self.__head.Element==element):
            self.__head=self.__end=None
            return True
        #more than two nodes
        node = self.__head
        lnode = node.Next
        while(lnode):
            if(lnode.Element==element):
                node.Next=node.Next.Next
                lnode = node.Next
                self.__size-=1
            else:
                node=lnode
                lnode=node.Next
        self.__end=node                
        #check first node
        if(self.__head.Element==element):
            if(self.__head.Next):
                self.__head=self.__head.Next
            else:
                self.__head=self.__end=self.__current=None
            self.__size-=1        
    def GetData(self,index):
        self.__locationNode(index)
        return self.__current.Element
    def Length(self):
        return self.__size
    def Find(self,element):
        node=self.__head
        index=0
        while(node):
            if(node.Element==element):return index
            index+=1
            node=node.Next
        return -1
    def IsEmpty(self):
        if(self.__size==0):return True
        else:return False
    def Sort(self):        
        temp=self.Display()
        from Algorithm.Sort import quicksort
        quicksort(temp,0,len(temp)-1)
        node=self.__head
        i=0
        while(node):
            node.Element=temp[i]
            node=node.Next
            i+=1
    def Display(self):
        node=self.__head
        temp=[]
        while(node):
            temp.append(node.Element)
            node=node.Next
        return temp