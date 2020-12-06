num=int(input("please enter a number:"))
factors=[]
i=1
while i<=num:
  if num%i==0:
    factors.append(i)
  i+=1
print("factors are:",factors)
if len(factors)==2:#also can say if factors==[1,num]:
  print("It is prime.")
else:
  print("It is not prime.")

