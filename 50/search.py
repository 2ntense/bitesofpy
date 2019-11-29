import time
from collections import namedtuple
from datetime import date

import feedparser

FEED = 'https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    return date.fromtimestamp(time.mktime(stime))


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    result = []
    d = feedparser.parse(feed)
    for e in d.entries:
        title = e.title
        link = e.link
        date_ = _convert_struct_time_to_dt(e.published_parsed)
        tags = [t["term"].lower() for t in e.tags]
        result.append(Entry(date=date_, title=title, link=link, tags=tags))

    return result


def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags
    """
    if "&" in search:
        s = search.split("&")
        for w in s:
            if w.lower() in entry.tags:
                continue
            return False
        return True
    elif "|" in search:
        s = search.split("|")
        for w in s:
            if w.lower() in entry.tags:
                return True
            return False
    else:
        if search.lower() in entry.tags:
            return True
        return False


def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term:
          - if enter was hit (empty string), print 'Please provide a search term'
          - if 'q' was entered, print 'Bye' and exit/break the infinite loop
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the title of each match ordered by date ascending
       6. Secondly, print the number of matches: 'n entries matched'
          (use entry if only 1 match)
    """
    entries = get_feed_entries()
    while True:
        user_input = input()
        if not user_input:
            print("Please provide a search term")
            continue
        if user_input == "q":
            print("Bye")
            break

        filtered = []

        for e in entries:
            match = filter_entries_by_tag(user_input, e)
            if match:
                filtered.append(e)

        for e in sorted(filtered, key=lambda x: x.date):
            print(e.title)

        print(f"{len(filtered)} {'entry' if len(filtered) == 1 else 'entries'} matched")


if __name__ == '__main__':
    main()
