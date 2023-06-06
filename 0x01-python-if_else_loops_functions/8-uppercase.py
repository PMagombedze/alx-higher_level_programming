#!/usr/bin/python3

def uppercase(str):
    """Print str in uppercase"""
    for n in str:
        if ord(n) <= 123 and ord(n) >= 97:
            n = chr(ord(n) - 32)
        print("{}".format(n), end="")
    print("")
