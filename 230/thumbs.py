THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:

    def __mul__(self, other):

        if other == 0:
            raise ValueError("Specify a number")
        elif other > 0:
            if other >= 4:
                return f"{THUMBS_UP} ({other}x)"
            else:
                return THUMBS_UP * other
        else:
            if other <= -4:
                return f"{THUMBS_DOWN} ({other * -1}x)"
            return THUMBS_DOWN * (other * -1)

    def __rmul__(self, other):
        return self.__mul__(other)
