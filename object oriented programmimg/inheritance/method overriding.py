class Base:
    def m(self):
        print("inside Base class")

class Derived(Base):
    def m(self):
        print("inside derived")

ob=Derived()
ob.m()