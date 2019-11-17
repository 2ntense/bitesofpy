import datetime
import re
from collections import Counter
import os
from urllib.request import urlretrieve

commits = os.path.join('/tmp', 'commits')
urlretrieve('https://bit.ly/2H1EuZQ', commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """

    f = open(commit_log)

    changes_month = Counter()
    for line in f.readlines():
        if not line.startswith("Date:"):
            raise ValueError("Line doesn't start with 'Date:'")
        split = re.split(r'^Date:\s{3}(.+?)\s\|\s(.+)', line)
        date_string = split[1]
        datetime_obj = datetime.datetime.strptime(date_string, "%a %b %d %H:%M:%S %Y %z")

        if year and year != datetime_obj.year:
            continue

        changes = split[2]

        insertions = 0
        re_insertions = re.search(r"(\d+) insertions?\(\+\)", changes)
        if re_insertions:
            insertions = int(re_insertions[1])
        deletions = 0
        re_deletions = re.search(r"(\d+) deletions?\(-\)", changes)
        if re_deletions:
            deletions = int(re_deletions[1])

        changes_month[YEAR_MONTH.format(y=datetime_obj.year, m=datetime_obj.month)] += insertions + deletions

    f.close()
    changes_month_most_common = changes_month.most_common()
    return changes_month_most_common[-1][0], changes_month_most_common[0][0]
