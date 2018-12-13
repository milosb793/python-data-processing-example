from datetime import datetime

from scripts.utils import *
from scripts.migrations.database import *
from scripts.migrations.run_migrations import *
from scripts.parsing_singlethread import *


records_to_insert = 1000
stopwatch = Stopwatch()

stopwatch.start()
create_database()
create_domain_table()
insert_all_normal(limit=records_to_insert)
stopwatch.stop()

print("Time of execution: ", stopwatch.results())
