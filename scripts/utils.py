

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


def date_diff(t_a, t_b):
    from dateutil.relativedelta import relativedelta

    t_diff = relativedelta(t_b, t_a)  # later/end time comes first!
    return '{h}h {m}m {s}s'.format(h=t_diff.hours, m=t_diff.minutes, s=t_diff.seconds)