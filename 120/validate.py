from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError
            if arg < 0:
                raise ValueError
        return func(*args)
    return wrapped
