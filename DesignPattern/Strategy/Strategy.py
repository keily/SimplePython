#coding=gbk

class Sale:
    def acceptCash(self,money):
        return money
class NormalSale:
    def acceptCash(self,money):
        return money
class DiscountSale:
    def __init__(self,discount):
        self.discount=discount
    def acceptCash(self,money):
        return money*self.discount
class GroupSale:
    def __init__(self,groupNum,discount):
        self.groupNum=groupNum
        self.discount=discount
    def acceptCash(self,money):
        if self.groupNum>10:
            return money*self.discount
        else:
            return money
class SaleContext:
    def __init__(self,context):
        self.context=context
    def getResult(self,money):
        return self.context.acceptCash(money)


