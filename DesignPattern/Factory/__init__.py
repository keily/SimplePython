from Factory import *

if __name__ == "__main__":
    sf = StudentFactory()
    s=sf.CreateLeiFeng()
    s.Sweep()
    sdf = VolenterFactory()
    sd=sdf.CreateLeiFeng()
    sd.Sweep()