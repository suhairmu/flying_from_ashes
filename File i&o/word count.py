f = open("/home/suhair/PycharmProjects/LumPy/File i&o/word")
list=[]
dict={}
for item in f:
    list.append(item.rstrip("\n"))
    #list=item.rstrip("\n").split(" ")
print(list)

for word in list:
    if (word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)

print("*****************************")