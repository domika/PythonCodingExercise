import re
import logging

from coding_task.app_config import read_max_number

SUPPORTED_DELIMITERS = " ,;:_"
DELIMITERS_PATTERN = r'[' + SUPPORTED_DELIMITERS + ']'
INPUT_PATTERN = r'^[0-9\-' + SUPPORTED_DELIMITERS + ']+$'


class InvalidInputException(Exception):
    def __init__(self):
        pass


class NegativeNumbersNotSupportedException(Exception):
    def __init__(self):
        pass


def __validate_input(input_string):
    if input_string is None or input_string == "" or re.match(INPUT_PATTERN, input_string):
        pass
    else:
        logging.error("The input string should contain numbers and delimiters only")
        raise InvalidInputException


def __validate(number, max_number):
    if number < 0:
        logging.error("Negative numbers are not supported")
        raise NegativeNumbersNotSupportedException
    if number > max_number:
        logging.warning(f"Number ignored: {number} (Greater than {max_number})")
        return 0
    return number


def __total_sum(numbers: list[int]) -> int:
    return sum(numbers)


def calculate_sum(input_string):
    logging.basicConfig(level=logging.INFO)
    __validate_input(input_string)
    if input_string is None or input_string == "":
        return 0
    else:
        max_number = read_max_number()
        numbers = list(map(int, re.split(DELIMITERS_PATTERN, input_string)))
        filtered_numbers = [__validate(number, max_number) for number in numbers]
        total_sum = __total_sum(filtered_numbers)
        return total_sum
