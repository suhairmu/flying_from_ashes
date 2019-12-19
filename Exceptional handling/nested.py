no1=int(input("Enter value for no1: "))
no2=int(input("Enter value for no2: "))
lst=[10,20,30]
try:
    res=no1/no2
    print("res=",res)
except Exception as e:
    print(e.args)

try:
    print(lst[5])
except Exception as e:
    print(e.args)

print("i've one database connection")