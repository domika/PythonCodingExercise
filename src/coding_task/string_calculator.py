import re
import logging

SUPPORTED_DELIMITERS = r'[\s,;:\_]'
MAX_NUMBER = 100


class NegativeNumbersNotSupportedException(Exception):
    def __init__(self):
        pass


def __validate(number):
    if number < 0:
        logging.error("Negative numbers are not supported")
        raise NegativeNumbersNotSupportedException
    if number > MAX_NUMBER:
        logging.warning(f"Number ignored: {number} (Greater than {MAX_NUMBER})")
        return 0
    return number


def __total_sum(numbers: list[int]) -> int:
    return sum(numbers)


def calculate_sum(input_string):
    logging.basicConfig(level=logging.INFO)

    if input_string is None or input_string == "":
        return 0
    else:
        numbers = list(map(int, re.split(SUPPORTED_DELIMITERS, input_string)))
        filtered_numbers = [__validate(number) for number in numbers]
        total_sum = __total_sum(filtered_numbers)
        return total_sum
