#!/usr/bin/python3
"""Sends a search request for a given string to the Star Wars API"""
import sys
import requests


if __name__ == "__main__":
    url_ = "https://swapi.co/api/people"
    args_ = {"search": sys.argv[1]}
    res = requests.get(url_, params=args_).json()
    print("Number of results: {}".format(res.get("count")))
    [print(n.get("name")) for n in results.get("results")]
