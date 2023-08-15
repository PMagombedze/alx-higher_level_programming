#!/usr/bin/python3

"""
base class
"""


import csv
import turtle
import json


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON serialization to file"""
        file_ = cls.__name__ + ".json"
        with open(file_, "w") as json_:
            if list_objs is None:
                json_.write("[]")
            else:
                dictList = [i.to_dictionary() for i in list_objs]
                json_.write(Base.to_json_string(dictList))

    @staticmethod
    def from_json_string(json_string):
        """return deserialization of a JSON string"""
        if json_string == [] or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return class instantied from dictionary"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                f = cls(1, 1)
            else:
                f = cls(1)
            f.update(**dictionary)
            return f

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write csv serialization to a file"""
        file_ = cls.__name__ + ".csv"
        with open(file_, "w", newline="") as csv_:
            if list_objs is None or list_objs == []:
                csv_.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fd = ["id", "width", "height", "x", "y"]
                else:
                    fd = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_, fd=fd)
                for n in list_objs:
                    writer.writerow(n.to_dictionary())

    @classmethod
    def load_from_file(cls):
        """Return a list of classes"""
        file_ = str(cls.__name__) + ".json"
        try:
            with open(file_, "r") as json_:
                dictList = Base.from_json_string(json_.read())
                return [cls.create(**d) for d in dictList]
        except IOError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes"""
        file_ = cls.__name__ + ".csv"
        try:
            with open(file_, "r", newline="") as csv_:
                if cls.__name__ == "Rectangle":
                    fd = ["id", "width", "height", "x", "y"]
                else:
                    fd = ["id", "size", "x", "y"]
                dictList = csv.DictReader(csv_, fd=fd)
                dictList = [dict([k, int(v)] for k, v in d.items())
                              for d in dictList]
                return [cls.create(**d) for d in dictList]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for n in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(n.x, n.y)
            turt.down()
            for i in range(2):
                turt.forward(n.width)
                turt.left(90)
                turt.forward(n.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for i in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(i.x, i.y)
            turt.down()
            for i in range(2):
                turt.forward(i.width)
                turt.left(90)
                turt.forward(i.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
