import concurrent.futures
import time

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

# t1.start()
# t2.start()

# t1.join()
# t2.join()
print("Done")

print()
start = time.perf_counter()

def do_something(sec):
    print(f"sleeping {sec} sec")
    sleep(sec)
    return f"done slee bp {sec}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something,1)
    # print(f1.result())
    secs = [5,4,3,2,1]
    """results = [executor.submit(do_something,sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())"""
    # both same work
    results = executor.map(do_something,secs)
    for result in results:
        print(result)


# runing 10 threads
# threads =[]
# for _ in range(10):
#    t = threading.Thread(target=do_something,args=[1.5])
#    t.start()
#    threads.append(t)
#
# for t in threads: t.join()

# t1 = threading.Thread( target=do_something)
# t2 = threading.Thread( target=do_something)

# t1.start()
# t2.start()
# t1.join()
# t2.join()

finish = time.perf_counter()
print(f"total time {round(finish-start,3)}")

# threading learned from
# https://youtu.be/IEEhzQoKtQU