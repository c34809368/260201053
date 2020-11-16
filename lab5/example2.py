N=int(input("How many numbers you would like to enter?"))
count=0
for i in range(1,N+1):
    m=int(input("please enter an integer:"))
    if m%2==0:
        count+=1
    else:
        count=count
print("percentage of even numbers is:",float(count/N*100),"%")