#coding=gbk
class Normal:
    def Open(self):
        print 'normal tool open'
class Small(Normal):
    def smallOpen(self):
        print 'small open'
class Big(Normal):
    def bigOpen(self):
        print 'big open'
class Adapter(Normal):
    def __init__(self,obj):
        self.obj=obj
    def Open(self):
        if 'small' in str(self.obj):
            self.obj.smallOpen()
        elif 'big' in str(self.obj):
            self.obj.bigOpen()
        else:
            self.obj.smallOpen()

