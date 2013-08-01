#coding=gbk
class Travl:
    def MoveTarget(self):
        print 'some travl tool'
class Ariplan(Travl):
    def Movetarget(self):
        print 'by ariplan'
class proxy(Travl):
    def Movetarget(self):
        self.tool=Ariplan()
        self.tool.Movetarget()
if __name__ == "__main__":
    p=proxy()
    p.Movetarget()
