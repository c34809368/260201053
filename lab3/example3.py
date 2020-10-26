gpa=float(input("please enter your GPA:"))
numOfLectures=int(input("please enter your number of lectures:"))
if gpa<2:
  if numOfLectures<47:
    print("Not enough number of lectures and GPA!")
  else:
    print("Not enough GPA!")
else:
  if numOfLectures<47:
    print("Not enough number of lectures!")
  else:
    print("GRADUATED!!")