from coding_task.string_calculator import *


def run_app():
    print("*** String Calculator app ***")
    print("The application lets you add numbers separated by commas or other delimiters.")
    print("Please use positive integers which cannot be greater than 100.")
    print("---")

    user_input = input("Please enter the numbers to be added: ")
    try:
        print("Total sum: ", calculate_sum(user_input))
    except NegativeNumbersNotSupportedException:
        print("Error: Negative numbers are not supported!")
    except Exception as ex:
        print("An unexpected error occurred: ", str(ex))
