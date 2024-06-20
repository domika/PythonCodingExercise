import re

SUPPORTED_DELIMITERS = r'[\s,;:\_]'
MAX_NUMBER = 100


class NegativeNumbersNotSupportedException(Exception):
    def __init__(self):
        pass


def __validate(number):
    if number < 0:
        raise NegativeNumbersNotSupportedException
    return number


def calculate_sum(input_string):
    if input_string is None or input_string == "":
        return 0
    else:
        numbers = list(map(int, re.split(SUPPORTED_DELIMITERS, input_string)))
        filtered_numbers = [__validate(number) for number in numbers if number <= MAX_NUMBER]
        total_sum = sum(filtered_numbers)
        return total_sum
