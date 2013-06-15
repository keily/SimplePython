
import os

'''
os.name字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。

os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径。

os.getenv()和os.putenv()函数分别用来读取和设置环境变量。

os.listdir()返回指定目录下的所有文件和目录名。

os.remove()函数用来删除一个文件。

os.system()函数用来运行shell命令。

os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。

os.path.split()函数返回一个路径的目录名和文件名。

os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录。

os.path.existe()函数用来检验给出的路径是否真地存在。
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