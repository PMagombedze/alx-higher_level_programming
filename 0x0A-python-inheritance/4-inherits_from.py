#!/usr/bin/python3
"""
inheritance
"""


def inherits_from(obj, a_class):
    """ returns True if object is instance of class that inherited"""
    if type(obj) != a_class:
        if issubclass(type(obj), a_class):
            return True
    return False
