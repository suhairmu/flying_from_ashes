st={}
print(type(st)) #empty dictionary

st=set()
print(type(st)) #empty set

st={10,10,20,20,30,30}
st1={10,10,10,20,30,30,40,50,10,60,70}
print(st|st1)
print(st&st1)
print(st1-st)
#