class Person:
    def setVal(self,na,ag):
        self.name=na
        self.age=ag
    def display(self):
        print("name",self.name)
        print("age",self.age)

    def __str__(self):
        return self.name

ob=Person()
ob1=Person()

ob.setVal("ajay",26)
ob.display()
ob1.setVal("vjay",28)
ob1.display()
#print(ob.age)
#print(ob1)


lst=[]
lst.append(ob)
lst.append(ob1)

for ob in lst:
    #print(lst)
    if ob.age>20:
        print(ob)

data=[ob for ob in lst if ob.age>27]        #list comprihension
print[data]



##evens=list(map(lambda a:a.age>25,lst))
##print(evens)