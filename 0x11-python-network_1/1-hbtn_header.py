#!/usr/bin/python3
"""url request"""
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    reqs = request.Request(argv[1])
    with request.urlopen(reqs) as n:
        print(n.headers.get('X-Request-Id'))
