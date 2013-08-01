#coding=gbk
class HandsetSoft(object):
    def Run(self):
        pass

class HandsetGame(HandsetSoft):
    def Run(self):
        print "Game"

class HandsetAddressList(HandsetSoft):
    def Run(self):
        print "Address List"

class HandsetBrand(object):
    def __init__(self):
        self.m_soft = None
    def SetHandsetSoft(self,temp):
        self.m_soft= temp
    def Run(self):
        pass

class HandsetBrandM(HandsetBrand):
    def Run(self):
        if not (self.m_soft == None):
            print "BrandM"
            self.m_soft.Run()

class HandsetBrandN(HandsetBrand):
    def Run(self):
        if not (self.m_soft == None):
            print "BrandN"
            self.m_soft.Run()

  
