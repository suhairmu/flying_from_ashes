# i=10
# while(i>=0):
#     print(i)
#     i-=1


# ran=int(input("Enter a range: "))
# i=0
# while(i<=ran):
#     if (i % 2) == 0:
#         print(i)
#     i+=1


rn=int(input("Enter range: "))
i=0
sum=0
while(i<=rn):
    if(i%2==0):
        sum=sum+i
    i+=1
print(sum)
