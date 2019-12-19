import re
str=input("Enter email id to validate: ")
x='[a-z][a-z0-9.]*@[a-z]*.com'
match=re.fullmatch(x,str)
if(match!=None):
    print("valid")
else:
    print("invalid")