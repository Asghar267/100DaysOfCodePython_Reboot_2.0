print("Day 5 other functions lambda map filter")

'''Python lambda expressions allow you to define anonymous functions. Anonymous functions are 
   functions without names. The anonymous functions are useful when you need to use them once. 
   A lambda expression typically contains one or more arguments, but it can have only one expression.'''

# Syntax of Lambda Function in python
#  lambda arguments: expression

double = lambda x: x * 2  # Program to show the use of lambda functions
print(double(5))

#   The filter() function in Python takes in a function and a list as arguments.
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: x % 2 == 0, my_list))  # filter out only the even items from list
print("filter even: ", new_list)

# The map() function in Python takes in a function and a list.
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2, my_list))  # double each item in a list using map()
print("\nmap: ",new_list)
