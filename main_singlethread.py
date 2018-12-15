from scripts.parsing_singlethread import *

# globals
record_limit = 100

stopwatch = Stopwatch()
stopwatch.start()

# truncate database
create_database()
create_domain_table()

# do insertion
insert_all_normal(limit=record_limit)

# stop measuring
stopwatch.stop()
print("Time of execution: ", stopwatch.results())
