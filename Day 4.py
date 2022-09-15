print("Day 4 \n Method/Functons and types\n")

"""What is a function in Python?
In Python, a function is a group of related statements that performs a specific task.
Functions help break our program into smaller and modular chunks. As our program grows 
larger and larger, functions make it more organized and manageable."""

print("Python User-defined Functions\n")  # 1 Python User-defined Functions
'''Functions that we define ourselves to do certain specific task are referred a
   s user-defined functions.'''


def greet(name):  # Method Declaration and Initialization
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")


greet('Paul')  # Method Calling

print(greet.__doc__)


def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))
print(absolute_value(-4))

print("\n Python Built-in Functions")  # 2 Python Built-in Functions
'''Functions that readily come with Python are called built-in functions. If we use functions written by others
  in the form of library, it can be termed as library functions.'''

num = -5
print(abs(num))  # abs() function returns the absolute value of the given number
anyiter = ['e', 'd', 'c']
print(any(anyiter))  # any() function returns True if any element of an iterable is

marks = [85, 40, 90, 50, 67]
print(min(marks))  # Return minimum number
print(max(marks))  # Return Maximum number
print(sum(marks))  # Return Sum of numbers
print(len(marks))  # Return length of list, tuple , dict set
