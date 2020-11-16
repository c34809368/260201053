num=int(input("please enter how many numbers to generate:"))
num0=1
num1=1
fibo=[1,1]
for _ in range(num-1):
  nextnum=num0+num1
  fibo.append(nextnum)
  num0=num1
  num1=nextnum
print(fibo)

