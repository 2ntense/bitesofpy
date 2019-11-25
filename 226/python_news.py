import re
from collections import namedtuple

import requests
from bs4 import BeautifulSoup

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html


Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)

    result = []
    for title in soup.find_all(class_="title"):
        title_str = title.text.strip()
        points_comments = title.parent.parent.parent.nextSibling.nextSibling.text
        r = re.search(r'(\d+)\spoints?.+(\d+)\scomments?', points_comments, flags=re.DOTALL)
        result.append(Entry(title=title_str, points=int(r[1]), comments=int(r[2])))

    return sorted(result, key=lambda x: x.points + x.comments, reverse=True)[:top]
