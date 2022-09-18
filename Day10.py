print("Day 10 Polymorphism \n")

print(" Polymorphism")
"""What is Polymorphism in Python?
   Polymorphism in Python is the ability of an object to take many forms. In simple words, polymorphism 
   allows us to perform the same action in many different ways.
   In polymorphism, a method can process objects differently depending on the class type or data type."""

print("\n Method Overriding")


class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


class Car(Vehicle):  # inherit from vehicle class

    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')


car = Car('Car x1', 'Red', 20000)  # Car Object
car.show()
# calls methods from Car class
car.max_speed()
car.change_gear()

vehicle = Vehicle('Truck x1', 'white', 75000)  # Vehicle Object
vehicle.show()
# calls method from a Vehicle class
vehicle.max_speed()
vehicle.change_gear()

print("\n Polymorphism In Built-in Methods")
students = ['Emma', 'Jessa', 'Kelly']
school = 'ABC School'

print('Reverse string')
for i in reversed('PYnative'):
    print(i, end=' ')

print('\nReverse list')
for i in reversed(['Emma', 'Jessa', 'Kelly']):
    print(i, end=' ')

print("\n\n Method Overloading")
'''The process of calling the same method with different parameters is known as method overloading. 
   Python does not support method overloading. Python considers only the latest defined method even if you 
   overload the method. Python will raise a TypeError if you overload the method.'''


def addition(a, b):
    c = a + b
    print(c)


def addition(a, b, c):
    d = a + b + c
    print(d)


# the below line shows an error
# addition(4, 5) #error

# This line will call the second product method
addition(3, 7, 5)

"""To overcome the above problem, we can use different ways to achieve the method overloading. In Python,
 to overload the class method, we need to write the method’s logic so that different code executes inside 
 the function depending on the parameter passes.

 For example, the built-in function range() takes three parameters and produce different result depending 
 upon the number of parameters passed to it."""

for i in range(5): print(i, end=', ')
print()
for i in range(5, 10): print(i, end=', ')
print()
for i in range(2, 12, 2): print(i, end=', ')

print("\n User-defined polymorphic method")


class Shape:
    def area(self, a, b=0):  # function with two default parameters
        if b > 0:
            print('Area of Rectangle is:', a * b)
        else:
            print('Area of Square is:', a ** 2)


square = Shape()
square.area(5)

rectangle = Shape()
rectangle.area(5, 3)

print("\n Constructor Chaining supper()")
"""Constructor Chaining
   Constructors are used for instantiating an object. The task of the constructor is to assign value to data
    members when an object of the class is created.
  Constructor chaining is the process of calling one constructor from another constructor. Constructor 
  chaining is useful when you want to invoke multiple constructors, one after another, by initializing only
  one instance.

  In Python, constructor chaining is convenient when we are dealing with inheritance. When an instance of
  a child class is initialized, the constructors of all the parent classes are first invoked and then, 
  in the end, the constructor of the child class is invoked.
  Using the super() method we can invoke the parent class constructor from a child class."""


# Example
class Vehicle:
    def __init__(self, engine):  # Constructor of Vehicle
        print('Inside Vehicle Constructor')
        self.engine = engine


class Car(Vehicle):
    def __init__(self, engine, max_speed):  # Constructor of Car
        super().__init__(engine)
        print('Inside Car Constructor')
        self.max_speed = max_speed


class Electric_Car(Car):
    def __init__(self, engine, max_speed, km_range):  # Constructor of Electric Car
        super().__init__(engine, max_speed)
        print('Inside Electric Car Constructor')
        self.km_range = km_range


ev = Electric_Car('1500cc', 240, 750)  # Object of electric car
print(f'Engine={ev.engine}, Max Speed={ev.max_speed}, Km range={ev.km_range}')
