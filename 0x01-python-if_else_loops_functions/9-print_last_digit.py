#!/usr/bin/python3
def print_last_digit(number):
    """return last digit of int"""
    n = abs(number)
    last_digit = n % 10
    print(last_digit, end="")
    return last_digit
