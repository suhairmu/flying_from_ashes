num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if(num1>num2) & (num1>num3):
    print(num1,"is greater")
elif(num2>num1) & (num2>num3):
    print(num2,"is greater")
elif(num3>num1) & (num3>num2):
    print(num3,"is greater")
else:
    print("3 numbers are equal")
