a=float(input("please enter a number:"))
b=float(input("please enter a number:"))
c=float(input("please enter a number:"))
delta=(b**2)-(4*a*c)
if delta>0:
    root_1=(-b + delta**(1/2))/(2*a)
    root_2=(-b - delta**(1/2))/(2*a)
    print("there are two real roots:",root_1, "and",root_2)
elif delta==0:
    root=-b/(2*a)
    print("there is only one root:",root)
else:
    print("there are two complex roots.")