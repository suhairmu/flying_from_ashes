#for i in range(1,10):
#    print(i)


# ll=int(input("Enter lower limit: "))
# ul=int(input("Enter upper limit: "))
# for i in range(ll,ul):
#     print(i)



# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()


# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()



# limit=int(input("Enter a limit: "))
# for i in range(1,limit):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# limit=int(input("Enter a limit: "))
# for i in range(1,limit):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# limit=int(input("Enter a limit: "))
# for i in range(1,limit):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()



# limit=int(input("Enter a limit: "))
# for row in range(5,1,-1):
#     for col in range(1,row+1):
#         print(row,end=" ")
#     print()


for row in range(1,6):
    for col in range(5,row-1,-1):
        print(col,end=" ")
    print()