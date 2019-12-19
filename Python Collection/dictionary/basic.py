dict={}

dict={"name":"sayooj","age":"26","gender":"m"}

print(dict['name'])
dict['name']="ajay"
print(dict)

for k,v in dict.items():
    print(k,v)
    print(v)
print('name' in dict)   #checking whether key (name) is in dictionary dict


