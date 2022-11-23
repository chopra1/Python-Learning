from abc import abstractmethod


class Base:
    def __init__(self):
        print("Base Class")  #output: Base Class

class Derived(Base):
    def __init__(self): 
        super().__init__()
        print("Derived Class") #output: Derived Class

class Something:
    pass

obj = Derived()

print(isinstance(obj,Derived)) #output: True
print(isinstance(obj,Something)) #output: False


class Parent:
    def __init__(self, name):
        print("Parent __init", name)

class Parent2:
    def __init__(self, name):
        print("Parent2 __init", name)

#Super - The super() buildin rturns a proxy object that allows you to refer parent class by 'super'.
# It allows us to avoid using base class explicitly. allow working with multiple inheritance.
class Child(Parent2,Parent):
    def __init__(self):
        print("Child __init__") #output: Child __init__
        super().__init__('Shubhum') #output: Parent2 __init Shubhum
        Parent.__init__(self, "Chetan") #output: Parent __init Chetan

child_obj = Child()


#composition - relationship - a part of, independent, strong connection
class Salary:
    def __init__(self, pay, reward):
        self.pay = pay
        self.reward = reward

    def annual_salary(self):
        return (self.pay*12) + self.reward

class Employee:
    def __init__(self, name, position, pay, reward):
        self.name = name
        self.position = position
        self.final_salary = Salary(pay, reward)

    def final_salary_m(self):
        return self.final_salary.annual_salary()

emp = Employee('Shubhum', "Py Dev", 100000, 10000)
print(emp.final_salary_m()) #output: 1210000


#Aggregation - has a relationship, independent, weak connection
class salary:
    def __init__(self, pay, reward):
        self.pay = pay
        self.reward = reward

    def annual_salary(self):
        return (self.pay*12) + self.reward

class employee:
    def __init__(self, name, position, sal):
        self.name = name
        self.position = position
        self.final_salary = sal

    def final_salary_m(self):
        return self.final_salary.annual_salary()

sal = salary(1000000, 100000)
emp = employee('Shubhum', "Py Dev", sal)
print(emp.final_salary_m()) #output: 12100000


#Abstract class - cannot use base class in abstract class
abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

square_obj = Square(10)
print(square_obj.area()) #output: 100
print(square_obj.perimeter()) #output: 40