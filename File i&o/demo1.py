f = open("/home/suhair/PycharmProjects/LumPy/File i&o/numfile",'r')
lst = []
for data in f:
    lst.append(data.rstrip("\n"))
print(lst)

for i in lst:
    num = int(i)
print(i)