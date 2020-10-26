age=int(input("please enter an age:"))
if age<=6 or age>=60:
    print("you are free of price.")
elif age>6 and age<18:
    print("the price you should pay is: 1.5 tl")
else:
    print("the price you should pay is: 3 tl")
    
