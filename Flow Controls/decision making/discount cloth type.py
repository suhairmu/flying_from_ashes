ctype=int(input("Select cloth type: 1 for Silk 2 for Linen 3 for Cotton: "))
print("You choosed: ",ctype)
prate=int(input("Purchased Amount: "))

if(ctype==1):
    if(prate>5000):
        orate=(prate-(prate*0.2))
        print("Amount to be paid is ",orate)
    elif(prate>4000) & (prate<=5000):
        orate=(prate-(prate*0.1))
        print("Amount to be paid is ",orate)
    elif(prate>3000) & (prate<=4000):
        orate=(prate-(prate*0.08))
        print("Amount to be paid is ",orate)
    elif(prate>2000) & (prate<=3000):
        orate=(prate-(prate*0.07))
        print("Amount to be paid is ",orate)
    else:
        print("No Discount")

if(ctype==2):
    if(prate>5000):
        orate=(prate-(prate*0.2))
        print("Amount to be paid is ",orate)
    elif(prate>4000) & (prate<=5000):
        orate=(prate-(prate*0.1))
        print("Amount to be paid is ",orate)
    elif(prate>3000) & (prate<=4000):
        orate=(prate-(prate*0.08))
        print("Amount to be paid is ",orate)
    elif(prate>2000) & (prate<=3000):
        orate=(prate-(prate*0.07))
        print("Amount to be paid is ",orate)
    else:
        print("No Discount")

if(ctype==3):
    if(prate>5000):
        orate=(prate-(prate*0.2))
        print("Amount to be paid is ",orate)
    elif(prate>4000) & (prate<=5000):
        orate=(prate-(prate*0.1))
        print("Amount to be paid is ",orate)
    elif(prate>3000) & (prate<=4000):
        orate=(prate-(prate*0.08))
        print("Amount to be paid is ",orate)
    elif(prate>2000) & (prate<=3000):
        orate=(prate-(prate*0.07))
        print("Amount to be paid is ",orate)
    else:
        print("No Discount")