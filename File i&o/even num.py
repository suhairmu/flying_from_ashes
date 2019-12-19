#to print even numbrs

f=open('/home/suhair/PycharmProjects/LumPy/File i&o/even')
list=[]
for item in f:
    list.append(int(item.rstrip('\n')))
print(list)
even=[]
for i in list:
    if(i%2==0):
        even.append(i)
print(even)