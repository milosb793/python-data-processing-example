from scripts.migrations.database import *


def extract_attributes_from_csv_record(record):
    alexa, domain = str(record).split(',')
    return {"alexa_rank": alexa, "domain": domain.strip()}


def parse_alexa_file():
    path = 'files/top-1m.csv'
    data = read_small_file(path)

    print("Total lines in a file: " + str(len(data)))

    return list(map(lambda x: extract_attributes_from_csv_record(x), data))


def insert_record(index, json):

    logo = fetch_logo(json['domain'])

    sql = f'''
        INSERT INTO domains VALUES ('{json['alexa_rank']}', '{json['domain']}', '{logo}')
    '''

    result = query(sql)

    print(f'\n\t{index}: +')


def insert_all_normal(limit=1000):
    data = parse_alexa_file()
    data = data[:limit]
    for (index, record) in zip(range(0, len(data)), data):
        insert_record(index, record)
