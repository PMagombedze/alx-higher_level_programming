#!/usr/bin/python3
"""
student to json
"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """inititalize vars"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary repr"""
        if (type(attrs) == list):
            if  all(type(item) == str for item in attrs):
                return {n: getattr(self, n) for n in attrs if hasattr(self, n)}
        return self.__dict__
