#!/usr/bin/python3
"""
write to a file
"""


def append_write(filename="", text=""):
    """writes str to text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
