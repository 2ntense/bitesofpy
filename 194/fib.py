from functools import lru_cache


@lru_cache(maxsize=None)
def cached_fib(n):
    return n if n in [0, 1] else cached_fib(n - 1) + cached_fib(n - 2)
