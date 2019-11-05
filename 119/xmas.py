def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    l = list()
    tmp = rows
    while rows > 0:
        l.append(" " * (tmp - rows) + "*" * (rows * 2 - 1))
        rows -= 1
    return "\n".join(reversed(l))
