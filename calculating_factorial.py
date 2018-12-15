import multiprocessing
from threading import Thread
from scripts.utils import Stopwatch


def factorial(num):
    return 1 if (num < 1) else num * factorial(num - 1)


def calculate_factorial(num):
    print("Finished: ", factorial(num), '\n' * 3)


if __name__ == '__main__':
    stopwatch = Stopwatch()

    # threads
    print("Calculating factorial with 10 threads: ")
    stopwatch.start()
    for i in range(10):
        num = i * 90
        t = Thread(target=calculate_factorial, args=(num,))
        print("Thread " + t.getName() + " is calculating " + str(num))
        t.start()
    stopwatch.stop()
    print("Time executing: ", stopwatch.results())
    stopwatch.reset()
    print("*" * 10)

    # processes
    print("Calculating factorial with 10 processes: ")
    stopwatch.start()
    for i in range(10):
        num = i * 90
        p = multiprocessing.Process(target=calculate_factorial, args=(num,))
        print("Thread " + p.name + " is calculating " + str(num))
        p.start()
    stopwatch.stop()
    print("Time executing: ", stopwatch.results())
    print("*" * 10)

    # single-threaded
    print("Calculating factorial with single thread: ")
    stopwatch.start()
    for i in range(10):
        num = i * 90
        print("Calculating " + str(num), ": ", factorial(num))
        stopwatch.stop()
    print("Time executing: ", stopwatch.results())
    print("*" * 10)
