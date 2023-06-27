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
            size (int): size of a side of square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates area
        Returns:
            area of square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter
        Args:
            value (int): size of square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
