#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :"""
    f = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for n in text:
        if f == 0:
            if n == ' ':
                continue
            else:
                f = 1
        if f == 1:
            if n == '.' or n == '?' or n == ':':
                print(n)
                print()
                f = 0
            else:
                print(n, end="")
