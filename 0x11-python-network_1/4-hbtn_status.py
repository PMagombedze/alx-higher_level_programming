#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests

    reqs = requests.get("https://alx-intranet.hbtn.io/status")
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(reqs.text), reqs.text))
