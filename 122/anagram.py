def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""

    if sorted("".join(word1.split()).lower()) == sorted("".join(word2.split()).lower()):
        return True
    return False
