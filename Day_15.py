print("Day 15 Multiprocessing")

from multiprocessing import freeze_support
import time
import multiprocessing
import concurrent.futures


start = time.perf_counter()

def do_something(sec =1):
    print(f"sleeping {sec} sec")
    time.sleep(sec)
    # return print(f"done slee bp {sec} ")
    return f"done slee bp {sec} "  # for  print(p1.result())


if __name__ == '__main__':
    freeze_support()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # p1 = executor.submit(do_something)
        secs = [5, 4, 3, 2, 1]
        """results = [executor.submit(do_something,sec) for sec in secs]
        for f in concurrent.futures.as_completed(results):
            print(f.result())"""
        # both same work
        results = executor.map(do_something, secs)
        for result in results:
            print(result)

    # processes = []
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something)
    #     p.start()
    #     processes.append(p)
    # for process in processes:
    #     process.join()

    # p1 = multiprocessing.Process(target=do_something)
    # p2 = multiprocessing.Process(target=do_something)
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    finish = time.perf_counter()
    print(f"total time {round(finish-start,3)}")