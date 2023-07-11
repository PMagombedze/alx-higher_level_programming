#!/usr/bin/python3
"""
write to a file
"""


def write_file(filename="", text=""):
    """writes str to text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
