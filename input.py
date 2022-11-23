#inheritance
class Polygon:
    __width = None
    __height = None

    def set_value(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

class Square(Polygon):
    def area(self):
        return self.get_width() * self.get_height()

class Triangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height() * 1/2

s1 = Square()
s1.set_value(8, 10)
print(s1.area()) #output: 80

t1 = Triangle()
t1.set_value(8, 10)
print(t1.area()) #output: 40.2


#operator overloading
a = 10
b = 20
print(a + b) #output: 30

p ="Hello "
q = "World"
print(p + q) #output: Hello World

x = [10, 20, 30]
y = [5, 6, 7]
print(x + y) #output: [10,20,30, 5, 6, 7]

class Books:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def __sub__(self, other):
        return self.pages - other.pages

    def __mul__(self, other):
        return self.pages * other.pages

    def __pow__(self, other):
        return self.pages ** other.pages

    def __truediv__(self, other):
        return self.pages / other.pages

    def __floordiv__(self, other):
        return self.pages // other.pages
    
    def __mod__(self, other):
        return self.pages % other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __lt__(self, other):
        return self.pages < other.pages

b1 = Books(150)
b2 = Books(100)

#formula : b1.__add__(b2)
print(b1+b2) #output: 250

#formula: b2.__sub__(b1)
print(b1-b2) #output: 50

#formula: b1.__mul__(b2)
print(b1*b2) #output: 15000

#formula: b1.__pow__(b2)
print(b1**b2) #output: uncountable

#formula: b1.__truediv__(b2)
print(b1/b2) #output: 1.5

#formula: b1.__floordiv__(b2)
print(b1//b2) #output: 1

#formula: b1.__mod__(b2)
print(b1%b2) #output: 50

#formula: b1.__gt__(b2)
print(b1>b2) #output: True

#formula: b1.__lt__(b2)
print(b1<b2) #output: False


class Python:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def __sub__(self, other):
        return self.pages - other.pages

    def __gt__(self, other):
        return self.pages > other.pages

class Java:
    def __init__(self, pages):
        self.pages = pages

p1 = Python(380)
p2 = Java(480)

print(p1+p2) #output: 860
print(p1-p2) #output: -100
print(p1>p2) #output: False


class student:
    def __init__(self, n, a, **m):
       self.name = n
       self.age = a
       self.marks = m

    def display(self):
        print("Hi", self.name) #output: Hi Chetan
        print("Your age", self.age) #output: Your age = 28
        print("Your marks", self.marks) #output: Your marks {'science': 95, 'english' = 98, 'maths' = 95} 

s1 = student("Chetan", 26, sciece=95, english=98, maths=95)
s1.display()