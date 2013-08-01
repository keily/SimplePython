from AbstractFactory import *

if __name__ == "__main__":
    factory = SqlFactory()
    user=factory.CreateUser()
    depart=factory.CreateDepartment()
    user.GetUser()
    depart.GetDepartment()