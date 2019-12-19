dict = {101:"ABX",102:"XYZ",103:"ASD"}
print(dict[102]) #calling value by key
dict[101] = "JKL"
print(dict[101])

# for item in dict.keys():
#     print(item, end="\t")
#     print(dict[item])

for item in dict.values():
    print(item, end="\t")

# for data in dict:
#     print(data)

#print(101 in dict)