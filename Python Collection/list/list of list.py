# list1 = [[10,20],[30,40],[50,30]]
# for item in list1:
#     print(item[0])


employees=[[10,"abc",15000],[11,"cde",5000],[12,"efg",15000],[13,"hij",5000]]
cnt=0
sum=0
for e in employees:
    if(e[2]>8000):
        print(e)
        cnt+=1
        sum+=e[2]
print("count=",cnt)
print("sum",sum)