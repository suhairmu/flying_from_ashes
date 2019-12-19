# ls=[1,2,3,4,5]
# def square(num):
#     return num*num
# ls=list(map(square,ls))
# print(ls)
#
# ls=[1,2,3,4,5]
# ls=list(map(lambda no:no*no,ls))
# print(ls)


# ls=[1,2,3,4,5]
# def double(num):
#     return num+num
# ls=list(map(double,ls))
# print(ls)


# lst=[1,2,3,4,5]
# def chk(no):
#     return no%2==0
# lst=list(filter(chk,lst))
# print(lst)

# lst=[1,2,3,4,5]
# lst=list(filter(lambda no:no%2==0,lst))
# print(lst)

lst=[1,2,3,4,5]
lst=list(map(lambda no:no*no,(filter(lambda no:no%2==0,lst))))
print(lst)