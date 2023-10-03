#!/usr/bin/python3
"""takes your GitHub credentials (username and password)"""
from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    creds = HTTPBasicAuth(argv[1], argv[2])
    reqs = get("https://api.github.com/user", auth=creds)
    print(request.json().get("id"))
