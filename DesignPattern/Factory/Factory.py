#coding=gbk
class LeiFeng:
    def Sweep(self):
        print "LeiFeng sweep"

class Student(LeiFeng):
    def Sweep(self):
        print "Student sweep"

class Volenter(LeiFeng):
    def Sweep(self):
        print "Volenter sweep"
class LeiFengFactory:
    def CreateLeiFeng(self):
        temp = LeiFeng()
        return temp
class StudentFactory(LeiFengFactory):
    def CreateLeiFeng(self):
        temp = Student()
        return temp
class VolenterFactory(LeiFengFactory):
    def CreateLeiFeng(self):
        temp = Volenter()
        return temp


