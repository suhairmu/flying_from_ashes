class Student:
    def setValue(self,name,roll):
        self.name=name
        self.roll=roll
    def printVal(self):
        print(self.name)
        print(self.roll)
    def __str__(self):  #to display object
        return self.name
obj=Student()
obj.setValue("vjay",105)
ob2=Student()
ob2.setValue("ajay",105)
ob2.printVal()
print(obj)

'''o/p
(w/o def__str)
ajay
105
<__main__.Student object at 0x7fb6802788d0>

(with def__str__)
ajay
105
vjay'''