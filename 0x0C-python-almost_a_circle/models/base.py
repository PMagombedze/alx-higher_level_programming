#!/usr/bin/python3
"""
base class
"""


import turtle
import json
import csv


class Base:
    """base class"""
    __nb_object = 0
    def __init__(self, id=None):
        """initialize"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
