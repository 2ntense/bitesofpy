import itertools
from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    for i in itertools.count(0, num_days):
        start_date = start_date + timedelta(days=num_days)
        for _ in range(num_bites):
            yield start_date
