#!/usr/bin/python3
"""
square class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, dim):
        """init constructor"""
        self.__dim = dim
        super().__init__(self.__dim, self.__dim)
