print("Day 1")

# print()
# The print() function prints the specified message to the
# screen, or other standard output device. The message
# can be a string, or any other object, the object will be
# converted into a string before written to the screen

print("Hello Bugs")

# Variables

# Variables are the names you give to computer
# memory locations which are used to store values in a computer program.

a = 5
name = "Asghar"

print(a)
print(name)

#    Data types

# integer      1,3,4
# float        2.0, 4.5, 5.0
# String       "asghar"
# List         [1,"Hello", 4.0]
# Tuple        (1,"hello",5.0)
# Dictionary   {"name":"Asghar, "Age":21}

# String

str = 'Hello World!'

# String Slicing
print(str)  # Prints complete string
print(str[0])  # Prints first character of the string
print(str[2:5])  # Prints characters starting from 3rd to 5th
print(str[2:])  # Prints string starting from 3rd character
print(str * 2)  # Prints string two times
print(str + "TEST \n")  # Prints concatenated string

# Sting Methods
print("upper   :", str.upper())  # change case String from lower to upper
print("lower   :", str.lower())  # change case String from upper to lower
print("capitalize: ", str.capitalize())  # Change String case into Capitalize
print("isupper :", str.isupper())  # this checks string is upper case or not and returns True/False
print("islower :", str.islower())  # this checks string is lower case or not and returns True/False
print("find    :", str.find("W"))  # Search String and return index if found else -1

names = ["John", "Peter", "Vicky"]
print("join :", str.join(names))  # this joins list,tuple, Dictionary elements with string
print("center :", str.center(20,
                             "0"))  # center align the string, using a specified character (space is default) as the fill character.
print("count :", str.count("o"))  # counts Word, Characters in string
print("casefold :", str.casefold())  # change case String from upper to lower
print("encode :", "My name is Ståle".encode(encoding="ascii",
                                            errors="namereplace"))  # The encode() method encodes the string, using the specified encoding.
# If no encoding is specified, UTF-8 will be used.
print("endswith :", str.endswith("!"))  # Returns true if the string ends with the specified value
txt = "H\te\tl\tl\to"
print("expandtabs :", txt.expandtabs(5))  # Sets the tab size of the string

txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
print("", txt1.format())  # formats specified values in a string

point = {'x': 4, 'y': -5, 'z': 0}
print('{x} {y} {z}'.format_map(point))
print("index :", str.index("W"))

# str = "dsewrs"
# str = "34235"
# str = " "
print("isalnum    :",
      str.isalnum())  # Returns True if all characters in the string are alphanumeric return false if special character or space
print("isalpha    :", str.isalpha())  # Returns True if all characters alphabatic not sepcial characters
print("iascii     :", str.isascii())  # Returns True if all characters in the string are ascii characters
print("isdecimal  :", str.isdecimal())  # Returns True if all characters in the string are decimals
print("issdigit   :", str.isdigit())  # Returns True if all characters in the string are digits
print("isidentifire :", str.isidentifier())  # A valid identifier cannot start with a number, or contain any spaces.
print("isnumaric ", str.isnumeric())  # Returns True if all characters in the string are numeric
print("isprintable :",
      str.isprintable())  # Returns True if all characters in the string are printable false if like \t \n \a in string
print("isspace :", str.isspace())  # Returns True if all characters in the string are whitespaces
print("title :", str.title())  # Returns True if all words in a text start with a upper case letter,
print("join :", str.join(names))  # Join all items in a tuple/list into a string, using a hash character as separator:
print("", str)
