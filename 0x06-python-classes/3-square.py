#!/usr/bin/python3
"""Defines Square class"""


class Square:
    """Represents square
    Attributes:
        __size (int): size of a side of square
    """
    def __init__(self, size=0):
        """initializes square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculates area of square
        Returns:
            area of square
        """
        return (self.__size) ** 2
