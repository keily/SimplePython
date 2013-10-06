#coding=UTF-8
'''
Created on 2013-10-6

@author: Administrator
'''
class Node(object):
    __element=None
    __next=None
    def __init__(self,elem=None,node=None):
        self.__element=elem
        self.__next=node
    @property
    def Element(self):return self.__element
    @Element.setter
    def Element(self,val):self.__element=val
    @property
    def Next(self):return self.__next
    @Next.setter
    def Next(self,val):self.__next=val