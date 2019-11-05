from collections import Counter

from bs4 import BeautifulSoup, Tag
import requests
import re

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

    start = False
    l = list()

    for c in div.children:
        if isinstance(c, Tag):
            if start:
                if c.text.startswith("***"):
                    start = False
                    break
                l.append(c)
            elif c.text.startswith("Top Books (2 or more mentions)"):
                start = True

    return [re.match(r"(.+?) \(.+?\)", b.text).group(1) for b in l][:limit]
