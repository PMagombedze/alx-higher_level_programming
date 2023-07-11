#!/usr/bin/python3
"""
append after
"""


def append_after(filename="", search_string="", new_string=""):
    """append after"""
    txt = ""
    with open(filename) as f:
        for n in f:
            txt += n
            if search_string in n:
                txt += new_string
    with open(filename, "w") as f_:
        f_.write(txt)
