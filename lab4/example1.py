number=input("please enter a number:")
num=list(number)
sumOfDigits=0
for i in num:
  if int(number)>9:
    sumOfDigits=int(num[-1])+int(num[-2])
  else:
    sumOfDigits=number
print(sumOfDigits)


#anotheroption#
number=int(input("please enter a number:"))
num=str(number)
num_1=map(int,num)
nums=list(num_1)
if number<10:
  digits=number
else:
  digits=nums[-1] + nums[-2]
print("sum of the last two digits is:",digits)