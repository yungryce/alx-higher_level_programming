#!/usr/bin/python3
"""
script that takes a URL, sends request to URL and displays body of response
"""

from sys import argv
import requests


if __name__ == "__main__":
    req = requests.get(argv[1])

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
