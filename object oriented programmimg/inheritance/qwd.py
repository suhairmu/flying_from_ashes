#Method Overriding

class Parent:
    def property(self):
        print("100k gold 2car 10lakh")
    def marriage(self):
        print("marriage with ajay")
class Child(Parent):
    def marriage(self):
        print("marriage with akhil")

ob=Child()
ob.property()
ob.marriage()