#!/usr/bin/python3

"""
rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x coordinate getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x coordinate setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y coordinate getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y coordinate setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def display(self):
        """Print the Rectangle using '#'s"""
        if self.height == 0 or self.width == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for n in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def area(self):
        """Return area rectangle"""
        return self.height * self.width

    def update(self, *args, **kwargs):
        """Update Rectangle"""
        if args and len(args) != 0:
            n = 0
            for i in args:
                if n == 0:
                    if i is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = i
                elif n == 1:
                    self.width = i
                elif n == 2:
                    self.height = i
                elif n == 3:
                    self.x = i
                elif n == 4:
                    self.y = i
                n += 1

        elif kwargs and len(kwargs) != 0:
            for k, j in kwargs.items():
                if k == "id":
                    if j is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = j
                elif k == "width":
                    self.width = j
                elif k == "height":
                    self.height = j
                elif k == "x":
                    self.x = j
                elif k == "y":
                    self.y = j

    def to_dictionary(self):
        """dictionary representation of Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() repr"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
