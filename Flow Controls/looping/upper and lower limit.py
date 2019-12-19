ul=int(input("Enter upper limit: "))
ll=int(input("Enter lower limit: "))
i=0
sum=0
while(ll<=ul):
    if(ll%2==0):
        #print(ll)
        sum=sum+ll
    ll+=1
print(sum)