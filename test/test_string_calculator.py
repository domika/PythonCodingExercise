import pytest

from string_calculator import calculate_sum

# 1. Adds numbers present in the input, e.g "1,2" = 3, "10,4" = 14
# 2. Treats empty or null input as zero, e.g "" = 0, null = 0
# 3. Supports different delimiters, e.g "1,2,3", "1 2 3"
# 4. Does not support negative numbers
# 5. Ignores numbers greater than 100

test_cases_for_sum_calculation = [
    ("5", 5),
    ("0,0", 0),
    ("0,1", 1),
    ("1,2", 3),
    ("10,4", 14),
    ("5,99", 104),
    ("1,2,3", 6),
    ("4,10,3", 17),
    ("1,2,3,4", 10),
    ("4,20,33,226", 283)
]

test_cases_for_empty_or_null_input = [
    ("", 0),
    (None, 0)
]

test_cases_for_various_delimiters = [
    ("1,2", 3),
    ("10 4", 14),
    ("5;99", 104),
    ("1-2-3", 6),
    ("3_6_1", 10),
    ("4:10:3", 17)
]

test_cases_for_mixed_delimiters = [
    ("1,2-3", 6),
    ("3_6-1", 10),
    ("1 4:10;3", 18)
]


@pytest.mark.parametrize("input_string, expected", test_cases_for_sum_calculation)
def test_sum_calculation(input_string, expected):
    assert calculate_sum(input_string) == expected


@pytest.mark.parametrize("input_string, expected", test_cases_for_empty_or_null_input)
def test_empty_or_null_input(input_string, expected):
    assert calculate_sum(input_string) == expected


@pytest.mark.parametrize("input_string, expected", test_cases_for_various_delimiters)
def test_various_delimiters(input_string, expected):
    assert calculate_sum(input_string) == expected


@pytest.mark.parametrize("input_string, expected", test_cases_for_mixed_delimiters)
def test_mixed_delimiters(input_string, expected):
    assert calculate_sum(input_string) == expected
