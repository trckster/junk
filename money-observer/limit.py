import os
from sys import argv, path
from json import loads, dumps

limits_filename = os.path.join(path[0], 'limits.dat')


def get_limits():
    open(limits_filename, 'a+').close()
    json_data = open(limits_filename, 'r').read()

    if not json_data:
        json_data = '{}'

    return loads(json_data)


def print_limits():
    limits = get_limits()

    for i in limits:
        print(f'{i.ljust(10)} - {limits[i]}')


def set_limit(categories, category, limit_amount):
    limits = get_limits()
    limits[category] = limit_amount
    open(limits_filename, 'w+').write(dumps(limits))


def get_categories(data):
    categories = []
    for i in data:
        if i['category'] not in categories:
            categories.append(i['category'])
    return categories


def limit(data):
    categories = get_categories(data)
    if argv[2] == 'set':
        set_limit(categories, argv[3], int(argv[4]))
    elif argv[2] == 'get':
        print_limits()
