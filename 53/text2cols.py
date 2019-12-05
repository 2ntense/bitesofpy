import itertools
from pprint import pprint

COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    columns = []

    for p in text.split("\n\n"):
        words = p.split(" ")
        lines = []
        line = []

        while words:
            for i, w in enumerate(words):
                line.append(w)
                if len(" ".join(line)) > COL_WIDTH:
                    lines.append(" ".join(line[:-1]))
                    words = words[i:]
                    line = []
                    break
            if line:
                lines.append(" ".join(line))
                words = []

        columns.append(lines)

    # print(list(itertools.zip_longest(*columns)))

    lines = []
    for l in itertools.zip_longest(*columns):
        line = []
        for i, j in enumerate(l):
            if not j:
                line.append(" " * (COL_WIDTH + 1))
                continue
            if i == len(l) - 1:
                line.append(j)
            else:
                line.append(j.ljust(COL_WIDTH + 1, " "))

        lines.append(line)

    x = []
    for l in lines:
        x.append("".join(l))

    return "\n".join(x)
