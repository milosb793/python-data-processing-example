from queue import Queue
from scripts.parsing_singlethread import *
from scripts.parsing_multithread import *

# globals
records_limit = 100

# initiaize stopwatch
stopwatch = Stopwatch()
stopwatch.start()

# truncate database
create_database()
create_domain_table()

# parse file and limit records
data = prepare_data(records_limit)

# create queue and fill it with data
queue = Queue()
[queue.put(e) for e in data]

# pop items from the queue until it's empty
# and create thread for each item
while not queue.empty():
    insert_chunk_thread(queue.get())

# wait threads to finish their tasks
wait_threads()

# stop measuring
stopwatch.stop()
print("Time of execution: ", stopwatch.results())