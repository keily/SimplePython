#coding=UTF-8
'''
Created on 2013-10-6

@author: Administrator
'''
from abc import ABCMeta, abstractmethod,abstractproperty

class IList:
    __metaclass__=ABCMeta
    @abstractmethod
    def Insert(self,index,element):pass
    @abstractmethod
    def Update(self,index,element):pass
    @abstractmethod
    def Delete(self,element):pass
    @abstractmethod
    def GetData(self,index):pass
    @abstractproperty
    def Length(self):pass
    @abstractmethod
    def Find(self,element):pass
    @abstractproperty
    def IsEmpty(self):pass
    @abstractmethod
    def Sort(self):pass
    @abstractmethod
    def Display(self):pass
    