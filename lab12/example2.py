class Employee:
  
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  
  def get_name(self):
    return self.name
  
  def get_salary(self):
    return self.salary
  
  def set_name(self,name):
    self.name=name
  
  def set_salary(self,salary):
    self.salary=salary
  
  def display_info(self):
    print("Name:", self.name)
    print("Salary:", self.salary)

e= Employee("Berra",12345)
e.display_info
