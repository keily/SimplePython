from Observer import *

if __name__ == "__main__":
    p = Secretary()
    s1 = StockObserver("xh",p)
    s2 = NBAObserver("wyt",p)
    p.Attach(s1);
    p.Attach(s2);
    p.action = "WARNING:BOSS ";
    p.Notify()