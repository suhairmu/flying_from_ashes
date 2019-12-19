num = int(input("Enter a number: "))
i=2
flg=0
while(i<num):
    if(num%i==0):
        flg=flg+1
        break
    else:
        flg=0
    i+=1
if(flg==0):
    print(num, "is a prime number")
else:
    print(num, " is not a prime number")