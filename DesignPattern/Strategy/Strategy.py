#coding=utf-8
'''
模式特点：定义算法家族并且分别封装，它们之间可以相互替换而不影响客户端。
程序实例：商场收银软件，需要根据不同的销售策略方式进行收费
'''
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


