movies = [[1,"summer",1996,4],[2,"winter",2006,4.5],[4,"autmn",1996,3],[5,"spring",2002,4.2]]
cnt=0

for item in movies:
    if (item[3]>4):
        print(item[1])
    if (item[2]==1996):
        cnt+=1
print(cnt)
rating=[]
for item in movies:
    rating.append(item[3])
print(max(rating))