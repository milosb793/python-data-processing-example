import json
from datetime import datetime

import requests


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
        Stopwatch.start_time = 0
        Stopwatch.end_time = 0


def fetch_logo(domain):
    url = f'http://autocomplete.clearbit.com/v1/companies/suggest?query={domain}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['logo'] or ''
    return ''