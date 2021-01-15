class Employee:
  def __init__(self, name, salary):
    self.set_name(name)
    self.set_salary(salary)
  
  def get_name(self):
    return self.name
  
  def set_name(self,name):
    self.name=name

  def get_salary(self):
    return self.salary
  
  def set_salary(self,salary):
    self.salary=salary
  
  def display_info(self):
    print("Name:",self.name)
    print("Salary:",self.salary,"\n")

class Company:
  def __init__(self):
    self.employee_list=[]
  
  def get_employee(self):
    return self.employee_list
  
  def set_employee_list(self,employee_list):
    self.employee_list=employee_list

  def add_employee(self,new_employee):
    if isinstance(new_employee,Employee):
      self.employee_list.append(new_employee)

  def calc_av_salary(self):
    total_salary=0
    for employee in self.employee_list:
      total_salary+=employee.salary

    av_salary=total_salary/len(self.employee_list)
    return av_salary

  def display_all_info(self):
    for employee in self.employee_list:
      employee.display_info()
  

company=Company()
e1=Employee("berra",5700)
e2=Employee("berilnur",4300)
e3=Employee("can",4300)

company.add_employee(e1)
company.add_employee(e2)
company.add_employee(e3)

avg_salary=company.calc_av_salary()

#e3.salary=3200

company.display_all_info()
print("Average salary is:",int(avg_salary))