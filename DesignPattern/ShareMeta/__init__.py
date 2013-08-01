from ShareMeta import *

if __name__ == "__main__":
    f = WebFactory()
    ws=f.GetWeb("blog")
    ws.Use("Lee")
    ws2=f.GetWeb("show")
    ws2.Use("Jack")
    ws3=f.GetWeb("blog")
    ws3.Use("Chen")
    ws4=UnShareWebSite("TEST")
    ws4.Use("Mr.Q")
    print f.webtype
    f.GetCount()