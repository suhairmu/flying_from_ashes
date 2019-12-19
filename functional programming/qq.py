class Student:
    def __init__(self,id,name,total):
        self.id=id
        self.name=name
        self.total=total
    def __str__(self):
        return self.name

f=open('/home/suhair/PycharmProjects/LumPy/functional programming/samp','r')
studentlist=[]
lst=[]
for lines in f:
    lst=(lines.rstrip("\n").split(","))
    print(lst)
    id=lst[0]
    name=lst[1]
    total=lst[2]
    studentlist.append(Student(id,name,total))  #created object to corresponding class, bcoz of constructor

# for ob in studentlist:
#     print(ob.id)

mlist=list(filter(lambda o:int(o.total)>150,studentlist))
for ob in mlist:
    print(ob)

# for o in studentlist:
#     print((o.name).upper)

# upplist=list(map(lambda o:(o.name).upper,studentlist))
# for st in upplist:
#     print(st)