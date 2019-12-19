sub1=int(input("Enter marks in first subject(out of 50):"))
sub2=int(input("Enter marks in second subject(out of 50):"))
sub3=int(input("Enter marks in third subject(out of 50):"))

tmark = sub1+sub2+sub3

if(tmark>140):
    print("A+ grade")
elif(tmark<=140) & (tmark>130):
    print("A grade")
elif (tmark <= 130) & (tmark > 120):
    print("B+ grade")
elif(tmark<=120) & (tmark>110):
    print("B grade")
elif(tmark<=110) & (tmark>100):
    print("C+ grade")
else:
    print("Failed")