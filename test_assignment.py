import pytest
import inspect
from assignment import find_factorial, sum_odd_numbers, is_perfect_number

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("input, expected", [
    (5, 120),
    (1, 1),
    (3, 6),
    (7, 5040)
])
def test1(input, expected):
    assert find_factorial(input) == expected
    assert check_contains_loop(find_factorial)

@pytest.mark.parametrize("input, expected", [
    (5, 25),
    (1, 1),
    (4, 16),
    (0, 0),
    (3, 9)
])
def test2(input, expected):
    assert sum_odd_numbers(input) == expected
    assert check_contains_loop(sum_odd_numbers)

@pytest.mark.parametrize("input, expected", [
    (6, True),
    (28, True),
    (12, False),
    (496, True),
    (8, False)
])
def test3(input, expected):
    assert is_perfect_number(input) == expected
    assert check_contains_loop(sum_odd_numbers)
