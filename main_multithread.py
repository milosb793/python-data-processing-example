from datetime import time, datetime
from queue import Queue
from threading import Thread

import multiprocessing

from scripts.parsing_singlethread import *
from scripts.parsing_multithread import *

stopwatch = Stopwatch()
stopwatch.start()

inserted_index = 0

create_database()
create_domain_table()
data = parse_alexa_file()

chunks = list(chunk(data, 100))[:10]


# for i, chunk in enumerate(chunks):
#     insert_chunk_thread(chunk)
#
#
# print("Threads spawned: ", len(thread_pool))
# map(lambda x: x.join(), thread_pool)

def worker():
    while not queue.empty():
        print("in worker")
        chunk = queue.get()
        insert_chunk(chunk)


queue = Queue()

for x in chunks:
    queue.put(x)

pool = []
for i in range(10):
    worker = Thread(target=worker)
    worker.start()
    pool.append(worker)

print("Thread spawned: ", len(pool))

[t.join() for t in pool]


stopwatch.stop()

print("Time of execution: ", stopwatch.results())
