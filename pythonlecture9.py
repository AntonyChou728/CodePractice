# MIT 6.100L 2022 Fall (Lecture 18) & MIT 6.0001 2016 Fall (Lecture 9)
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"<{self.x}, {self.y}>"
    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

"""
the type of center is Coordinate object
the type of radius is int
If either are not, raise an error
"""
class Circle(object):
    def __init__(self, center, radius):
        if type (center) != Coordinate:
            raise ValueError("center must be a Coordinate object")
        if type (radius) != int:
            raise ValueError("radius must be an integer")
        self.center = center
        self.radius = radius
    def is_inside(self, point):
        return point.distance(self.center) < self.radius

center = Coordinate(2, 2)
my_circle = Circle(center, 2)
print(my_circle.center.x)  # Output: 2

# error examples
my_circle = Circle(2, 2)  # Raises TypeError: center must be a Coordinate object
my_circle = Circle(center, "two")  # Raises TypeError: radius

#----------------------------------------------------------------------------------

# Class Default Constructor and Method
class Animal(object):
    def __init__(self, newname = ""): # default constructor
        self.name = newname
    def set_name(self, newname = ""): # default name
        self.name = newname
    def get_name(self):
        return self.name
    
a = Animal() # default constructor
a.set_name() # default name
print(a.get_name())  # Output: (empty string)

a = Animal("dog")
a.set_name("dog")
print(a.get_name())  # Output: dog

#----------------------------------------------------------------------------------

# Class Inheritance example

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage   
    def set_name(self, newname):
        self.name = newname
    def __str__(self):
        return "Animal: " + str(self.name) + ", " + str(self.age)
    
class Cat(Animal): # Inherit from parent class Animal
    def speak(self):
        return "meow"
    def __str__(self): # Override the __str__ method
        return "Cat: " + str(self.name) + ", " + str(self.age)
    
class Dog(Animal): # Inherit from parent class Animal
    def speak(self):
        return "woof"
    def __str__(self): # Override the __str__ method
        return "Dog: " + str(self.name) + ", " + str(self.age)
    
class Person(Animal): # Inherit from parent class Animal
    def __init__(self, name, age):
        Animal.__init__(self, age) # Call the parent constructor
        self.name = name          # Set the name attribute
        self.friends = []       # Initialize an empty list of friends
    def get_friends(self):
        return self.friends
    def add_friend(self, friendname):
        if friendname not in self.friends:
            self.friends.append(friendname)
    def speak(self):
        return "hello"
    def age_diff(self, other):
        return abs(self.age - other.age)
    def __str__(self): # Override the __str__ method
        return "Person: " + str(self.name) + ", " + str(self.age)
    
my_cat = Cat(3) # Create a Cat object, age is 3
my_cat.set_name("大橘")   # set name
print(my_cat.get_name())  # Output: 大橘
print(my_cat.speak())     # Output: meow
print(my_cat)             # Output: Cat: 大橘, 3

my_dog = Dog(5) # Create a Dog object, age is 5
my_dog.set_name("Fido")
print(my_dog.get_name())  # Output: Fido
print(my_dog.speak())     # Output: woof
print(my_dog)             # Output: Dog: Fido, 5

myself = Person("David", 30) # Create a Person object, age is 30
print(myself.get_name())  # Output: David
print(myself.speak())     # Output: hello
print(myself)             # Output: Person: David, 30
friend = Person("Alice", 25)
myself.add_friend(friend.get_name())
print(myself.get_friends())  # Output: ['Alice']
print("Age difference:", myself.age_diff(friend))  # Output: Age difference: 5

#----------------------------------------------------------------------------------
# Another example of Inheritance
import random

class Student(Person):
    def __init__(self, name, age, major=None): # major is optional
        Person.__init__(self, name, age) # Call the parent constructor
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random() # random float: 0.0 <= r < 1.0
        if r < 0.25:
            return "I have homework."
        elif 0.25 <= r < 0.5:
            return "I need to study."
        elif 0.5 <= r < 0.75:
            return "I should get a job."
        else:
            return "I am cooked."
    def __str__(self): # Override the __str__ method
        return "Student: " + str(self.name) + ", " + str(self.age) + ", " + str(self.major)
    
s1 = Student("Bob", 20, "CS")
s2 = Student("Carol", 22) # major is optional
print(s1)  # Output: Student: Bob, 20, CS
print(s2)  # Output: Student: Carol, 22, None
print(s1.speak()) # Random output
print(s2.speak()) # Random output

#----------------------------------------------------------------------------------
#################################
## Use of class variables  
#################################
class Rabbit(Animal):
    # a class variable, tag, shared across all instances
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        # zfill used to add leading zeroes 001 instead of 1
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)
    def __eq__(self, other):
        # compare the ids of self and other's parents
        # don't care about the order of the parents
        # the backslash tells python I want to break up my line
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid # 相同父母且順序相同
        parents_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid # 相同父母但順序不同
        return parents_same or parents_opposite # True if same parents
    def __str__(self):
        return "rabbit:"+ self.get_rid()

print("\n---- rabbit tests ----")
print("---- testing creating rabbits ----")
r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)
print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r1 parent1:", r1.get_parent1())
print("r1 parent2:", r1.get_parent2())

print("---- testing rabbit addition ----")
r4 = r1+r2   # r1.__add__(r2)
print("r1:", r1)
print("r2:", r2)
print("r4:", r4)
print("r4 parent1:", r4.get_parent1())
print("r4 parent2:", r4.get_parent2())

print("---- testing rabbit equality ----")
r5 = r3+r4
r6 = r4+r3
print("r3:", r3)
print("r4:", r4)
print("r5:", r5)
print("r6:", r6)
print("r5 parent1:", r5.get_parent1())
print("r5 parent2:", r5.get_parent2())
print("r6 parent1:", r6.get_parent1())
print("r6 parent2:", r6.get_parent2())
print("r5 and r6 have same parents?", r5 == r6)
print("r4 and r6 have same parents?", r4 == r6)