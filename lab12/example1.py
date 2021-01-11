import math
class Cylinder:
  def __init__(self,radius,height):
    self.radius=radius
    self.height=height
  
  def get_radius(self):
    return self.radius
  
  def get_height(self):
    return self.height
  
  def set_radius(self,radius):
    self.radius=radius
  
  def set_height(self,height):
    self.height=height
  
  def calc_base_area(self):
    return math.pi*(self.radius**2)
  
  def calc_surface_area(self):
    return 2*math.pi*self.radius*self.height

  def calculate_area(self):
    base_area=calc_base_area
    surface_area=calc_surface_area
    area=(2*base_area)+surface_area
    return area

  def calculate_volume(self):
    return self.calculate_base_area() * self.height



cylinder=Cylinder(3,5)
print(cylinder.calculate_area())
print(cylinder.calculate_volume())





