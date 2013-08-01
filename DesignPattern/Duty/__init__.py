from Duty import *

if __name__ == "__main__":
    common = CommonManager("Zhang")
    major = MajorDomo("Lee")
    common.SetSuccessor(major)
    req = Request("rest",33)
    common.GetRequest(req)
    req2 = Request("salary",3)
    common.GetRequest(req2)