class Student:
    clgname="luminar"

    def __init__(self,stname,id):   #constructor
        self.st_name=stname
        self.id=id
    def printVal(self):
        print("name=",self.st_name)
        print("id",self.id)

st=Student("ajay",4005) #constructor invoke automatically when we create object, assigning value
st.printVal()