print("Day 11 some OOP Exercises \n")



print("\n Exercise 1")
"""Create a Class with instance attributes, Write a Python program to create a Vehicle class with
   max_speed and mileage instance attributes."""
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

v1 = Vehicle(150, 5500)
print(f"Max Speed is {v1.max_speed} and Mileage {v1.mileage}")

print("\n Exercise 2")
"""Exercise 2: Create a Vehicle class without any variables and methods"""
class Vehicle:
        pass


print("\n Exercise 3")
"""Create a child class Bus that will inherit all of the variables and methods of the Vehicle class"""
class Vehicle:
    def __init__(self,name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)


print("\n Exercise 4")
"""Class Inheritance, Create a Bus class that inherits from the Vehicle class. Give the capacity
    argument of Bus.seating_capacity() a default value of 50."""

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity(70))


print("\n Exercise 5")

"""Define a property that must have the same value for every class instance (object)
   Define a class attribute”color” with a default value white. I.e., Every Vehicle should
   be white."""
class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

b = Bus("School Bus",80, 15)
c = Car("Audi",180, 150)
print(f"Color: {b.color} Speed: {b.max_speed} Mileage: {b.mileage}")
print(f"Color: {b.color} Speed: {b.max_speed} Mileage: {b.mileage}")



print("\n Exercise 6")
"""Class Inheritance: Create a Bus child class that inherits from the Vehicle class. The default fare charge of
  any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as
  a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

  Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare()
  method of a Vehicle class in Bus class"""

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        total_fare =  super().fare()
        final_amount =total_fare / 100 * 10 + total_fare
        return final_amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


print("\n Exercise 7")
"""Check type of an object
   Write a program to determine which class a given Bus object belongs to."""
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print("type: ", type(School_bus))


print("\n Exercise 8")
"""Determine if School_bus is also an instance of the Vehicle class"""
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print("is_instance: ",isinstance(School_bus, Vehicle))



