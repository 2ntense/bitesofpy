from difflib import SequenceMatcher
from os import path
from urllib.request import urlretrieve


DICTIONARY = path.join('/tmp', 'dictionary.txt')
if not path.isfile(DICTIONARY):
    urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)


def load_words():
    """Return a set of words from DICTIONARY"""
    with open(DICTIONARY) as f:
        return {word.strip().lower() for word in f.readlines()}


def suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    if words is None:
        words = load_words()

    best_match = {"word": None, "ratio": 0}
    s = SequenceMatcher(None, misspelled_word)
    for word in words:
        s.set_seq2(word)
        ratio = s.ratio()
        if ratio > best_match["ratio"]:
            best_match["word"] = word
            best_match["ratio"] = ratio
    return best_match["word"]
