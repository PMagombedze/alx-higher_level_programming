#!/usr/bin/python3
"""
defines Rectangle class
"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """ïnitialize rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns printable rep of rectangle"""
        strn = ""
        if self.__height != 0 and self.__width != 0:
            strn = strn + "\n".join("#" * self.__width
                                    for n in range(self.__height))
        return strn
