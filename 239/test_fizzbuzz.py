import pytest
from fizzbuzz import fizzbuzz

one = [x for x in range(1, 100) if x % 3 == 0 and x % 5 == 0]
two = [x for x in range(1, 100) if x % 3 == 0 and x % 5 != 0]
three = [x for x in range(1, 100) if x % 3 != 0 and x % 5 == 0]
four = [x for x in range(1, 100) if x % 3 != 0 and x % 5 != 0]


@pytest.mark.parametrize("num, expected", [
    (one, "Fizz Buzz"),
    (two, "Fizz"),
    (three, "Buzz"),
    (four, four),
])
def test_fizz_buzz(num, expected):
    if type(expected) == list:
        for i, n in enumerate(num):
            assert fizzbuzz(n) == expected[i]
    else:
        for n in num:
            assert fizzbuzz(n) == expected
