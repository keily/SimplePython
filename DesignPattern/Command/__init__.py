from Command import *

if __name__ == "__main__":
    barbucer=Barbucer()
    cmd=BakeMuttonCmd(barbucer)
    cmd2=ChickenWingCmd(barbucer)
    girl=Waiter()
    girl.SetCmd(cmd)
    girl.SetCmd(cmd2)
    girl.Notify()