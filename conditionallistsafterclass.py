def is_natural_number(num_str):
    """
    Checks if a string representation is a natural number (positive integer).
    """
    try:
        num = int(num_str)
        # Check if the number is greater than 0
        if num > 0:
            return True
        else:
            return False
    except ValueError:
        # If conversion to int fails, it's not an integer
        return False

# Main part of the program
if __name__ == "__main__":
    user_input = input("Enter a number: ")

    if is_natural_number(user_input):
        print(f"'{user_input}' is a natural number.")
    else:
        print(f"'{user_input}' is not a natural number.")
