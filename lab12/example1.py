import math
class Cylinder:
  def __init__(self, radius, height):
    self.set_radius(radius)
    self.set_height(height)

  def get_radius(self):
    return self.radius
  
  def set_radius(self,radius):
    if radius>0:
      self.radius=radius

  def get_height(self):
    return self.height
  
  def set_height(self,height):
    if height>0:
      self.height=height

  def calc_base(self):
    base=math.pi * (self.radius**2) 
    return base
  
  def calc_surface(self):
    surface=2*math.pi*self.radius * self.height
    return surface

  def calc_area(self):
    base_area=self.calc_base()
    surface_area=self.calc_surface()
    area=(2*base_area)+surface_area
    return area

  def calc_volume(self):
    base_area=self.calc_base()
    volume=base_area*self.height
    return volume


c1=Cylinder(3,5)
area=c1.calc_area()
volume=c1.calc_volume()
print("Area of the cylinder is:",area)
print("Volume of the cylinder is:",volume)





