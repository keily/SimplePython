from TemplateMethod import *

if __name__=="__main__":
    q1=TestingA()
    q2=TestingB()
    print 'student1'
    q1.quest1()
    q1.quest2()
    print 'student2'
    q2.quest1()
    q2.quest2()