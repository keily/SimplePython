import wx
import mainframe
#app=wx.App()
#frame=wx.Frame(parent=None,title='ssss')
#frame.Show()
#app.MainLoop()
if __name__=='__main__':
    app=wx.App()
    frame=mainframe.mainframe()
    frame.Show(True)
    app.MainLoop()
