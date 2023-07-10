#!/usr/bin/python3
"""
inherits from list
"""


class MyList(list):
    """inherit from base class (list)"""
    def __init__(self):
        """__init__(constructor)"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
