#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL 
"""
import requests
import sys


if __name__ == "__main__":
    try:
        print(requests.get(sys.argv[1]).headers["X-Request-Id"])
    except:
        pass
