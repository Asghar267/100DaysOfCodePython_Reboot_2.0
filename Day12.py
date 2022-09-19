print("Day 12 Collection Module in Python\n")
"""The collection Module in Python provides different types of containers. A Container is an 
   object that is used to store different objects and provide a way to access the contained objects 
   and iterate over them."""

# Counters
# OrderedDict
# DefaultDict
# ChainMap
# NamedTuple
# DeQue
# UserDict
# UserList
# UserString

from collections import Counter

print("Counter")
""""It is used to keep the count of the elements in an iterable """
# With sequence of items
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))
print(Counter({'A': 3, 'B': 5, 'C': 2}))  # with dictionary
print(Counter(A=3, B=5, C=2))  # with keyword arguments

print("\n OrderedDict")
"""An OrderedDict is also a sub-class of dictionary but unlike dictionary, it remembers the order
   in which the keys were inserted. """
from collections import OrderedDict

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

od.pop('a')  # deleting element
od['a'] = 1  # Re-inserting the same

print('\nAfter Deleting a and re-inserting')
for key, value in od.items():
    print(key, value)

print("\n DefaultDict")
"""DefaultDict
   A DefaultDict is also a sub-class to dictionary. It is used to provide some default values for the key
    that does not exist and never raises a KeyError."""
from collections import defaultdict

# Defining the dict
d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]

for i in L:  # Iterate through the list for keeping the count
    # The default value is 0 so there is no need to enter the key first
    d[i] += 1

print(d)

d = defaultdict(list)  # Defining a dict
for i in range(5):
    d[i].append(i)

print("Dictionary with values as list:")
print(d)

print("\n ChainMap")
"""ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries."""
from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
c = ChainMap(d1, d2, d3)  # Defining the chainmap

print("All the ChainMap contents are : \n", c)
print("Accessing Value: ", c['a'])  # Accessing Values using key name

print(c.values())  # Accessing values using values() method
print(c.keys())  # Accessing keys using keys()  method

d4 = {'g': 8, 'h': 9}
c2 = c.new_child(d4)  # using new_child() to add new dictionary
print("Displaying new ChainMap : ")
print(c2)

print("NamedTuple")
"""A NamedTuple returns a tuple object with names for each position which the ordinary tuples lack."""
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'DOB'])  # Declaring namedtuple()
S = Student('Nandini', '19', '2541997')  # Adding values

print("The Student age using index is : ", end="")
print(S[1])  # Access using index
print("The Student name using keyname is : ", end="")
print(S.name)  # Access using name

li = ['Manjeet', '19', '411997']  # initializing iterable
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}  # initializing dict

print("The namedtuple instance using iterable is  : ")
print(Student._make(li))  # using _make() to return namedtuple()

print("The OrderedDict instance using namedtuple is  : ")
print(S._asdict())  # using _asdict() to return an OrderedDict()

print("\n Deque ")
""" Deque (Doubly Ended Queue) is the optimized list for quicker append and pop operations from both sides 
    of the container. It provides O(1) time complexity for append and pop operations as compared to list with O(n) time 
    complexity."""
from collections import deque

de = deque([1, 2, 3])  # initializing deque
de.append(4)  # append() to insert element at right end  inserts 4 at the end of deque
print("deque after appending at right is : \n", de)

de.appendleft(6)  # appendleft() to insert element at right end inserts 6 at the beginning of deque
print("deque after appending at left is : \n", de)

de.pop()  # pop() to delete element from right end deletes 4 from the right end of deque
print("deque after deleting from right is : \n", de)

de.popleft()  # popleft() to delete element from left end deletes 6 from the left end of deque
print("deque after deleting from left is : \n", de)

print("\n Userdict")
"""UserDict is a dictionary-like container that acts as a wrapper around the dictionary objects.This 
  container is used when someone wants to create their own dictionary with some modified or new functionality. """
from collections import UserDict


class MyDict(UserDict):  # Creating a Dictionary where deletion is not allowed

    # def __del__(self):  # Function to stop deletion from dictionary
    #     raise RuntimeError("Deletion not allowed") #gives default error without deleting

    def pop(self, s=None):  # Function to stop pop from dictionary
        raise RuntimeError("Deletion not allowed")

    def popitem(self, s=None):  # Function to stop popitem from Dictionary
        raise RuntimeError("Deletion not allowed")


d = MyDict({'a': 1, 'b': 2, 'c': 3})  # Driver's code
# d.pop(1)  # UnComment to check errors


print("\n UserList")
"""UserList is a list like container that acts as a wrapper around the list objects. This is useful 
   when someone wants to create their own list with some modified or additional functionality."""
from collections import UserList


class MyList(UserList):  # Creating a List where deletion is not allowed

    def remove(self, s=None):  # Function to stop deletion from List
        raise RuntimeError("Deletion not allowed")

    def pop(self, s=None):  # Function to stop pop from List
        raise RuntimeError("Deletion not allowed")


L = MyList([1, 2, 3, 4])  # Driver's code
print("Original List \n", L)

L.append(5)  # Inserting to List"
print("After Insertion \n", L)
# L.remove() # Deleting From List


print("UserSting")
"""UserString is a string like container and just like UserDict and UserList it acts as a wrapper 
   around string objects. It is used when someone wants to create their own strings with some modified 
   or additional functionality. """
from collections import UserString


class Mystring(UserString):  # Creating a Mutable String

    def append(self, s):  # Function to append to string
        self.data += s

    def remove(self, s):  # Function to remove from string
        self.data = self.data.replace(s, "")


s1 = Mystring("Geeks")
print("Original String:", s1.data)

s1.append("s")  # Appending to string
print("String After Appending:", s1.data)

s1.remove("e")  # Removing from string
print("String after Removing:", s1.data)
