class Student:
    def setVal(self,id,na,cls):
        self.id=id
        self.name=na
        self.clas=cls
    def display(self):
        print("id",self.id)
        print("name",self.name)
        print("class",self.clas)

ob=Student()
ob1=Student()

ob.setVal(123,"roshan",12)
ob.display()
ob1.setVal(258,"vishnu",10)
ob1.display()
print(ob.name)