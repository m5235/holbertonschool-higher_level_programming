#!/usr/bin/python3
"""
error_code
"""
from urllib import request
import urllib.error
import sys


if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as res:
            print(res.read().decode("utf8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
