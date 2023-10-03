#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL"""
import sys
import requests


if __name__ == "__main__":
    url_ = sys.argv[1]
    reqs = requests.get(url_)
    print(reqs.headers.get("X-Request-Id"))
