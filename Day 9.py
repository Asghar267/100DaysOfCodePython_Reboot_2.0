print("Day 9 Instance vs Static vs Class methods, \n")

# Instance Method
print(" Instance Method")


class Student:
    """The instance method performs a set of actions on the data/value provided by the instance variables.
        A instance method is bound to the object of the class.
  The instance method acts on an object’s attributes. It can modify the object state by
        changing the value of instance variables."""

    def __init__(self, roll_no, name, age):
        self.roll_no = roll_no  # instance variable
        self.name = name
        self.age = age

    def show(self):  # instance method access instance variable
        print('Roll Number:', self.roll_no, 'Name:', self.name, 'Age:', self.age)

    def update(self, roll_number, age):  # instance method to modify instance variable
        self.roll_no = roll_number
        self.age = age


print('class VIII')
stud = Student(20, "Emma", 14)  # create object
stud.show()  # call instance method

print('class IX')
stud.update(35, 15)  # Modify instance variables
stud.show()
print("\n ", Student.__doc__)  # documentation string

# Class Method
print("\n Class Method using @classmethod")
"""A class method is bound to the class and not the object of the class. 
  It can access only class variables. It can modify the class state by changing 
  the value of a class variable that would apply across all the class objects."""
from datetime import date


class Student:  # Example 1: Create Class Method Using @classmethod Decorator
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)  # calculate age an set it as a age and return new object

    def show(self):
        print(self.name + "'s age is: " + str(self.age))


jessa = Student('Jessa', 20)
jessa.show()
joy = Student.calculate_age("Joy", 1995)  # create new object using the factory method
joy.show()

print("\n Access Class Variables in Class Methods")


class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, school_name):
        cls.school_name = school_name  # class_name.class_variable

    def show(self):  # instance method
        print(self.name, self.age, 'School:', Student.school_name)


jessa = Student('Jessa', 20)
jessa.show()
Student.change_school('XYZ School')  # change school_name
jessa.show()

print("\n Class Method using classmethod()")  # Example 2: Create Class Method Using classmethod() function
"""classmethod() is used to convert a normal method into a class method."""


class School:
    name = 'ABC School'  # class variable

    def school_name(cls):
        print('School Name is :', cls.name)


School.school_name = classmethod(School.school_name)  # create class method
School.school_name()  # call class method

print("\n Class Method in Inheritance")
'''In inheritance, the class method of a parent class is available to a child class'''


class Vehicle:
    brand_name = 'BMW'

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_price(cls, name, price):
        return cls(name, (price * 75))  # ind_price = dollar * 76   # create new Vehicle object

    def show(self):
        print(self.name, self.price)


class Car(Vehicle):
    def average(self, distance, fuel_used):
        mileage = distance / fuel_used
        print(self.name, 'Mileage', mileage)


bmw_us = Car('BMW X5', 65000)
bmw_us.show()
# class method of parent class is available to child class this will return the object of calling class
bmw_ind = Car.from_price('BMW X5', 65000)
bmw_ind.show()
print(type(bmw_ind))  # check type

print("\n Static Method")
"""Static method is a general utility method that performs a task in isolation. 
   This method doesn’t have access to the instance and class variable."""


class Employee:
    @staticmethod
    def sample(x):
        print('Inside static method', x)


Employee.sample(10)  # call static method
emp = Employee()  # can be called using object
emp.sample(10)


class Employee(object):
    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    def work(self):  # instance method
        requirement = self.gather_requirement(self.project_name)  # call static method from instance method
        for task in requirement:
            print('Completed', task)


emp = Employee('Kelly', 12000, 'ABC Project')
emp.work()

print("\n Advantages of a Static Method")
"""Advantages of a Static Method
Consume Less memory: Instance methods are object too, and creating them has a cost. Having a static method 
avoids that. Let’s assume you have ten employee objects and if you create gather_requirement() as a instance 
method then Python have to create a ten copies of this method (seperate for each object) which will consume 
more memeory. On the other hand static method has only one copy per class."""

kelly = Employee('Kelly', 12000, 'ABC Project')
jessa = Employee('Jessa', 7000, 'XYZ Project')

print(kelly.work is jessa.work)  # False because seperate copy of instance method is created for each object

# True because only one copy is created  kelly and jess objects share the same methods
print(kelly.gather_requirement is jessa.gather_requirement)
print(kelly.gather_requirement is Employee.gather_requirement)  # True

print("\n Call Static Method from Another Method")
class Test:
    @staticmethod
    def static_method_1():
        print('static method 1')

    @staticmethod
    def static_method_2():
        Test.static_method_1()

    @classmethod
    def class_method_1(cls):
        cls.static_method_2()


Test.class_method_1()  # call class method
