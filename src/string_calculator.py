import re

supported_delimiters = r'[\s,;:\-_]'


def calculate_sum(input_string):
    if input_string is None or input_string == "":
        return 0
    else:
        numbers = list(map(int, re.split(supported_delimiters, input_string)))
        filtered_numbers = [number for number in numbers if number <= 100]
        total_sum = sum(filtered_numbers)
        return total_sum
