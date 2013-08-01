#coding=gbk
'''
ģʽ�ص㣺���ù�������Ч��֧�ִ���ϸ���ȵĶ���

����ʵ����һ����վ�����������û��������𷵻���Ӧ������վ���������������վ�Ѿ��ڷ������ϣ���ô����������վ�����ϲ�ͬ�û��Ķ��ص����ݣ����û�У���ô����һ����

�����ص㣺Ϊ��չʾÿ����վ�����û�����Ĵ���������Ϊ���ǽ�����һ�����ô������ֵ䡣

������������֮���Բ���Python��sysģ���е�sys.getrefcount()����ͳ�����ü�������Ϊ�еĶ�������ڱ𴦱���ʽ�����ã��Ӷ����������ü�����
'''
import sys

class WebSite:
    def Use(self):
        pass

class ConcreteWebSite(WebSite):
    def __init__(self,strName):
        self.name = strName
    def Use(self,user):
        print "Website type:%s,user:%s" %(self.name,user)

class UnShareWebSite(WebSite):
    def __init__(self,strName):
        self.name = strName
    def Use(self,user):
        print "UnShare Website type:%s,user:%s" %(self.name, user)

class WebFactory:
    def __init__(self):
        test = ConcreteWebSite("test")
        self.webtype ={"test":test}
        self.count = {"test":0}
    def GetWeb(self,webtype):
        if webtype not in self.webtype:
            temp = ConcreteWebSite(webtype)
            self.webtype[webtype] = temp
            self.count[webtype] =1
        else:
            temp = self.webtype[webtype]
            self.count[webtype] = self.count[webtype]+1
        return temp
    def GetCount(self):
        for key in self.webtype:
            #print "type: %s, count:%d" %(key,sys.getrefcount(self.webtype[key]))
            print "type: %s, count:%d " %(key,self.count[key])


