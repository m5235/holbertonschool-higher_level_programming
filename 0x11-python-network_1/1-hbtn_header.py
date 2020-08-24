#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response
"""
from urllib import request
import sys

if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    with request.urlopen(req) as res:
        print(res.getheader("X-Request-Id"))
