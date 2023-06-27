#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """Represents square
    Attributes:
        __size (int): size of a side of square
    """
    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of square
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

    def my_print(self):
        """prints square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
