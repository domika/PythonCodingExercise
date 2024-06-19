def calculate_sum(input_string):
    if input_string is None or input_string == "":
        return 0
    else:
        numbers = input_string.split(',')
        number1, number2 = map(int, numbers)
        return number1 + number2
