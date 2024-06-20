import pytest

from coding_task.string_calculator import calculate_sum
from coding_task.string_calculator import InvalidInputException
from coding_task.string_calculator import NegativeNumbersNotSupportedException


test_cases_for_sum_calculation = [
    ("5", 5),
    ("0,0", 0),
    ("0,1", 1),
    ("1,2", 3),
    ("10,4", 14),
    ("5,99", 104),
    ("1,2,3", 6),
    ("4,10,3", 17),
    ("1,2,3,4", 10)
]

test_cases_for_empty_or_null_input = [
    ("", 0),
    (None, 0)
]

test_cases_for_various_delimiters = [
    ("1,2", 3),
    ("10 4", 14),
    ("5;99", 104),
    ("3_6_1", 10),
    ("4:10:3", 17)
]

test_cases_for_mixed_delimiters = [
    ("1,2;3", 6),
    ("3_6 1", 10),
    ("1 4:10;3", 18)
]

test_cases_for_ignore_numbers_over_100 = [
    ("99,100", 199),
    ("9,101", 9),
    ("4,20,33,226", 57)
]


@pytest.mark.parametrize("input_string, expected", test_cases_for_sum_calculation)
def test_sum_calculation(input_string, expected):
    """
    Test 'calculate_sum()' to add numbers provided in the input string

    :param input_string: comma separated numbers
    :param expected: total sum of numbers
    """
    assert calculate_sum(input_string) == expected


@pytest.mark.parametrize("input_string, expected", test_cases_for_empty_or_null_input)
def test_empty_or_null_input(input_string, expected):
    """
    Test 'calculate_sum()' to treat empty or NULL input as zero

    :param input_string: input
    :param expected: total sum of numbers
    """
    assert calculate_sum(input_string) == expected


@pytest.mark.parametrize("input_string, expected", test_cases_for_various_delimiters)
def test_various_delimiters(input_string, expected):
    """
    Test 'calculate_sum()' to support various delimiters

    :param input_string: delimited numbers
    :param expected: total sum of numbers
    """
    assert calculate_sum(input_string) == expected


@pytest.mark.parametrize("input_string, expected", test_cases_for_mixed_delimiters)
def test_mixed_delimiters(input_string, expected):
    """
    Test 'calculate_sum()' to support mixed delimiters

    :param input_string: delimited numbers
    :param expected: total sum of numbers
    """
    assert calculate_sum(input_string) == expected


@pytest.mark.parametrize("input_string, expected", test_cases_for_ignore_numbers_over_100)
def test_ignore_numbers_over_100(input_string, expected):
    """
    Test 'calculate_sum()' to ignore numbers greater than a hundred

    :param input_string: comma separated numbers
    :param expected: total sum of numbers
    """
    assert calculate_sum(input_string) == expected


def test_calculates_sum_should_throw_exception_when_invalid_input_is_provided():
    """
    Test 'calculate_sum()' to throw 'InvalidInputException' exception when invalid input is provided
    """
    with pytest.raises(InvalidInputException):
        calculate_sum("abc1,2")


def test_calculates_sum_should_throw_exception_when_negative_number_is_provided():
    """
    Test 'calculate_sum()' to throw 'NegativeNumbersNotSupportedException' exception when negative numbers are provided
    """
    with pytest.raises(NegativeNumbersNotSupportedException):
        calculate_sum("1,2,-3")
