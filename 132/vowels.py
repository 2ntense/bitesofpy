VOWELS = list('aeiou')


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    def count_vowels(word):
        count = 0
        for c in word:
            if c in VOWELS:
                count += 1
        return count

    top = ["", 0]
    for word in text.lower().split():
        count = count_vowels(word)
        if count > top[1]:
            top[0] = word
            top[1] = count_vowels(word)

    return tuple(top)
