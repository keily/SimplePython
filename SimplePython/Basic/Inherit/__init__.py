
class Cattle:
    '''this is parent class --Cattle '''
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
        print('initialized a Cattle,name:%s' % (self.name))
        
    def show(self):
        '''show this bull's information'''
        print('this is a Cattle,height:%s weight:%s' % (self.height,self.weight))

class Bull(Cattle):
    '''this is bull'''
    def __init__(self,name,height,weight,color):
        Cattle.__init__(self, name, height, weight)
        self.color=color
        print('initialized a bull,name:%s' % (self.name))
    def show(self):
        Cattle.show(self)
        print('this is a bull,color:%s' % (self.color))
        
class Cow(Cattle):
    '''this is Cow'''
    def __init__(self,name,height,weight,milk):
        Cattle.__init__(self, name, height, weight)
        self.milk=milk
        print('initialized a Cow,name:%s' % (self.name))
    def show(self):
        Cattle.show(self)
        print('this is a Cow,color:%s' % (self.milk))
        
redbull=Bull('redbull-1','150cm','500kg','red')
smelcow=Cow('smelcow-1','140cm','350kg','5kg/perday')

niu=[redbull,smelcow]
for n in niu:
    n.show()
    
