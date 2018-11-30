

def read_small_file(path):
    import os

    file_exists = os.path.isfile(path)
    if file_exists:
        with open(path, 'r') as file:
            return file.readlines()
    else:
        raise FileNotFoundError


def parse_json(string):
    import json

    return json.loads(string)