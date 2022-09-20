print("Day 14 Multithreading\n ")

import threading
from time import sleep

print("\n Multi-threading in Python")
"""In Python, the threading module provides a very simple and intuitive API for spawning multiple
   threads in a program. Let us consider a simple example using a threading module: """
def print_square(numbers):
    print("Calculate Square of Numbers")
    for num in numbers:
        sleep(0.2)
        print("Square: ", num * num)


def print_cube(numbers):
    print("Calculate cube of Numbers")
    for num in numbers:
        sleep(0.2)
        print("Cube: ", num * num * num)


arr = [1, 2, 4, 6, 8, 10, 12]
t1 = threading.Thread(target=print_square, args=(arr,))
t2 = threading.Thread(target=print_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()
print("Done")



# Python program to illustrate the concept
# of threading
import threading
import os

def task1():
	print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task 1: {}".format(os.getpid()))

def task2():
	print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task 2: {}".format(os.getpid()))

if __name__ == "__main__":

	# print ID of current process
	print("ID of process running main program: {}".format(os.getpid()))

	# print name of main thread
	print("Main thread name: {}".format(threading.current_thread().name))

	# creating threads
	t1 = threading.Thread(target=task1, name='t1')
	t2 = threading.Thread(target=task2, name='t2')

	# starting threads
	t1.start()
	t2.start()

	# wait until all threads finish
	t1.join()
	t2.join()
