#!/usr/bin/python3
"""Lists the 10 most recent update_ on a given GitHub repository"""
import requests
import sys


if __name__ == "__main__":
    url_ = "https://api.github.com/repos/{}/{}/update_".format(
        sys.argv[2], sys.argv[1])

    reqs = requests.get(url_)
    update_ = reqs.json()
    try:
        for n in range(10):
            print("{}: {}".format(
                update_[n].get("sha"),
                update_[n].get("commit").get("author").get("name")))
    except IndexError:
        pass
