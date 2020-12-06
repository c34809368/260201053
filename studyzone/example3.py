#perfect number
num=int(input("please enter a number:"))
factors=[]
i=1
while i<num:
  if num%i==0:
    factors.append(i)
  i+=1
print(factors)
sumnum=0
for i in factors:
  sumnum+=i
if sumnum==num:
  print("it is a perfect number.")
else:
  print("it is not a perfect number.")
  