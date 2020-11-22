number=int(input("please enter a number:"))
num=str(number)
num_1=map(int,num)
nums=list(num_1)
if number<10:
  digits=number
else:
  digits=nums[-1] + nums[-2]
print("sum of the last two digits is:",digits)

# loop ile yapmayı denemeliyim #



