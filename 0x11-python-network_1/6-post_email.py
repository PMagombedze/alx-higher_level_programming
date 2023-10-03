#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email"""
import sys
import requests


if __name__ == "__main__":
    url_ = sys.argv[1]
    val = {"email": sys.argv[2]}

    reqs = requests.post(url_, data=val)
    print(reqs.text)
