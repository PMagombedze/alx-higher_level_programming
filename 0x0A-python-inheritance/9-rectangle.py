#!/usr/bin/python3
"""
rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""
    def __init__(self, width, height):
        """init constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """rectangle area"""
        return self.__height * self.__width

    def __str__(self):
        """rect print()"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
