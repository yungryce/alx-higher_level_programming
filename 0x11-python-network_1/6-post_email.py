#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to URL with
email as a parameter, and finally displays the body of the response"""

import sys
import requests
if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=payload)

    print(req.text)
