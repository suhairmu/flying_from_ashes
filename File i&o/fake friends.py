import operator
f = open("/home/suhair/PycharmProjects/LumPy/File i&o/fakefriends.csv")
dict={}
for item in f:
    item=item.rstrip("\n")
    data=item.split(",")
    print(data)
    age=data[2]
    print("age",age)

    if(age not in dict):
        dict[age]=1
    else:
        dict[age]+=1
print(dict)

sorted_dict = sorted(dict.items(), key=operator.itemgetter(0))
print(sorted_dict)
print(sorted_dict[0]) #print(sorted_dict[-1])

'''import operator
d = {"Pierre": 42, "Anne": 33, "Zoe": 24}
sorted_d = sorted(d.items(), key=operator.itemgetter(1))'''