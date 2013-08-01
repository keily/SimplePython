# coding:utf-8 __author__ = 'zz'

import os,wx
import urllib
import sys
import traceback
from bs4 import BeautifulSoup

reload(sys)  
sys.setdefaultencoding('utf8')

#自定义输出图片下载信息
class ImageOutMessage():
    def __init__(self,obj):
        self.Object = obj
    def emit(self,strMessage):
        if strMessage:
            self.Object.AppendText(strMessage)

class main_windows(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Down DouBan Image",size = (450,400))
        bkg = wx.Panel(self,-1)

        DownImageButton = wx.Button(bkg,label = "DownImage")
        DownImageButton.Bind(wx.EVT_BUTTON,self.DownImage)

        self.UrlText = wx.TextCtrl(bkg)
        self.contents = wx.TextCtrl(bkg,style = wx.TE_MULTILINE)
        self.contents.SetEditable(False)

        hbox = wx.BoxSizer()
        hbox.Add(self.UrlText,proportion = 1,flag=wx.EXPAND)
        hbox.Add(DownImageButton,proportion = 0,flag= wx.LEFT,border = 5)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox,proportion = 0,flag = wx.EXPAND,border =5)
        vbox.Add(self.contents,proportion = 1,flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,border = 5)

        bkg.SetSizer(vbox)

    def ReadHtml(self,src):
##        try:
            content = urllib.urlopen(src).read()
            strHtml = BeautifulSoup(''.join(content))
            return strHtml
##        except Exception, e:
##            self.contents.AppendText("STOP,ERROR:%s.\n"%(e))
##            return None
        
    def NextPage(self,strUrl):
##        try:
            #从页面Html源码中获取下一个页面地址，最后一页返回None
            content = self.ReadHtml(strUrl)
            strHref = None
            for line in content('link'):
                if line.find_all(rel= 'next') > 0 :
                    if (line.get('href')).find('start=') > 0:
                        strHref = line.get('href')

            if strHref:
                return strHref
            else:
                return None
##        except Exception,e:
##            self.contents.AppendText("STOP,ERROR:%s.\n"%(e))


    def PicInfo(self,src):
##        try:
            #从Html源码中获取全部图片的相对地址
            lstPicHref = []
            content = self.ReadHtml(src)
            for line in content('img'):
                # 判断img地址是否为缩略图
                if (line.get('src')).find('thumb/public') > 0:
                    strPicHref = line.get('src')
                    #将缩略图地址修改为原图地址
                    strPicHref = strPicHref.replace('thumb','photo')
                    lstPicHref.append(strPicHref)
                    #判断返回值
            if lstPicHref:
                return lstPicHref
            else:
                return None
##        except Exception,ex:
##            self.contents.AppendText("STOP,ERROR:%s.\n"%(ex))

    def WritePic(self,HtmlTitle,listPicHref,FilePath):
##        try:
            #获取当前页面Title对应的文件夹路径
            strFilePath = FilePath + HtmlTitle + '\\'
            #对获取到的Title的编码形式进行转换
            if isinstance(strFilePath, unicode):
                strFilePath.encode('gb2312')
            else:
                strFilePath.decode('utf-8').encode('gb2312')
                #判断strFilePath是否存在 ，不存在创建该目录
            if not os.path.exists(strFilePath):
                os.mkdir(strFilePath)

            PicLength = len(listPicHref)
            self.contents.AppendText("%s.\n"%( 'Current page {} picture waiting for download...'.format(PicLength)))
            i = 1
            for item in listPicHref:
                strPicName = item.split("/")
                #将图片写入到本地指定路径
                urllib.urlretrieve(item,strFilePath + strPicName[7],None)
                self.contents.AppendText("%s.\n"%('Download picture {}/{}:{}'.format(i,PicLength,strPicName[7])))
                i += 1
##        except Exception,ex:
##            self.contents.AppendText("STOP,ERROR:%s.\n"%(ex))


    def DownImage(self,event):
##        try:
            strUrl = self.UrlText.GetValue()
            #验证strUrl格式是否符合要求
            if strUrl.find("www.douban.com/photos/album/") > 0:
                if strUrl:
                    # 获取页面Title
                    strTitle = self.ReadHtml(strUrl).html.head.title.string
                    strFilePath = os.getcwd() + '\\DownFile\\'
                    strTitle = ''.join(strTitle.split())
                    #验证图片存放路径是否存在
                    if not os.path.exists(strFilePath):
                        os.mkdir(strFilePath)
                    while strUrl:
                        #验证下一页路径是否重复
                        if strUrl.find('start') > 0:
                            strPrevNumber =strUrl.split('=')
                        else:
                            strPrevNumber = ['1','0']

                        listPicHref = self.PicInfo(strUrl)
                        self.contents.AppendText("%s.\n"%(strUrl))
                        self.WritePic(strTitle,listPicHref,strFilePath)
                        strUrl = self.NextPage(strUrl)
                        #判断是否有下一页Url
                        if not strUrl:
                            break
                        strUrlNumber = strUrl.split('=')
                        if int(strPrevNumber[1]) > int(strUrlNumber[1]):
                            break
                    self.contents.AppendText("Download complete")
                else:
                    self.contents.AppendText("URL cannot be empty")
            else:
                self.contents.SetValue("")
                self.contents.AppendText("URL format is invalid, for example:\n %s"%("http://www.douban.com/photos/album/92848474/"))
##        except Exception,ex:
##            self.contents.AppendText("STOP,ERROR:%s.\n"%(ex))

class App(wx.App):
    def OnInit(self):
        self.frame = main_windows()
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True


if __name__ == "__main__":
    app = App()
    app.MainLoop()




