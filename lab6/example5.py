n=int(input("Please enter a number: "))
print("corresponding identity matrix of your number is:")
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()