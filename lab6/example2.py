grades=[[50,90,60],[15,60,75],[99,95,91]]
averageGrades=[]
for grade in grades:
  midterm1=grade[0]
  midterm2=grade[1]
  final=grade[2]
  average=(midterm1*0.3)+(midterm2*0.3)+(final*0.4)
  averageGrades.append(average)
print("average grades of the students are:",averageGrades)
