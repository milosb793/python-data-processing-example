from datetime import datetime

from scripts.utils import *
from scripts.migrations.database import *
from scripts.migrations.run_migrations import *
from scripts.parsing_singlethread import *

start_time = datetime.now()

create_database()
create_domain_table()
insert_all_normal()

end_time = datetime.now()

print("Time of execution: ", date_diff(start_time, end_time))
