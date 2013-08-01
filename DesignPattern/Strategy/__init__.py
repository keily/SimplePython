from Strategy import *

if __name__=="__main__":
    money = input("money:")
    context={}
    context[1] = SaleContext(NormalSale())
    context[2] = SaleContext(DiscountSale(0.8))
    context[3] = SaleContext(GroupSale(30,0.6))
    ctype = input("type:[1]for normal,[2]for 80% discount [3]for Group Sale.60% discount")
    if ctype in context:
        cc = context[ctype]
    else:
        print "Undefine type.Use normal mode."
        cc = context[1]
    print "you will pay:%d" %(cc.getResult(money))