#!/usr/bin/python3
"""
adds all arguments to a Python list
"""


import sys


if __name__ == "__main__":
    file_ = __import__("5-save_to_json_file").save_to_json_file
    load_ = __import__("6-load_from_json_file").load_from_json_file

    try:
        c = load_from_json_file("add_item.json")
    except FileNotFoundError:
        c = []
    c.extend(sys.argv[1:])
    file_(c, "add_item.json")
