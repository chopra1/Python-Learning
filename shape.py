class Shape:
  length = None
  breadth = None

  def set_value(self, length, breadth):
    self.length = length
    self.breadth = breadth

  def get_length(self):
    return self.length

  def get_breadth(self):
    return self.breadth

class Square(Shape):
  def area(self):
    return self.length * self.breadth

s1 = Square()
s1.set_value(8, 8)
print(s1.area())

class Rectangle(Shape):
  def area(self):
    return self.length * self.breadth

r1 = Rectangle()
r1.set_value(8, 12)
print(r1.area())

class Triangle(Shape):
  def area(self):
    return self.length * self.breadth * 1/2

t1 = Triangle()
t1.set_value(6, 10)
print(t1.area())

class Circle(Shape):
  def __init__(self, r):
    self.radius = r

  def area(self):
    return self.radius**2*3.14

c1 = Circle(8)
print(c1.area())