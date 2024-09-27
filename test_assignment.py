import pytest
import inspect
from assignment import print_love_python, sum_of_n_numbers, sum_of_digits, count_digits, print_from_five_to

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source
    
def test1(capsys):
    print_love_python()
    captured = capsys.readouterr()
    assert captured.out.strip() == "\n".join(["I Love Python"] * 10)
    assert check_contains_loop(print_love_python)

@pytest.mark.parametrize("input, expected", [
    (5, 15),
    (11, 66),
    (3, 6),
    (0, 0)
])
def test2(input, expected):
    assert sum_of_n_numbers(input) == expected
    assert check_contains_loop(sum_of_n_numbers)

@pytest.mark.parametrize("input, expected", [
    (125, 8),
    (5, 5),
    (1234, 10),
    (0, 0)
])
def test3(input, expected):
    assert sum_of_digits(input) == expected
    assert check_contains_loop(sum_of_digits)

@pytest.mark.parametrize("input, expected", [
    (123, 3),
    (9, 1),
    (56741, 5),
])
def test4(input, expected):
    assert count_digits(input) == expected
    assert check_contains_loop(count_digits)

@pytest.mark.parametrize("input, expected", [
    (9, [5, 6, 7, 8, 9]),
    (7, [5, 6, 7]),
    (-2, [5, 4, 3, 2, 1, 0, -1, -2])
])
def test5(capsys, input, expected):
    print_from_five_to(input)
    captured = capsys.readouterr()
    assert captured.out.strip().splitlines() == list(map(str, expected))
    assert check_contains_loop(print_from_five_to)
