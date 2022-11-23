class Base:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def showData(self):
        print("Id: " + str(self.id)) #output: Id : 101 
        print("Name: " + self.name) #output: Namev: Alex

class Derived(Base):
    pass

s1 = Derived(101, 'Alex')

s1.showData()

class base:
    def __init__(self):
     print("init of base class")

class derived(base):
    def __init__(self):
     print("init of derived class") #output: init of derived class

obj = derived()

class BASE:
    def __init__(self):
        print("init of base class") #output: init of base class

class DERIVED(BASE):
    def __init__(self):
        super().__init__() #__init__ meethod chainning
        print("init of derived class") #output: init of derived class

obj = DERIVED()

class bas:
    pass

class derive:
    pass

objOne = bas()
objTwo = derive()

print(isinstance(objOne,bas)) #output: True
print(isinstance(objTwo,derive)) #output: True

#when a single derived class inherits properties from a single base class, it is called single inheritance
class A:
    def display(self):
        print("Single Inheritance") #output: Single Inheritance

class B(A):
    pass

obj = B()

obj.display()

#when there is inheritance on multiple levels, it is called multilevel inheritance
class a:
    def display(self):
        print("display method")

class b(a):
    def show(self):
        print("show method")

class c(b):
    pass

obj = c()

obj.display() #output: display method
obj.show() #output: show method

#when one single class inherits from multiple base class, it is called multiple inheritance.
class D:
    def display(self):
        print("display method")

class E:
    def show(self):
        print("show method")

class F(D, E):
    pass

obj = F()

obj.display() #output: display method
obj.show() #output: show method

#when multiple derived classes inherits from same base class, it is called hierarchical inheritance
class G:
    def display(self):
        print("display method")

class H(G):
    pass

class I(G):
    pass

objOne = H()
objTwo = I()

objOne.display() #output: display method
objTwo.display() #output: display method

#Polymorphism
# method overriding refers to the scenerio where a method present in derived class has the same name as the method present in the base class.
class BAse:
    def display(self):
        print("base class")

class DErived(BAse):
    def display(self):
        print("derived class")

obj = DErived()
obj.display() #output: derived class

#What will be the output offollowing code?
def calculator(x,y):
    return x + y

def calculator(x,y):
    return x - y

def calculator(x,y):
    return x / y

def calculator(x,y):
    return x * y

print(calculator(3,2)) #output: 6