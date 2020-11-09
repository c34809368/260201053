number=int(input("please enter a number:"))
nums=list(number)
if number<10:
  digits=number
else:
  digits=nums[-1] + nums[-2]
print("sum of the last two digits is:",digits)




