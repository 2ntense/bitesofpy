def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return {c.lower() for c in text if not c.isascii()}
