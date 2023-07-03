#!/usr/bin/python3
"""
defines Rectangle class
"""


class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ïnitialize rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        self.__width = value

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns biggest rect based on area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns new Rectangle instance"""
        return (cls(size, size))

    def __str__(self):
        """returns printable rep of rectangle"""
        strn = ""
        if self.__height != 0 and self.__width != 0:
            strn = strn + "\n".join(str(self.print_symbol) * self.__width
                                    for n in range(self.__height))
        return strn

    def __repr__(self):
        """return string rep of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """print bye rectangle if instance of rect is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
