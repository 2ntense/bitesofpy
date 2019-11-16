import re


def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    s = re.split(pattern=r'(".+?")', string=text)

    l = list()
    for i in s:
        if len(i.strip()) == 0:
            continue
        if i[0] == "\"":
            l.append(i[1:-1])
        else:
            l.extend(i.strip().split(" "))

    return l
