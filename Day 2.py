print("This is Day 2")

# list Methods
print("\n list Methods")
lis = [1, 4, 5, 6, "helo", 'Bugs']
lis.append("Python")  # Adds an element at the end of the list
print("append :", lis)
print(lis.pop())  # Removes the element at the specified position
print(lis.index(4))  # Returns the index of the first element with the specified value
print(lis.reverse())  # Reverses the order of the list
print(lis.clear())  # Removes all the elements from the list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("\n", letters)
letters[2:5] = ['C', 'D', 'E'] #replace some values
print("replaced some values :",letters)
letters[2:5] = [] # now remove them
print("Removed some values: ", letters)



# tuple Methods
print("\n Tuple Methods")
tup = (1, 4, 5, 6, "helo", 'Bugs')
print(tup)
print("count: ", tup.count(5))  # Returns the number of times a specified value occurs in a tuple
print("index: ",
      tup.index(6))  # Searches the tuple for a specified value and returns the position of where it was found

# Dictionary Methods

print("\n Dictonary Methods")
dic = {"Name": "Asghar", "age": 20, "city": "Karachi"}
print(dic)
print(dic.keys())  # Returns a list containing the dictionary's keys
print(dic.values())  # Returns a list of all the values in the dictionary
dic.update({"ID": 13932})
print("update :", dic)  # Updates the dictionary with the specified key-value pairs
print(dic.pop("age"))  # Removes the element with the specified key
print(dic)
print("\n Set Methods")

#   Set Methods
fruits = {"apple", "banana", "cherry"}
fruits.add("Mango")
print("add: ", fruits)  # Adds an element to the set
print(fruits.discard("apple"))  # Remove the specified item
drinks = {"Pepsi", "coca", "Red bull"}
print(fruits.update(drinks))  #
print(fruits)  #
