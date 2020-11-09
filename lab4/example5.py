num=int(input('please enter a number:'))
fact=1
if num==0 or num==1:
    fact=1
else:
    for i in range(2,num+1):
        fact*=i
print("the factorial of the input number is:", fact)