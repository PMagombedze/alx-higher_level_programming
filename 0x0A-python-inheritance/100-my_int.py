#!/usr/bin/python3
"""
class MyInt that inherits int
"""


class MyInt(int):
    """inherits"""
    def __ne__(self, value):
        """invert == , !="""
        return self.real == value

    def __eq__(self, value):
        """invert !=, =="""
        return self.real != value
