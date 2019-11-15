STAR = '*'


def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    stars = -1
    reverse = False

    for i in range(width):
        if stars == width:
            reverse = True
        if reverse:
            stars -= 2
        else:
            stars += 2
        yield " " * int((width - stars) / 2) + STAR * stars + " " * int((width - stars) / 2)
