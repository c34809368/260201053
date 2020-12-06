#armstrong number
num=input("please enter a number:")
num1=0
for i in num:
  num1+=(int(i)**3)
if num1==int(num):
  print("It is an armstrong number.")
else:
  print("It is not an armstrong number")
