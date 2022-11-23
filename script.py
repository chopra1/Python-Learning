class Student:
    def __init__(self):
        self.name = 'Shubhum'
        self.age = 22
        self.marks = 95
        #print("__init__ is called!") #__init__ is called! __init__ is called!

    def talk(self):
        print("Name - ", self.name)
        print("Age - ", self.age)
        print("Marks - ", self.marks)

s1 = Student()
s1.name = 'Sunny' #name changed to Sunny now
print(s1.name) #output: Shubhum then Sunny

s2 = Student()
#print(s2.name) #output: Shubhum


class student:
    def __init__(self, n, a, *m):
        self.name = n
        self.age = a
        self.marks = m

    def display(self):
        print("Hi", self.name) #output: Hi Chetan
        print("Your age", self.age) #Your age 26
        print("Your marks", self.marks) #Your marks 95

s1 = student("Chetan", 26, 95)
s1.display()


class stud:
    def __init__(self, n, a, **m):
        self.name = n
        self.age = a
        self.marks = m

    def display(self):
        print("Hi", self.name) #output: Hi Chetan
        print("Your age", self.age) #Your age 26
        print("Your marks", self.marks) #Your marks {'science': 95, 'english': 90, 'maths': 80}

s1 = stud("Chetan", 26, science = 95, english = 90, maths = 80)
s1.display()


class speed:
    def __init__(self):
        self.speed = 10
        self.__new_speed = 25

    def get_new_speed(self):
        return self.__new_speed

    def set_new_speed(self, new_speed):
        self.__new_speed = new_speed

s = speed()
s.speed = 30 #output: 30
print(s.speed) #output: 30 before it was 10

s.__new_speed = 60 #output : 60 updated from 25
print(s.__new_speed) #output : error because by using double underscore obj becomes private and cannot be visible.

s.set_new_speed(40)
print(s.get_new_speed()) #output:40 before it was 25


class Example:
    def __init__(self):
        self.x = 10    #public
        self._y = 50   #secure but visible
        self.__z = 100 #secure(private)

    def public_method(self):
        print(self.x)   #output:10
        print(self._y)  #output:50
        print(self.__z) #output:100
        #way 2 - private data can be visible here by-
        self.__private_method() #output: inside private method

    def __private_method(self):
        print("inside private method") #output:error because private,cannot be visible

s = Example()
s.public_method()
s.__private_method()