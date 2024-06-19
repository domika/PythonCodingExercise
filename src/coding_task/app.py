from coding_task.string_calculator import calculate_sum


def run_app():
    user_input = input("Enter delimited numbers to add: ")
    try:
        print("Total sum: ", calculate_sum(user_input))
    except Exception as ex:
        print("An unexpected error occurred: ", str(ex))
