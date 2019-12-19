# import re
# x='[abc]' #either a or b or c
# matcher=re.finditer(x,'a7b @k9z')
# for match in matcher:
#     print("match available at ",match.start())
#     print("group=",match.group())


import re
x='[^abc]'  #   ^ means except
            # predefined character class/set x='[a-z]' '[A-Z]' '[0-9]' '[a-zA-Z0-9]' '[^a-zA-Z0-9]'
            # predefined characters are '\s' space | '\d' digit or '[0-9]' | '\D' except digit or '[^0-9]'
            # '\w' all words ie, '[a-zA-Z0-9]' |
matcher=re.finditer(x,'a7b @k9z')
for match in matcher:
    print("match available at ",match.start())
    print("group=",match.group())