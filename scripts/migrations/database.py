from scripts.utils import *


def get_credentials():
    import os
    path = os.path.dirname(os.path.abspath(__file__)) + "/../../.env.json"
    return parse_json(''.join(read_small_file(path)))['database']


def create_connection(**kwargs):
    import mysql.connector as mysql

    if kwargs is None or kwargs == {}:
        kwargs = get_credentials()

    connection = mysql.connect(**kwargs)

    return connection


def get_cursor(database):
    return database.cursor()


def close_connection(connection):
    connection.close()


def query(sql, database='alexa_top_1m', multi=False):
    resultset = None

    try:
        credentials = get_credentials()

        if database is not None:
            credentials['database'] = database

        connection = create_connection(**credentials)
        cursor = get_cursor(connection)
        resultset = cursor.execute(sql, multi=multi)

    except Exception as e:
        print(f'Could not execute query: {sql}\nError: \n\n{e}')
        raise Exception(f'Could not execute query: {sql}\nError: \n\n{e}')

    return resultset


def query_many(sql):
    resultset = None

    try:
        connection = create_connection()
        cursor = get_cursor(connection)
        resultset = cursor.executemany(sql)

    except Exception as e:
        print(f'Could not execute query: {sql}\nError: \n\n{e}')
        exit(0)

    return resultset


def create_database():
    #
    # sql = '''
    #     DROP DATABASE IF EXISTS alexa_top_1m;
    #     CREATE DATABASE alexa_top_1m;
    # '''
    #
    # result = query(sql, multi=True)

    results = []
    results.append(query('DROP DATABASE IF EXISTS alexa_top_1m;', database=None))
    results.append(query('CREATE DATABASE alexa_top_1m;', database=None))


    # print(results)
    # if results[0] and results[1]:
    print("Database created!")
    # else:
    #     print("Database isn't created!")
    #     exit(0)


def create_domain_table():

    query('DROP TABLE IF EXISTS domains;')

    sql = '''
        CREATE TABLE domains (
             alexa_rank INT AUTO_INCREMENT,
             domain VARCHAR(255) NOT NULL,
             PRIMARY KEY (alexa_rank)
        );
    '''

    result = query(sql)

    print("Table `domains` is created!")


def add_index():
    sql = '''
        CREATE INDEX domains_INDEX ON domains (domain);
    '''

    result = query(sql)

    if result:
        print("Index is successfully added!")
    else:
        print("Failed to add index!")
        exit(0)



def drop_index():
    sql = '''
        DROP INDEX domains_INDEX ON domains; 
    '''

    result = query(sql)

    if result:
        print("Index is successfully removed!")
    else:
        print("Failed to drop index!")
        exit(0)
