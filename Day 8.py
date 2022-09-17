print("Day 8 more on OOP Encapsulation, Inheritance, \n")

# Encapsulation
"""Encapsulation in Python describes the concept of bundling data and methods within a single
 unit. So, for example, when you create a class, it means you are implementing encapsulation."""

# Inheritance
"""Inheritance
    Inheritance is a way of creating a new class for using details of an existing class 
    without modifying it. The newly formed class is a derived class (or child class). Similarly, 
    the existing class is a base class (or parent class)."""

print("\nEmployee Class Encapsulation")


class Employee:
    def __init__(self, name, salary, project):  # constructor
        self.name = name  # data members
        self.salary = salary  # data members
        self.project = project  # data members

    def show(self):  # method to display employee's details
        print("Name: ", self.name, 'Salary:', self.salary)  # accessing public data member

    def work(self):  # method
        print(self.name, 'is working on', self.project)


emp = Employee('Jessa', 8000, 'NLP')  # creating object of a class
emp.show()  # calling public method of the class
emp.work()

print("\nCompany and Employee class Access")


# Access Modifiers in Python achieve by using single underscore and double underscores.
# Public    Member: Accessible anywhere from otside oclass.
# Private   Member: Accessible within the class
# Protected Member: Accessible within the class and its sub-classes

# base class
class Company:
    def __init__(self):
        self._project = "NLP"  # Protected member Accessible within the class and its sub-classes


class Employee(Company):  # constructor
    def __init__(self, name, salary):
        self.name = name  # public data member Accessible anywhere from within or outside class.
        self.__salary = salary  # private member Accessible within the class
        Company.__init__(self)

    def show(self):
        # private members are accessible from a class
        print("Employee name :", self.name, 'Salary:', self.__salary)
        print("Working on project :", self._project)  # Accessing protected member in child class


emp = Employee('Jessa', 10000)
print('Name: ', emp.name)
print('Salary:', emp._Employee__salary)  # direct access to private member using name mangling
emp.show()
print('Project:', emp._project)  # Direct access protected data member
# print('Salary: ', emp.__salary) # accessing private data members

print("\nClass Student Getter and Setter")


class Student:
    def __init__(self, name, roll_no, age):
        self.name = name
        # private member, private members to restrict access, avoid direct data modification
        self.__roll_no = roll_no
        self.__age = age

    def show(self):
        print('Student Details:', self.name, self.__roll_no)

    def get_roll_no(self):  # getter methods
        return self.__roll_no

    def set_roll_no(self, number):  # setter method to modify data member, to allow data modification with rules
        if number > 50:
            print('Invalid roll no. Please set correct roll number')
        else:
            self.__roll_no = number


jessa = Student('Jessa', 10, 15)
jessa.show()  # before Modify
jessa.set_roll_no(120)  # changing roll number using setter
jessa.set_roll_no(25)
jessa.show()

print("\n Single Level Inheritance")
"""In single inheritance, a child class inherits from a single-parent class. 
   Here is one child class and one parent class."""


class Vehicle:  # Base class
    def Vehicle_info(self):
        print('Inside Vehicle class')


class Car(Vehicle):  # Child class
    def car_info(self):
        print('Inside Car class')


car = Car()  # Create object of Car

# access Vehicle's info using car object
car.Vehicle_info()
car.car_info()

print("\n Multiple Inheritance")
"""In multiple inheritance, one child class can inherit from multiple parent classes.
   So here is one child class and multiple parent classes."""


class Person:  # Parent class 1
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)


class Company:  # Parent class 2
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)


class Employee(Person, Company):  # Child class Multiple Inheritance
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)


emp = Employee()
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')

print("\n Multilvel Inheritance")


class Vehicle:  # Base class
    def Vehicle_info(self):
        print('Inside Vehicle class')


class Car(Vehicle):  # Child class
    def car_info(self):
        print('Inside Car class')


class SportsCar(Car):  # Child class
    def sports_car_info(self):
        print('Inside SportsCar class')


s_car = SportsCar()
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()

print("\n Hierarchical Inheritance")
"""In Hierarchical inheritance, more than one child class is derived from a single parent 
   class. In other words, we can say one parent class and multiple child classes."""


class Vehicle:
    def info(self):
        print("This is Vehicle")


class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)


class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)


obj1 = Car()
obj1.info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.info()
obj2.truck_info('Ford')

print("\n Hybrid Inheritance")
"""When inheritance is consists of multiple types or a combination of different
   inheritance is called hybrid inheritance."""


class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")


class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")


class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")


class SportsCar(Car, Vehicle):  # Sports Car can inherits properties of Vehicle and Car
    def sports_car_info(self):
        print("Inside SportsCar class")


s_car = SportsCar()
s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()
