f=open('/home/suhair/PycharmProjects/LumPy/File i&o/rwfile','r')
lst=[]
for data in f:
    #print(data)
    #print(data,end="")
    #lst.append(data)
    lst.append(data.rstrip("\n"))

print(lst)