#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
n = "Last digit of"
if number > 0:
    last_digit = number % 10
    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
    elif last_digit == 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
    elif last_digit < 6 and last_digit != 0:
        print(f"{n} {number} is {last_digit} and is less than 6 and not 0")
if number < 0:
    last_digit = abs(number) % 10
    if last_digit != 0:
        print(f"{n} {number} is -{last_digit} and is less than 6 and not 0")
    elif last_digit == 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
if number == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
