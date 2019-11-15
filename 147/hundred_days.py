from datetime import date

from dateutil.relativedelta import relativedelta

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    weekdays = list()
    counter = 0
    while len(weekdays) != 100:
        day = start_date + relativedelta(days=counter)
        if 1 <= day.isoweekday() <= 5:
            weekdays.append(day)
        counter += 1
    return weekdays
