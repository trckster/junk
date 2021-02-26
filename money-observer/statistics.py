from sys import argv
from datetime import datetime
from dateutil import parser
from limit import get_limits


def get_date():
    month = datetime.now().month
    year = datetime.now().year

    if len(argv) > 2:
        needed_month = argv[2]

        if needed_month == 'last':
            month = (month - 2) % 12 + 1

            if month == 12:
                year -= 1

    return month, year


def stat(data):
    print('Statistics:')
    month, year = get_date()

    categories = []
    amounts = {}

    for item in data:
        created_at = parser.parse(item['created_at'])
        category = item['category']

        if category not in categories:
            categories.append(category)

        if created_at.year == year and created_at.month == month:
            if category in dict.keys(amounts):
                amounts[category] += item['amount']
            else:
                amounts[category] = item['amount']

    limits = get_limits()
    overall = 0
    i = 1
    for category in amounts:
        limit = 0
        if category in dict.keys(limits):
            limit = limits[category]

        percent = 0
        if limit:
            percent = amounts[category] / limit * 100

        print(f'{i}. {category.ljust(10)}  -  {amounts[category]} RUB ({limit}, {percent:.2f}%)')
        overall += amounts[category]
        i += 1

    print(f'Overall: {overall} RUB')
