#coding=gbk
'''
ģʽ�ص㣺�������װ�ɶ��󣬴Ӷ�ʹ���ò�ͬ������Կͻ����в��������������Ŷӻ��¼������־���Լ�֧�ֿɳ����Ĳ�����

����ʵ�����տ���������ʳ����⴮�ͼ��ᡣ�ͻ������Ա�㵥������Ա����õĵ����ߴ�����ɴ��������⿡�

�����ص㣺ע���ڱ����б�ʱ��Ҫ��ע�͵ķ�ʽɾ������������bug��bugʾ�������ں��棬����Ϊ������Ϊremove������for������ѯ�б��˳���µġ�
'''
class Barbucer:
    def MakeMutton(self):
        print "Mutton"
    def MakeChickenWing(self):
        print "Chicken Wing"

class Command:
    def __init__(self,temp):
        self.receiver=temp
    def ExecuteCmd(self):
        pass

class BakeMuttonCmd(Command):
    def ExecuteCmd(self):
        self.receiver.MakeMutton()

class ChickenWingCmd(Command):
    def ExecuteCmd(self):
        self.receiver.MakeChickenWing()

class Waiter:
    def __init__(self):
        self.order =[]
    def SetCmd(self,command):
        self.order.append(command)
        print "Add Order"
    def Notify(self):
        for cmd in self.order:
            #self.order.remove(cmd)
            #lead to a bug
            cmd.ExecuteCmd()
            


