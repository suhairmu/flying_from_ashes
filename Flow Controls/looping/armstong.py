num = int(input("Enter a number: ")) #0, 1, 153, 370, 371 and 407
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp//=10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")