
import os

'''
os.name�ַ���ָʾ������ʹ�õ�ƽ̨���������Windows������'nt'��������Linux/Unix�û�������'posix'��

os.getcwd()�����õ���ǰ����Ŀ¼������ǰPython�ű�������Ŀ¼·����

os.getenv()��os.putenv()�����ֱ�������ȡ�����û���������

os.listdir()����ָ��Ŀ¼�µ������ļ���Ŀ¼����

os.remove()��������ɾ��һ���ļ���

os.system()������������shell���

os.linesep�ַ���������ǰƽ̨ʹ�õ�����ֹ�������磬Windowsʹ��'\r\n'��Linuxʹ��'\n'��Macʹ��'\r'��

os.path.split()��������һ��·����Ŀ¼�����ļ�����

os.path.isfile()��os.path.isdir()�����ֱ���������·����һ���ļ�����Ŀ¼��

os.path.existe()�����������������·���Ƿ���ش��ڡ�
'''

x,y=os.path.split(os.getcwd())
#(x:'E:\\dev', y:'Python27')

os.getenv('path').split(';')
'''
F:\oracle\product\10.2.0\db_1\bin
C:\Windows\system32
C:\Windows
E:\dev\oracle
F:\java\JDK\bin
E:\dev\Python27
'''