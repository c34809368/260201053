employees={}
for _ in range(5):
  empName=input("please enter the employee's name:")
  salary=int(input("please enter the employee's salary:"))
  employees[empName]=salary
print(employees)
print(sorted(employees, key=employees.get, reverse=True)[:3])