#coding=gbk

class Testing:
    def quest1(self):
        print 'Q1:a,b,c,d'
        print '(%s)'%self.answer1()
    def quest2(self):
        print 'Q2:a,b,c,d'
        print '(%s)'%self.answer2()
    def answer1(self):
        return ''
    def answer2(self):
        return ''
class TestingA(Testing):
    def answer1(self):
        return 'a'
    def answer2(self):
        return 'b'
class TestingB(Testing):
    def answer1(self):
        return 'c'
    def answer2(self):
        return 'd'


