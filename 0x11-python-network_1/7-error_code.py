#!/usr/bin/python3
"""
error codes
"""
import requests
import sys


if __name__ == "__main__":
    data = requests.get(str(sys.argv[1]))
    if data.status_code != 200:
        print("Error code: {}".format(data.status_code))
    else:
        print(data.text)
