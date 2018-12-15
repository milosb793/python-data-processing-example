from queue import Queue
import multiprocessing
from threading import Thread
from datetime import time, datetime
from scripts.parsing_singlethread import *
from scripts.parsing_multithread import *

stopwatch = Stopwatch()
stopwatch.start()

inserted_index = 0
records_limit = 100


create_database()
create_domain_table()
data = parse_alexa_file()[:records_limit]

queue = Queue()
[queue.put(e) for e in data]

pool = []
while not queue.empty():
    process = multiprocessing.Process(target=insert_chunk, args=([queue.get()],))
    process.start()
    pool.append(process)

print("Total processes spawned: ", len(pool), "Waiting for processes to join: ")

[p.join() for p in pool]

print("Processes joined!")


stopwatch.stop()

print("Time of execution: ", stopwatch.results())