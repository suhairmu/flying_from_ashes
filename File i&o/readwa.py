f=open("/home/suhair/PycharmProjects/LumPy/File i&o/sample") #by default it is read mode
f2=open("/home/suhair/PycharmProjects/LumPy/File i&o/sample123","w")
for data in f:
    f2.write(data)