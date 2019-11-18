from collections import Counter
import re
from bs4 import BeautifulSoup, Tag
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None, limit=5):
    """Make a BeautifulSoup object loading in content,
       find all links and filter on AMAZON, extract the book title
       and count them, return the top "limit" books (default 5)"""
    if content is None:
        content = load_page()
    soup = BeautifulSoup(content, "html.parser")
    div = soup.find("div", class_="entry-content")

    start = 0
    cntr = Counter()

    for c in div.children:
        if isinstance(c, Tag):
            if c.text.startswith("###"):
                break
            elif start == 2:
                for book in c.find_all(href=re.compile(AMAZON)):
                    cntr[book.text] += 1
            elif c.text.startswith("***"):
                start += 1

    return [book[0] for book in cntr.most_common(limit)]
