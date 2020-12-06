studentnumber=int(input("please enter how many students there are in this class:"))
grades=[]
averageGrades=[]
for i in range(studentnumber):
  grades=input("enter midterm-1, midterm-1 and final seperated with comma:").split(",")
  midterm1=int(grades[0])
  midterm2=int(grades[1])
  final=int(grades[2])
  average=(midterm1*0.3)+(midterm2*0.3)+(final*0.4)
  averageGrades.append(average)
print("average grades of the students are:",averageGrades)
A_students=0
for average in averageGrades:
  if average>90:
    A_students+=1
print("there are",A_students,"AA students in this class.")