print("Day 6 Objected Oriented Programming oop")


# Python3 program to
# demonstrate instantiating
# a class
class Dog:  # A simple class
	attr1 = "mammal"  # attribute
	attr2 = "dog"

	def fun(self):  # A sample method
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)


Rodger = Dog()  # Object instantiation
print(Rodger.attr1)  # Accessing class attributes and method through objects
Rodger.fun()
Rodger.attr1 = "Elephant"
Rodger.fun()

# __init__ method
# The __init__ method is similar to constructors in C++ and Java. Constructors are
# used to initialize the object’s state.

# Sample class with init method
class Person:
	def __init__(self, name): # init method or constructor
		self.name = name

	def say_hi(self): 	# Sample Method
		print('Hello, my name is', self.name)

p = Person('Nikhil')
p.say_hi()

'''Class and Instance Variables
Instance variables are for data, unique to each instance and class variables are for attributes and methods 
shared by all instances of the class. Instance variables are variables whose value is assigned inside a 
constructor or method with self whereas class variables are variables whose value is assigned in the class.'''


class Dog:
	animal = 'dog' 	# Class Variable

	def __init__(self, breed, color): # The init method or constructor
		self.breed = breed 		# Instance Variable
		self.color = color

	def setColor(self, color): # Adds an instance variable
		self.color = color

	def getColor(self): 	# Retrieves instance variable
		return self.color

# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)

Rodger.setColor("Black")
print(Rodger.getColor())