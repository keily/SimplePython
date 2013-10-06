#coding=utf-8
'''
模式特点：工厂根据条件产生不同功能的类。
程序实例：四则运算计算器，根据用户的输入产生相应的运算类，用这个运算类处理具体的运算。
'''
class Operation:
    def getResult(self):
        pass

class OperationAdd(Operation):
    def getResult(self):
        return self.op1+self.op2

class OperationSub(Operation):
    def getResult(self):
        return self.op1-self.op2

class OperationMul(Operation):
    def getResult(self):
        return self.op1*self.op2

class OperationDiv(Operation):
    def getResult(self):
        try:
            return self.op1/self.op2
        except:
            print 'op2 is zero'
            return 0

class OperationFactory:
    def __init__(self):
        self.operator={}
        self.operator['+']=OperationAdd()
        self.operator['-']=OperationSub()
        self.operator['*']=OperationMul()
        self.operator['/']=OperationDiv()
    def createOp(self,op):
        if op in self.operator:
            return self.operator[op]
        else:
            return Operation


    
    
