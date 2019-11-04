import string


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    return [w for w in text.split() if not all(c in string.ascii_letters or c in string.punctuation for c in w)]
