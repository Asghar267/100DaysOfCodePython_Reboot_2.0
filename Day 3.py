print("This is Day 3")
print("today we will learn if else elif and for loop while loop \n")

print("If else elsif Statements\n") # If else elsif
'''An if else statement in programming is a conditional statement
   that runs a different set of statements depending on whether an
   expression is true or false. '''

# Example 1
age = 17
if age >= 18:
    print("You are eligible")
else:
    print("Sorry, You are not Eligible \n")

# Example 2
a, b = 200, 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b\n")

#Short Hand If
if a > b: print("a is greater than b\n")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

print("\n loops and their types") # Loops
"""A for loop is used for iterating over a sequence (that is either a 
   list, a tuple, a dictionary, a set, or a string)."""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("\n looping through Sting 'Mango'")
for x in "Mango":
  print(x)

print("Break Statement") #break
'''With the break statement we can stop the loop 
before it has looped through all the items:'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


print("\nContinue Statment") #The continue Statement
"""With the continue statement we can stop the current iteration of the loop, and
   continue with the next:"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("For i in range") # The range() Function
'''To loop through a set of code a specified number of times, 
   we can use the range() function,'''
for x in range(6):
  print(x)

print("\n Thanks.....")