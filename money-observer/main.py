#!/usr/bin/python3

import os
from sys import argv, path
from json import dumps, loads
from datetime import datetime
from statistics import stat
from limit import limit

possible_commands = [
    'logs',
    'add',
    'help',
    'stat',
    'rm',
    'limit'
]

filename = os.path.join(path[0], 'base.dat')


def save_it(data):
    with open(filename, 'w+') as f:
        f.write(dumps(data))


def rm(data):
    print('Deleting:')

    for item in data:
        if item['id'] == int(argv[2]):
            print(item)
            data.remove(item)

            break

    save_it(data)

    print('Deleted.')


def help(data):
    print('Possible commands:')
    print(possible_commands)


def logs(data):
    print('Logs:')

    for item in data:
        id = (str(item['id']) + '.').ljust(5)
        amount = str(item['amount']).ljust(7)
        category = item['category'].ljust(10)
        print(f"{id} {amount} {category} {item['created_at']}")


def add(data):
    print('Add:')

    last_id = len(data)

    for i in argv[3:]:
        data.append({
            'id': last_id,
            'amount': int(i),
            'category': argv[2],
            'created_at': datetime.today().isoformat()
        })

        last_id += 1

    save_it(data)

    print(f'Successfully added {len(argv[3:])} items')


if '__main__' == __name__:
    if argv[1] not in possible_commands:
        print('Bad command')
        exit()

    open(filename, 'a+').close()
    json_data = open(filename, 'r').read()

    if not json_data:
        json_data = '[]'

    locals()[argv[1]](loads(json_data))
