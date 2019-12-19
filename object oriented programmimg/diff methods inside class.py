class Student:
    schoolname="luminartechnolab"       #static/class variable (schoolname.variablename), to use memory efficiently
    def setval(self,id,name):           #instance method
        self.id=id                      #instance variable (self.id)
        self.name=name                  #instance variable
    def printval(self):                 ##instance method
        print(self.id,"==",self.name,"==",Student.schoolname)

    @classmethod                        #decorator symbol '@'
    def setschool(cls,name):            #class level method, invoking by object name
        cls.schoolname=name             #clas  level variable (school name), even though using cls.


    @staticmethod
    def greetings():                    #static level method, invoke by using class name
        print("welcome")

s=Student()
s.setval(100,"noname")
s.printval()
s.setschool("Luminar Techno SOl")
s.printval()
Student.greetings()