#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body"""
import sys
import requests


if __name__ == "__main__":
    url_ = sys.argv[1]
    reqs = requests.get(url_)
    if reqs.status_code >= 400:
        print("Error code: {}".format(reqs.status_code))
    else:
        print(reqs.text)
