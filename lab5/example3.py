num_1=str(input("please enter the first number:"))
num_2=str(input("please enter the second number:"))
count=0
for i in num_1:
  for x in num_2:
    if i==x:
      count+=1
print(count)
