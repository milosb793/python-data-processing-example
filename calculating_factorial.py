from datetime import datetime, time
from threading import Thread
from time import sleep
import multiprocessing

from scripts import utils


class Stopwatch():
    start_time = 0
    end_time = 0

    def start(self):
        Stopwatch.start_time = datetime.now()

    def stop(self):
        Stopwatch.end_time = datetime.now()

    def results(self, format=''):
        return (Stopwatch.end_time - Stopwatch.start_time).total_seconds()

    def reset(self):
        Stopwatch.start_time = None
        Stopwatch.end_time = None


def factorial(num):
    return 1 if (num < 1) else num * factorial(num - 1)


def calculate_factoriel(num):
    print("Finished: ", factorial(num), '\n'*3)


if __name__ == '__main__':
    stopwatch = Stopwatch()

    print("Calculating factorial with 10 threads: ")
    stopwatch.start()
    for i in range(10):
        num = i * 90
        t = Thread(target=calculate_factoriel, args=(num,))
        print("Thread " + t.getName() + " is calculating " + str(num))
        t.start()
    stopwatch.stop()
    print("Time executing: ", stopwatch.results())
    stopwatch.reset()
    print("*"*10)


    print("Calculating factorial with 10 processes: ")
    stopwatch.start()
    for i in range(10):
        num = i * 90
        p = multiprocessing.Process(target=calculate_factoriel, args=(num,))
        print("Thread " + p.name + " is calculating " + str(num))
        p.start()
    stopwatch.stop()
    print("Time executing: ", stopwatch.results())
    print("*"*10)


    print("Calculating factorial with single thread: ")
    stopwatch.start()
    for i in range(10):
        num = i * 90
        print("Calculating " + str(num), ": ", factorial(num))
        stopwatch.stop()
    print("Time executing: ", stopwatch.results())
    print("*"*10)




