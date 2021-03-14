from sys import argv
from limit import get_limits
from datetime import datetime
from dateutil import parser
from calendar import monthrange


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
    overall = limit_overall = 0
    i = 1
    for category in amounts:
        limit = 0
        if category in dict.keys(limits):
            limit = limits[category]

        percent = 0
        if limit:
            percent = amounts[category] * 100 / limit

        today_limit = limit * datetime.now().day // monthrange(year, month)[1]

        today_percent = 0
        if today_limit:
            today_percent = amounts[category] * 100 / today_limit

        print(f'{i}. {category.ljust(10)}  -  {amounts[category]} RUB ({limit}, {percent:.2f}%) ' +
              f'({today_limit}, {today_percent:.2f}%)')

        limit_overall += limit
        overall += amounts[category]
        i += 1

    percent_overall = overall * 100 / limit_overall
    today_limit_overall = limit_overall * datetime.now().day // monthrange(year, month)[1]
    today_percent_overall = overall * 100 / today_limit_overall

    print()
    print(f'Overall: {overall} RUB ({limit_overall}, {percent_overall:.2f}%) ' +
          f'({today_limit_overall}, {today_percent_overall:.2f}%)')
