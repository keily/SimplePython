from SimpleFactory import *

if __name__=="__main__":
    op=raw_input("operator:")
    op1=input("a:")
    op2=input("b:")
    factory=OperationFactory()
    cal=factory.createOp(op)
    cal.op1=op1
    cal.op2=op2
    print cal.getResult()