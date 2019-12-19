# ls = [10,11,13,14,12,18,19]
# print(ls)
# ls.append(33)  #append() takes exactly one argument
# print(ls)
#
# print("even numbers are: ")
# for i in ls:
#     if (i%2==0):
#         print(i)
#     else:
#         pass
#
# print(ls[1:3])  #slicing operation, representing by index
# print(ls[1:])
# print(ls[:5])
#
# print("****************************************************************")
#
# data=[10,20,30],[1,2,3],[100,200,300]   #list of list
# print(data[0])
# print(data[0][0])

xyz=[["ajay",25,15000],["vjay",26,17000],["bjay",27,20000]]
for item in xyz:
    if (item[2]>16000):
        print(item)