class MyClass:
    id = 101
    name = 'Alex'
#variables

s1 = MyClass()

print(str(s1.id) + " : " + s1.name) #output: 101 : Alex

class MyClass2:
    id = 101
    name = 'Alex'
#variables

    def showData(self):
        print("Id: " + str(self.id)) #output: Id : 101
        print("Name: " + self.name) #output: Name : Alex
    #method

s1 = MyClass2()

s1.showData()

class MyClass3:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        #__init__() method

    def showData(self):
        print("Id: " + str(self.id)) #output: Id : 102
        print("Name: " + self.name) #output: Name : Alex

s2 = MyClass3(101, 'Alex')

s2.id = 102
#update

s2.showData()

class MyClass4:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def showData(self):
        print("Id: " + str(self.id)) 
        print("Name: " + self.name)

s3 = MyClass4(101, 'Alex', 90)
del s3.marks
print(s3.marks)

class MyClass5:
    pass