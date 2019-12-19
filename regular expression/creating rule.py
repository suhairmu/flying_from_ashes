# import re
# str=input("Enter string to validate: ")
# x='[a-kA-K][369][a-zA-Z]*'  # * denotes no limit of characters
# match=re.fullmatch(x,str)
# if(match!=None):
#     print("valid")
# else:
#     print("invalid")


import re
str=input("Enter vehichle registration number in caps: ")
#x='[K][L][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9][0-9]'
x='KL\d{2}[A-Z]{2}\d{4}'
match=re.fullmatch(x,str)
if(match!=None):
    print("valid")
else:
    print("invalid")


# import re
# str=input("Enter a mobile number: ")
# x='[6-9]\d{9}'
# match=re.fullmatch(x,str)
# if(match!=None):
#     print("valid")
# else:
#     print("invalid")