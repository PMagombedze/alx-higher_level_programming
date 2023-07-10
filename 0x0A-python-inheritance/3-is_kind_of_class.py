#!/usr/bin/python3
"""
kind of class
"""


def is_kind_of_class(obj, a_class):
    """returns True if object is instance/of class inherited"""
    if isinstance(obj, a_class):
        return True
    return False
