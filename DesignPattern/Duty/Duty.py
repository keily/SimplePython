#coding=gbk
'''
模式特点：使多个对象都有机会处理请求，从而避免发送者和接收者的耦合关系。将对象连成链并沿着这条链传递请求直到被处理。

程序实例：请假和加薪等请求发给上级，如果上级无权决定，那么递交给上级的上级。

代码特点：无
'''
class Request:
    def __init__(self,tcontent,tnum):
        self.content = tcontent
        self.num = tnum

class Manager:
    def __init__(self,temp):
        self.name = temp
    def SetSuccessor(self,temp):
        self.manager = temp
    def GetRequest(self,req):
        pass

class CommonManager(Manager):
    def GetRequest(self,req):
        if(req.num>=0 and req.num<10):
            print "%s handled %d request." %(self.name,req.num)
        else:
            self.manager.GetRequest(req)

class MajorDomo(Manager):
    def GetRequest(self,req):
        if(req.num>=10):
            print "%s handled %d request." %(self.name,req.num)


