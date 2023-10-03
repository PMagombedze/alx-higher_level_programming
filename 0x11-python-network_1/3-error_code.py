#!/usr/bin/python3
"""sends a request to the URL"""
import urllib.error as error
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    reqs = request.Request(argv[1])
    try:
        with request.urlopen(reqs) as n:
            print(n.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
