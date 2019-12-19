#In this pgm 'self' is used as instance method, not variable. for an instance variable we've to use self.variable_names
class Parent1:
    def m1(self):
        print("inside P1")
class Parent2:
    def m2(self):
        print("inside P2")
class Child(Parent1,Parent2):
    def m3(self):
        print("inside Child")
c=Child()
c.m3()
c.m2()
c.m1()