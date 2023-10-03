#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email."""
import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url_ = sys.argv[1]
    val = {"email": sys.argv[2]}
    html = urllib.parse.urlencode(val).encode("ascii")

    reqs = urllib.request.Request(url_, html)
    with urllib.request.urlopen(reqs) as response:
        print(response.read().decode("utf-8"))
