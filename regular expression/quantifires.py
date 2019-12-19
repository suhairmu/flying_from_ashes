import re
x='a$'
matcher=re.finditer(x,'abaabaaabacaaab')
for match in matcher:
    print("position ",match.start())
    print("group=",match.group())


#'a+'       count single a and sequence of a
#'a*'       a+ including zero number of a
#'a?'       individual count of a and zero number of a
#'a{m}'     repeat number count of a, for eg 'a{3}'
#'a{2,3}'   setting range of repeating a's, minimum and maximum value
#'^a'       wheather its starting with a
#'a$'       ending with a