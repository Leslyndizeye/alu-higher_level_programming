#!/usr/bin/python3


def print_last_digit(number):
    # Ensure the number is positive and get the last digit
    last_digit = abs(number) % 10

    # Print the last digit without a newline character
    print(last_digit, end="")

    return last_digit

# Example usage:
# number = 12345
# last_digit = print_last_digit(number)
# This will print 5 and also return 5
