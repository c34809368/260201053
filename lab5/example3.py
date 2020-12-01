num_1=input("please enter the first number:")
num_2=input("please enter the second number:")
first=list(num_1)
second=list(num_2)
count=0
while len(first)!=len(second):
  if len(first)>len(second):
    second.insert(0,0)
  else:
    first.insert(0,0)


for i in range(0,len(first)):
  if first[i]==second[i]:
    count+=1
  else:
    continue
print(count)

#çok redundant bir daha bak
