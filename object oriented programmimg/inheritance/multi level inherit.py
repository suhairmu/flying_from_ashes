class A:            #parent
    def m(self):
        print("Inside A")
class B(A):         #child
    def m1(self):
        print("Inside B")
class C(B):         #subchild
    def m2(self):
        print("Inside C")
c=C()
c.m()
c.m1()
c.m2()