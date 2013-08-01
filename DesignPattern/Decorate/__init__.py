from Decorate import *

if __name__ == "__main__":
    p = Person("somebody")
    bt = BigTrouser()
    ts = TShirts()
    bt.Decorate(p)
    #bt.Show()
    ts.Decorate(bt)
    ts.Show()