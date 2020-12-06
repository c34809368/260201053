n=int(input("Enter a number:"))
print("Enter a number, then press enter:")
matrix = [] 
for i in range(n): 
    a =[] 
    for j in range(n):
         a.append(int(input())) 
    matrix.append(a) 
for i in range(n): 
    for j in range(n): 
        print(matrix[i][j], end = " ") 
    print() 
sumnum=0
for i in range(n):
    sumnum+=matrix[i][i]
print(sumnum)