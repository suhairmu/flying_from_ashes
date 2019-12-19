num = int(input("Enter a number: "))
res = 0
while(num!=0):
    mod = num%10
    res = res*10+mod
    num = num//10
print("res=",res)