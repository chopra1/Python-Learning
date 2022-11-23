class Cat:
  def __init__(self, input_name, input_breed, input_age = 0, input_is_brave = False):
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_brave = input_is_brave
    self.is_cuddly = True

  def have_birthday(self):
    self.age = self.age + 1
    print("{name} had a birthday! {name} is {age} years old.".format(name = self.name, age = self.age))

  def scare(self, other_cat):
    if(other_cat.is_brave):
      print("{other_name} was NOT scared of {name}!".format(name = self.name, other_name = other_cat.name))
    else:
      print("{other_name} was scared by {name}!".format(name = self.name, other_name = other_cat.name))

  def __repr__(self):
    description = "This {breed} named {name} is {age} years old.".format(breed = self.breed, name = self.name, age=self.age)
    if self.is_cuddly:
      description += " {name} is a cuddly cat.".format(name = self.name)
    else:
      description += " {name} is an cuddly cat.".format(name = self.name)
    return description

new_cat = Cat("Leo", "Tabby", 3, True)
cat_two = Cat("Rashid", "Bengal", 6, False)

print(new_cat)
print(new_cat.age)
new_cat.have_birthday()
new_cat.scare(cat_two)
cat_two.scare(new_cat)

#output: <__main__.Cat object at 0x00000031B09BBFD0>
# above line changed to - This Tabby named Leo is 3 years old. Leo is a cuddly cat.
#3
#Leo had a birthday! Leo is 4 years old.
#Rashid was scared by Leo!
#Leo was NOT scared of Rashid!


class Dog:
  def __init__(self, input_name, input_breed, input_age = 0, input_friendliness=True):
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_friendly = input_friendliness
    self.friends = []
 
  def __repr__(self):
    description = "This {breed} named {name} is {age} years old and has {number_of_friends} friends.".format(breed = self.breed, name = self.name, age=self.age, number_of_friends=len(self.friends))
    if self.is_friendly:
      description += " {name} is a friendly dog.".format(name = self.name)
    else:
      description += " {name} is an unfriendly dog.".format(name = self.name)
    return description
 
  def have_birthday(self):
    self.age = self.age + 1
    print("{name} had a birthday! {name} is {age} years old.".format(name = self.name, age = self.age))

  def become_friends(self, other_dog):
    if(other_dog.is_friendly):
      self.friends.append(other_dog)
      other_dog.friends.append(self)
      print("{name} become friends with {other_name}!".format(name = self.name, other_name = other_dog.name))
    else:
      print("{other_name} did not want to become friends with {name}!".format(name = self.name, other_name = other_dog.name))

dog_one = Dog("Sparky", "Golden Retriever", 5)
dog_two = Dog("Bruno", "Chihuahua", 10, False)
 
print(dog_one)
#output:This Golden Retriever named Sparky is 5 years old and has 0 friends. Sparky is a friendly dog.
print(dog_two)
#output: This Chihuahua named Bruno is 10 years old and has 0 friends. Bruno is an unfriendly dog.
dog_one.have_birthday()
#output: Sparky had a birthday! Sparky is 6 years old.
dog_two.become_friends(dog_one)
#output: Bruno become friends with Sparky!