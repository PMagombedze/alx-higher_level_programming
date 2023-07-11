#!/usr/bin/python3
"""
json string to object
"""


import json


def from_json_string(my_str):
    """returns obj represented by json"""
    return json.loads(my_str)
