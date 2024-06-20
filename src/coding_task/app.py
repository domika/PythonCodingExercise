from coding_task.string_calculator import *


def run_app():
    user_input = input("Enter delimited numbers to add: ")
    try:
        print("Total sum: ", calculate_sum(user_input))
    except NegativeNumbersNotSupportedException:
        print("Error: Negative numbers are not supported!")
    except Exception as ex:
        print("An unexpected error occurred: ", str(ex))
