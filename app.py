print("Hello World") #output: Hello World

x = 10
y = 20
print(x+y) #output: 30

z = 6
print(z) #output: 6

z = "Alex"
print(z) #oitput: Alex

z = 6
print(type(z)) #output: <class 'int'>

z = "Alex"
print(type(z)) #output: <class 'str'>

z = "Are you there!"
print(type(z)) #output: <class 'str'>

z = 10.7
print(type(z)) #output: <class 'float'> 

z = 1/3
print(type(z)) #output: <class 'float'>

print(True)

listOfNumbers = [1,2,3,4,5,6] 
print(listOfNumbers) #output: [1,2,3,4,5,6]

ListOfMultipleTypes = [1,"Ajay",10/3,40.7,1011] 
print(ListOfMultipleTypes) #output: [1, 'Ajay', 3.33333333335, 48.7, 1011]

setOfNumbers = {1,2,2,3,3,3}
print(setOfNumbers) #output: {1,2,3}
print(len(setOfNumbers)) #output: 3

numberTuple = (10,20,30)
print(numberTuple) #output: (10,20,30)

someNumbers = [100,200,300]
for item in someNumbers:
    print(item) #output: 100 200 300

a = 10
if a > 5:
  print(True) #output: True
else:
  print(False)

x = 5
if x > 0:
    print("positive") #output: positive
elif x == 0:
   print("zero")
else:
    print('negative')

for i in range(1,10):
    print(i) #output: 1 2 3 4 5 6 7 8 9

for i in range(1,5):    
    print(i, end=' ') #output: 1 2 3 4

for num in range(1,11):
    if num % 2 == 0:
     print(num, end=" , ") #output: 2 , 4 , 6 , 8 , 10

def function_new(value_one,value_two):
    print(value_one + value_two)
function_new(10,20) #output: 30

class student:
    id = 101
    name = "Aman"
obj = student()
print(obj.name) #output: Aman
print(obj.id) #output: 101

class Student:
    def __init__(self, id, name, marks):
     self.id = id
     self.name = name
     self.marks = marks
    def show(self):
        print(str(self.id) + ":" + self.name)
        obj = Student(102,"Bala",90)
        obj.show() #output: 102:Bala