n_1=input("please enter the first number:")
n_2=input("please enter the second number:")
n_3=input("please enter the third number:")
if n_1<n_2 and n_1<n_3:
    min_num=n_1
elif n_2<n_3:
    min_num=n_2
else:
    min_num=n_3

print("minimum number is:",min_num)



