print("   Day 13 OS Module in Python\n")

"""The OS module in Python provides functions for interacting with the operating system. OS comes under 
   Python’s standard utility modules. This module provides a portable way of using operating system-dependent
   functionality. The *os* and *os.path* modules include many functions to interact with the file system."""

# importing os module
import os

#Handling the Current Working Directory CWD
cwd = os.getcwd() # get Current Working Directory
print("CWD :",cwd)

#Changing the Current working directory
os.chdir('../')
print("after Changing directory: ",os.getcwd())

""""Creating a Directory"""
print("\n Creating a Directory")

"""Using os.mkdir() method in Python is used to create a directory named path with the specified 
  numeric mode. This method raises FileExistsError if the directory to be created already exists."""

dir = "python_2"
parent_dir = "G:\Python 100Days code Reboot2.0/"

path = os.path.join(parent_dir, dir)
os.mkdir(path)
print("Directory created: ", dir)

dir = "java"
mode = 0o666 # mode

path = os.path.join(parent_dir, dir) # Path

# Create the directory 'GeeksForGeeks' in
# '/home / User / Documents'  with mode 0o666
# os.mkdir(path, mode)
print("Directory '% s' created" % dir)


"""os.makedirs() method in Python is used to create a directory recursively. That means while making 
  leaf directory if any intermediate-level directory is missing, os.makedirs() method will create them all."""

# Leaf directory
directory = "learnDjango"

# Parent Directories
parent_dir = "G:\Python 100Days code Reboot2.0\A\B"
path = os.path.join(parent_dir, directory)

# os.makedirs(path) # Directory 'A' and 'B' will be created too if it does not exists
print("Directory '% s' created" % directory)


print("\n Listing out Files and Directories")
"""Listing out Files and Directories with Python os.listdir() method in Python is used to get the 
   list of all files and directories in the specified directory."""

path = "/"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")

# print the list
print(len(dir_list))
print(dir_list)

print("\n Deleting Directory or Files")
"""Deleting Directory or Files using Python OS module proves different methods for removing
 directories and files in Python. These are – 
 Using os.remove()
 Using os.rmdir()"""


file = "newfile.txt" #file name for deleting
location = "G:\Python 100Days code Reboot2.0\java" #file location
path = os.path.join(location,file)
# os.remove(path) # removing file

# Using os.rmdir() used to remove or delete an empty directory. OSError will be raised
# if the specified path is not an empty directory.
directory = "python_2"
parent_dir = "G:\Python 100Days code Reboot2.0/"
path = os.path.join(parent_dir, directory)
os.rmdir(path)
print("Directory Deleted: ", directory)


print("\n  Commonly Used Functions")

""". os.name: This function gives the name of the operating system dependent module imported."""
print("OS name: ",os.name)


print("\n os.popen()")
"""3. os.popen(): This method opens a pipe to or from command. The return value can be read 
  or written depending on whether the mode is ‘r’ or ‘w’. """

fd = "GFG.txt"
# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

# popen() provides a pipe/gateway and accesses the file directly
file = os.popen(fd, 'w')
file.write("Hello") # File not closed, shown in next function.

print("\n os.close()")
""" os.close(): Close file descriptor fd. A file opened using open(), can be closed by close()only. 
   But file opened through os.popen()"""
# os.close(file) #gives error


print("\n os.rename ")
""" os.rename(): A file old.txt can be renamed to new.txt, """
fd = "GFG.txt"
# os.remove('New.txt') # removing file if exist to avoid error
# os.rename(fd,'New.txt')

print("\n os.path.exists()")
"""This method will check whether a file exists or not by passing the name of the file as a parameter. """
result = os.path.exists("file_name")  # giving the name of the file as a parameter.
print(result)


print("\n  os.path.getsize(): ")
"""In this method, python will give us the size of the file in bytes. To use this method we need to pass the name of the file as a parameter."""
result = os.path.exists("file_name")  # giving the name of the file as a parameter.
print(result)