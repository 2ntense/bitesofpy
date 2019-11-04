def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    return [w for w in text.split() if not all(ord(c) < 128 for c in w)]
