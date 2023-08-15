#!/usr/bin/python3

"""
square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update square"""
        if args and len(args) != 0:
            n = 0
            for i in args:
                if n == 0:
                    if i is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = i
                elif n == 1:
                    self.size = i
                elif n == 2:
                    self.x = i
                elif n == 3:
                    self.y = i
                n += 1

        elif kwargs and len(kwargs) != 0:
            for k, j in kwargs.items():
                if k == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif k == "size":
                    self.size = j
                elif k == "x":
                    self.x = j
                elif k == "y":
                    self.y = j

    def to_dictionary(self):
        """dict representation of Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return print() and str() repr of Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
