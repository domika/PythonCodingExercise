def calculate_sum(input_string):
    numbers = input_string.split(',')
    number1, number2 = map(int, numbers)
    return number1 + number2
