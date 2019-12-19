class Person:
    def setVal(self,na,ag):
        self.name=na
        self.age=ag
    def display(self):
        print("name",self.name)
        print("age",self.age)

ob=Person()
ob1=Person()

ob.setVal("ajay",26)
ob.display()
ob1.setVal("vjay",28)
ob1.display()
print(ob.age)