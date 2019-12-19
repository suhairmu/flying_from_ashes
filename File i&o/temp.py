f = open("/home/suhair/PycharmProjects/LumPy/File i&o/temp")
f2 = open("/home/suhair/PycharmProjects/LumPy/File i&o/temp out","w")
# list=[]
dict={}
# for item in f:
#     #list.append(item.rstrip("\n"))
#     list=item.rstrip("\n").split(",")
#     print(list[0])
#     print(list[1])
#

for temp in f:
    temp=temp.rstrip()
    data=temp.split(",")
    district=data[0]
    tem=data[1]
    print("district", district)
    print("temp",tem)

    if(district not in dict):
        dict[district]=tem
    else:
        old=dict[district]
        if(old<tem):
            dict[district] = tem
        else:
            dict[district] = old

print(dict)

for k,v in dict.items():
    i=str(k)
    j=str(v)
    f2.write("\n")
    f2.write(k)
    f2.write("\t")
    f2.write(v)