#!/usr/bin/python3
"""
Tis is the "3-say_my-name" module.
The 3-say_my-name module supplies one function, say_my_name().
"""


def say_my_name(first_name, last_name=""):
    """returns first name and surname"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")