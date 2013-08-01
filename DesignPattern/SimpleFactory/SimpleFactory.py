#coding=gbk

class Operation:
    def getResult(self):
        pss

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


    
    
