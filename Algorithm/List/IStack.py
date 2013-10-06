#coding=UTF-8
'''
Created on 2013-10-6

@author: Administrator
'''
from abc import ABCMeta, abstractmethod,abstractproperty
class IStack:
    __metaclass__=ABCMeta
    @abstractmethod
    def Push(self):pass
    @abstractmethod
    def Pop(self):pass
    @abstractmethod
    def Top(self):pass
    @abstractproperty
    def IsEmpty(self):pass
    @abstractproperty
    def Length(self):pass
    @abstractmethod
    def Display(self):pass

    