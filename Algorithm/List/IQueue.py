#coding=UTF-8
'''
Created on 2013-10-6

@author: Administrator
'''
from abc import ABCMeta, abstractmethod,abstractproperty
'''
Queue接口
'''
class IQueue:
    __metaclass__=ABCMeta
    @abstractmethod
    def Append(self,element):pass
    @abstractmethod
    def Delete(self):pass
    @abstractmethod
    def Front(self):pass
    @abstractproperty
    def IsEmpty(self):pass
    @abstractproperty
    def Length(self):pass
    @abstractmethod
    def Display(self):pass