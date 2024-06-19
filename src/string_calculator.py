def calculate_sum(input_string):
    if input_string is None or input_string == "":
        return 0
    else:
        numbers = list(map(int, input_string.split(',')))
        total_sum = sum(numbers)
        return total_sum
