import itertools


def sequence_generator():
    def sequence():
        for i in range(1, 26 + 1):
            yield i
            yield chr(i + 64)

    return itertools.cycle(sequence())
