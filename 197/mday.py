from datetime import date, timedelta


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    v_date = date(year, 5, 1)
    return v_date + timedelta(days=6 - v_date.weekday() + 7)
