N=int(input("How many numbers you would like to enter?"))
count=0
for _ in range(N):
    m=int(input("please enter an integer:"))
    if m%2==0:
        count+=1
print("percentage of even numbers is:",float(count/N*100),"%")